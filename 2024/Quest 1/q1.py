with open("input.txt") as f:
    monsters=f.read().strip()
sol=0
potion={
    "A":0,
    "B":1,
    "C":3,
    "D":5,
    "x":0
}
for monster in monsters:
    # print(monster)
    sol+= potion.get(monster)

print("Part 1:",sol)

with open("input2.txt") as f:
    monsters2=f.read().strip()
    # monsters2="AxBCDDCAxD"
sol=0

for monster in range(0,len(monsters2),2):
    # print(monsters[monster:monster+2])
    if "x" in monsters2[monster:monster+2]:

        sol+= potion.get(monsters2[monster])
        sol+= potion.get(monsters2[monster+1])
    else:
        sol+= potion.get(monsters2[monster])+1
        sol+= potion.get(monsters2[monster+1])+1
    
print("Part 2:",sol)

with open("input3.txt") as f:
    monsters3=f.read().strip()
    # monsters3="xBxAAABCDxCC"
sol=0

for monster in range(0,len(monsters3),3):
    if "x" in monsters3[monster:monster+3]:
        if monsters3[monster:monster+3].count("x")>1:
            for i in range(3):
                sol+= potion.get(monsters3[monster+i])
        else:
            for i in range(3):
                if monsters3[monster+i] != "x":
                    sol+= potion.get(monsters3[monster+i])+1
    else:
        # sol+= potion.get(monsters3[monster])+2
        # sol+= potion.get(monsters3[monster+1])+2
        # sol+= potion.get(monsters3[monster+2])+2
        for i in range(3):
                sol+= potion.get(monsters3[monster+i])+2
    
print("Part 3:",sol)