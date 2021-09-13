from datetime import datetime
from .media import Media

class Gif():
    
    __slots__ = (
        "id",
        "title",
        "h1_title",
        "media",
        "bg_color",
        "created_at",
        "itemurl",
        "url",
        "tags",
        "flags",
        "shares",
        "has_caption",
        "has_audio"
    )

    def __init__(self, response:dict):
        self.id: int = int(response["id"])
        self.title: str = response["title"]
        self.h1_title: str = response["h1_title"]
        self.media: list = Media(response["media"][0])
        self.bg_color: str = response["bg_color"]
        self.created_at: float = response["created"] #Unix Time
        self.itemurl: str = response["itemurl"]
        self.url: str = response["url"]
        self.tags: list = response["tags"]
        self.flags: list = response["flags"]
        self.shares: int = response["shares"]
        self.has_caption: bool = response["hascaption"]
        self.has_audio: bool = response["hasaudio"]

    def __repr__(self) -> str:

        attrs = [
            ('id', self.id),
            ('title', self.title),
            ('created_at', self.created_at),
        ]
        joined = ' '.join('%s=%r' % t for t in attrs)
        return f'<{self.__class__.__name__} {joined}>'

    @property
    def utc_time(self):
        """
        Return UTC gif creation time.
        """

        return datetime.utcfromtimestamp(self.created_at).strftime('%Y-%m-%d %H:%M:%S')