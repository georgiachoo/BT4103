from fuzzywuzzy import fuzz
from fuzzywuzzy import process
import difflib
import pandas as pd

df = pd.read_csv("data/Master.csv")

print(list(df['Item Id']))

words = list(df['Item Id'])
print(difflib.get_close_matches('DEF016955', words))