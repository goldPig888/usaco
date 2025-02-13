def minimum_boredom_value(test_cases):
    results = []
    
    for N, M, arr in test_cases:
        residue_costs = {}
        
        # Compute residues and their frequency
        for a in arr:
            r = a % M
            residue_costs[r] = residue_costs.get(r, 0) + 1
        
        # Calculate the minimum cost to align all to a residue
        min_cost = float('inf')
        for r in residue_costs:
            total_cost = 0
            for a in arr:
                # Cost to align a[i] to the residue r
                diff = abs(a % M - r)
                total_cost += min(diff, M - diff)
            min_cost = min(min_cost, total_cost)
        
        results.append(min_cost)
    
    return results


# Input parsing and execution
if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().split()
    
    T = int(data[0])
    idx = 1
    test_cases = []
    
    for _ in range(T):
        N, M = map(int, data[idx:idx+2])
        idx += 2
        arr = list(map(int, data[idx:idx+N]))
        idx += N
        test_cases.append((N, M, arr))
    
    results = minimum_boredom_value(test_cases)
    for result in results:
        print(result)