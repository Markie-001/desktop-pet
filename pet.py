import sys
from PySide6.QtCore import Qt, QRect, QTimer
from PySide6.QtGui import QPixmap, QTransform
from PySide6.QtWidgets import QApplication, QLabel

SIZE, SCALE = 32, 4
COLUMNS = 6
facing = 1

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
    sheet_x = (number % COLUMNS) * SIZE
    sheet_y = (number // COLUMNS) * SIZE
    picture = sheet.copy(QRect(sheet_x, sheet_y, SIZE, SIZE))
    if facing == -1:
        picture = picture.transformed(QTransform().scale(-1, 1))
    return picture.scaled(SIZE * SCALE, SIZE * SCALE, Qt.KeepAspectRatio, Qt.FastTransformation)

anim = "walk"
frame = 0

def next_frame():
    global frame
    start, count = ANIMATION[anim]
    frame = (frame + 1) % count
    pet.setPixmap(get_frame(start + frame))
pet.setPixmap(get_frame(ANIMATION[anim][0]))

def play(name):
    global anim, frame
    anim = name
    frame = 0
    pet.setPixmap(get_frame(ANIMATION[anim][0]))
    timer.start(SPEED[anim])
    print("Now playing:", anim)

def on_click(event):
    global facing
    if event.button() == Qt.RightButton:
        app.quit()
        return
    names = list(ANIMATION)
    position = names.index(anim)
    next_name = names[(position + 1) % len(names)]
    if next_name == "idle":
        facing = -facing
    play(next_name)

timer = QTimer()
timer.timeout.connect(next_frame)
timer.start(SPEED[anim])

pet_x = 100
def move():
    global pet_x, facing
    area = pet.screen().availableGeometry()
    pet_y = area.y() + area.height() - pet.height()

    if anim == "walk":
        pet_x = pet_x + 2 * facing
        if pet_x < area.left():
            pet_x = area.left()
            facing = 1
        if pet_x > area.right() - pet.width():
            pet_x = area.right() - pet.width()
            facing = -1
    pet.move(pet_x, pet_y)

mover = QTimer()
mover.timeout.connect(move)
mover.start(33)

pet.resize(SIZE * SCALE, SIZE * SCALE)
pet.mousePressEvent = on_click
pet.show()

sys.exit(app.exec())