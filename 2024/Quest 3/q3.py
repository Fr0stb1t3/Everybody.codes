#Attempt 1

# from pprint import pprint
# from copy import deepcopy
# from collections import Counter
# inGridSample="""..........
# ..###.##..
# ...####...
# ..######..
# ..######..
# ...####...
# .........."""

# with open("input.txt") as f:
#     inGrid=f.read().strip()

# inGridSample=inGridSample.replace("#","1")
# inGrid = inGrid.replace("#","1")
# # print(inGrid)
# inGrid=inGrid.split()
# inGrid = [list(i) for i in inGrid]
# inGridSample=inGridSample.split()
# inGridSample = [list(i) for i in inGridSample]
# # pprint(inGrid)

# def grid_to_str(grid):
#     g1=["".join(j) for j in grid]
#     return "\n".join(g1)
# def check_coords(grid, coords, val,val2):
#     return all(grid[x][y] == val == val2 for x, y in coords)
# def get_coordinates(i, j,max_x,may_y, directions=[(-1,0), (1,0), (0,-1), (0,1)]):
#     coordinates = []
#     for dx, dy in directions:
#         new_x = i + dx
#         new_y = j + dy
#         if new_x<0 or new_x>=max_x or new_y<0 or new_y>=may_y:
#             continue
#         coordinates.append((new_x, new_y))
#     return coordinates
# def grid_digger(g,layer,DMAP=[(-1,0),(1,0),(0,-1),(0,1)]):
#     grid=deepcopy(g)
#     m,n=len(grid),len(grid[0])
#     flag=False
#     if layer>=10:
#         flag=True
#     replacement=[]
#     for i in range(m):
#         for j in range(n):
#             if grid[i][j]==".":
#                 continue
#             else:
#                 val = grid[i][j]
#                 coords=get_coordinates(i,j,m,n,DMAP)
#                 # print(check_coords(grid=grid,coords=coords,val=val,val2=str(layer-1)))
#                 # print(coords)
#                 # print(grid[coords[0][0]][coords[0][1]],grid[coords[1][0]][coords[1][1]],grid[coords[2][0]][coords[2][1]],grid[coords[3][0]][coords[3][1]],"#",val)
#                 if flag and layer >10:
#                     # if grid[coords[0][0]][coords[0][1]] == grid[coords[1][0]][coords[1][1]] == grid[coords[2][0]][coords[2][1]] == grid[coords[3][0]][coords[3][1]] == val == chr(ord('a')+layer-1):
#                     #     replacement.append((i,j))
#                     if check_coords(grid=grid,coords=coords,val=val,val2=chr(ord('a')+layer-10-1)):
#                         replacement.append((i,j))
#                 else:   
#                     # if grid[coords[0][0]][coords[0][1]] == grid[coords[1][0]][coords[1][1]] == grid[coords[2][0]][coords[2][1]] == grid[coords[3][0]][coords[3][1]] == val == str(layer-1):
#                     #     replacement.append((i,j))
#                     if check_coords(grid=grid,coords=coords,val=val,val2=str(layer-1)):
#                         replacement.append((i,j))
#     # print(replacement)
#     for i,j in replacement:
#         if flag:
#             grid[i][j] = chr(ord('a')+layer-10)
#         else:
#             grid[i][j] = str(layer)
#     return grid

# def part(grid,part=1):
#     layer=2
#     gp= deepcopy(grid)
#     if part == 3:
#         gn= grid_digger(grid,layer,DMAP=[(-1,0),(1,0),(0,-1),(0,1),(-1,1),(-1,-1),(1,-1),(1,1)])
#     else:    
#         gn= grid_digger(grid,layer)
#     while grid_to_str(gp) != grid_to_str(gn):
#         layer+=1
#         # if layer ==10:
#         #     break
#         gp = deepcopy(gn)
#         gn = grid_digger(gp,layer)
#     print(grid_to_str(gn))
#     p=Counter(grid_to_str(gn))
#     del p["."]
#     del p["\n"]

#     print(p)
#     sol=0
#     for key,val in p.items():
#         if key.isalpha():
#             sol += (ord(key) - ord('a')+10)*int(val)
#         else:
#             sol += int(key)*int(val)

#     print(f'Part {part}:',sol)

# # part(grid=inGridSample)
# # part(grid=inGrid)

# with open("input2.txt") as f:
#     inGrid_p2=f.read().strip()
#     inGrid_p2 = inGrid_p2.replace("#","1")
    
#     inGrid_p2=inGrid_p2.split()
#     inGrid_p2 = [list(i) for i in inGrid_p2]

# # part(grid=inGrid_p2,part=2)

# with open("input3.txt") as f:
#     inGrid_p3=f.read().strip()
#     inGrid_p3 = inGrid_p3.replace("#","1")
    
#     inGrid_p3=inGrid_p3.split()
#     # filler=["."]*len(inGrid_p3[0])
#     # print(filler)
#     # inGrid_p3 = [["."]+list(i)+["."] for i in inGrid_p3]
#     # inGrid_p3.insert(0,filler)
#     # inGrid_p3.append(filler)
#     inGrid_p3 = [list(i)for i in inGrid_p3]

# # print(grid_to_str(inGrid_p3))
# part(grid=inGrid_p3,part=3)
# # part(grid=inGridSample,part=2)
# # part(grid=inGridSample,part=3)

# Optimized code
ADJ = [(0,-1),(0,1),(1,0),(-1,0)]
ADDJ = [(1,1),(-1,-1),(1,-1),(-1,1)]
def new_depth(i,j):
    dep = 1e100
    for di,dj in ADJ:
        ni = i+di
        nj = j+dj
        if ni<0 or ni>=len(depths) or nj<0 or nj>=len(depths[0]):
            dep = 0
        else:
            dep = min(dep,depths[ni][nj])
    return dep + 1

for part in [1,2,3]:
    if part == 3:
        ADJ += ADDJ
    with open(f"input{part}.txt") as f:
        lines = f.read().splitlines()
    depths = [[0]*len(line) for line in lines]
    locations = [(i,j) for i,line in enumerate(lines) for j,c in enumerate(line) if c=="#"]
    total = 0
    prev_total = -1
    while total != prev_total:
        for i,j in locations:
            depths[i][j] = new_depth(i,j)
        prev_total = total
        total = sum(map(sum,depths))
    print(f"Part {part}:",total)