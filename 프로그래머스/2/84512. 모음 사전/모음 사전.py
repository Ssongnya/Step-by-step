def solution(word):
    answer = 0

    vowel = ['A', 'E', 'I', 'O', 'U']
    case = [781, 156, 31, 6, 1]
    
    for i, alpha in enumerate(word):
        idx = vowel.index(alpha)
        answer += case[i] * idx + 1
    
    return answer