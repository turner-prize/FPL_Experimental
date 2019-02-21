import requests
from loguru import logger

def Starting11():
    r = requests.get("https://fantasy.premierleague.com/drf/entry/2579502/event/1/picks")
    team = r.json()
    picks = team['picks']
    return [i['element'] for i in picks]


Week1ElementList = Starting11()


val = 0
total = 0
gw = 1

for i in Week1ElementList:
    r = requests.get(f"https://fantasy.premierleague.com/drf/element-summary/{i}")
    player = r.json()
    histDict = {i['round']: i for i in player['history']}
    weeklyStats = histDict[gw]
    val += weeklyStats['value']
    total += weeklyStats['total_points']

logger.info(f"Total Value of Team : £{val/10}")
logger.info(f"Total Score for Week {gw} : {total}")


#get all players info for week 1
#identify 'worst' player from gw 1 based on chosen metric
#drop player
#work out freed up budget
#choose best player based on available budget and team