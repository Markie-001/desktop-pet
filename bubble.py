from PySide6.QtCore import Qt, QTimer
from PySide6.QtWidgets import QLabel

def make_bubble():
    bubble = QLabel()
    bubble.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.Tool)
    bubble.setAttribute(Qt.WA_MacAlwaysShowToolWindow)
    bubble.setWordWrap(True)
    bubble.setMaximumWidth(250)
    bubble.setStyleSheet(
        "background: white; color: #2b2140; border: 3px solid #2b2140;"
        "padding: 6px 10px; font: bold 13px 'Courier New';"
    )
    return bubble

def text_bubble(bubble, pet, text):
    bubble.setText(text)
    bubble.adjustSize()
    bubble.move(pet.x() + pet.width() // 2 - bubble.width() // 2, pet.y() - bubble.height())
    bubble.show()
    QTimer.singleShot(4000, bubble.hide)