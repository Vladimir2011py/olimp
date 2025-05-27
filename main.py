# 1aa70a8db2d6a41e18661e26ee1eca8ba891a1489944148cd11be4c36dac8394
import requests
import json


token = "1aa70a8db2d6a41e18661e26ee1eca8ba891a1489944148cd11be4c36dac8394"
team = requests.get("https://lksh-enter.ru/teams", headers={"Authorization": token}).json()

matches = requests.get("https://lksh-enter.ru/matches", headers={"Authorization": token})
mat=requests.get("https://lksh-enter.ru/matches", headers={"Authorization": token}).json()
s="https://lksh-enter.ru/players"
player_id=[]
player_name=[]
for search_id_players in range(len(team)):
    player_id.extend(team[search_id_players]['players'])
for search_players in player_id:

    play = requests.get(s+"/"+str(search_players), headers={"Authorization": token}).json()
    player_name.append(play['name']+' '+play['surname'])
player_name.sort()
for print_player in player_name:
    print(print_player)


while True:
    log=input().split()
    if log[0]=='versus?':
        id_1=int(log[1])
        id_2=int(log[2])
        if id_1 in player_id and id_2 in player_id:
            for te in team:
                if id_1 in te['players']:
                    f_id_1=te['id']
                if id_2 in te['players']:
                    f_id_2=te['id']
            kol=0
            for ma in mat:
                if (f_id_1 == ma['team1'] and f_id_2 == ma['team2']) or (f_id_1 == ma['team2'] and f_id_2 == ma['team1']):
                    kol+=1
            print(kol)
        else:
            kol=0
            print(0)
    if log[0]=="stasts?":
        win=0
        lose=0
        goal=0
        nogoal=0
        teamm=log[1][1:-1]
        for te in team:
            if teamm in te['name']:
                id_teamm=te['id']
        for ma in mat:
            if id_teamm==ma['team1']:
                if ma['team1_score']>ma['team2_score']:
                    win+=1
                elif ma['team2_score']>ma['team1_score']:
                    lose+=1
                goal+= ma['team1_score']
                nogoal+= ma['team2_score']
            elif id_teamm==ma['team2']:
                if ma['team2_score']>ma['team1_score']:
                    win+=1
                elif ma['team1_score']>ma['team2_score']:
                    lose+=1
                goal+= ma['team2_score']
                nogoal+= ma['team1_score']
        print(win,lose,goal-nogoal)



