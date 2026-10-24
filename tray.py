from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QSystemTrayIcon, QMenu


# Make the tray icon with a menu
def make_tray(picture, actions):
    menu = QMenu()
    for name, action in actions.items():
        menu.addAction(name, action)
    tray = QSystemTrayIcon(QIcon(picture))
    tray.setContextMenu(menu)
    tray.show()
    return tray, menu