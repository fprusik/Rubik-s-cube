import pygame

pygame.init()
DIS_WIDTH = 1000
DIS_HEIGHT = 800
dis = pygame.display.set_mode((DIS_WIDTH, DIS_HEIGHT), pygame.DOUBLEBUF)
pygame.display.set_caption('Rubik\'s Cube')
BLUE = (54, 180, 240, 255)
CGREY = (59, 68, 72, 255)
CRED = (222, 14, 68, 255)
CWHITE = (255, 255, 255, 255)
clock = pygame.time.Clock()
dis.fill(CGREY)
white_rect = pygame.Rect(0, 0, 300, 300)
white_rect.center = (DIS_WIDTH/2, DIS_HEIGHT/2)

pygame.display.update()

class MousePointer():
    def __init__(self):
        self.mouse_x, self.mouse_y = pygame.mouse.get_pos()
        self.prev_mouse_x = 0
        self.prev_mouse_y = 0
        self.change_state = False
        self.moving_active = False

    def mouse_in_rect(self)-> bool:
        '''Check if mouse is inside the rect and return bool value'''
        if ( self.mouse_x in range(white_rect.topleft[0], white_rect.topright[0]) 
        and ( self.mouse_y in range(white_rect.topleft[1], white_rect.bottomleft[1]))):
            #print('IN')
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
            return True
        elif self.change_state:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
            return True
        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
            return False

def game_loop()-> None:
    while True:
        for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    quit()

        # Get position of the mouse and load it to variables            
        mpointer.mouse_x, mpointer.mouse_y = pygame.mouse.get_pos()
        # If mouse is inside the rectangle and scroll is clicked, set flag
        if mpointer.mouse_in_rect() and pygame.mouse.get_pressed()[1]: 
            mpointer.moving_active = True
        # If flag is set and scroll is still pressed, move rectangle
        if mpointer.moving_active and pygame.mouse.get_pressed()[1]:
            # Check if it's first click in this turn
            if not mpointer.change_state: 
                mpointer.change_state = True
                mpointer.prev_mouse_x, mpointer.prev_mouse_y = mpointer.mouse_x, mpointer.mouse_y
            else:
                # Check if there was some movements of the mouse. If yes, draw rectangle in new position
                if mpointer.prev_mouse_x != mpointer.mouse_x or mpointer.prev_mouse_y != mpointer.mouse_y:
                    # Calculate differences between old and new values
                    diff_x = mpointer.mouse_x - mpointer.prev_mouse_x
                    diff_y = mpointer.mouse_y - mpointer.prev_mouse_y
                    # Enter differences into rectangle's position
                    white_rect.center = (white_rect.center[0] + diff_x, white_rect.center[1] + diff_y)
                    # Update old values
                    mpointer.prev_mouse_x = mpointer.mouse_x
                    mpointer.prev_mouse_y = mpointer.mouse_y
        else:
            # If scroll is not pressed
            mpointer.change_state = False
            mpointer.moving_active = False

        # Erase old view and draw the rectangle
        dis.fill(CGREY)    
        pygame.draw.rect(dis, CWHITE, white_rect)
        
        # Update the view
        pygame.display.flip()
        clock.tick(60)



mpointer = MousePointer()
game_loop()
pygame.quit()
quit()
