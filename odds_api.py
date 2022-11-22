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
    print(odds_json[1])

    # Check the usage quota
    print('Remaining requests: ', odds_response.headers['x-requests-remaining'])
    print('Used requests: ', odds_response.headers['x-requests-used'])

# Bookmakers
# barstool, betmgm, betonlineag, betfair, foxbet, lowvig, circasports, superbook, draftkings, fanduel, williamhill_us, betus, twinspires, unibet_us, sugarhouse, betrivers, gtbets, wynnbet, 



