
import nuke

def setValue():

    # Lets be positive...
    exit = False

    # check whether to see nothing is selected
    try:
        test1 = nuke.selectedNode()
    except ValueError:
        nuke.message('No node(s) selected?')
        exit = True
   
    # check to see if node selection is of same type, ask to continue or not
    if not exit:
        readType = nuke.selectedNode().Class()
        for node in nuke.selectedNodes():
            if node.Class() != readType:
                exit = True
            else:
                pass
        if exit:
            nuke.message('Nodes are not of same class.')
   

    # Show GUI if all is ok so far   
    if not exit:
        gui()
   


   



def gui():

    # Fetch all available knobs, quick version
     #knobs = ' '.join(sorted(nuke.selectedNode().knobs()))

     # Fetch all available knobs, advanced version
    knobs_result = ''
    knobs_list = []
    hideNoneType = True

    #for node in nuke.selectedNodes():
    for knob in nuke.selectedNode().knobs():
        valueTypeArray = str.split( str( type( nuke.selectedNode()[knob].value() ) ), '\'' )
        thisRound = '"' + str( knob ) + ' (' + valueTypeArray[1] + ')"'
        if (hideNoneType) and (valueTypeArray[1] == 'NoneType'):
            # Skip NoneType
            pass
        else:
            knobs_list.append([ thisRound ])
    knobs_list.sort()
    for i in range(0, len(knobs_list)):
        knobs_result =  knobs_result + knobs_list[i][0] + ' '
    knobs = knobs_result

    # set some vars
    knobNameLabel = 'Knob name'
    knobValueLabel = 'Knob value'

    # launch gui
    p = nuke.Panel('Set selected nodes\' value to...')
    p.addEnumerationPulldown(knobNameLabel, knobs)
    p.addSingleLineInput(knobValueLabel, '')
    p.addButton('Cancel')
    p.addButton('Set value')
    ret = p.show()

    if ret != 0:
        # if not cancel...
        #knobName = p.value(knobNameLabel)
        knobNameWorking = str.split( p.value(knobNameLabel), ' (' )
        knobName = knobNameWorking[0]
        knobValue = p.value(knobValueLabel)
        execute(knobName, knobValue)





def execute(knobName, knobValue):

    exit = False
    valuePrevious = ''
    unknownFormat = False
    valueType = ''
    nodeNames = ''

    for node in nuke.selectedNodes():

        valuePrevious = node[knobName].value()
        nodeName = node.name()
        nodeNames = nodeNames + node.name() + ' '

        # Check whether value is float, int, list or string
        valueSelected = nuke.selectedNode()[knobName].value()
        valueTypeResponse = type( nuke.selectedNode()[knobName].value() )
        valueTypeArray = str.split( str(valueTypeResponse), '\'' )
        valueType = valueTypeArray[1]
        #print('DEBUG: ' + knobName + '=' + str(valueSelected) + ' and is of type ' + str(valueType) )


        # Transform into correct value type
        if valueType == 'float':
            try:
                setValue = float(knobValue)
            except:
                setValue = ''
                exit = True
        elif valueType == 'int':
            try:
                setValue = int(knobValue)
            except:
                setValue = ''
                exit = True
        elif valueType == 'str':
            setValue = str(knobValue)
        elif valueType == 'bool':
                if (str.lower(knobValue) == 'false') or (knobValue == '0'):
                    setValue = False
                elif (str.lower(knobValue) == 'true') or (knobValue == '1'):
                    setValue = True
                else:
                    setValue = ''
                    exit = True
        elif valueType == 'list':
            setValue = knobValue
            setValue = setValue.replace(" ", "").split(",")
        else:
            exit = True
            unknownFormat = True

       
        #print('Attempting to set value to: ' + str(setValue) + ' previous value: ' + str(node[knobName].value()) + ' exit?=' + str(exit))
        # Set value
        if not exit:
            try:
                node[knobName].setValue(setValue)
            except:
                exit = True
           

            if ( node[knobName].value() !=  setValue ) and ( valueType != 'list' ):
                # Value to set is not equal to the actual value now being in effect; meaning the value was not accepted. Do not perform check on lists.
                exit = True
   

    # If format was not covered in the if statement where we transform the value types...
    if unknownFormat:
        nuke.message('Not supported format type (' + str(valueType) + '). At least not for now. Let me know.')

    # Summary of what happened, unless error occured
    if not exit:
        nuke.message('Knob "' + str(knobName) + '" is now set to "' + str(setValue) + '" for:\n' + nodeNames )
    else:
        nuke.message('Error: The value you entered was not accepted.\n\nHint: The value of knob "' + str(knobName) + '" is currently set to "' + str(valuePrevious) + '" for ' + nodeName + '.')
