import logging
import json

import requests

from services.aspectLogging import LogAspect


class LMACApiClient:
    def __init__(self, apiKey: str, apiUrl: str):
        self._apiKey = apiKey
        self._apiUrl = apiUrl
        self._logger = LogAspect('runtime').logger()

    def _sendRequest(self, apiFunction: str, jsonData: any):
        response = requests.post(
            self._apiUrl,
            json={
                'apiFunction': apiFunction,
                'apiKey': self._apiKey,
                'arguments': jsonData
            },
            headers={
                'Content-type': 'application/json',
                'Accept': 'text/plain'
            }
        )
        response = response.json()

        return response['result'] != 'error'

    def addContestOutcomes(self, outcomes: list[dict]) -> bool:
        return self._sendRequest('addContestOutcomes', {'outcomes': outcomes})


class DataHandler:
    COLUMN_CONTEST_ID = 0

    def __init__(self, apiKey: str, apiUrl: str):
        self.logger = logging.getLogger()
        self._apiClient = LMACApiClient(apiKey, apiUrl)

    def _getJsonFromWinnersDict(self, winners: dict):
        output = {}

        for artist, entity in winners.items():
            output.update({artist: entity.tojson()})

        return json.dumps(output)

    def updateContests(self, contests: dict):
        print('saving')

        contestList = []

        for contest in contests.values():
            winners = {}
            for winner in contest.winners.keys():
                winners[winner] = contest.winners[winner].toDict()

            contestDict = contest.toDict()
            contestDict['winners'] = winners

            contestList.append(contestDict)

            print(contestDict)

        self._apiClient.addContestOutcomes(contestList)

