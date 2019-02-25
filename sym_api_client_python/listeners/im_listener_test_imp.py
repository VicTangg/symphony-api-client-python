from .imListener import IMListener
import logging
# A sample implementation of Abstract imListener class
# The listener can respond to incoming events if the respective event
# handler has been implemented


class IMListenerTestImp(IMListener):

    def __init__(self, sym_bot_client):
        self.botClient = sym_bot_client

    def on_im_message(self, im_message):
        logging.debug('message received in IM', im_message)

    def on_im_created(self, im_created):
        logging.debug('IM created!', im_created)
