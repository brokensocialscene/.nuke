# ASSIGNING KNOB DEFAULTS

nuke.knobDefault('RotoPaint.feather_type','smooth')
nuke.knobDefault('RotoPaint.source_filter','0')
nuke.knobDefault('VectorBlur.uv','motion')
nuke.knobDefault('Bezier.output', 'alpha')
nuke.knobDefault('Blur.label', '[value size]')

nuke.knobDefault('Text.message',  '[format "%03d" [frame]] ')
nuke.knobDefault('RotoPaint.toolbar_source_translate_round','1')
nuke.knobDefault('Merge.label', '[value mix]')
nuke.knobDefault('TimeOffset.label', '[value time_offset]')

#ASSIGNING DEFAULTS TO PAINT.
#LTT = "lifetime"  "2"="single"
#OPC ="opacity"
nuke.knobDefault("RotoPaint.toolbox", '''bezier {
{ brush ltt 2 opc .4}
{ eraser ltt 2 opc .1}
{ clone ltt 2 opc .4}
{ blur ltt 2 opc .3}
{ sharpen ltt 2}
{ smear ltt 2}
{ reveal ltt 2 opc .3}
{ dodge ltt 2}
{ burn ltt 2}
}''')


##########################################################

#IMPORT
import setValue


##########################################################

#Adds the labelAutobackdrop.py script

import labelAutobackdrop
myToolbar = nuke.toolbar( 'Nodes' )
myToolbar.addCommand( 'Other/Backdrop', lambda:
labelAutobackdrop.autoBackdrop(), 'shift+b', icon='Backdrop.png')

##########################################################
