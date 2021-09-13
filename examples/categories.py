from gifpy import Gifpy, categories

KEY = "" #Your API key goes here
gifpy = Gifpy(KEY, "en_US")
categories = gifpy.categories("trending")
print(categories[0].__slots__)
print(categories[0].name)