import sys
from PySide6.QtCore import Qt, QRect, QTimer
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QApplication, QLabel

SIZE, SCALE = 32, 4
COLUMNS = 6

ANIMATION = {
    "idle":  (1, 4),
    "walk":  (5, 6),
    "sit":   (11, 4),
    "sleep": (15, 4),
    "drag":  (19, 4),
    "fall":  (23, 2),
    "land":  (25, 3),
    "happy": (28, 4),
}

SPEED = {"idle": 250, "walk": 120, "sit": 300, "sleep": 500,
         "drag": 150, "fall": 150, "land": 120, "happy": 200}

app = QApplication(sys.argv)

pet = QLabel()
pet.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.Tool)
pet.setAttribute(Qt.WA_TranslucentBackground)
pet.setAttribute(Qt.WA_MacAlwaysShowToolWindow)

sheet = QPixmap("assets/cat.png")
def get_frame(number):
    x = (number % COLUMNS) * SIZE
    y = (number // COLUMNS) * SIZE
    picture = sheet.copy(QRect(x, y, SIZE, SIZE))
    return picture.scaled(SIZE * SCALE, SIZE * SCALE, Qt.KeepAspectRatio, Qt.FastTransformation)

anim = "idle"
frame = 0

def next_frame():
    global frame
    start, count = ANIMATION[anim]
    frame = (frame + 1) % count
    pet.setPixmap(get_frame(start + frame))

pet.setPixmap(get_frame(ANIMATION[anim][0]))

timer = QTimer()
timer.timeout.connect(next_frame)
timer.start(SPEED[anim])

pet.resize(SIZE * SCALE, SIZE * SCALE)
pet.mousePressEvent = lambda e: app.quit()
pet.show()

sys.exit(app.exec())