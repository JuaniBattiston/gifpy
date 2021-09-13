# Gifpy

A simple API wrapper for the Tenor API

# Installation

**Python 3.9 or higher is recommended**
```
python3 -m pip install gifpy
```
Clone repository:
```
$ git clone https://github.com/Batucho/gifpy
```

# API Token

You can get your API token here:  [Tenor Developer Dashboard](https://tenor.com/developer/dashboard)

# Code Examples

### Simple Search
```py
from gifpy import Gifpy

gifpy = Gifpy("key", "en_US")
search = gifpy.search("code!", limit  =  5)

print(search[0].__slots__)
print(search[0].id)
```
### Gif Search
```py
from gifpy import Gifpy

KEY =  ""  #Your API key goes here
gifpy = Gifpy(KEY, "en_US")

# Look up only one gif
gif = gifpy.gifs("15997191") # Returns a Gif Object
print(gif.__slots__)

#Look up many gifs
gifs = gifpy.gifs("15997191,19025805,22726592") # Returns a list of Gif Objects
print(gifs)
print(gifs[0].id)
```

### [More examples here!](https://github.com/Batucho/gifpy/tree/main/examples)

**Feel free to contribute or inform any bug!**