from gifpy import Gifpy

KEY = "" #Your API key goes here
gifpy = Gifpy(KEY, "en_US")

# Look up only one gif
gif = gifpy.gifs("15997191") # Returns a Gif Object
print(gif.__slots__)

#Look up many gifs
gifs = gifpy.gifs("15997191,19025805,22726592") # Returns a list of Gif Objects
print(gifs)
print(gifs[0].id)