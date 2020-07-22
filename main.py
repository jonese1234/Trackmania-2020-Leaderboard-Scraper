from .util import authentication, leaderboard
import json
from .util.github import Upload
import time
from datetime import datetime
from .settings import rankLimit

summer2020Path = "data/summer2020.json"
summer2020GroupId = "3987d489-03ae-4645-9903-8f7679c3a418"


def ReadData(file):
    print("Opening data from file (" + file + ")")
    with open(file, encoding='utf-8') as json_file:
        data = json.load(json_file)
        print("Returning data")
        return data


def RunLeaderboardScrape():
    auth = authentication.GetAuthentication()
    summer2020 = ReadData(summer2020Path)
    upload = Upload()
    for x in summer2020["playlist"]:
        print("Getting " + str(x["position"] + 1) + " Data")
        result = leaderboard.GetLeaderboard(auth["accessToken"], summer2020GroupId, x["mapUid"], rankLimit)
        print(result)
        print("uploading " + str(x["position"] + 1) + " data")
        upload.UploadMapLeaderboard("Summer-2020/" + str(x["position"] + 1), result)
        print("uploading " + str(x["position"] + 1) + " data done")
        print("Sleeping to reduce api limiting")
        time.sleep(2)


if __name__ == "__main__":
    start = time.perf_counter()
    print("Running Trackmania2020 Leaderboard Update Service")
    print("Time (UTC): " + datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S"))

    print("Running Process")
    RunLeaderboardScrape()

    stop = time.perf_counter()
    print(f"Finished in {stop - start:0.4f} seconds")