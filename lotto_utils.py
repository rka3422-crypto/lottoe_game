import random 
import pandas as pd

def make_game():
    return sorted(random.sample(range(1,46),6))

def make_games(count):
    games=[]
    for i in range(count):
        games.append(make_game())
    return games

def to_text(game):
    words = []
    for n in game:
        words.append(f'{n:3d}')
    return ' '.join(words)

COLS = ['당첨번호1', '당첨번호2', '당첨번호3',
'당첨번호4', '당첨번호5', '당첨번호6']

def load_counts(fname):
    df = pd.read_csv(fname, encoding='utf-8-sig')
    count = {}
    for n in range(1, 46):
        count[n] = 0
    for col in COLS:
        for n in df[col]:
            count[n] += 1
    return count

def top_numbers(count, top=20):
    items = sorted(count.items(), key=lambda x: x[1], reverse=True)
    nums = []
    for n, c in items[:top]:
        nums.append(n)
    return nums

def make_hot_game(count):
    return sorted(random.sample(top_numbers(count), 6))
