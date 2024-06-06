import curses
import random

names = ["Jack", "John", "Mary", "Lisa"]
surnames = ["Smith"]
faction_names = ["Colony"]


class Node:
    def __init__(self, x, y):
        self.nodes = []
        self.x = x
        self.y = y
        self.name = names[0]
        self.surname = surnames[0]
    def render(self,stdscr):
        stdscr.addstr(self.y, self.x, self.name + " " + self.surname)
        for n in self.nodes:
            n.render(stdscr)
class Tree:
    def __init__(self, x, y):
        self.nodes = [Node(x - 10, y + 4), Node(x + 10, y + 4)]
        self.x = x
        self.y = y
    def render(self,stdscr):
        stdscr.addstr(self.y, self.x, faction_names[0])
        for n in self.nodes:
            n.render(stdscr)
def main(stdscr):
    # Clear screen
    stdscr.clear()
    
    # Set up a color pair
    curses.start_color()
    curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_CYAN, curses.COLOR_YELLOW)
    cursor = [0,0]
    height, width = stdscr.getmaxyx()
    tree = Tree(int(width / 2), 2)
    # Main loop
    while True:
        # Clear the screen
        stdscr.clear()

        # Add a string to the middle of the screen
        # Refresh the screen
        stdscr.refresh()
        tree.render(stdscr);
        key = stdscr.getch()
        if key == curses.KEY_UP:
            cursor[0] -= 1
        if key == curses.KEY_DOWN:
            cursor[0] += 1
        if key == curses.KEY_LEFT:
            cursor[1] -= 1
        if key == curses.KEY_RIGHT:
            cursor[1] += 1
        
        if key == ord('q'):
            break
        elif key == ord('c'):
            pass
        elif key == ord('m'):
            pass
# Run the curses application
curses.wrapper(main)

