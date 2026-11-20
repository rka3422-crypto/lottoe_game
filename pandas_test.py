import pandas as pd
from lotto_utils import *


count = load_counts('lotto.csv')

for i in range(3):
    print(to_text(make_hot_game(count)))