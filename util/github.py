from ..settings import githubRepo, githubToken
from github import Github
from datetime import datetime
import json


class Upload:
    def __init__(self):
        self.g = Github(githubToken)
        self.repo = self.g.get_repo(githubRepo)

    def UploadMapLeaderboard(self, mapFolder, data):
        time = datetime.utcnow()
        try:
            contents = self.repo.get_contents(mapFolder)
            latest = next((x for x in contents if x.name == 'latest.json'), None)
            self.repo.update_file(latest.path,
                                  "Updated data at " + time.strftime("%Y-%m-%d %H:%M:%S"),
                                  json.dumps(data),
                                  latest.sha,
                                  branch="master")
        except:
            self.repo.create_file(mapFolder + "/latest.json",
                                  "Updated data at " + time.strftime("%Y-%m-%d %H:%M:%S"),
                                  json.dumps(data),
                                  branch="master")

        self.repo.create_file(mapFolder + "/history/" + time.strftime("%Y-%m-%d %H:%M:%S") + ".json",
                              "Uploaded data at " + time.strftime("%Y-%m-%d %H:%M:%S"),
                              json.dumps(data),
                              branch="master")