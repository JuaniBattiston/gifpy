from gifpy import Gifpy

KEY = "" #Your API key goes here
gifpy = Gifpy(KEY, "en_US")
autocomplete = gifpy.autocomplete("Hell")
print(autocomplete)