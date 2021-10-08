from gifpy import Gifpy

KEY = ""  # Your API key goes here
gifpy = Gifpy(KEY, "en_US")
search = gifpy.search("code!", limit=5)
print(search[0].__slots__)
print(search[0].id)
