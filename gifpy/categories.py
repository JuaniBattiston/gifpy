class Category:

    __slots__ = ("tag", "type", "search_term", "path", "image", "name", "character")

    def __init__(self, tag, _type):
        self.tag = tag
        self.type = _type
        self.search_term = tag["searchterm"]
        self.path = tag["path"]
        self.image = tag["image"] if _type != "emoji" else ""
        self.name = tag["name"]
        self.character = tag["character"] if _type == "emoji" else ""

    def __repr__(self):

        return f"<{self.__class__.__name__} type={self.type} name={self.name}>"
