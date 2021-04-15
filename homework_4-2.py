#!/usr/bin/env python
# coding: utf-8

# In[62]:


from random import sample

class BCJudge:
    
    def __init__(self, players, digits=4, rounds=10, runs=100):
        self.digits = digits
        self.runs = runs
        self.rounds = rounds
        self.names = players.split(',')
        self.players = [None] * len(self.names)
        for i, n in enumerate(self.names):
            self.players[i] = getattr(__import__(n), n.capitalize())(digits)
            
    def play(self, verbose=True):
        players_win = [0] * len(self.players)
        
        for ro in range(self.rounds):
            for p in self.players:
                p.renew()
            self.game = sample(range(10), k=self.digits)
            result = [None] * len(self.players)
            winners = set()
            for r in range(self.runs):
                for i, p in enumerate(self.players):
                    g = p.guess(result[i])
                    result[i] = self._judge(g)
                    if result[i][0] == len(self.game):
                        winners.add(self.names[i])
                        players_win[i] += 1
                if winners:
                    if verbose:
                        print(f"[round {ro: >2}] {', '.join(winners)} win {str(self.game)} for {r+1} runs")
                    break
        
            if verbose and not winners:
                print(f'[round {ro: >2}] No one wins {str(self.game)} for {r+1} runs')
                                                         
        return {n:players_win[i] for i, n in enumerate(self.names)}
    
    #  判定 ?A ?B
    def _judge(self, guess):
        a = 0
        b = 0
        for k in range(self.digits):
            if self.game[k] == guess[k]:
                a += 1
                continue
            for j in [d for d in range(len(self.game)) if d != k]:
                if guess[j] == self.game[k]:
                    b += 1
                    break
         
        return a, b
                              

from sys import argv
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('players', help='players module name, seperated by common')
parser.add_argument('-d', '--digits', default=4, type=int)
parser.add_argument('-R', '--rounds', default=10, type=int)
parser.add_argument('-r', '--runs', default=100, type=int)
parser.add_argument('-v', '--verbose', action='store_true')
                          
#avoid jupyter notebook exception
if argv[0][-21:] == 'ipykernel_launcher.py':
    args = parser.parse_args(args=[])
else:
    args = parser.parse_args()

args = parser.parse_args()

game = BCJudge(args.players, digits=args.digits, rounds=args.rounds, runs=args.runs)
r = game.play(args.verbose)
order = sorted(list(r.items()), key=lambda x: x[1], reverse=True)
print(f'winners statistics:', end=' ')
for o in order:
    print(f'{o[0]} {o[1]}/{args.rounds}', end=' ')


# In[ ]:




