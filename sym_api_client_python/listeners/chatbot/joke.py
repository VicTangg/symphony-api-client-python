import requests
import logging
import json


class JokeClient:

    def __init__(self):
        pass

    def get_random_joke(self):
        logging.debug('Getting a random joke..')
        url = 'https://official-joke-api.appspot.com/jokes/random'

        try:
            response = requests.get(url)
            response_body = json.loads(response.text)
            setup = response_body['setup']
            punchline = response_body['punchline']
            return setup, punchline
        except requests.exception.HTTPError as e:
            return "", ""
