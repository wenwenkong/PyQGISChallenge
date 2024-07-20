# Code to delete the 2nd column from the shoreline.shp
layer = iface.activeLayer()
layer.startEditing()
layer.deleteAttribute(1)
# layer.commitChanges()
layer.rollBack()
