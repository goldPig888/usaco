def write_file(file, lines):
    with open(file, 'w') as f:
        f.writelines(lines)

def smallest(list, start):
    min = start
    for i in range(start, len(list)):
        if list[i] < list[min]:
            min = i
    return min

def largest(list, start):
    max = start
    for i in range(start, len(list)):
        if list[i] > list[max]:
            max = i
    return max

def lim(list, start, end):
    min = start
    for i in range(start, end):
        if list[i] < list[min]:
            min = i
    return min

def exercise_1():
    with open("input.in", 'r') as f:
        n = int(f.readline())
        nums = list(map(int, f.readline().strip().split()))
    i = 0
    while (i != n):
        pos = smallest(nums, i)
        if (i !=pos):
            nums[i] = nums[pos] + nums[i]
            nums[pos] = nums[i] - nums[pos]
            nums[i] = nums[i] - nums[pos]
        i+=1
    write_file("output.out", [str(x) + " " for x in nums])

def exercise_2():
    with open("input.in", 'r') as f:
        n = int(f.readline())
        words = list(map(str, f.readline().strip().split()))
    i = 0
    while (i != n):
        pos = largest(words, i)
        if (i !=pos):
            temp = words[i]
            words[i] = words[pos]
            words[pos] = temp
        i+=1
    write_file("output.out", [str(x) + " " for x in words])

def exercise_3():
    with open("input.in", 'r') as f:
        n, x, y = map(int, f.readline().strip().split())
        nums = list(map(int, f.readline().strip().split()))
        while (x != y):
            pos = lim(nums, x, y)
            temp = nums[x]
            nums[x] = nums[pos]
            nums[pos] = temp
            x+=1
    write_file("output.out", [str(x) + " " for x in nums])

def exercise_4():
    with open("input.in", 'r') as f:
        n = int(f.readline())
        a = list(map(int, f.readline().strip().split()))
        b = list(map(int, f.readline().strip().split()))
        ans = []
        for i in range(n*2):
            if len(a) == 0:
                ans.append(b.pop(0))
            elif len(b) == 0:
                ans.append(a.pop(0))
            elif a[0] < b[0]:
                ans.append(a.pop(0))
            else:
                ans.append(b.pop(0))
        write_file("output.out", [str(x) + " " for x in ans])


"""

### BUILT IN SORT AND SEARCH FUNCTIONS
n = int(input())
array = input().split()
for i in range(n):
    array[i] = int(array[i])
    
array.sort()

for i in range(n):
    print(array[i], end=" ")
print()


### FOR REVERSE ORDER
array.sort(reverse=True)

### CUSTOM COMP

def comp(a):
    return a
    
like for reverse order, you can do:
def comp(a):
    return -a
"""
