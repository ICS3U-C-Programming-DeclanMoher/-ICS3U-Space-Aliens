import ugame
import stage 
import time
import random
import constants

def game_scene():
#this functino is the main game scene

#setting score
    score = 0
    
    def show_alien():
        #Moves the alien around the screen
        for alien_number in range(len(aliens)):
            if aliens[alien_number].x < 0:
                aliens[alien_number].move(random.randint(0 + constants.SPRITE_SIZE,constants.SCREEN_X - constants.SPRITE_SIZE), constants.OFF_TOP_SCREEN)
                break
    

    #importing background from files into 
    image_bank_background = stage.Bank.from_bmp16("mt_game_studio.bmp")
    image_bank_sprites = stage.Bank.from_bmp16("space_aliens.bmp")
    
    #buttons that keep state information
    a_button = constants.button_state["button_up"]
    b_button = constants.button_state["button_up"]
    start_button = constants.button_state["button_up"]
    select_button = constants.button_state["button_up"]

    #get sounds ready 
    pew_sound = open("pew.wav", 'rb')
    boom_sound = open("boom.wav", 'rb')

    # create the sound controller
    sound = ugame.audio
    sound.stop()
    sound.mute(False)


    #setting size for ship and background
    background = stage.Grid(image_bank_background, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y)
    for x_location in range(constants.SCREEN_GRID_X):
        for y_location in range (constants.SCREEN_GRID_Y):
            tile_picked = random.randint(1,3)
            background.tile(x_location,y_location, tile_picked)
    
    #create lasers for when we shoot
    ship = stage.Sprite(image_bank_sprites, 5, 75, constants.SCREEN_Y -(2 * constants.SPRITE_SIZE))

    aliens = []
    for alien_number in range(constants.TOTAL_NUMBER_OF_ALIENS):
        a_single_alien = stage.Sprite(image_bank_sprites, 9, constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)
        aliens.append(a_single_alien)

    show_alien()
   
    lasers = []
    for laser_number in range(constants.TOTAL_NUMBER_OF_LASERS):
        a_single_laser = stage.Sprite(image_bank_sprites, 10,constants.OFF_SCREEN_X,constants.OFF_SCREEN_Y)
        lasers.append(a_single_laser)
    #setting layers and size of the game 
    game = stage.Stage(ugame.display, constants.FPS)
    game.layers = lasers + [ship] + aliens + [background]

    #calling to render the game 
    game.render_block()

    while True:
        #user inputs and setting buttons to actions
        keys = ugame.buttons.get_pressed()
        
        if keys & ugame.K_O != 0:
            if a_button == constants.button_state["button_up"]:
                a_button = constants.button_state["button_just_pressed"]
            elif a_button == constants.button_state["button_just_pressed"]:
                a_button = constants.button_state["button_still_pressed"]
        else:
            if a_button == constants.button_state["button_still_pressed"]:
                a_button = constants.button_state["button_released"]
            else:
                a_button = constants.button_state["button_up"]
        if keys & ugame.K_X != 0:
            pass
        if keys & ugame.K_START != 0:
            pass
        if keys & ugame.K_SELECT != 0:
            pass
        if keys & ugame.K_RIGHT != 0:
            if ship.x < (constants.SCREEN_X - constants.SPRITE_SIZE):
                ship.move(ship.x + 1, ship.y)
            else:
                ship.move((0), ship.y)

        if keys & ugame.K_LEFT != 0:
            if ship.x > 0:
                ship.move((ship.x -constants.SPRITE_MOVEMENT_SPEED), ship.y)
            else:
                ship.move(constants.SCREEN_X - constants.SPRITE_SIZE, ship.y)

        if keys & ugame.K_UP != 0:
            pass
        if keys & ugame.K_DOWN != 0:
            pass

        if keys & ugame.K_X:
            pass
        if keys & ugame.K_O:
            pass
        if keys & ugame.K_START:
            pass
        if keys & ugame.K_SELECT:
            pass
#creating borders
        if keys & ugame.K_RIGHT:
            if ship.x <= constants.SCREEN_X - constants.SPRITE_SIZE:
                ship.move(ship.x + 1, ship.y)
        else:
            pass
#creating borders
        if keys & ugame.K_LEFT:
            if ship.x >= 0:
                ship.move(ship.x - 1, ship.y)
        else:
            pass
        if keys & ugame.K_UP:
            pass
        if keys & ugame.K_DOWN:
            pass


        if a_button == constants.button_state["button_just_pressed"]:
            for laser_number in range(len(lasers)):
                if lasers[laser_number].x < 0:
                    lasers[laser_number].move(ship.x, ship.y)
                    sound.play(pew_sound)
                    break

        for laser_number in range(len(lasers)):
            if lasers[laser_number].x > 0:
                lasers[laser_number].move(lasers[laser_number].x, lasers[laser_number].y-constants.LASER_SPEED)
                if lasers[laser_number].y< constants.OFF_TOP_SCREEN:
                    lasers[laser_number].move(constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)
            

        for alien_number in range(len(aliens)):
            if aliens[alien_number].x > 0:
                aliens[alien_number].move(aliens[alien_number].x, aliens[alien_number].y + constants.ALIEN_SPEED)
                if aliens[alien_number].y > constants.SCREEN_Y:
                    aliens[alien_number].move(constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)
                    show_alien()


        for laser_number in range(len(lasers)):
            if lasers[laser_number].x > 0:
                for alien_number in range(len(aliens)):
                    if aliens[alien_number].x > 0:
                        if stage.collide(lasers[laser_number].x + 6,lasers[laser_number].y + 2,
                                        lasers[laser_number].x + 11 ,lasers[laser_number].y + 12,
                                        aliens[alien_number].x + 1,aliens[alien_number].y,
                                        aliens[alien_number].x + 15,aliens[alien_number].y + 15):

                            aliens[alien_number].move(constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)
                            lasers[laser_number].move(constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)
                            # sound.stop()
                            # sound.play(boom_sound)
                            # sound.stop()
                            show_alien()
                            show_alien()
                            score = score + 1

#redraw sprites
    game.render_sprites (lasers + [ship] + aliens)
    game.tick()

def splash_scene():
#splash scene function

    #importing background from files into code
    image_bank_dumb_background = stage.Bank.from_bmp16("mt_game_studio.bmp")


        #sets the background to image 0 in image bank 
    background = stage.Grid(image_bank_dumb_background, constants.SCREEN_X,constants.SCREEN_Y)

    background.tile(2, 2, 0)  # blank white

    background.tile(3, 2, 1)

    background.tile(4, 2, 2)

    background.tile(5, 2, 3)

    background.tile(6, 2, 4)

    background.tile(7, 2, 0)  # blank white

    background.tile(2, 3, 0)  # blank white

    background.tile(3, 3, 5)

    background.tile(4, 3, 6)

    background.tile(5, 3, 7)

    background.tile(6, 3, 8)

    background.tile(7, 3, 0)  # blank white


    background.tile(2, 4, 0)  # blank white

    background.tile(3, 4, 9)

    background.tile(4, 4, 10)

    background.tile(5, 4, 11)

    background.tile(6, 4, 12)

    background.tile(7, 4, 0)  # blank white



    background.tile(2, 5, 0)  # blank white

    background.tile(3, 5, 0)

    background.tile(4, 5, 13)

    background.tile(5, 5, 14)

    background.tile(6, 5, 0)

    background.tile(7, 5, 0)  # blank white

    #setting layers and size of the game 
    game = stage.Stage(ugame.display, constants.FPS)
    game.layers = [background]

    #calling to render the game 
    game.render_block()

    while True:
        #waits 2 seconds
        time.sleep(2.0)
        menu_scene()


def menu_scene():
    #importing background from files into 
    image_bank_background = stage.Bank.from_bmp16("space_aliens_background.bmp")
    
    #adds text objects
    text = []
    text1 = stage.Text(width=29, height=12, font=None, palette=constants.RED_PALETTE, buffer=None)
    text1.move(20, 10)
    text1.text("Mac Game Studios")
    text.append(text1)

    text2 = stage.Text(width=29, height=12, font=None, palette=constants.RED_PALETTE, buffer=None)
    text2.move(40, 110)
    text2.text("PRESS START")
    text.append(text2)

    #sets the background to image 0 in image bank 
    background = stage.Grid(image_bank_background, constants.SCREEN_X,constants.SCREEN_Y)


    #setting layers and size of the game 
    game = stage.Stage(ugame.display, constants.FPS)
    game.layers = text + [background]

    #calling to render the game 
    game.render_block()

    while True:
        #user inputs and setting buttons to actions
        keys = ugame.buttons.get_pressed()
    
        #updating the every second
       
        if keys & ugame.K_START != 0:
            game_scene()
    



if __name__ == "__main__":
    splash_scene()