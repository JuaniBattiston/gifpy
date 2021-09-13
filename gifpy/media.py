from .errors import GifpyInvalidFormat
from .errors import GifpyFormatNotAvailable

class MediaFormat():

    __slots__ = (
        "format_dict",
        "url",
        "size",
        "dims",
        "preview",
        "duration"
    )

    def __init__(self, format_dict: list):
        self.format_dict = format_dict
        self.url = format_dict["url"]
        self.size = format_dict["size"]
        self.dims = format_dict["dims"]
        self.preview = format_dict["preview"]
        self.duration = format_dict["duration"] if "duration" in format_dict else None
    
    def __repr__(self) -> str:

        attrs = [
            ('url', self.url),
            ('size', self.size),
            ('dims', self.dims),
            ('preview', self.preview),
            ('duration', self.duration),
        ]
        joined = ' '.join('%s=%r' % t for t in attrs)
        
        return f'<{self.__class__.__name__} {joined}>'


class Media():

    def __init__(self, media: list):
        self.media = media
        
    def get_format(self, _format):

        available_formats = ("gif", "mediumgif", "tinygif", "nanogif", "mp4",
        "loopedmp4","tinymp4","nanomp4","webm","tinywebm","nanowebm")

        if _format not in available_formats:
            raise GifpyFormatNotAvailable

        if _format not in self.media:
            raise GifpyInvalidFormat
        
        return MediaFormat(self.media[_format])