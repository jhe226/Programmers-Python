from collections import deque
def solution(numbers, target):
    answer = 0
    queue = deque()
    n = len(numbers)
    queue.append([numbers[0], 0])
    queue.append([-1*numbers[0],0])
    while queue:
        tmp, idx = queue.popleft()
        idx += 1
        if idx < n:
            queue.append([tmp+numbers[idx], idx])
            queue.append([tmp-numbers[idx], idx])
        else:
            if tmp == target:
                answer += 1
    return answer


'''
<다른 풀이>
# 재귀 이용

    def solution(numbers, target):
    if not numbers and target == 0 :
        return 1
    elif not numbers:
        return 0
    else:
        return solution(numbers[1:], target-numbers[0]) + solution(numbers[1:], target+numbers[0])
'''
