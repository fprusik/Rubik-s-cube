from cmath import cos, pi, sin
import pygame
import math

pygame.init()
DIS_WIDTH = 1000
DIS_HEIGHT = 800
RECT_WIDTH = 180
RECT_HEIGHT = 180
dis = pygame.display.set_mode((DIS_WIDTH, DIS_HEIGHT), pygame.DOUBLEBUF)
pygame.display.set_caption('Rubik\'s Cube')
BLUE = (54, 180, 240, 255)
CGREY = (59, 68, 72, 255)
CRED = (222, 14, 68, 255)
CWHITE = (255, 255, 255, 255)
CGREEN = (127, 255, 212, 255)
clock = pygame.time.Clock()
dis.fill(CGREY)
white_rect = pygame.Rect(0, 0, RECT_WIDTH, RECT_HEIGHT)
white_rect.center = (DIS_WIDTH/2, DIS_HEIGHT/2)
polygon_list = [(DIS_WIDTH/3-50, DIS_HEIGHT/3+50), (DIS_WIDTH/3-50, DIS_HEIGHT/3-50), 
(DIS_WIDTH/3+50, DIS_HEIGHT/3-50), (DIS_WIDTH/3+50, DIS_HEIGHT/3+50)]
rad = 50
#vertices = [math.pi/4, 3*math.pi/4, 5*math.pi/4, 7*math.pi/4]
x1 = 200
y1 = 400
h = 300
w = 300
point1 = [x1,y1]
point2 = [x1,y1-h]
point3 = [x1+w,y1-h]
point4 = [x1+w,y1]
# point1 = [200,400]
# point2 = [200,100]
# point3 = [500,100]
# point4 = [500,400]
#pol_list = [[200,200], [200,100], [300,100], [300,200]]

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
    x_axis=0
    while True:
        for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    quit()

        # Get position of the mouse and load it to variables            
        mpointer.mouse_x, mpointer.mouse_y = pygame.mouse.get_pos()
        # If mouse is inside the rectangle and scroll is clicked, set flag
        # if mpointer.mouse_in_rect() and pygame.mouse.get_pressed()[1]: 
        if pygame.mouse.get_pressed()[1]: 
            mpointer.moving_active = True
        # If flag is set and scroll is still pressed, move rectangle
        if mpointer.moving_active and pygame.mouse.get_pressed()[1]:
            # Check if it's first click in this turn
            if not mpointer.change_state: 
                mpointer.change_state = True
                mpointer.prev_mouse_x, mpointer.prev_mouse_y = mpointer.mouse_x, mpointer.mouse_y
            else:
                # Check if there was some movements of the mouse. If yes, draw new dimensions
                if mpointer.prev_mouse_x != mpointer.mouse_x or mpointer.prev_mouse_y != mpointer.mouse_y:
                    # Calculate differences between old and new values
                    diff_x = mpointer.mouse_x - mpointer.prev_mouse_x
                    diff_y = mpointer.mouse_y - mpointer.prev_mouse_y

                    x_axis += diff_x
                    if x_axis >= 359: x_axis=0
                    elif x_axis < 0: x_axis = 359
                    # if diff_x < 0:
                    #     if point1[1] <= point4[1]:
                    #         if point1[0] <= point4[0]:
                    #             print(point1[0])
                    #             print(point4[0])
                    #             point1[1] += diff_x
                    #             point2[1] -= diff_x
                    #             point3[0] += 4*diff_x # (+) and (-) gives (-)
                    #             point4[0] += 4*diff_x # (+) and (-) gives (-)
                    #             if point1[0] >= point4[0]:
                    #                 point4[0] = point1[0]
                    #                 point3[0] = point1[0]
                    #     else:
                    #         point3[1] += diff_x
                    #         point4[1] -= diff_x
                    #         point1[0] += 4*diff_x
                    #         point2[0] += 4*diff_x
                         
                    # elif diff_x > 0:
                    #     if point4[1] <= point1[1]:
                    #         if point1[0] <= point4[0]:
                    #             print(3)
                    #             point3[1] += diff_x
                    #             point4[1] -= diff_x
                    #             point1[0] += 4*diff_x 
                    #             point2[0] += 4*diff_x 
                    #             if point1[0] >= point4[0]:
                    #                 point1[0] = point4[0]
                    #                 point2[0] = point4[0]
                    #     else:
                    #         pass
                            
                    # Enter differences into rectangle's position
                    # white_rect.width = white_rect.width
                    # white_rect.center = (white_rect.center[0] + diff_x, white_rect.center[1] + diff_y)
                    # Update old values
                    mpointer.prev_mouse_x = mpointer.mouse_x
                    mpointer.prev_mouse_y = mpointer.mouse_y
        else:
            # If scroll is not pressed
            mpointer.change_state = False
            mpointer.moving_active = False

        # Erase old view and draw the rectangle
        dis.fill(CGREY)    
        # pygame.draw.rect(dis, CWHITE, white_rect)
        # pygame.draw.circle(dis, CRED, white_rect.center, 3)
        
        # POLYGON
        # pol_list = [[round(rad*math.cos(vertices[0]))+200, round(rad*math.sin(vertices[0]))+200],
        # [round(rad*math.cos(vertices[1]))+200, round(rad*math.sin(vertices[1]))+200],
        # [round(rad*math.cos(vertices[2]))+200, round(rad*math.sin(vertices[2]))+200], 
        # [round(rad*math.cos(vertices[3]))+200, round(rad*math.sin(vertices[3]))+200]]
        # pygame.draw.polygon(dis, CRED, pol_list)
        # for i in range(len(vertices)):
        #     vertices[i] += (math.pi/180)





        # POLYGON WITH PERSPECTIVE
        #pol_list = [point1, point2, point3, point4]
        #pygame.draw.polygon(dis, CRED, pol_list)
        # if point1[1] > point2[1]:
        #     print(point1[1])
        #     point1[0] -= 1 
        #     point2[0] -= 1
        #     point3[0] -= 4
        #     point4[0] -= 4

        #     point1[1] -= 1
        #     point2[1] += 1


        which_wall = x_axis % 90
        print(which_wall)
        proportions_B = which_wall/90
        print(proportions_B)
        proportions_A = 1 - proportions_B
        print(proportions_A)
        
        if x_axis >= 0 and x_axis < 90:
            fig_color_A  = CGREEN
            fig_color_B  = CRED
        elif x_axis >= 90 and x_axis < 180:
            fig_color_A  = CRED
            fig_color_B  = CWHITE
        elif x_axis >= 180 and x_axis < 270:
            fig_color_A  = CWHITE
            fig_color_B  = BLUE
        elif x_axis >= 270:
            fig_color_A  = BLUE
            fig_color_B  = CGREEN
        point1_A = [x1,y1-y1*proportions_B/10]
        point2_A = [x1,y1-h+y1*proportions_B/10]
        point3_A = [x1+w*proportions_A,y1-h]
        point4_A = [x1+w*proportions_A,y1]
        pointsA = [point1_A, point2_A, point3_A, point4_A]

        point1_B = [x1+w-w*proportions_B,y1]
        point2_B = [x1+w-w*proportions_B,y1-h]
        point3_B = [x1+w,y1-h+y1*proportions_A/10]
        point4_B = [x1+w,y1-y1*proportions_A/10]
        pointsB = [point1_B, point2_B, point3_B, point4_B]

        pygame.draw.polygon(dis, fig_color_A, pointsA)
        pygame.draw.polygon(dis, fig_color_B, pointsB)
        


        # Update the view
        pygame.display.flip()
        clock.tick(30)




mpointer = MousePointer()
game_loop()
pygame.quit()
quit()
