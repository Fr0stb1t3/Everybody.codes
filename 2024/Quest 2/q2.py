import re
import numpy as np

runesInput="""WORDS:THE,OWE,MES,ROD,HER

AWAKEN THE POWER ADORNED WITH THE FLAMES BRIGHT IRE"""
with open("input.txt") as f:
    runes,inscriptions=f.read().strip().split("\n\n")
    # runes,inscriptions=runesInput.strip().split("\n\n")
    runes=runes[6:].split(",")
    inscriptions=inscriptions.split()

# print(runes)
# print(inscriptions)
count=0
for word in inscriptions:
    for rune in runes:
        if rune in word:
            count+=1

print("Part 1:",count)

runesInput="""WORDS:THE,OWE,MES,ROD,HER,QAQ

AWAKEN THE POWE ADORNED WITH THE FLAMES BRIGHT IRE
THE FLAME SHIELDED THE HEART OF THE KINGS
POWE PO WER P OWE R
THERE IS THE END
QAQAQ"""

with open("input2.txt") as f:
    runes,inscriptions=f.read().strip().split("\n\n")
    # runes,inscriptions=runesInput.strip().split("\n\n")
    runes=runes[6:].split(",")
    inscriptions_lines=inscriptions.splitlines()
    inscriptions = [i.split() for i in inscriptions_lines]
    runes += [w[::-1] for w in runes]
    runes=list(set(runes))


# print(runes)
# print(inscriptions)

count = 0

for line in inscriptions_lines:
    indexes: set[int] = set()
    for rune in runes:
        if rune in line:
            start = 0
            while True:
                start = line.find(rune,start)
                if start == -1:
                    break
                indexes.update([start+i for i in range(len(rune))])
                start+=1
    # print(indexes)
    count +=len(indexes)
                

print("Part 2:",count)

runesInput="""WORDS:THE,OWE,MES,ROD,RODEO

HELWORLT
ENIGWDXL
TRODEOAL"""

with open("input3.txt") as f:
    runes,inscriptions=f.read().strip().split("\n\n")
    # runes,inscriptions=runesInput.strip().split("\n\n")
    runes=runes[6:].split(",")
    runes.extend([rune[::-1] for rune in runes])
    inscriptions_lines=inscriptions.splitlines()
    inscriptions_grid=[[0]*len(line) for line in inscriptions_lines]

for i,line in enumerate(inscriptions_lines):
    for j in range(len(line)):
        for rune in runes:
            l=len(rune)
            if (line*2)[j:j+l] == rune:
                for k in range(l):
                    inscriptions_grid[i][(j+k)%len(line)] = 1
senil = list(map("".join,zip(*inscriptions_lines)))
for j,enil in enumerate(senil):
    for i in range(len(enil)):
        for rune in runes:
            l=len(rune)
            if enil[i:i+l] == rune:
                for k in range(l):
                    inscriptions_grid[i+k][j] = 1

# print(inscriptions_grid)

print("Part 3",sum(map(sum,inscriptions_grid)))