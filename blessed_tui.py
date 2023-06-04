import blessed
from blessed import Terminal
from main import main

# Standard Reset
term = Terminal()
term.on_white()
top_y = term.height // 5
print(term.home + term.clear + term.move_y(top_y))

options = [ "│             Upload File               │",\
            "│       Download QF_UF Repository       │",\
            "│            Use Repository             │" ]

start = ( term.height // 5 ) + 3
offset = 0
with term.cbreak(), term.hidden_cursor(): #, term.fullscreen():
    current_y = top_y
    print(term.center("┌────┤"+term.cyan2(" CONGRUENCE CLOSURE WITH DAG ")+"├────┐"))
    current_y+=3
    print(term.center('│                                       │'))
    print(term.center("│       "+ term.deepskyblue4("Please select an option")+ "         │"))
    for i in range(8):
        current_y+=1
        if 5>i>1: print(term.center(options[i-2]))
        else: print(term.center('│                                       │'))
    current_y+=2
    print(term.center('└─────┤ Andrea Mangrella VR490856 ├─────┘'))
    print(term.move_y(term.height - 5) + term.center(f"{term.link('https://github.com/kativenOG', 'Github Project Page')}"))
    
    inp = ""
    while True:
        inp = term.inkey()
        print(term.move_y(start + 3 + offset) + term.center(options[offset]))
        if inp.lower() == "j" or inp.code == term.KEY_DOWN: offset= offset + 1 if(offset!=2) else 0
        if inp.lower() == "k" or inp.code == term.KEY_UP: offset= offset - 1 if(offset!=0) else 2
        print(term.move_y(start + 3 + offset) + term.center(term.black_on_cyan2(options[offset])))
        if inp.lower() == "q": exit()
        elif inp.code == term.KEY_ENTER: break
    match offset:
        case 0:
            print(term.home() + term.clear())
            file =  "./inputs/input1.smt2"
            print(term.move_y(2)+term.center(term.deepskyblue4(file)))
            print( term.center(term.black_on_cyan2(main(file))))

# print(term.move_down(2) + 'You pressed ' + term.bold(repr(inp)))
