from gifpy import Gifpy

KEY = "" #Your API key goes here
gifpy = Gifpy(KEY, "en_US")
search = gifpy.random("code!", limit = 5)
print(search)
print(search[0].url)