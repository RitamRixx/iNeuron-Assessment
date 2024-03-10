def max_min_distance(stalls, k):
    stalls.sort()

    low, high = 0, stalls[-1] - stalls[0]
    result = 0
    while low <= high:
        mid = (low + high) // 2
        if is_valid(stalls, k, mid):
            result = mid
            low = mid + 1
        else:
            high = mid - 1

    return result

def is_valid(stalls, k, distance):
    count = 1
    prev_stall = stalls[0]
    for stall in stalls[1:]:
        if stall - prev_stall >= distance:
            count += 1
            prev_stall = stall
    return count >= k


stalls = [1, 2, 4, 8, 9]
k = 3
print(max_min_distance(stalls, k))