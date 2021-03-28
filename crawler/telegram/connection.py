import configparser
import pathlib # todo: change pathing system
import json
import logging
from datetime import datetime as dt
import pandas as pd

from telethon import TelegramClient, sync #todo: needs to use async data pull later
CONFIG = configparser.ConfigParser()
CONFIG.read("crawler/telegram/config/telegram_keys.ini")

LOGGER = logging.getLogger(__name__)

class TelegramConnection:
    def __init__(self, config=CONFIG["Telegram"]):
        self._config = config
        self.open = False

    def __repr__(self):
        return f'Connection to telegram open: <{self.open}>'

    @property
    def client(self):
        self._client = TelegramClient(f'session_{dt.now().strftime("%Y%m%d%M%H%S")}', api_id=self._config['api_id'], api_hash=self._config['api_hash'])
        return self._client

    def _start(self):
        await self.client.start()
        LOGGER.info('Started Connection to Telegram...')
        self.open = True

    def get_users_in_channel(self, channel_name):
        '''
        Method to pull users currently enlisted in a given channel.

        :param channel_name: string
        :return: pandas DataFrame containing user details
        '''
        if not self.open:
            self._start()
        users = self.client.get_participants(channel_name)
        firstname = []
        lastname = []
        username = []
        if len(users):
            for x in users:
                firstname.append(x.first_name)
                lastname.append(x.last_name)
                username.append(x.username)
        return pd.DataFrame

