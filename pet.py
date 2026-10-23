import sys
import random
from PySide6.QtCore import Qt, QRect, QTimer
from PySide6.QtGui import QPixmap, QTransform
from PySide6.QtWidgets import QApplication, QLabel

SIZE, SCALE, COLUMNS = 32, 4, 6

# Animations: (first picture, number of pictures)
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
# Frame speed in ms 😂
SPEED = {"idle": 250, "walk": 120, "sit": 300, "sleep": 500,
         "drag": 150, "fall": 150, "land": 120, "happy": 200}

anim, frame, facing, pet_x = "walk", 0, 1, 100

# Start the app and make the cat window
app = QApplication(sys.argv)
pet = QLabel()
pet.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.Tool)
pet.setAttribute(Qt.WA_TranslucentBackground)
pet.setAttribute(Qt.WA_MacAlwaysShowToolWindow)
pet.resize(SIZE * SCALE, SIZE * SCALE)
sheet = QPixmap("assets/cat.png")

# Show the current picture
def show_frame():
    number = ANIMATION[anim][0] + frame
    picture = sheet.copy(QRect(number % COLUMNS * SIZE, number // COLUMNS * SIZE, SIZE, SIZE))
    if facing == -1:
        picture = picture.transformed(QTransform().scale(-1, 1))
    pet.setPixmap(picture.scaled(SIZE * SCALE, SIZE * SCALE, Qt.KeepAspectRatio, Qt.FastTransformation))

# Next picture
def next_frame():
    global frame
    frame = (frame + 1) % ANIMATION[anim][1]
    show_frame()

# Switch animation
def play(name):
    global anim, frame
    anim, frame = name, 0
    show_frame()
    timer.start(SPEED[anim])

# Walk and turn at the edges
def move():
    global pet_x, facing
    area = pet.screen().availableGeometry()
    if anim == "walk":
        pet_x += 2 * facing
        if pet_x <= area.left():
            facing = 1
        if pet_x >= area.right() - pet.width():
            facing = -1
    pet.move(pet_x, area.bottom() - pet.height())

# Doing random things
def change_mood():
    global facing
    choice = random.choice(["walk", "walk", "idle", "sit", "sleep"])
    facing = random.choice([1, -1])
    play(choice)
    mood_timer.start(random.randint(10000, 20000) if choice == "sleep" else random.randint(3000, 8000))

# Left click for :)
def on_press(event):
    if event.button() == Qt.RightButton:
        app.quit()
# Right click for quit
def on_release(event):
    if event.button() == Qt.LeftButton:
        play("happy")
        mood_timer.start(2000)

# Timers
timer = QTimer()
timer.timeout.connect(next_frame)
mover = QTimer()
mover.timeout.connect(move)
mover.start(33)
mood_timer = QTimer()
mood_timer.timeout.connect(change_mood)
mood_timer.start(5000)

# Start
pet.mousePressEvent = on_press
pet.mouseReleaseEvent = on_release
play(anim)
pet.show()
sys.exit(app.exec())