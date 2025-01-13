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

def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0
    while low <= high:
        mid = (high + low) // 2
        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            return mid
    return -1

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

def exercise_5():
    with open("input.in", 'r') as f:
        n, x = map(int, f.readline().strip().split())
        b = list(map(int, f.readline().strip().split()))
        print(n,x,b)
        if (binary_search(b, x)) != -1:
            print("yes")
        else:
            print("no")

def exercise_6():
    with open("input.in", 'r') as f:
        n, word = map(str, f.readline().strip().split())
        words = list(map(str, f.readline().strip().split()))
        for i in range(int(n)):
            if words[i] == word:
                print("yes")
        print("no")
        
def  exercise_7():
    with open("input.in", 'r') as f:
        n = int(f.readline())
        a = list(map(str, f.readline().strip().split()))
        b = list(map(str, f.readline().strip().split()))
        set_a = set(a)
        ans = set_a.intersection(b)
        write_file("output.out", [str(x) + " " for x in ans])
        

"""
Sample Python code (search.py):

n = int(input())
x = int(input())
array = list(map(int, input().split()))
array.sort()

from bisect import bisect_left
pos = bisect_left(array, x, 0, n)
if (pos < n and array[pos] == x):
    print("yes")
else:
    print("no")
    
to sort the same array with respect to primarily x values in descending order and secondarily y values in ascending order
In Python, we need to reverse the order of the sortings, so we need to sort the y values in ascending order then sort the x values in decreasing order. This takes advantage of Python preserving the order of elements if two elements have the same key.

def comp(a):
    return a[1]

def comp1(a):
    return -a[0]

p1.sort(key = comp)
p1.sort(key = comp1)
"""

def compx(point):
    return point[0]

def compy(point):
    return (int(point[1]) // 10) % 10

#Exercise 1.5: Write a program that sorts a given point array with respect to primarily ones digit of x values and secondarily tens digit of y values in ascending order. Read n, then n pairs (x, y) in each line from input.
def exercise_8():
    with open("input.in", 'r') as f:
        n = int(f.readline())
        points = []
        for i in range(n):
            points.append(list(map(int, f.readline().strip().split())))

        points.sort(key=lambda point: (point[0] % 10, (point[1] // 10) % 10))

        for point in points:
            print(point[0], point[1])

"""
def lower_bound(array, x):
    L, R = 0, len(array)
    while L < R:
        mid = (L + R) // 2
        if array[mid] < x:  # Move right if mid value is less than x
            L = mid + 1
        else:               # Move left otherwise
            R = mid
    return L  # L is the position where x could be inserted

def upper_bound(array, x):
    L, R = 0, len(array)
    while L < R:
        mid = (L + R) // 2
        if array[mid] <= x:  # Move right if mid value is less than or equal to x
            L = mid + 1
        else:                # Move left otherwise
            R = mid
    return L  # L is the position where x (or next larger value) could be inserted

def binary_search(array, x):
    lowerbound = lower_bound(array, x)
    if lowerbound < len(array) and array[lowerbound] == x:
        return lowerbound  # x exists
    return -1  # x does not exist


Range Query Using LB and UB:

To find how many elements fall into the range 
[𝐴,𝐵]
count_in_range = upper_bound(array, B) - lower_bound(array, A)

"""