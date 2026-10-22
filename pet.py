import sys
import random
from PySide6.QtCore import Qt, QRect, QTimer
from PySide6.QtGui import QPixmap, QTransform
from PySide6.QtWidgets import QApplication, QLabel

SIZE, SCALE = 32, 4
COLUMNS = 6
facing = 1
# The animations of the pet :)
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
# The frame speed of the pet 😂 HAHAHAHAHAHA
SPEED = {"idle": 250, "walk": 120, "sit": 300, "sleep": 500,
         "drag": 150, "fall": 150, "land": 120, "happy": 200}
# Start the app
app = QApplication(sys.argv)

pet = QLabel()
pet.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.Tool)
pet.setAttribute(Qt.WA_TranslucentBackground)
pet.setAttribute(Qt.WA_MacAlwaysShowToolWindow)

sheet = QPixmap("assets/cat.png")

# Get the pic from the sheet
def get_frame(number):
    sheet_x = (number % COLUMNS) * SIZE
    sheet_y = (number // COLUMNS) * SIZE
    picture = sheet.copy(QRect(sheet_x, sheet_y, SIZE, SIZE))
    if facing == -1:
        picture = picture.transformed(QTransform().scale(-1, 1))
    return picture.scaled(SIZE * SCALE, SIZE * SCALE, Qt.KeepAspectRatio, Qt.FastTransformation)

anim = "walk"
frame = 0

# Next frame/picture
def next_frame():
    global frame
    start, count = ANIMATION[anim]
    frame = (frame + 1) % count
    pet.setPixmap(get_frame(start + frame))
pet.setPixmap(get_frame(ANIMATION[anim][0]))

# Switch animation
def play(name):
    global anim, frame
    anim = name
    frame = 0
    pet.setPixmap(get_frame(ANIMATION[anim][0]))
    timer.start(SPEED[anim])
    print("Now playing:", anim)

# Left click to change animation, right click to quit
def on_click(event):
    if event.button() == Qt.RightButton:
        app.quit()
        return
    play("happy")
    mood_timer.start(2000)

timer = QTimer()
timer.timeout.connect(next_frame)
timer.start(SPEED[anim])

# Walking and when reaching the edges it will turn
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

# Change what the cat is doing
def change_mood():
    global facing
    choice = random.choice(["walk", "walk", "idle", "sit", "sleep"])
    if choice == "walk":
        facing = random.choice([1, -1])
    play(choice)

    if choice == "sleep":
        mood_timer.start(random.randint(10000, 20000))
    else:
        mood_timer.start(random.randint(3000, 8000))

mood_timer = QTimer()
mood_timer.timeout.connect(change_mood)
mood_timer.start(5000)

pet.resize(SIZE * SCALE, SIZE * SCALE)
pet.mousePressEvent = on_click
pet.show()

sys.exit(app.exec())