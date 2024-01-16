import ugame
import stage 
import time
import random
import constants
import supervisor

def game_scene():
#this functino is the main game scene

#setting score
    score = 0
    
    score_text = stage.Text(width=29, height=14)
    score_text.clear()
    score_text.cursor(0,0)
    score_text.move(1,1)
    score_text.text("Score: {0}".format(score))
    

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
    pew2_sound = open("pew2.wav", 'rb')
    crash_sound = open("crash.wav", 'rb')
    intro_sound = open("fanfare_x.wav", 'rb')
    dead_sound = open("hit_with_frying_pan_y.wav", 'rb')
    bell_sound = open("boxing_bell.wav", 'rb')
    # create the sound controller
    sound = ugame.audio
    sound.stop()
    sound.mute(False)

    sound.play(bell_sound)


    #setting size for ship and background
    background = stage.Grid(image_bank_background, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y)
    for x_location in range(constants.SCREEN_GRID_X):
        for y_location in range (constants.SCREEN_GRID_Y):
            tile_picked = random.randint(1,3)
            background.tile(x_location,y_location, tile_picked)
    
    #create lasers for when we shoot
    ship = stage.Sprite(image_bank_sprites, 5, 75, constants.SCREEN_Y -(2 * constants.SPRITE_SIZE))

#spawning more aliens
    aliens = []
    for alien_number in range(constants.TOTAL_NUMBER_OF_ALIENS):
        a_single_alien = stage.Sprite(image_bank_sprites, 9, constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)
        aliens.append(a_single_alien)

    show_alien()
   
   #spawning more lasers
    lasers = []
    for laser_number in range(constants.TOTAL_NUMBER_OF_LASERS):
        a_single_laser = stage.Sprite(image_bank_sprites, 10,constants.OFF_SCREEN_X,constants.OFF_SCREEN_Y)
        lasers.append(a_single_laser)

    
    #setting layers and size of the game 
    game = stage.Stage(ugame.display, constants.FPS)
    game.layers = [score_text] + lasers + [ship] + aliens + [background]

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

        #moving the ship left and right 
        if keys & ugame.K_RIGHT != 0:
            if ship.x < (constants.SCREEN_X - constants.SPRITE_SIZE):
                ship.move(ship.x + 1, ship.y)
            else:
                ship.move(0, ship.y)

        if keys & ugame.K_LEFT != 0:
            if ship.x > 0:
                ship.move(ship.x -constants.SPRITE_MOVEMENT_SPEED, ship.y)
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
        if keys & ugame.K_UP:
            pass
        if keys & ugame.K_DOWN:
            pass

            #shooting lasers
        if a_button == constants.button_state["button_just_pressed"]:
            for laser_number in range(len(lasers)):
                if lasers[laser_number].x < 0:
                    lasers[laser_number].move(ship.x, ship.y)
                    sound.play(pew2_sound)
                    break

            #moving the lasers
        for laser_number in range(len(lasers)):
            if lasers[laser_number].x > 0:
                lasers[laser_number].move(lasers[laser_number].x, lasers[laser_number].y-constants.LASER_SPEED)
                if lasers[laser_number].y< constants.OFF_TOP_SCREEN:
                    lasers[laser_number].move(constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)
            
            #moving,hitting and score
        for alien_number in range(len(aliens)):
            if aliens[alien_number].x > 0:
                aliens[alien_number].move(aliens[alien_number].x, aliens[alien_number].y + constants.ALIEN_SPEED)
                if aliens[alien_number].y > constants.SCREEN_Y:
                    aliens[alien_number].move(constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)
                    show_alien()
                    score -= 1
                    if score < 0:
                        score = 0
                    score_text.clear()
                    score_text.cursor(0,0)
                    score_text.move(1,1)
                    score_text.text("Score: {0}".format(score))

        #colliding with lasers
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
                            sound.play(crash_sound)
                            show_alien()
                            show_alien()
                            score += 1
                            score_text.clear()
                            score_text.cursor(0,0)
                            score_text.move(1,1)
                            score_text.text("Score: {0}".format(score))
            #die from aliens
        for alien_number in range(len(aliens)):
            if aliens[alien_number].x > 0:
                if stage.collide(aliens[alien_number].x + 1, aliens[alien_number].y,
                                aliens[alien_number].x + 15, aliens[alien_number].y + 15,
                                ship.x, ship.y,
                        ship.x + 15, ship.y + 15):
                    #alien hit the ship
                        sound.stop()
                        sound.play(dead_sound)
                        time.sleep(3)
                        game_over_scene(score)

#redraw sprites
        game.render_sprites (lasers + [ship] + aliens)
        game.tick()

def splash_scene():
#splash scene function

    intro_sound = open("fanfare_x.wav", 'rb')
    sound = ugame.audio
    sound.stop()
    sound.mute(False)
    sound.play(intro_sound)

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
    
def game_over_scene(final_score):
    #this function displays game over scene

    #turns off sound from game or last scene
    sound = ugame.audio
    sound.stop()

    #plays end game sound
    outro_sound = open("snore_x.wav", 'rb')
    sound = ugame.audio
    sound.stop()
    sound.mute(False)
    sound.play(outro_sound)

    #image background for when game over
    image_bank_2 = stage.Bank.from_bmp16("darksouls.bmp")

    background = stage.Grid(image_bank_2, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y)


    text = []
    text1 = stage.Text(width=29, height=14, font=None, palette=constants.RED_PALETTE, buffer=None)
    text1.move(22, 20)
    text1.text("Final Score: {:0>3d}".format(final_score))
    text.append(text1)

    text = []
    text2 = stage.Text(width=29, height=14, font=None, palette=constants.RED_PALETTE, buffer=None)
    text2.move(43, 60)
    text2.text("GAME OVER")
    text.append(text1)

    text3 = stage.Text(width=29, height=14, font=None, palette=constants.RED_PALETTE, buffer=None)
    text3.move(32, 110)
    text3.text("PRESS SELECT")
    text.append(text3)

    # creates a stage for the background to show up with 60FPS
    game = stage.Stage(ugame.display, constants.FPS)
    #Sets layers
    game.layers = text + [background]
    #rendering background to location of sprite list 
    game.render_block()

    #repeat forever game loop
    while True:
        # get input 
        keys = ugame.buttons.get_pressed()

        #start button to restart the game 
        if keys & ugame.K_SELECT != 0:
            supervisor.reload()

            #updat game logic
            game.tick()
if __name__ == "__main__":
    splash_scene()