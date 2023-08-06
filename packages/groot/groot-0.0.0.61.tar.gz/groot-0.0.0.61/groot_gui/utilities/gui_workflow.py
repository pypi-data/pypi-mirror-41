import warnings
from typing import Callable, Dict, Iterator, Sequence, Union, Tuple, Type, List, cast

import intermake
import mhelper
from PyQt5.QtWidgets import QWidget
import groot
import mhelper.mannotation.predefined_inspectors
from intermake import BasicCommand
from mhelper import MEnum, ResourceIcon, AnnotationInspector
from groot_gui.forms.resources import resources


TWorkflows = Union[groot.Stage, Sequence[groot.Stage]]


class EIntent( MEnum ):
    """
    The modes of an `Intent` (something the user wishes to do).
    The response is usually a list of suitable actions for that intent.
    
    :cvar DIRECT             :  Intent to perform an action (not really an intent - we know what the action is already).
    :cvar VIEW               :  Intent to view a stage of the workflow .
    :cvar CREATE             :  Intent to progress a stage into the workflow.
    :cvar DROP               :  Intent to remove a stage from the workflow.
    :cvar INSPECT            :  Intent to inspect an object.
    """
    DIRECT = 0
    VIEW = 1
    CREATE = 2
    DROP = 3
    INSPECT = 4


class Intent:
    """
    An `Intent` defines something the user wants to do. 
    """
    
    def __init__( self, parent: QWidget, type: EIntent, target: object ):
        self.parent = parent
        self.type = type
        self.target = target
    
    
    @property
    def is_inspect( self ):
        return self.type == EIntent.INSPECT
    
    
    def has( self, t: type ):
        return isinstance( self.target, t )
    
    
    def __repr__( self ):
        return "{}(parent={}, type={}, target={})".format( type( self ).__name__, repr( self.parent ), repr( self.type ), repr( self.target ) )
    
    
    def warn( self ):
        warnings.warn( "The intent ({}) is not recognised by the handler.".format( repr( self ) ) )


class IAction:
    def call( self, intent: Intent ) -> None:
        raise NotImplementedError( "abstract" )
    
    
    def on_register( self, handler: "IntentHandler" ):
        pass


class IntentHandler:
    """
    Defines something that can handle an `Intent`.
    """
    
    
    def __init__( self, *, abv: str = None, name: str, action: IAction, handles: Dict[EIntent, Sequence[object]] = None, icon: ResourceIcon = None, key: str = None ):
        """
        :param name:        Mandatory.  Display name.
                                        
        :param action:      Mandatory.  Action to take.
                                        This must be:
                                        * A `FrmBase` derived class
                                            * The handler will show the form and call its `on_apply_request` method 
                                        * An `Command` OR a `Function` bound to one.
                                            * The handler will request arguments before proceeding
                                        * A `Callable`
                                            * The handler will call the callable with no parameters
                                            
        :param handles:     Optional.   What this `IntentHandler` is actually capable of handling.
                                        A dict of:
                                            K : EIntent          = Intent
                                            V : Sequence[object] = Sequence of values for this intent.
                                                                   The type of object depends on `K` - for
                                                                   VIEW/CREATE/DROP these are stages, while for INSPECT
                                                                   they are the types capable of being inspected.
        :param icon:        Optional.   Display icon.
         
        :param key:         Optional.   Arbitrary key is used to refer to the intent.
        """
        action.on_register( self )
        
        if handles is None:
            handles = { }
        
        for k, v in list( handles.items() ):
            handles[k] = mhelper.array_helper.as_sequence( v, cast = tuple )
        
        for e in EIntent:
            if e not in handles:
                handles[e] = ()
        
        self.abv = abv or name
        self.name = name
        self.action: IAction = action
        self.handles: Dict[EIntent, Tuple[object, ...]] = handles
        self.icon = icon
        self.key = key
    
    
    def execute( self, parent: QWidget, intent: EIntent, target: object ):
        """
        Launches this handler.
        :param parent:  Parent window. 
        :param intent:  Reason for request.
        :param target:  Reason for request.  
        """
        i = Intent( parent, intent, target )
        self.action.call( i )
    
    
    def __repr__( self ):
        return "{}(name={},action={},handles={},icon={},key={})".format( type( self ).__name__, repr( self.name ), repr( self.action ), repr( self.handles ), repr( self.icon ), repr( self.key ) )
    
    
    def __str__( self ):
        return self.key or self.name
    
    
    @property
    def is_visible( self ):
        from groot_gui.forms.frm_base import FrmBase
        if isinstance( self.action, type ) and issubclass( self.action, FrmBase ):
            from groot_gui.forms.frm_main import FrmMain
            return self.action.__name__ in FrmMain.INSTANCE.mdi
        else:
            return False


_FrmBase = "FrmBase"


class ShowForm( IAction ):
    def __init__( self, class_: Type[_FrmBase] ):
        self.class_ = class_
    
    
    def call( self, intent: Intent ) -> None:
        from groot_gui.forms.frm_main import FrmMain
        FrmMain.INSTANCE.show_form( self.class_, intent )
    
    
    def on_register( self, handler: IntentHandler ):
        self.class_.handler_info = handler


class ShowArgs( IAction ):
    def __init__( self, function: Callable ):
        self.command: BasicCommand = BasicCommand.retrieve( function )
    
    
    def call( self, intent: Intent ) -> None:
        if intent.type == EIntent.DIRECT:
            argskwargs: mhelper.ArgsKwargs = mhelper.assert_type_or_none( "intent.target", intent.target, mhelper.mannotation.predefined_inspectors.ArgsKwargs )
        else:
            argskwargs = mhelper.ArgsKwargs()
        
        # TODO: Use the controller directly
        intermake.acquire( self.command, window = intent.parent, confirm = True ).run( *argskwargs.args, **argskwargs.kwargs )


class RunAction( IAction ):
    def __init__( self, func: Callable ):
        self.func = func
    
    
    def call( self, intent: Intent ) -> None:
        if intent.type == EIntent.DIRECT and intent.target:  # Deprecated?
            argskwargs: mhelper.mannotation.predefined_inspectors.ArgsKwargs = mhelper.assert_type_or_none( "intent.target", intent.target, mhelper.mannotation.predefined_inspectors.ArgsKwargs )
            self.func( intent.parent.actions, *argskwargs.args, **argskwargs.kwargs )
        else:
            self.func( intent.parent.actions )


class IntentHandlerCollection:
    """
    The GUI is built on a "intent" model, the GUI says _what_ it's going to do, not _how_.
    
    In response to the _what_ the `IntentHandlerCollection`'s responsibility is to provide
    an `IntentHandler` that can handle the _what_, or multiple `IntentHandler`s that the
    user can then choose from.
    """
    
    
    def __init__( self ):
        from groot_gui.utilities.gui_actions import GuiActions
        import groot
        
        # Workflow viewing
        from groot_gui.forms.frm_webtree import FrmWebtree
        self.VIEW_TEXT = IntentHandler( abv = "Report",
                                        name = "Report dialogue",
                                        action = ShowForm( FrmWebtree ),
                                        icon = resources.text,
                                        key = "view_trees",
                                        handles = { EIntent.VIEW   : (groot.STAGES.SEQUENCES_2,
                                                                      groot.STAGES.SIMILARITIES_3,
                                                                      groot.STAGES.MAJOR_4,
                                                                      groot.STAGES.MINOR_5,
                                                                      groot.STAGES.DOMAINS_6,
                                                                      groot.STAGES.ALIGNMENTS_7,
                                                                      groot.STAGES.TREES_8,
                                                                      groot.STAGES.FUSIONS_9,
                                                                      groot.STAGES.SPLITS_10,
                                                                      groot.STAGES.CONSENSUS_11,
                                                                      groot.STAGES.SUBSETS_12,
                                                                      groot.STAGES.PREGRAPHS_13,
                                                                      groot.STAGES.SUPERTREES_14,
                                                                      groot.STAGES.FUSE_15,
                                                                      groot.STAGES.CLEAN_16,
                                                                      groot.STAGES.CHECKED_17),
                                                    EIntent.INSPECT: (object,) } )
        
        from groot_gui.forms.frm_lego import FrmLego
        self.VIEW_LEGO = IntentHandler( abv = "Lego",
                                        name = "Lego diagram editor",
                                        action = ShowForm( FrmLego ),
                                        icon = resources.lego,
                                        key = "view_lego",
                                        handles = { EIntent.VIEW   : (groot.STAGES.SEQUENCES_2,
                                                                      groot.STAGES.SIMILARITIES_3,
                                                                      groot.STAGES.MAJOR_4,
                                                                      groot.STAGES.MINOR_5,
                                                                      groot.STAGES.DOMAINS_6),
                                                    EIntent.INSPECT: (groot.Gene, groot.Domain, groot.Component, groot.Edge) } )
        
        from groot_gui.forms.frm_alignment import FrmAlignment
        self.VIEW_ALIGNMENT = IntentHandler( abv = "Alignment",
                                             name = "Sequence viewer",
                                             action = ShowForm( FrmAlignment ),
                                             icon = resources.align,
                                             key = "view_alignments",
                                             handles = { EIntent.VIEW   : (groot.STAGES.SEQUENCES_2,
                                                                           groot.STAGES.MINOR_5,
                                                                           groot.STAGES.ALIGNMENTS_7),
                                                         EIntent.INSPECT: (groot.IHasFasta,) } )
        
        from groot_gui.forms.frm_fusions import FrmFusions
        self.VIEW_FUSIONS = IntentHandler( name = "Fusion explorer",
                                           abv = "Fusions",
                                           action = ShowForm( FrmFusions ),
                                           icon = resources.fusion,
                                           handles = { EIntent.VIEW: (groot.STAGES.FUSIONS_9,) } )
        
        from groot_gui.forms.frm_view_splits import FrmViewSplits
        self.VIEW_SPLITS = IntentHandler( abv = "Splits",
                                          name = "Splits matrix",
                                          action = ShowForm( FrmViewSplits ),
                                          icon = resources.split,
                                          handles = { EIntent.VIEW   : (groot.STAGES.SEQUENCES_2,
                                                                        groot.STAGES.MAJOR_4,
                                                                        groot.STAGES.SPLITS_10,
                                                                        groot.STAGES.CONSENSUS_11),
                                                      EIntent.INSPECT: (groot.Split, groot.Gene, groot.Component, groot.Fusion) } )
        
        from groot_gui.forms.frm_samples import FrmLoadFile
        self.VIEW_OPEN_FILE = IntentHandler( name = "Browse open",
                                             action = ShowForm( FrmLoadFile ),
                                             icon = resources.open,
                                             key = "view_open_file" )
        
        from groot_gui.forms.frm_samples import FrmSaveFile
        self.VIEW_SAVE_FILE = IntentHandler( name = "Browse save",
                                             action = ShowForm( FrmSaveFile ),
                                             icon = resources.save )
        
        from groot_gui.forms.frm_genes import FrmGenes
        self.VIEW_GENES = IntentHandler( abv = "Genes",
                                         name = "Gene editor",
                                         action = ShowForm( FrmGenes ),
                                         icon = resources.genes,
                                         handles = { EIntent.VIEW   : (groot.STAGES.SEQUENCES_2,
                                                                       groot.STAGES.MAJOR_4,
                                                                       groot.STAGES.MAJOR_4,
                                                                       groot.STAGES.MINOR_5,
                                                                       groot.STAGES.DOMAINS_6),
                                                     EIntent.INSPECT: (groot.Gene,) } )
        
        # Creating
        self.CREATE_BLAST_FASTA = IntentHandler( name = "Import file",
                                                 action = RunAction( GuiActions.import_file ),
                                                 icon = resources.create,
                                                 key = "import_file",
                                                 handles = { EIntent.CREATE: (groot.STAGES.SEQUENCES_2,
                                                                              groot.STAGES.SIMILARITIES_3) } )
        self.CREATE_MAJOR = IntentHandler( name = "Create major",
                                           action = ShowArgs( groot.create_major ),
                                           icon = resources.create,
                                           key = "create_major",
                                           handles = { EIntent.CREATE: groot.STAGES.MAJOR_4 } )
        
        self.CREATE_MINOR = IntentHandler( name = "Create minor",
                                           action = ShowArgs( groot.create_minor ),
                                           icon = resources.create,
                                           handles = { EIntent.CREATE: groot.STAGES.MINOR_5 } )
        
        from groot_gui.forms.frm_run_algorithm import FrmCreateDomains
        self.CREATE_DOMAINS = IntentHandler( name = "Create domains",
                                             action = ShowForm( FrmCreateDomains ),
                                             icon = resources.create,
                                             key = "view_domains",
                                             handles = { EIntent.VIEW   : (groot.STAGES.DOMAINS_6,),
                                                         EIntent.CREATE : (groot.STAGES.DOMAINS_6,),
                                                         EIntent.DROP   : (groot.STAGES.DOMAINS_6,),
                                                         EIntent.INSPECT: (groot.domain_algorithms.Algorithm,) } )
        
        from groot_gui.forms.frm_run_algorithm import FrmCreateAlignment
        self.CREATE_ALIGNMENTS = IntentHandler( name = "Create alignments",
                                                action = ShowForm( FrmCreateAlignment ),
                                                icon = resources.create,
                                                key = "create_alignments",
                                                handles = { EIntent.CREATE: groot.STAGES.ALIGNMENTS_7 } )
        
        from groot_gui.forms.frm_run_algorithm import FrmCreateTrees
        self.CREATE_TREES = IntentHandler( name = "Create trees",
                                           action = ShowForm( FrmCreateTrees ),
                                           icon = resources.create,
                                           key = "create_trees",
                                           handles = { EIntent.CREATE: groot.STAGES.TREES_8 } )
        
        self.CREATE_FUSIONS = IntentHandler( name = "Create fusions",
                                             action = ShowArgs( groot.create_fusions ),
                                             icon = resources.create,
                                             key = "create_fusions",
                                             handles = { EIntent.CREATE: groot.STAGES.FUSIONS_9 } )
        
        self.CREATE_SPLITS = IntentHandler( name = "Create splits",
                                            action = ShowArgs( groot.create_splits ),
                                            icon = resources.create,
                                            handles = { EIntent.CREATE: groot.STAGES.SPLITS_10 } )
        
        self.CREATE_CONSENSUS = IntentHandler( name = "Create consensus",
                                               action = ShowArgs( groot.create_consensus ),
                                               icon = resources.create,
                                               handles = { EIntent.CREATE: groot.STAGES.CONSENSUS_11 } )
        
        self.CREATE_SUBSETS = IntentHandler( name = "Create subsets",
                                             action = ShowArgs( groot.create_subsets ),
                                             icon = resources.create,
                                             key = "create_subsets",
                                             handles = { EIntent.CREATE: groot.STAGES.SUBSETS_12 } )
        
        self.CREATE_PREGRAPHS = IntentHandler( name = "Create pregraphs",
                                               action = ShowArgs( groot.create_pregraphs ),
                                               icon = resources.create,
                                               handles = { EIntent.CREATE: groot.STAGES.PREGRAPHS_13 } )
        
        from groot_gui.forms.frm_run_algorithm import FrmCreateSubgraphs
        self.CREATE_SUBGRAPHS = IntentHandler( name = "Create subgraphs",
                                               action = ShowForm( FrmCreateSubgraphs ),
                                               icon = resources.create,
                                               key = "create_subgraphs",
                                               handles = { EIntent.CREATE: groot.STAGES.SUPERTREES_14 } )
        
        self.CREATE_FUSED = IntentHandler( name = "Create fused",
                                           action = ShowArgs( groot.create_fused ),
                                           icon = resources.create,
                                           key = "create_fused",
                                           handles = { EIntent.CREATE: groot.STAGES.FUSE_15 } )
        
        self.CREATE_CLEANED = IntentHandler( name = "Create cleaned",
                                             action = ShowArgs( groot.create_cleaned ),
                                             icon = resources.create,
                                             handles = { EIntent.CREATE: groot.STAGES.CLEAN_16 } )
        
        self.CREATE_CHECKED = IntentHandler( name = "Create checked",
                                             action = ShowArgs( groot.create_checked ),
                                             icon = resources.create,
                                             handles = { EIntent.CREATE: groot.STAGES.CHECKED_17 } )
        
        # Dropping
        self.DROP_GENES = IntentHandler( name = "Drop genes",
                                         action = ShowArgs( groot.drop_genes ),
                                         icon = resources.remove,
                                         handles = { EIntent.DROP: (groot.STAGES.SEQUENCES_2,) },
                                         key = "drop_genes" )
        
        self.DROP_MAJOR = IntentHandler( name = "Drop major",
                                         action = ShowArgs( groot.drop_components ),
                                         icon = resources.remove,
                                         handles = { EIntent.DROP: groot.STAGES.MAJOR_4 } )
        
        self.DROP_MINOR = IntentHandler( name = "Drop minor",
                                         action = ShowArgs( groot.drop_components ),
                                         icon = resources.remove,
                                         handles = { EIntent.DROP: groot.STAGES.MINOR_5 } )
        
        self.DROP_ALIGNMENTS = IntentHandler( name = "Drop alignments",
                                              action = ShowArgs( groot.drop_alignment ),
                                              icon = resources.remove,
                                              key = "drop_alignments",
                                              handles = { EIntent.DROP: groot.STAGES.ALIGNMENTS_7 } )
        
        self.DROP_TREES = IntentHandler( name = "Drop trees",
                                         action = ShowArgs( groot.drop_trees ),
                                         icon = resources.remove,
                                         key = "drop_trees",
                                         handles = { EIntent.DROP: groot.STAGES.TREES_8 } )
        
        self.DROP_FUSIONS = IntentHandler( name = "Drop fusions",
                                           action = ShowArgs( groot.drop_fusions ),
                                           icon = resources.remove,
                                           handles = { EIntent.DROP: groot.STAGES.FUSIONS_9 } )
        
        self.DROP_CANDIDATES = IntentHandler( name = "Drop splits",
                                              action = ShowArgs( groot.drop_splits ),
                                              icon = resources.remove,
                                              handles = { EIntent.DROP: groot.STAGES.SPLITS_10 } )
        
        self.DROP_VIABLE = IntentHandler( name = "Drop consensus",
                                          action = ShowArgs( groot.drop_consensus ),
                                          icon = resources.remove,
                                          handles = { EIntent.DROP: groot.STAGES.CONSENSUS_11 } )
        
        self.DROP_SUBSETS = IntentHandler( name = "Drop subsets",
                                           action = ShowArgs( groot.drop_subsets ),
                                           icon = resources.remove,
                                           handles = { EIntent.DROP: groot.STAGES.SUBSETS_12 } )
        
        self.DROP_PREGRAPHS = IntentHandler( name = "Drop pregraphs",
                                             action = ShowArgs( groot.drop_pregraphs ),
                                             icon = resources.remove,
                                             key = "drop_subgraphs",
                                             handles = { EIntent.DROP: groot.STAGES.PREGRAPHS_13 } )
        
        self.DROP_SUBGRAPHS = IntentHandler( name = "Drop subgraphs",
                                             action = ShowArgs( groot.drop_supertrees ),
                                             icon = resources.remove,
                                             key = "drop_subgraphs",
                                             handles = { EIntent.DROP: groot.STAGES.SUPERTREES_14 } )
        
        self.DROP_FUSED = IntentHandler( name = "Drop fused",
                                         action = ShowArgs( groot.drop_fused ),
                                         icon = resources.remove,
                                         handles = { EIntent.DROP: groot.STAGES.FUSE_15 } )
        
        self.DROP_CLEANED = IntentHandler( name = "Drop cleaned",
                                           action = ShowArgs( groot.drop_cleaned ),
                                           icon = resources.remove,
                                           handles = { EIntent.DROP: groot.STAGES.CLEAN_16 } )
        
        self.DROP_CHECKED = IntentHandler( name = "Drop checked",
                                           action = ShowArgs( groot.drop_checked ),
                                           icon = resources.remove,
                                           handles = { EIntent.DROP: groot.STAGES.CHECKED_17 } )
        
        self.SET_OUTGROUPS = IntentHandler( name = "Set outgroups",
                                            action = ShowArgs( groot.set_outgroups ),
                                            icon = resources.create,
                                            handles = { EIntent.CREATE: (groot.STAGES.OUTGROUPS_7b,) } )
        
        self.SET_GENE_NAME = IntentHandler( name = "Set gene name",
                                            action = ShowArgs( groot.set_gene_name ),
                                            icon = resources.create,
                                            handles = { EIntent.CREATE: (groot.STAGES.SEQUENCES_2,) } )
        
        self.IMPORT_GENE_NAMES = IntentHandler( name = "Import gene names",
                                                action = ShowArgs( groot.import_gene_names ),
                                                icon = resources.create,
                                                handles = { EIntent.CREATE: (groot.STAGES.SEQUENCES_2,) } )
        
        self.SET_MAJOR = IntentHandler( name = "Set major",
                                        action = ShowArgs( groot.set_major ),
                                        icon = resources.create,
                                        handles = { EIntent.CREATE : (groot.STAGES.MAJOR_4,),
                                                    EIntent.INSPECT: (groot.Gene, List[groot.Gene]) } )
        
        # Actions
        self.ACT_FILE_NEW = IntentHandler( name = "New",
                                           action = ShowArgs( groot.file_new ),
                                           icon = resources.new,
                                           key = "new_model" )
        
        self.ACT_FILE_SAVE = IntentHandler( name = "Save",
                                            action = RunAction( GuiActions.save_model ),
                                            icon = resources.save )
        
        self.ACT_FILE_SAVE_AS = IntentHandler( name = "Save as",
                                               action = RunAction( GuiActions.browse_save ),
                                               key = "file_save_as" )
        
        self.ACT_FILE_OPEN = IntentHandler( name = "Open",
                                            action = RunAction( GuiActions.browse_open ),
                                            key = "file_open" )
        
        self.ACT_FILE_SAVE_TO = IntentHandler( name = "Save file (x)",
                                               action = RunAction( GuiActions.save_model_to ),
                                               key = "save_file_to" )
        
        self.ACT_FILE_LOAD_FROM = IntentHandler( name = "Load file (x)",
                                                 action = RunAction( GuiActions.load_file_from ),
                                                 key = "load_file_from" )
        
        self.ACT_FILE_SAMPLE_FROM = IntentHandler( name = "Load sample (x)",
                                                   action = RunAction( GuiActions.load_sample_from ),
                                                   key = "load_sample_from" )
        
        self.ACT_EXIT = IntentHandler( name = "Exit",
                                       action = RunAction( GuiActions.exit ) )
        
        self.ACT_STOP_WIZARD = IntentHandler( name = "Stop wizard",
                                              action = RunAction( GuiActions.stop_wizard ),
                                              key = "stop_wizard" )
        
        self.ACT_WIZARD_NEXT = IntentHandler( name = "Continue wizard",
                                              action = RunAction( GuiActions.wizard_next ),
                                              key = "wizard_next" )
        
        self.ACT_1 = IntentHandler( name = "Enable inbuilt browser",
                                    action = RunAction( GuiActions.enable_inbuilt_browser ),
                                    key = "enable_inbuilt_browser" )
        
        self.ACT_2 = IntentHandler( name = "dismiss_startup_screen",
                                    action = RunAction( GuiActions.dismiss_startup_screen ),
                                    key = "dismiss_startup_screen" )
        
        # Miscellaneous views
        from groot_gui.forms.frm_startup import FrmStartup
        self.VIEW_STARTUP = IntentHandler( name = "Startup",
                                           action = ShowForm( FrmStartup ) )
        
        from groot_gui.forms.frm_view_options import FrmViewOptions
        self.VIEW_PREFERENCES = IntentHandler( name = "Preferences",
                                               action = ShowForm( FrmViewOptions ),
                                               key = "view_options",
                                               icon = resources.settings )
        
        from groot_gui.forms.frm_workflow import FrmWorkflow
        self.VIEW_WORKFLOW = IntentHandler( name = "Workflow",
                                            action = ShowForm( FrmWorkflow ),
                                            icon = resources.workflow,
                                            key = "view_workflow" )
        
        from groot_gui.forms.frm_wizard import FrmWizard
        self.VIEW_WIZARD = IntentHandler( name = "Wizard",
                                          action = ShowForm( FrmWizard ),
                                          icon = resources.wizard,
                                          key = "view_wizard" )
        
        from groot_gui.forms.frm_about import FrmAbout
        self.VIEW_ABOUT = IntentHandler( name = "About",
                                         action = ShowForm( FrmAbout ),
                                         icon = resources.groot_logo )
        self.VIEW_HELP = IntentHandler( name = "Help",
                                        action = RunAction( GuiActions.show_help ),
                                        icon = resources.help_cursor,
                                        key = "view_help" )
        self.VIEW_MY_HELP = IntentHandler( name = "Window help",
                                           action = RunAction( GuiActions.show_my_help ),
                                           icon = resources.help )
        self.VIEW_INTERMAKE = IntentHandler( name = "Intermake",
                                             action = RunAction( GuiActions.show_intermake ) )
    
    
    def __iter__( self ) -> Iterator[IntentHandler]:
        for v in self.__dict__.values():
            if isinstance( v, IntentHandler ):
                yield v
    
    
    def find_by_key( self, key: str ) -> IntentHandler:
        for item in self:
            if item.key == key:
                return item
        
        raise KeyError( key )
    
    
    def list_avail( self, intent: EIntent, target: object ) -> List["IntentHandler"]:
        """
        Iterates over the `IntentHandler`s capable of handling this intent.
        """
        r = []
        
        if intent is EIntent.INSPECT:
            if not isinstance( target, type ):
                target = type( target )
            
            for handler in handlers():
                if any( AnnotationInspector( target ).is_direct_subclass_of( cast(type, x) ) for x in handler.handles[intent] ):
                    r.append( handler )
        else:
            for handler in handlers():
                if target in handler.handles[intent]:
                    r.append( handler )
        
        return r


__handlers: IntentHandlerCollection = None


def handlers() -> IntentHandlerCollection:
    global __handlers
    if __handlers is None:
        __handlers = IntentHandlerCollection()
    return __handlers
