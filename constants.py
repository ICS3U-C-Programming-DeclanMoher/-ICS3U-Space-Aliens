#pybagde is set to the size of 160x128 aswell with sprites being 16x16
SCREEN_X = 160
SCREEN_Y = 128
SCREEN_GRID_X = 10
SCREEN_GRID_Y = 8
SPRITE_SIZE = 16
TOTAL_NUMBER_OF_ALIENS = 4
TOTAL_NUMBER_OF_LASERS = 5
SHIP_SPEED = 1.3
ALIEN_SPEED = 1
LASER_SPEED = 3.5
OFF_SCREEN_X = -100
OFF_SCREEN_Y = -100
OFF_TOP_SCREEN = -1* SPRITE_SIZE
OFF_BOTTOM_SCREEN = SCREEN_Y + SPRITE_SIZE
FPS = 60
SPRITE_MOVEMENT_SPEED = 1


#button state for maintianing information
button_state ={
    "button_up" : "up",
"button_just_pressed": "just pressed",
"button_still_pressed" : "still pressed",
"button_released" : "released"
}

#new pallet for red filled text
RED_PALETTE = (b'\xff\xff\x00\x22\xcey\x22\xff\xff\xff\xff\xff\xff\xff\xff\xff'
b'\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff')