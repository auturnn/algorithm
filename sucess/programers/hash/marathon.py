def solution(participant: list, completion: list):
    participant.sort()
    completion.sort()

    for i in range(len(participant)-1):
        if participant[i] != completion[i]:
            return participant[i]

    return participant[len(participant)-1]


"""
최적해.

import collections

def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]
"""
