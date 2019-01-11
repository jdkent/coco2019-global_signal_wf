from nipype import Node, Workflow
from nipype.interfaces import fsl
from nipype.interfaces.utility import IdentityInterface

def init_global_signal():
    input_node = Node(interface=IdentityInterface(fields=['img']), name='input_node')
    output_node = Node(interface=IdentityInterface(fields=['timeseries']), name='output_node')

    bet = Node(fsl.BET(functional=True), name='bet')
    extract = Node(fsl.ImageMeants(), name='extract')

    wf = Workflow(name='global_signal')

    wf.connect([
        (input_node, bet, [('img', 'in_file')]),
        (input_node, extract, [('img', 'in_file')]),
        (bet, extract, [('mask_file', 'mask')]),
        (extract, output_node, [('out_file', 'timeseries')]),
    ])

    return wf