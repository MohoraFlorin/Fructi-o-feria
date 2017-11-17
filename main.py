# importing curses...
import curses
import time
from random import randint, randrange


# asking for color preference on startup
color_pref = int(input('Choose color mode (0-WHITE, 1-GREEN, 2-RED, 3-BLUE): '))

#Things screen related
screen = curses.initscr()
dims = screen.getmaxyx()
curses.start_color()
curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)#
curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)  # Color pairs
curses.init_pair(3, curses.COLOR_CYAN, curses.COLOR_BLACK) #
curses.noecho()
max_x = int(dims[1])
max_y = int(dims[0])
screen.keypad(1)
curses.curs_set(0)
screen.refresh()
#Game function: Movement, Game Over Screen and mainly the core of the game.
def game():
        screen.clear()
        x = int(dims[1] - 5)
        y = int(dims[0] - 3)
        xl = int(dims[1] - 20)
        q = -1
        gameover = 2
        apples = False
        placeholder = 2
        screen.border(0)
        while q != ord('q'):
            screen.addch(y, x, ord('A'), curses.color_pair(color_pref)|curses.A_BOLD)
            screen.addstr(0, xl, 'Score: ', curses.color_pair(color_pref)|curses.A_BOLD)
            screen.refresh()
            q = screen.getch()
            #Movement UP
            if q == curses.KEY_UP and y > 1:
                screen.addch(y, x, ' ')
                y -= 1
            #Movement DOWN
            elif q == curses.KEY_DOWN and y < int(dims[0]) - 2:
                screen.addch(y, x, ' ')
                y += 1
            #Movement LEFT
            elif q == curses.KEY_LEFT and x > 1:
                screen.addch(y, x, ' ')
                x -= 1
            #Movement RIGHT
            elif q == curses.KEY_RIGHT and x < int(dims[1]) - 2:
                screen.addch(y, x, ' ')
                x += 1

        if q == ord('q'):
            gameover = 1

        if gameover != placeholder:
            gameover_true()


#Game Over Screen
def gameover_true():
            screen.clear()
            screen.border()
            screen.nodelay(0)
            #Coordinates for the text
            xv = int(dims[0]/2)
            xc = int(dims[0]/2 - 3)
            xz = int(dims[1]/2 - 12)
            xd = int(dims[1]/2 - 3)
            xa = int(dims[0]/2 + 2)
            xb = int(dims[0]/2 + 3)
            #Printing the text
            screen.addstr(xc, xz, 'Game Over!', curses.color_pair(color_pref)|curses.A_BOLD)
            screen.addstr(xa, xz, 'Press q to quit.', curses.color_pair(color_pref)|curses.A_BOLD)
            screen.addstr(xb, xz, 'Press SPACE to return.', curses.color_pair(color_pref)|curses.A_BOLD)
            screen.addstr(xv, xz, 'You have died.', curses.color_pair(color_pref)|curses.A_BOLD)
            screen.refresh()
            q = 0
            while q not in [32, 113]:
                q = screen.getch()
            if q == 32:
                screen.clear
                menu()

def menu():
    screen.nodelay(0)
    screen.clear()
    #Coordinates for the text
    xc = int(dims[0]/2 - 3)
    xo = int(dims[0]/2 - 1)
    xi = int(dims[0]/2 + 1)
    xd = int(dims[1]/2 - 20)
    xp = int(dims[1]/2 - 6)
    xg = int(dims[1]/2 - 2)
    selection = -1
    option = 0
    #Main menu objects:
    while selection < 0:
        graphics = [0]*3
        graphics[option] = curses.A_REVERSE
        screen.addstr(0, xd, '<===========[Fructi-o-feria]===========>', curses.color_pair(color_pref)|curses.A_BOLD)
        screen.addstr(xc, xg, 'Play', curses.color_pair(color_pref)|graphics[0]|curses.A_BOLD)
        screen.addstr(xo, xp, 'Instructions', curses.color_pair(color_pref)|graphics[1]|curses.A_BOLD)
        screen.addstr(xi, xg, 'Exit', curses.color_pair(color_pref)|graphics[2]|curses.A_BOLD)
        screen.refresh()
        #Selecting one
        action = screen.getch()
        if option == 3:
            option = 1
        if action == curses.KEY_UP:
            option -= 1
        elif action == curses.KEY_DOWN:
            option += 1
        elif action == ord('\n'):
            selection = option
        if selection == 0:
            game()
        if selection == 1:
            instructions()




def instructions():
    screen.clear()
    screen.nodelay(0)
    xd = int(dims[1]/2 - 20)
    xa = int(dims[1]/2 - 38)
    sa = int(dims[0]/2 - 1)
    sb = int(dims[0]/2 - 2)
    sc = int(dims[0]/2 - 3)
    sd = int(dims[0]/2 - 5)
    screen.addstr(0, xd, '<===========[Fructi-o-feria]===========>', curses.color_pair(color_pref)|curses.A_BOLD)
    screen.addstr(sa, xa, 'Use the arrow keys to move.', curses.color_pair(color_pref)|curses.A_BOLD)
    screen.addstr(sb, xa, 'You collect points by picking up the apples on the ground.', curses.color_pair(color_pref)|curses.A_BOLD)
    screen.addstr(sc, xa, 'Your objective is to pick as many apples as you can before the timer reaches 0s.', curses.color_pair(color_pref)|curses.A_BOLD)
    screen.addstr(sd, xa, 'Press ENTER to go back to the menu.', curses.color_pair(color_pref)|curses.A_BOLD)
    screen.refresh()
    screen.getch()
    menu()

menu()
curses.endwin()
