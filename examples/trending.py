from gifpy import Gifpy

KEY = "" #Your API key goes here
gifpy = Gifpy(KEY, "en_US")
trending_gifs = gifpy.trending()
print([i.id for i in trending_gifs])