from pprint import pprint
with open("input1.txt") as f:
    nails=f.read().strip().splitlines()
    nails=list(map(int,nails))
    nails.sort()
    # print(nails)

def part(nums,part=1):
    minval=nums[0]
    sol=0
    for num in nums:
        sol+= (num-minval)
    print(f"Part {part}:",sol)

part([3,4,7,8])
part(nails)

with open("input2.txt") as f:
    nails2=f.read().strip().splitlines()
    nails2=list(map(int,nails2))
    nails2.sort()
    # print(nails)
part(nails2,2)
with open("input3.txt") as f:
    nails3=f.read().strip().splitlines()
    nails3=list(map(int,nails3))
    nails3.sort()
    # print(nails)

def part3(nums):
    minVal = nums[len(nums)//2]
    sol=0
    for i in range(len(nums)):
        sol+=abs(minVal-nums[i])
    print("Part 3:",sol)

part3([2,4,5,6,8])
part3(nails3)