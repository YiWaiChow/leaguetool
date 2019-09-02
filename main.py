from Champion.Champ_List import ChampionList
from Champion.Score.ScoreCalculator import Scorecalculator
from Champion.Score.decisionTree import ScoreAVLTree
from Game.CurrentGame import Game
from User.User import User

CL = ChampionList()
CG= Game()
name = input("enter your user name below:")
perfer = input("enter your champion preference, Example: AD , AP, AR, MR")
user = User(name)
user.add_prefer(perfer)
print("please enter your champion pool one 1 by one, type end when all champion from your champion pool is enter , "
      "this tool currently support up to champion with alphabet a-b")
champ_input = None

while champ_input != "end":
    champ_input = input("type here")
    champion = CL.find_champ(champ_input)
    if champion is None:
        print("either champion is not currently supported or name is incorrect")
    else:
        user.add_champ_to_pool(champion)
    print("here is the champion entered so far")
    print(user.get_pool())
print("now enter all enemy champion that is selected so far in this game, if all champion are entered, type end")
champ_input = None
position = 1
"entering enemy team champion"
while champ_input != "end":
    if position == 6:
        break
    champ_input = input("enter here")
    champion = CL.find_champ(champ_input)
    if champ_input == "end":
        print("all enemy champion is entered")
    elif champion is None:
        print("either champion is not currently supported or name is incorrect")
    else:
        CG.add_champ(champion, position, "e")
        position += 1
print("now enter all allies champion that is selected so far in this game, if all champion are entered, type end")
champ_input = None
position = 1
while champ_input != "end" :
    if position == 6:
        break
    champ_input = input("enter here")
    champion = CL.find_champ(champ_input)
    if champ_input == "end":
        print("all allies champion is entered")
    elif champion is None:
        print("either champion is not currently supported or name is incorrect")
    else:
        CG.add_champ(champion, position, "a")
        position += 1
SC = Scorecalculator(CL, CG, user)
att_list = SC.att_in_need()
print("here is the attrivbute in need for this game")
print(att_list)
SC.calculate_champscore(att_list)
for champ in CL.get_champ_list():
    print(champ.get_score())
SAT = ScoreAVLTree()
TopNode = None
for x in CL.get_champ_list():
    print(x)
    if x not in CG.achamp and x not in CG.echamp:
        print(x)
        TopNode = SAT.insert(TopNode, x)
SAT.preOrder(TopNode)
MAX_node = SAT.max_score(TopNode)
print("here is the recommanded champion based on the attribute needed and peference of the user ")
for x in (MAX_node.get_champ_list()):
    if x not in CG.echamp:
        print(x)






