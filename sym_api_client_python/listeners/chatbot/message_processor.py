from .joke import JokeClient
from time import sleep
import xml.etree.ElementTree as ET


class MessageProcessor:
    def __init__(self, bot_client):
        self.bot_client = bot_client

    def process(self, msg):
        msg_xml = msg['message']
        msg_root = ET.fromstring(msg_xml)
        msg_txt = msg_root[0].text

        words = msg_txt.split(" ")
        if words[0] == '/bot':
            if words[1] == "joke":
                joke_client = JokeClient()
                setup, punchline = joke_client.get_random_joke()
                for line in setup, punchline:
                    stream_id = msg['stream']['streamId']
                    msg_to_send = dict(
                        message='<messageML><div class="wysiwyg">' +
                                '<p>' +
                                line +
                                '</p></div>' 
                                '</messageML>')
                    self.bot_client.get_message_client().\
                        send_msg(stream_id, msg_to_send)
                    sleep(3)
                self.bot_client.get_message_client().send_msg_with_attachment(
                    stream_id,
                    '<messageML>A png to make you happy</messageML>',
                    'gif.png',
                    './sym_api_client_python/listeners/chatbot/giphy.png')
                return
