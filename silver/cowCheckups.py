def count_checked_cows(N, a, b):
    from collections import defaultdict

    # Map positions of each species in b
    position_map = defaultdict(list)
    for i in range(N):
        position_map[b[i]].append(i)

    # Fenwick Tree (Binary Indexed Tree) helper functions
    def update(bit, index, value):
        while index <= N:
            bit[index] += value
            index += index & -index

    def query(bit, index):
        sum_val = 0
        while index > 0:
            sum_val += bit[index]
            index -= index & -index
        return sum_val

    # Fenwick Tree for counting matches
    bit = [0] * (N + 1)
    match_count = 0

    # Traverse all possible l and r
    for l in range(N):
        # Reset BIT for new l
        bit = [0] * (N + 1)

        # Add matches for current l
        for r in range(l, N):
            # Reverse would mean matching a[r] with b[reversed position]
            for pos in position_map[a[r]]:
                if l <= pos <= r:
                    update(bit, pos + 1, 1)
            
            # Count matches in current range
            matches = query(bit, r + 1) - query(bit, l)
            match_count += matches

    return match_count


# Input handling
N = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# Output the result
print(count_checked_cows(N, a, b))