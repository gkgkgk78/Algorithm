def check(mid, rocks, n):
    # mid : 최소거리를 의미함

    ind = 0
    last = len(rocks)
    before = 0
    count = 0
    while ind< last:
        now = rocks[ind]
        if now - before >= mid:
            before = now
        else:
            count += 1
        ind += 1
    return count


def solution(distance, rocks, n):
    answer = 0
    rocks.append(distance)
    rocks.sort()

    left = 0
    right = distance+1

    while left+1 < right :
        mid = (left + right) // 2
        now = check(mid, rocks, n)
        if now > n:
            right = mid
        else:
            answer = mid

            left = mid
    return answer