import blessed,os
from os.path import isdir
from blessed import Terminal
from git.repo.base import Repo
from main import main


def fs_search(term)->str:
    target_file = ""
    while target_file == "":
        print(term.home() + term.clear() )
        paths = os.listdir()
        paths = [x for x in paths if x[0]!= "."]
        cap =  len(paths)
        if len(paths)> 10: cap = 10 
        selected = 0 
        
        lower_bound,upper_bound = 0,cap
        while True: 
            paths = [x for x in paths if x[0]!= "."]
            x_len = max(max(list(map(lambda x: len(x),paths))),30) 
            cap =  len(paths)
            if len(paths)> 10: cap = 10 

            n_lines = (x_len - 18 )//2
            print(term.move_y(term.height - cap -int(term.height*0.5)) + term.center("┌"+ "─"*n_lines + "┤" + term.cyan2(" SELECT SMT2 FILE ")+ "├" + "─"*n_lines +"┐"))
            print(term.center("│ " + " "*x_len + " │"))
            print(term.center("│ " + " "*x_len + " │"))
            print(term.move_y(term.height -  cap - int(term.height*0.5) + 2))
            for filename in paths[lower_bound:upper_bound]:
                spaces = " "*(x_len - len(filename))
                if filename == paths[selected]: 
                    print(term.center("│ " + term.black_on_cyan2(filename)+ spaces + " │"))
                else:
                    print(term.center("│ " + filename + spaces + " │"))
            print(term.center("│ " + " "*x_len + " │"))
            print(term.center("└─" + "─"*x_len + "─┘"))
            inp = term.inkey()
            if inp.lower() == "j" or inp.code == term.KEY_DOWN: 
                if selected >= cap:
                    upper_bound += 1
                    lower_bound -= 1
                else:selected = (selected + 1) if(selected<(len(paths)-1)) else 0
            elif inp.lower() == "k" or inp.code == term.KEY_UP: 
                if selected >= cap:
                    upper_bound -= 1
                    lower_bound += 1
                selected = (selected - 1) if(selected>0) else (len(paths) -1)
            elif inp.code == term.KEY_LEFT or inp.lower()=="h": 
                    os.chdir("..")
                    selected,paths = 0, os.listdir()
                    break
            elif inp.code == term.KEY_ENTER or inp.code == term.KEY_RIGHT or inp.lower()=="l": 
                check = paths[selected].split(".")[-1] == "smt2"
                check_string = "Accepted " if (check) else "Is not an smt2 File"
                print(term.move_y(0) + term.center(check_string))
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

    return target_file 

def tui_main():
    term = Terminal()
    print(term.home + term.clear)
    while True:
        top_y = term.height // 5
        print(term.home + term.move_y(1)+ term.clear_eof + term.move_y(top_y))
        
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
                    target_file = fs_search(term) 
                    while True: 
                        print( term.center(term.black_on_cyan2(main(target_file,term))))
                        inp = term.inkey()
                        if inp.lower() == "q" or inp.code == term.KEY_ESCAPE: exit()
        
                case 1: # Download QF_UF Repo 
                    if not os.path.isdir("./qf_uf_repo"):
                        print(term.move_xy(0,0) + term.clear_eol + term.center(term.blink("Donwloading the package!")))
                        Repo.clone_from("https://clc-gitlab.cs.uiowa.edu:2443/SMT-LIB-benchmarks/QF_UF.git","./qf_uf_repo")
                        print(term.move_xy(0,0) + term.center("Package Downloaded!"))
                    else:
                        print(term.move_xy(0,0) + term.clear_eol + term.center("Package as already been Downloaded!"))
                case 2: # Use file from repo
                    if os.path.isdir("./qf_uf_repo"):
                        os.chdir("./qf_uf_repo") 
                        target_file = fs_search(term) 
                        while True: 
                            print( term.center(term.black_on_cyan2(main(target_file,term))))
                            inp = term.inkey()
                            if inp.lower() == "q" or inp.code == term.KEY_ESCAPE: exit()
                    else:
                        print(term.move_xy(0,0) + term.clear_eol + term.center("Donwload the Package first!"))
                case _:
                    pass

if __name__ == "__main__": 
    tui_main()
