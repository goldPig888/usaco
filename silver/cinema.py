def euclidean(p1,p2):
    return ((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)**0.5

def comp_dist(x):
    return x[0], x[1], x[2]

w, r = map(int, input().strip().split())
coords = []
priority = 1
grid = [[0 for i in range(w)] for j in range(r)]
for i in range(1, r+1):
    for j in range(1, w+1):
        dist = euclidean([i,j],[1, ((w+1)/2)])
        coords.append([dist,i,j])
coords.sort(key=comp_dist)

for i in coords:
    grid[i[1]-1][i[2]-1] = priority
    priority += 1
        
grid.sort(reverse=True)
for i in grid:
    print(" ".join([str(x) for x in i]))
        

