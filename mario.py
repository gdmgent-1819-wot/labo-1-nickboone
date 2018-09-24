from sense_hat import SenseHat

sense = SenseHat()

X = [255, 0, 0]  # Red
O = [255, 255, 255]  # White
B = [139,69,19]  # Brown
W = [255,235,205] # Skin 
Z = [0,0,0] # Black


question_mark = [
O, O, X, X, X, X, O, O,
O, O, X, X, X, X, X, O,
O, O, B, B, W, W, W, O,
O, O, B, B, W, W, O, O,
O, O, W, X, O, Z, Z, O,
O, O, W, W, W, W, W, O,
O, O, X, X, X, X, O, O,
O, O, X, X, X, X, O, O
]
# when user pressed joystick the mario jumps
while True:
    for event in sense.stick.get_events():
        if format(event.action) == "pressed":
            
            question_mark = [
                O, O, X, X, X, X, O, O,
                O, O, X, X, X, X, X, O,
                O, O, B, B, W, W, W, O,
                O, O, B, B, W, W, O, O,
                O, O, W, X, O, Z, Z, O,
                O, O, W, W, W, W, W, O,
                O, O, X, X, X, X, O, O,
                O, O, O, O, O, O, O, O
                ]
            
            sense.set_pixels(question_mark)
        if format(event.action) == "released":
            question_mark = [
                O, O, X, X, X, X, O, O,
                O, O, X, X, X, X, X, O,
                O, O, B, B, W, W, W, O,
                O, O, B, B, W, W, O, O,
                O, O, W, X, O, Z, Z, O,
                O, O, W, W, W, W, W, O,
                O, O, X, X, X, X, O, O,
                O, O, X, X, X, X, O, O
                ]
            sense.set_pixels(question_mark)


sense.set_pixels(question_mark)