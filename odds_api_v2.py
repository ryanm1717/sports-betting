import requests

api_key = '80c0806d1839879de2ad8c1906b4cd58'

# Use the sport_key or 'upcoming'
sport = 'americanfootball_nfl'

# Regions - us | uk | eu | au - can use multiple with commas
regions = 'us'

# Markets - h2h | spreads | totals - can use multiple with commas
markets = 'h2h'

# Odds format - decimal | american
odds_format = 'american'

# Date format - iso | unix
date_format = 'iso'

# List of in-season sports - key can be used to get odds
#sports_response = requests.get(
#    'https://api.the-odds-api.com/v4/sports',
#    params={
#        'api_key': api_key
#    }
#)

#if sports_response.status_code != 200:
#    print(f'Failed to get sports: status_code {sports_response.status_code}, response body {sports_response.text}')
#else:
#    print('List of in-season sports:', sports_response.json())

# Notable sports keys:
# - NFL: 'americanfootball_nfl'
# - NBA: 'basketball_nba'
# - Premier League: 'soccer_epl'
# - NCAA Football: 'americanfootball_ncaaf'
# - NCAA Basketball: 'basketball_ncaab'
# - NHL: 'icehockey_nhl'

# Bookmakers:
# ['sugarhouse', 'bovada', 'betus', 'barstool', 'superbook', 'unibet_us', 'draftkings', 'twinspires', 'williamhill_us', 'fanduel', 'betonlineag', 'betrivers', 
# # 'lowvig', 'pointsbetus', 'wynnbet', 'circasports', 'mybookieag', 'betmgm', 'betfair', 'gtbets', 'foxbet']

class Game:
    def __init__(self, game_id, sport_key, sport_title, commence_time, home_team, away_team, h2h_sportsbooks, h2h_home_odds, h2h_away_odds):
        self.game_id = game_id
        self.sport_key = sport_key
        self.sport_title = sport_title
        self.commence_time = commence_time
        self.home_team = home_team
        self.away_team = away_team
        self.h2h_sportsbooks = h2h_sportsbooks
        self.h2h_home_odds = h2h_home_odds
        self.h2h_away_odds = h2h_away_odds

    def best_odds(self):
        h2h_home_best_odds = -999999
        h2h_home_worst_odds = 999999
        h2h_home_best_odds_sportsbook_list = []

        h2h_away_best_odds = -999999
        h2h_away_worst_odds = 999999
        h2h_away_best_odds_sportsbook_list = []

        for i in range(0, len(self.h2h_home_odds)):
            if self.h2h_home_odds[i] == h2h_home_best_odds:
                h2h_home_best_odds_sportsbook_list.append(self.h2h_sportsbooks[i])

            if self.h2h_home_odds[i] > h2h_home_best_odds:
                h2h_home_best_odds_sportsbook_list.clear()
                h2h_home_best_odds_sportsbook_list.append(self.h2h_sportsbooks[i])
                h2h_home_best_odds = self.h2h_home_odds[i]

            if self.h2h_away_odds[i] == h2h_away_best_odds:
                h2h_away_best_odds_sportsbook_list.append(self.h2h_sportsbooks[i])

            if self.h2h_away_odds[i] > h2h_away_best_odds:
                h2h_away_best_odds_sportsbook_list.clear()
                h2h_away_best_odds_sportsbook_list.append(self.h2h_sportsbooks[i])
                h2h_away_best_odds = self.h2h_away_odds[i]
        
        matchup = 'Matchup between ' + self.home_team + ' vs. ' + self.away_team + ' - odds below\n' 
        home_odds = 'Best odds for ' + self.home_team + ': ' + str(h2h_home_best_odds) + ' at ' + str(h2h_home_best_odds_sportsbook_list) + '\n'
        away_odds = 'Best odds for ' + self.away_team + ': ' + str(h2h_away_best_odds) + ' at ' + str(h2h_away_best_odds_sportsbook_list) + '\n'

        return matchup + home_odds + away_odds
        

# List of live and upcoming games for the specified sport, along with odds for different bookmakers - deducts from usage quota
odds_response = requests.get(
    f'https://api.the-odds-api.com/v4/sports/{sport}/odds',
    params={
        'api_key': api_key,
        'regions': regions,
        'markets': markets,
        'oddsFormat': odds_format,
        'dateFormat': date_format,
    }
)

if odds_response.status_code != 200:
    print(f'Failed to get odds: status code {odds_response.status_code}, response body {odds_response.text}')
    
else:
    odds_json = odds_response.json()
    print('Number of events: ', len(odds_json), '\n')

    g_id = 1
    game_class = {}
    for game in odds_json:

        home_team = game['home_team']
        away_team = game['away_team']

        h2h_sportsbook = []
        h2h_home_odds = []
        h2h_away_odds = []

        for bookmaker in game['bookmakers']:
            h2h_sportsbook.append(bookmaker['key'])

            if home_team == bookmaker['markets'][0]['outcomes'][0]['name']:
                h2h_home_odds.append(bookmaker['markets'][0]['outcomes'][0]['price'])
                h2h_away_odds.append(bookmaker['markets'][0]['outcomes'][1]['price'])
            else:
                h2h_home_odds.append(bookmaker['markets'][0]['outcomes'][1]['price'])
                h2h_away_odds.append(bookmaker['markets'][0]['outcomes'][0]['price'])

        game_class['game_' + str(g_id)] = Game(game_id=game['id'], sport_key=game['sport_key'], sport_title=game['sport_title'], commence_time=game['commence_time'], home_team=game['home_team'], away_team=game['away_team'], h2h_sportsbooks=h2h_sportsbook, h2h_home_odds=h2h_home_odds, h2h_away_odds=h2h_away_odds)

        g_id += 1

    #print(game_class['game_1'].best_odds())
    #print(game_class['game_1'].h2h_sportsbooks)
    #print(game_class['game_1'].h2h_home_odds)
    #print(game_class['game_1'].h2h_away_odds)
    
    for x in game_class:
        print(game_class[x].best_odds())

    # Check the usage quota
    print('Remaining requests: ', odds_response.headers['x-requests-remaining'])
    print('Used requests: ', odds_response.headers['x-requests-used'])

    


