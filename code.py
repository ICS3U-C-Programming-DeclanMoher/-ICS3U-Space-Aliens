import ugame
import stage 
import time
import random
import constants

def game_scene():
    #importing background from files into 
    image_bank_background = stage.Bank.from_bmp16("space_aliens_background.bmp")
    image_bank_sprites = stage.Bank.from_bmp16("space_aliens.bmp")
    
    #sets the background to image 0 in image bank 
    background = stage.Grid(image_bank_background, constants.SCREEN_X,constants.SCREEN_Y)
    
    #buttons that keep state information
    a_button = constants.button_state["button_up"]
    b_button = constants.button_state["button_up"]
    start_button = constants.button_state["button_up"]
    select_button = constants.button_state["button_up"]

    #get sound ready 
    pew_sound = open("pew.wav", 'rb')
    sound = ugame.audio
    sound.stop()
    sound.mute(False)

    #setting size for ship and background
    background = stage.Grid(image_bank_background, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y)
    ship = stage.Sprite(image_bank_sprites, 5, 75, constants.SCREEN_Y -(2 * constants.SPRITE_SIZE))
    alien = stage.Sprite(image_bank_sprites, 9,
    int(constants.SCREEN_X / 2 - constants.SPRITE_SIZE / 2),
    16)

    #setting layers and size of the game 
    game = stage.Stage(ugame.display, constants.FPS)
    game.layers = [ship] + [background]

    #calling to render the game 
    game.render_block()

    while True:
        #user inputs and setting buttons to actions
        keys = ugame.buttons.get_pressed()
        
        #updating the every second
        game.render_sprites ([ship] + [alien])
        game.tick()

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
                ship.move((constants.SCREEN_X - constants.SPRITE_SIZE), ship.y)

        if keys & ugame.K_LEFT != 0:
            if ship.x > 0:
                ship.move((ship.x -constants.SPRITE_MOVEMENT_SPEED), ship.y)
            else:
                ship.move(0, ship.y)

            if keys & ugame.K_UP != 0:
                pass
            if keys & ugame.K_DOWN != 0:
                pass
    #playing pew sound when a button pressed 
        if a_button == constants.button_state["button_just_pressed"]:
            sound.play(pew_sound)            
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

def splash_scene():
#splash scene function

    #importing background from files into code
    image_bank_dumb_background = stage.Bank.from_bmp16("dumb_game_studio.bmp")


    #sets the background to image 0 in image bank 
    background = stage.Grid(image_bank_background, constants.SCREEN_X,constants.SCREEN_Y)

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
    menu_scene()