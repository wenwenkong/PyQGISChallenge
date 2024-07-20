# iface is the instance of the currently running QGIS application,
# which is the interface of the QgisInterface classAttribute

title = iface.mainWindow().windowTitle()
print(title)
new_title = title.replace('QGIS', 'My QGIS')
iface.mainWindow().setWindowTitle(new_title)

# Change the icon in the title bar (only applicable to Windows users)
import os
icon = 'qgis-black.png'
data_dir = os.path.join(os.path.expanduser('~'), 'Downloads', 'pyqgis_masterclass')
icon_path = os.path.join(data_dir, icon)
icon = QIcon(icon_path)
iface.mainWindow().setWindowIcon(icon)

# Remove actions from menu bars
vector_menu = iface.vectorMenu()
raster_menu = iface.rasterMenu()
menubar = vector_menu.parentWidget()
menubar.removeAction(vector_menu.menuAction())
menubar.removeAction(raster_menu.menuAction())
menubar.addAction(vector_menu.menuAction())
menubar.addAction(raster_menu.menuAction())

# Add useful item in the Help meanu bar
# Also create a trigger 
import webbrowser

def open_website():
    webbrowser.open('https://gis.stackexchange.com')
    
website_action = QAction('Go to gis.stackexchange')
website_action.triggered.connect(open_website)
iface.helpMenu().addSeparator()
iface.helpMenu().addAction(website_action)

# Change visibility of a Toolbar
# Add a button to a toolbar
iface.pluginToolBar().setVisible(True)

import os
from datetime import datetime

icon = 'question.svg'
data_dir = os.path.join(os.path.expanduser('~'), 'Downloads', 'pyqgis_masterclass')
icon_path = os.path.join(data_dir, icon)

def show_time():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    iface.messageBar().pushInfo('Current Time', current_time)
    
action = QAction('Show Time')
action.triggered.connect(show_time)
action.setIcon(QIcon(icon_path))
iface.addToolBarIcon(action)

