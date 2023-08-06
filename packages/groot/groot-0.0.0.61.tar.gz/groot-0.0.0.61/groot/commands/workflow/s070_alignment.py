from typing import Callable, List, Optional
from intermake import pr, Controller
from mhelper import io_helper, string_helper

from groot import constants
from groot.application import app
from groot.data import Component, Model, global_view
from groot.constants import EChanges
from groot.utilities import cli_view_utils, external_runner
from groot.utilities.extendable_algorithm import AlgorithmCollection


DAlgorithm = Callable[[Model, str], str]
"""A delegate for a function that takes a model and unaligned FASTA data, and produces an aligned result, in FASTA format."""

alignment_algorithms = AlgorithmCollection( DAlgorithm, "Alignment" )


@app.command( folder = constants.F_CREATE )
def create_alignments( algorithm: alignment_algorithms.Algorithm, component: Optional[List[Component]] = None ) -> EChanges:
    """
    Aligns the component.
    If no component is specified, aligns all components.
    
    Requisites: `create_minor` and FASTA data.
    
    :param algorithm:   Algorithm to use. See `algorithm_help`.
    :param component:   Component to align, or `None` for all.
    """
    model = global_view.current_model()
    
    if not all( x.site_array for x in model.genes ):
        raise ValueError( "Refusing to make alignments because there is no site data. Did you mean to load the site data (FASTA) first?" )
    
    to_do = cli_view_utils.get_component_list( component )
    before = sum( x.alignment is not None for x in model.components )
    
    for component_ in pr.pr_iterate( to_do, "Aligning" ):
        fasta = component_.get_unaligned_legacy_fasta()
        component_.alignment = external_runner.run_in_temporary( algorithm, component_.model, fasta )
    
    after = sum( x.alignment is not None for x in model.components )
    pr.printx( "<verbose>{} components aligned. {} of {} components have an alignment ({}).</verbose>".format( len( to_do ), after, len( model.components ), string_helper.as_delta( after - before ) ) )
    
    return EChanges.COMP_DATA


@app.command( folder = constants.F_SET )
def set_alignment( component: Component, alignment: str ) -> EChanges:
    """
    Sets a component tree manually.
    
    :param component:        Component. 
    :param alignment:        Alignment to set. 
    """
    if component.alignment:
        raise ValueError( "This component already has an alignment. Did you mean to drop the existing alignment first?" )
    
    component.alignment = alignment
    
    return EChanges.COMP_DATA


@app.command( folder = constants.F_DROP )
def drop_alignment( component: Optional[List[Component]] = None ) -> EChanges:
    """
    Removes the alignment data from the component.
    If no component is specified, drops all alignments.
    :param component: Component to drop the alignment for, or `None` for all.
    """
    to_do = cli_view_utils.get_component_list( component )
    count = 0
    
    for component_ in to_do:
        component_.alignment = None
        count += 1
    
    pr.printx( "<verbose>{} alignments removed across {} components.</verbose>".format( count, len( to_do ) ) )
    
    return EChanges.COMP_DATA


@app.command( names = ["print_alignments", "alignments"], folder = constants.F_PRINT )
def print_alignments( component: Optional[List[Component]] = None, x = 1, n = 0, file: str = "" ) -> EChanges:
    """
    Prints the alignment for a component.
    
    :param file:        File to write to. See `file_write_help`. If this is empty then colours and headings are also printed. 
    :param component:   Component to print alignment for. If not specified prints all alignments.
    :param x:           Starting index (where 1 is the first site).
    :param n:           Number of sites to display. If zero a number of sites appropriate to the current UI will be determined.
    """
    to_do = cli_view_utils.get_component_list( component )
    m = global_view.current_model()
    
    if not n:
        n = Controller.ACTIVE.console_width - 5
    
    r = []
    
    colour = not file
    sec = colour or len( to_do ) > 1
    
    for component_ in to_do:
        if sec:
            r.append( "<section name='Component {}'>".format( pr.escape( component_ ) ) )
        
        if component_.alignment is None:
            raise ValueError( "No alignment is available for this component. Did you remember to run `align` first?" )
        else:
            if colour:
                r.append( cli_view_utils.colour_fasta_ansi( component_.alignment, m.site_type, m, x, n ) )  # TODO: Should provide XML element defining the style instead of formatting within this function
            else:
                r.append( component_.alignment )
        
        if sec:
            r.append( "</section>" )
    
    with io_helper.open_write( file ) as file_out:
        file_out.write( "\n".join( r ) + "\n" )
    
    return EChanges.INFORMATION
