import requests
import json

site = input()
token = "1aa70a8db2d6a41e18661e26ee1eca8ba891a1489944148cd11be4c36dac8394"
team = requests.get(site + "/teams", headers={"Authorization": token}).json()
print(team)
matches = requests.get(site + "/matches", headers={"Authorization": token}).json()

s = "https://lksh-enter.ru/players"
player_id = []
player_name = []
for search_id_players in range(len(team)):
    player_id.extend(team[search_id_players]['players'])
for search_players in player_id:
    play = requests.get(s + "/" + str(search_players), headers={"Authorization": token}).json()
    full_name = (play['name'] + ' ' + play['surname']).strip()
    if full_name:
        player_name.append(full_name)
player_name.sort()
for print_player in player_name:
    print(print_player)

while True:
    try:
        log = input().split()
        if not log:
            continue

        if log[0] == 'versus?':
            if len(log) < 3:
                print(0)
                continue

            id_1 = int(log[1])
            id_2 = int(log[2])
            if id_1 in player_id and id_2 in player_id:
                f_id_1 = None
                f_id_2 = None
                for te in team:
                    if id_1 in te['players']:
                        f_id_1 = te['id']
                    if id_2 in te['players']:
                        f_id_2 = te['id']
                if f_id_1 and f_id_2:
                    kol = 0
                    for ma in matches:
                        if (f_id_1 == ma['team1'] and f_id_2 == ma['team2']) or (
                                f_id_1 == ma['team2'] and f_id_2 == ma['team1']):
                            kol += 1
                    print(kol)
                else:
                    print(0)
            else:
                print(0)

        elif log[0] == "stats?":
            if len(log) < 2:
                print(0, 0, 0)
                continue

            team_name = ' '.join(log[1:]).strip('"')
            win = 0
            lose = 0
            goal = 0
            nogoal = 0
            team_found = False

            for te in team:
                if team_name == te['name']:
                    team_found = True
                    id_teamm = te['id']
                    break

            if not team_found:
                print(0, 0, 0)
                continue

            for ma in matches:
                if id_teamm == ma['team1']:
                    if ma['team1_score'] > ma['team2_score']:
                        win += 1
                    elif ma['team2_score'] > ma['team1_score']:
                        lose += 1
                    goal += ma['team1_score']
                    nogoal += ma['team2_score']
                elif id_teamm == ma['team2']:
                    if ma['team2_score'] > ma['team1_score']:
                        win += 1
                    elif ma['team1_score'] > ma['team2_score']:
                        lose += 1
                    goal += ma['team2_score']
                    nogoal += ma['team1_score']

            print(win, lose, goal - nogoal)

        elif log[0] == "exit":
            break

    except Exception:
        continue
