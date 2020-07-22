import requests


def BuildLeaderboardUrl(groupCode, mapCode, score):
    baseUrl = "https://live-services.trackmania.nadeo.live/api/token/leaderboard/group/"
    url = baseUrl + groupCode + "/map/" + mapCode + "/surround/0/50?score=" + str(score)
    return url


def CallLeaderboardApi(auth, url):
    headers = {'Authorization': 'nadeo_v1 t=' + auth}
    result = requests.get(url, headers=headers)
    return result.json()


def FixLeaderboard(leaderboard):
    leaderboard["tops"][0]["top"].pop(0)
    for x in leaderboard["tops"][0]["top"]:
        value = x["position"]
        x["position"] = int(value - 1)


def GetLeaderboard(authToken, groupCode, mapCode, limit):
    x = 1
    nextScore = 0
    leaderboard = {}
    while x > 0:
        url = BuildLeaderboardUrl(groupCode, mapCode, nextScore)
        if x == 1:
            leaderboard = CallLeaderboardApi(authToken, url)
        else:
            limitLeaderboard = CallLeaderboardApi(authToken, url)
            limitLeaderboard["tops"][0]["top"].pop(0)
            leaderboard["tops"][0]["top"].extend(limitLeaderboard["tops"][0]["top"])
        nextScore = leaderboard["tops"][0]["top"][-1]["score"]
        x = limit - (len(leaderboard["tops"][0]["top"]) - 1)
    FixLeaderboard(leaderboard)
    return leaderboard
