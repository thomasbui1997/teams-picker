import random

print('Welcome to Team Allocator!')

players = []
num_players = int(input('Number of players: '))

print('Enter names: ')

for i in range(num_players):
    players.append(input())
    

while True:
    random.shuffle(players)

    response = input('Team sport? Y/N: ')

    if response.upper() == 'Y':
        half = len(players) // 2
        team1 = players[:half]
        team2 = players[half:]

        print('Team 1 Captain: ' + random.choice(team1))
        for player in team1:
            print(player)

        print()

        print('Team 2 Captain: ' + random.choice(team2))
        for player in team2:
            print(player)
    else:
        for i in range(0, len(players), 2):
            start = random.randrange(i, i+2)
            print(players[i] + ' vs ' + players[i+1])
            print(players[start] + ' starts')

    response = input('Pick teams again? Y/N: ')
    if response.upper() == 'N':
        break

