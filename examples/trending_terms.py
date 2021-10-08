from gifpy import Gifpy

KEY = ""  # Your API key goes here
gifpy = Gifpy(KEY, "en_US")
trending_terms = gifpy.trending_terms()
print(trending_terms)
