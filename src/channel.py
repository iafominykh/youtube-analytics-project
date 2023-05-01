import json
import os
from googleapiclient.discovery import build

class Channel:
    """Класс для ютуб-канала"""

    @classmethod
    def get_service(cls):
        api_key: str = os.getenv('YT_API_KEY')
        return build('youtube', 'v3', developerKey=api_key)

    def __init__(self, channel_id: str):
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.__channel_id = channel_id
        youtube = self.get_service()
        self.channel = youtube.channels().list(id=channel_id, part='snippet,statistics').execute()
        self.title = self.channel["items"][0]["snippet"]["title"]
        self.description = self.channel["items"][0]["snippet"]["description"]
        self.url = "https://www.youtube.com/channel/" + channel_id
        self.subscriberCount = int(self.channel["items"][0]["statistics"]["subscriberCount"])
        self.video_count = int(self.channel["items"][0]["statistics"]["videoCount"])
        self.viewCount = int(self.channel["items"][0]["statistics"]["viewCount"])



    def print_info(self):
        """Выводит в консоль информацию о канале."""
        # dict_to_print = youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()
        print(json.dumps(self.channel, indent=2, ensure_ascii=False))




    def to_json(self, file_name):
        """Метод, сохраняющий в файл значения атрибутов экземпляра Channel"""
        dictionary = {
            'id': self.__channel_id,
            'title': self.title,
            'description': self.description,
            'url': self.url,
            'subscriberCount': self.subscriberCount,
            'video_count': self.video_count,
            'viewCount': self.viewCount
        }

        with open(file_name, 'w', encoding='utf-8') as file:
            json.dump(dictionary, file, ensure_ascii=False)

    def __repr__(self):
        return f'{self.__channel_id}'

    def __str__(self):
        return f'{self.url}'

    def __add__(self, other):
        return int(self.subscriberCount) + int(other.subscriberCount)

    def __sub__(self, other):
        return int(self.subscriberCount) - int(other.subscriberCount)

    def __gt__(self, other):
        return int(self.subscriberCount) > int(other.subscriberCount)

    def __ge__(self, other):
        return int(self.subscriberCount) >= int(other.subscriberCount)

    def __lt__(self, other):
        return int(self.subscriberCount) < int(other.subscriberCount)

    def __le__(self, other):
        return int(self.subscriberCount) <= int(other.subscriberCount)

    def __eq__(self, other):
        return int(self.subscriberCount) == int(other.subscriberCount)

    def __str__(self):
        return f'{self.url}'
