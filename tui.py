import blessed,os
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
        if inp.lower() == "q" or inp.code == term.KEY_ESCAPE: exit()
        elif inp.code == term.KEY_ENTER: break
    match offset:
        case 0: # Upload file
            target_file = ""
            while target_file == "":
                paths = os.listdir()
                paths = [x for x in paths if x[0]!= "."]
                print(term.home() + term.clear() )
                selected = 0 
                print(term.move_y(term.height - len(paths) - int(term.height*0.6)) + term.center("┌────┤"+term.cyan2(" SELECT SMT2 FILE ")+"├────┐"))
                print(term.center(    '│                            │'))
                print(term.center(    '│                            │'))
                while True: 
                    paths = [x for x in paths if x[0]!= "."]
                    print(term.move_y(term.height - len(paths) - int(term.height*0.6) + 2))
                    for filename in paths:
                        spaces = " "*(27 - len(filename))
                        if filename == paths[selected]: 
                            print(term.center("│ " + term.black_on_cyan2(filename)+ spaces + "│"))
                        else:
                            print(term.center("│ " + filename + spaces + "│"))
                    print(term.center('│                            │'))
                    print(term.center('└────────────────────────────┘'))
                    inp = term.inkey()
                    if inp.lower() == "j" or inp.code == term.KEY_DOWN: 
                        selected = (selected + 1) if(selected<(len(paths)-1)) else 0
                    elif inp.lower() == "k" or inp.code == term.KEY_UP: 
                        selected = (selected - 1) if(selected>0) else (len(paths) -1)
                    elif inp.code == term.KEY_LEFT or inp.lower()=="h": 
                            os.chdir("..")
                            selected,paths = 0, os.listdir()
                            break
                    elif inp.code == term.KEY_ENTER or inp.code == term.KEY_RIGHT or inp.lower()=="l": 
                        check = paths[selected].split(".")[-1] == "smt2"
                        print(term.move_y(0) + term.center(str(check)))
                        if check: # Is a smt file 
                            target_file = paths[selected] 
                            break
                        else:  # Changes dir only if is a directory 
                            if os.path.isdir(paths[selected]):
                                os.chdir(paths[selected])
                                selected,paths = 0, os.listdir()
                                break

                    elif inp.lower() == "q" or inp.code == term.KEY_ESCAPE: 
                        exit()

            while True: 
                print( term.center(term.black_on_cyan2(main(target_file,term))))
                inp = term.inkey()
                if inp.lower() == "q" or inp.code == term.KEY_ESCAPE: exit()

        case 1: # Download QF_UF Repo 
            pass
        case 2: # Use file from repo
            print(term.home() + term.clear())
            file =  "./inputs/input1.smt2"
            print(term.move_y(2)+term.center(term.deepskyblue4(file)))
            print( term.center(term.black_on_cyan2(main(file))))
        case _:
            pass

# print(term.move_down(2) + 'You pressed ' + term.bold(repr(inp)))
