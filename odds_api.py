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
    print('Number of events: ', len(odds_json))
    print(odds_json[0])
    
    for game in odds_json:
        home_team = game['home_team']
        away_team = game['away_team']

        bookmaker_odds = {}

        home_team_best_odds = -999999
        home_team_best_odds_bookmaker_list = []
        away_team_best_odds = -999999
        away_team_best_odds_bookmaker_list = []
        
        for bookmaker in game['bookmakers']:
            if home_team == bookmaker['markets'][0]['outcomes'][0]['name']:
                bookmaker_odds[bookmaker['key']] = {bookmaker['markets'][0]['outcomes'][0]['name']: bookmaker['markets'][0]['outcomes'][0]['price'], bookmaker['markets'][0]['outcomes'][1]['name']: bookmaker['markets'][0]['outcomes'][1]['price']}

                if bookmaker['markets'][0]['outcomes'][0]['price'] == home_team_best_odds:
                    home_team_best_odds_bookmaker_list.append(bookmaker['key'])
                    #home_team_best_odds = bookmaker['markets'][0]['outcomes'][0]['price']

                if bookmaker['markets'][0]['outcomes'][0]['price'] > home_team_best_odds:
                    home_team_best_odds_bookmaker_list.clear()
                    home_team_best_odds_bookmaker_list.append(bookmaker['key'])
                    home_team_best_odds = bookmaker['markets'][0]['outcomes'][0]['price']
                
                if bookmaker['markets'][0]['outcomes'][1]['price'] == away_team_best_odds:
                    away_team_best_odds_bookmaker_list.append(bookmaker['key'])
                    #away_team_best_odds = bookmaker['markets'][0]['outcomes'][1]['price']

                if bookmaker['markets'][0]['outcomes'][1]['price'] > away_team_best_odds:
                    away_team_best_odds_bookmaker_list.clear()
                    away_team_best_odds_bookmaker_list.append(bookmaker['key'])
                    away_team_best_odds = bookmaker['markets'][0]['outcomes'][1]['price']

            else:
                bookmaker_odds[bookmaker['key']] = {bookmaker['markets'][0]['outcomes'][1]['name']: bookmaker['markets'][0]['outcomes'][1]['price'], bookmaker['markets'][0]['outcomes'][0]['name']: bookmaker['markets'][0]['outcomes'][0]['price']}

                if bookmaker['markets'][0]['outcomes'][1]['price'] == home_team_best_odds:
                    home_team_best_odds_bookmaker_list.append(bookmaker['key'])
                    #home_team_best_odds = bookmaker['markets'][0]['outcomes'][1]['price']

                if bookmaker['markets'][0]['outcomes'][1]['price'] > home_team_best_odds:
                    home_team_best_odds_bookmaker_list.clear()
                    home_team_best_odds_bookmaker_list.append(bookmaker['key'])
                    home_team_best_odds = bookmaker['markets'][0]['outcomes'][1]['price']
                
                if bookmaker['markets'][0]['outcomes'][0]['price'] == away_team_best_odds:
                    away_team_best_odds_bookmaker_list.append(bookmaker['key'])
                    #away_team_best_odds = bookmaker['markets'][0]['outcomes'][0]['price']

                if bookmaker['markets'][0]['outcomes'][0]['price'] > away_team_best_odds:
                    away_team_best_odds_bookmaker_list.clear()
                    away_team_best_odds_bookmaker_list.append(bookmaker['key'])
                    away_team_best_odds = bookmaker['markets'][0]['outcomes'][0]['price']
        
        print('Matchup: ' + home_team + ' vs. ' + away_team + ' - Odds below:')
        if len(home_team_best_odds_bookmaker_list) > 1 and len(away_team_best_odds_bookmaker_list) > 1:
            print('Best odds for ' + home_team + ': ' + str(home_team_best_odds) + ' at ' + str(home_team_best_odds_bookmaker_list))
            print('Best odds for ' + away_team + ': ' + str(away_team_best_odds) + ' at ' + str(away_team_best_odds_bookmaker_list))
        elif len(home_team_best_odds_bookmaker_list) == 1 and len(away_team_best_odds_bookmaker_list) > 1:
            print('Best odds for ' + home_team + ': ' + str(home_team_best_odds) + ' at ' + home_team_best_odds_bookmaker_list[0])
            print('Best odds for ' + away_team + ': ' + str(away_team_best_odds) + ' at ' + str(away_team_best_odds_bookmaker_list))
        elif len(home_team_best_odds_bookmaker_list) > 1 and len(away_team_best_odds_bookmaker_list) == 1:
            print('Best odds for ' + home_team + ': ' + str(home_team_best_odds) + ' at ' + str(home_team_best_odds_bookmaker_list))
            print('Best odds for ' + away_team + ': ' + str(away_team_best_odds) + ' at ' + away_team_best_odds_bookmaker_list[0])
        else:
            print('Best odds for ' + home_team + ': ' + str(home_team_best_odds) + ' at ' + home_team_best_odds_bookmaker_list[0])
            print('Best odds for ' + away_team + ': ' + str(away_team_best_odds) + ' at ' + away_team_best_odds_bookmaker_list[0])            
        print(bookmaker_odds)
        print('')

    # Check the usage quota
    print('Remaining requests: ', odds_response.headers['x-requests-remaining'])
    print('Used requests: ', odds_response.headers['x-requests-used'])





