from gifpy import Gifpy, categories

KEY = "" #Your API key goes here
gifpy = Gifpy(KEY, "en_US")
suggestion = gifpy.search_suggestions("Hell")
print(suggestion)