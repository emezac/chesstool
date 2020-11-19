import os
import sys
import parser as parser
from Cheetah.Template import Template
import pgn as pgn

def get_groups(seq, group_by):
    data = []
    for line in seq:
        # Here the `startswith()` logic can be replaced with other
        # condition(s) depending on the requirement.
        if line.startswith(group_by):
            if data:
                yield data
                data = []
        data.append(line)

    if data:
        yield data

def generate_boards(game, button, label):
    templateDef = open("helper/template.html", encoding="ISO-8859-1").read()
    t = Template(templateDef)
    t.title = game
    t.set_button = label
    t.set_position = button
    f = open(game+".html", "w")
    f.write(str(t))
    f.close()

with open(sys.argv[1], encoding = "ISO-8859-1") as f:
    print("processing "+sys.argv[1])
    for i, group in enumerate(get_groups(f, "[Event "), start=1):
        orig_name = "Game_{}".format(i)+".pgn"
        f =  open (orig_name,"w")
        fen_name = "game_pgn_{}".format(i) + ".fen"
        pgn_name_proc = "proc_game_pgn_{}".format(i)+".pgn"
        f2 = open (pgn_name_proc,"w")
        f.write("Game_{}".format(i)+"\n")
        datapgn = "".join(group)
        f2.write(datapgn)
        game = parser.parse(datapgn, actions=pgn.Actions())
        f.write("Tag Pairs:")
        f.write(str(game.tag_pairs).replace("'","").replace('"',''))
        f.write("Move Text:")
        f.write(str(game.movetext))
        f.write("Score:")
        f.write(str(game.score))
        f.write("\nFen_file: ")
        f.close()
        f2.close()
        os.system('bin/pgn-extract -Wepd ' + pgn_name_proc +">" + fen_name)
        os.system('helper/process.sh ' + fen_name + ' > pgnfiles/fen/' + fen_name)
        fen_file = open('pgnfiles/fen/' + fen_name, 'r')
        lines = fen_file.readlines()
        count = 0
        button = " $('#clearBoardBtn').on('click', board.clear)\n"
        labelbutton = ""
        lastmove = game.movetext[-1].move_number
        for line in lines:
              count += 1
              if count <= lastmove:
                mylabel= str(game.move(count)).replace(" ","-").rstrip("\n")
                labelbutton +='<button id ="{}">{}</button>'.format(count, mylabel)
                labelbutton +='\n '
                button += "$('#"+str(count)+"').on('click', function () { "
                button += " board.position('"+line.strip()+"')"
                button += "})"
                button += "\n "
        generate_boards(orig_name,button,labelbutton)
        os.system('mv Game* pgnfiles')
    os.system('mv pgnfiles/*.html templates')
    os.system('rm game_pgn* proc_game*')
