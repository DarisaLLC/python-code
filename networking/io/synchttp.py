#!/usr/local/bin/python3 

import requests

base_url = 'http://stats.nba.com/stats'
HEADERS = {
    'user-agent': ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) "
                   "AppleWebKit/537.36 (KHTML, like Gecko) "
                   "Chrome/45.0.2454.101 Safari/537.36"),
}


def get_players(player_args):
    endpoint = '/commonallplayers'
    params = {'leagueid': '00', 'season': '2016-17', 'isonlycurrentseason': '1'}
    url = f'{base_url}{endpoint}'
    print('Getting all players...')
    resp = requests.get(url, headers=HEADERS, params=params)
    data = resp.json()
    player_args.extend(
        [(item[0], item[2]) for item in data['resultSets'][0]['rowSet']])


def get_player(player_id, player_name):
    endpoint = '/commonplayerinfo'
    params = {'playerid': player_id}
    url = f'{base_url}{endpoint}'
    print(f'Getting player {player_name}')
    resp = requests.get(url, headers=HEADERS, params=params)
    print(resp)
    data = resp.text
    with open(f'{player_name.replace(" ", "_")}.json', 'w') as file:
        file.write(data)


player_args = []
get_players(player_args)
for args in player_args:
    get_player(*args)
