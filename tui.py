import curses, curses.ascii, math
from curses import A_REVERSE, KEY_DOWN, KEY_UP, KEY_LEFT, KEY_RIGHT, KEY_ENTER
# stdscr = curses.initscr()
def main(screen):
    # screen.clear()
    key = 0
    screen.border()
    while key != curses.ascii.ESC:
        height, width = screen.getmaxyx()
        title = "CONGRUENCE CLOSURE"
        screen.addstr(math.ceil(height/4),math.ceil((width-len(title))/2),title, curses.A_REVERSE | curses.A_BOLD | curses.A_DIM)

        current_key = str(key) + "," + str(height)  + "," + str(width)
        screen.addstr(height-3,width-15,current_key, curses.A_REVERSE | curses.A_BOLD | curses.A_DIM)

        # Test
        begin_x = 20; begin_y = 7
        height = 5; width = 40
        menu= curses.newwin(height, width, begin_y, begin_x)
        menu.addstr(0,0,"prova",curses.A_REVERSE)
        menu.border()

        # Always
        key = screen.getch() # Listen for key 
        screen.refresh() # Update changes on screen 
        screen.erase() # Deactivate pixels that are no longer used 
        screen.border()


if __name__ == "__main__":
    curses.wrapper(main)

# def main(screen):
#     ch, first, selected, paths = 0, 0, 0, os.listdir()
#     while ch != curses.ascii.ESC:
#         height, width = screen.getmaxyx()
#         screen.erase()
#         for y, filename in enumerate(paths[first : first+height]):
#             color = A_REVERSE if filename == paths[selected] else 0
#             screen.addstr(y, 0, filename[:width-1], color)
#         ch = screen.getch()
#         selected += (ch == KEY_DOWN) - (ch == KEY_UP)
#         selected = max(0, min(len(paths)-1, selected))
#         first += (selected >= first + height) - (selected < first)
#         if ch in [KEY_LEFT, KEY_RIGHT, KEY_ENTER, ord('\n'), ord('\r')]:
#             new_dir = '..' if ch == KEY_LEFT else paths[selected]
#             if os.path.isdir(new_dir):
#                 os.chdir(new_dir)
#                 first, selected, paths = 0, 0, os.listdir()

# if __name__ == '__main__':
#     curses.wrapper(main)
