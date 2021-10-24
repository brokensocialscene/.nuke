

import nuke

nameLabel = ""
enumerationPulldown = " 42 50 70 90 "
enumerationColour = " Grey Blue Green Yellow"

def autoBackdrop():

  global nameLabel, enumerationPulldown, enumerationColour
  selNodes = nuke.selectedNodes()
  if not selNodes:
    return nuke.nodes.BackdropNode()


 
  p = nuke.Panel('Label')
  p.addSingleLineInput("Label Name", nameLabel)
  p.addEnumerationPulldown("Font Size:", enumerationPulldown)
  p.addEnumerationPulldown("Colour:", enumerationColour)
  result = p.show()
  nameLabel = p.value("Label Name")
  enumVal = p.value("Font Size:")
  enumCol = p.value("Colour:")
  if enumCol == "Grey":
    r = 0.353
    g = 0.353
    b = 0.353
  if enumCol == "Blue":
    r = 0.39
    g = 0.45
    b = 0.48
  if enumCol == "Green":
    r = 0.39
    g = 0.44
    b = 0.38
  if enumCol == "Yellow":
    r = 0.53
    g = 0.52
    b = 0.35
  if enumCol == None:
    r = 0.18
    g = 0.18
    b = 0.18
  hexColour = int('%02x%02x%02x%02x' % (r*255,g*255,b*255,1),16)


  # Calculate bounds for the backdrop node.
  bdX = min([node.xpos() for node in selNodes])
  bdY = min([node.ypos() for node in selNodes])
  bdW = max([node.xpos() + node.screenWidth() for node in selNodes]) - bdX
  bdH = max([node.ypos() + node.screenHeight() for node in selNodes]) - bdY
 
  # Expand the bounds to leave a little border. Elements are offsets for left, top, right and bottom edges respectively
  left, top, right, bottom = (-30, -99, 30, 30)
  bdX += left
  bdY += top
  bdW += (right - left)
  bdH += (bottom - top)

  if enumCol == None:
    pass
  else:
  
    n = nuke.nodes.BackdropNode(xpos = bdX,
    bdwidth = bdW,
    ypos = bdY,
    bdheight = bdH,
    note_font = 'Bitstream Vera Sans',
    label = nameLabel,
    note_font_size=enumVal,
    name = nameLabel,
    tile_color = hexColour,
    gl_color = hexColour)
