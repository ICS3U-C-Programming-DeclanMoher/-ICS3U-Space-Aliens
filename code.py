import ugame
import stage 

import constants

def game_scene():
    #importing background from files into 
    image_bank_background = stage.Bank.from_bmp16("space_aliens_background.bmp")
    image_bank_sprites = stage.Bank.from_bmp16("space_aliens.bmp")

#setting size for ship and background
    background = stage.Grid(image_bank_background, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y)
    ship = stage.Sprite(image_bank_sprites, 5, 75, constants.SCREEN_Y -(2 * constants.SPRITE_SIZE))

#setting layers and size of the game 
    game = stage.Stage(ugame.display, constants.FPS)
    game.layers = [ship] + [background]

    #calling to render the game 
    game.render_block()

    while True:
    #updating the every second
        game.render_sprites ([ship])
        game.tick()

    #user inputs and setting buttons to actions
        keys = ugame.buttons.get_pressed()

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

            pass
if __name__ == "__main__":
    game_scene()