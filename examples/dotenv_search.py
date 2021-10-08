from gifpy import Gifpy
from dotenv import load_dotenv
import os

load_dotenv()

gifpy = Gifpy(os.getenv("KEY"), "en_US")
search = gifpy.search("code!", limit=5)
print(search[0].__slots__)
print(search[0].id)
