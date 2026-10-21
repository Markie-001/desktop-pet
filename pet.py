import sys
from PySide6.QtCore import Qt, QRect
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QApplication, QLabel

SIZE, SCALE = 32, 4

app = QApplication(sys.argv)

pet = QLabel()
pet.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.Tool)
pet.setAttribute(Qt.WA_TranslucentBackground)
pet.setAttribute(Qt.WA_MacAlwaysShowToolWindow)  # keeps it visible on Mac

sheet = QPixmap("assets/cat.png")
frame = sheet.copy(QRect(0, 0, SIZE, SIZE))           # first idle frame
frame = frame.scaled(SIZE * SCALE, SIZE * SCALE, Qt.KeepAspectRatio, Qt.FastTransformation)

pet.setPixmap(frame)
pet.resize(frame.size())
pet.mousePressEvent = lambda e: app.quit()             # click the cat to close it
pet.show()

sys.exit(app.exec())