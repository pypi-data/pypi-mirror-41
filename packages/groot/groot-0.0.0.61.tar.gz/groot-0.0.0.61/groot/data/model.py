from typing import Dict, FrozenSet, Iterable, Iterator, List, Sequence, Tuple

from groot import constants
from groot.constants import Stage
from groot.data.model_collections import ComponentCollection, EdgeCollection, FusionCollection, GeneCollection, UserDomainCollection, UserGraphCollection, UserReportCollection
from groot.data.model_core import FusionGraph, Point, Pregraph, Report, Split, Subgraph, Subset, Gene, Formation, HasTable
from groot.data.model_interfaces import ESiteType
from groot.data.model_meta import ModelStatus
from intermake import Controller

from mhelper import file_helper as FileHelper, string_helper, NOT_PROVIDED



class Model( HasTable ):
    """
    The model used by Groot.
    """
    
    
    def __init__( self ) -> None:
        """
        CONSTRUCTOR
        Creates a new model with no data
        Use the `import_*` functions to add data from a file.
        """
        # Classic model data
        self.genes = GeneCollection( self )
        self.edges = EdgeCollection( self )
        self.components = ComponentCollection( self )
        self.fusions: FusionCollection = None
        self.splits: FrozenSet[Split] = None
        self.consensus: FrozenSet[Split] = None
        self.subsets: FrozenSet[Subset] = None
        self.subgraphs: Sequence[Subgraph] = None
        self.subgraphs_sources: Sequence[int] = None
        self.subgraphs_destinations: Sequence[int] = None
        self.fusion_graph_unclean: FusionGraph = None
        self.fusion_graph_clean: FusionGraph = None
        self.report: Report = None
        
        # Metadata
        self.file_name = None
        self.command_history: List[str] = []
        self.__seq_type = ESiteType.UNKNOWN
        self.lego_domain_positions: Dict[Tuple[int, int], Dict[str, object]] = { }
        
        # User-data
        self.user_domains = UserDomainCollection( self )
        self.user_graphs = UserGraphCollection( self )
        self.user_reports = UserReportCollection( self )
        self.user_comments = ["MODEL CREATED AT {}".format( string_helper.current_time() )]
    
    
    def iter_pregraphs( self ) -> Iterable[Pregraph]:
        """
        Iterates through the model pregraphs.
        """
        if self.subsets:
            for subset in self.subsets:  # type: Subset
                if subset.pregraphs is not None:
                    yield from subset.pregraphs
    
    
    @property
    def fusion_points( self ) -> Iterator[Point]:
        if self.fusions:
            for event in self.fusions:
                for formation in event.formations:
                    yield from formation.points
    
    
    def get_status( self, stage: Stage ) -> ModelStatus:
        return ModelStatus( self, stage )
    
    
    def has_any_tree( self ):
        return any( x.tree for x in self.components )
    
    
    def on_tabulate( self ):
        return { "graphs"                : list( self.iter_graphs() ),
                 "sequences"             : self.genes,
                 "components"            : self.components,
                 "edges"                 : self.edges,
                 "comments"              : self.user_comments,
                 "site_type"             : self.site_type,
                 "file_name"             : self.file_name,
                 "fusions"               : self.fusions,
                 "user_domains"          : self.user_domains,
                 "user_graphs"           : self.user_graphs,
                 "splits"                : self.splits,
                 "consensus"             : self.consensus,
                 "fusion_graph_unclean"  : self.fusion_graph_unclean,
                        "fusion_graph_clean"    : self.fusion_graph_clean,
                        "report"                : self.report,
                        "subsets"               : self.subsets,
                        "pregraphs"             : self.iter_pregraphs(),
                        "subgraphs"             : self.subgraphs,
                        "subgraphs_sources"     : self.subgraphs_sources,
                        "subgraphs_destinations": self.subgraphs_destinations,
                        "results"               : Controller.ACTIVE.result_history,
                        "commands"              : Controller.ACTIVE.app.commands.get_root_folder() }
    
    
    def __str__( self ):
        return self.name
    
    
    @property
    def name( self ) -> str:
        from groot.data import global_view
        if self is not global_view.current_model():
            return "Not the current model"
        
        if self.file_name:
            return FileHelper.get_filename_without_extension( self.file_name )
        elif self.genes:
            return "Unsaved model"
        else:
            return "Empty model"
    
    
    @property
    def site_type( self ) -> ESiteType:
        """
        API
        Obtains the type of data in the model - protein, DNA or RNA.
        """
        if self.__seq_type != ESiteType.UNKNOWN:
            return self.__seq_type
        
        s = ESiteType.UNKNOWN
        one_dna = False
        
        for x in self.genes:
            if x.site_array:
                for y in x.site_array:
                    if y in constants.DNA_BASES:
                        one_dna = True
                    else:
                        s = ESiteType.PROTEIN
        
        if one_dna and s == ESiteType.UNKNOWN:
            s = ESiteType.DNA
        
        self.__seq_type = s
        
        return s
    
    
    def _has_data( self ) -> bool:
        return bool( self.genes )
    
    
    def iter_reports( self ):
        if self.report:
            yield self.report
        
        yield from self.user_reports
    
    
    def iter_graphs( self ):
        yield from (x.named_tree for x in self.components if x.tree is not None)
        yield from (x.named_tree_unrooted for x in self.components if x.tree_unrooted is not None)
        
        if self.subgraphs:
            yield from self.subgraphs
            
        if self.fusion_graph_unclean:
            yield self.fusion_graph_unclean
        if self.fusion_graph_clean:
            yield self.fusion_graph_clean
        yield from self.user_graphs
    
    
    def is_legacy_accession( self, name ):
        return self.by_legacy_accession( name, None ) is not None
    
    
    def by_legacy_accession( self, name: str, default = NOT_PROVIDED ):
        if Gene.is_legacy_accession( name ):
            return self.genes.by_legacy_accession( name )
        elif Point.is_legacy_accession( name ):
            return self.fusions.find_point_by_legacy_accession( name )
        elif Formation.is_legacy_accession( name ):
            return self.fusions.find_formation_by_legacy_accession( name )
        elif default is not NOT_PROVIDED:
            return default
        else:
            raise ValueError( "{} is not a legacy accession.".format( name ) )
