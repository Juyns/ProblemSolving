# 18429 - better ver.
"""
    asdhugh1님의 코드를 보고 공부한 뒤 재작성
    접근 방식:
        permutation이 아니라 dp로 접근하며, dp를 dictionary로 구현.
        키: 숫자들을 구분자를 두고 연결한 문자열. "구분자".join(map(str, subarray))의 형태
        이후 length 0과 length 1인 경우의 예외처리가 된 재귀함수 활용. subarray를 잘게 잘라서 각 key에 대한 value를 부여
        (0이면 500이 넘지 못한 경우, 1이면 500이 넘는 경우)
"""

n, k = map(int, input().split())
kits = list(map(int, input().split()))
dp = {}
def make_key(lst):
    return ".".join(map(str, lst))

def calculate_weights(current, kits):
    l = len(kits)
    result = 0
    if l == 0:
        return 0
    elif l == 1:
        if current + kits[0] - k < 500: return 0
        return 1
    for i in range(l):
        temp = current + kits[i] - k
        if temp < 500:
            continue
        sub_list = kits[:i] + kits[i+1:]
        new_key = make_key(sub_list)
        if new_key not in dp:
            dp[new_key] = calculate_weights(temp, sub_list)
        result += dp[new_key]
    return result

print(calculate_weights(500, kits))

"""
    실수했던 부분: current 값 변경을 calculate_weights 실행 후 원상복구 안 해줌. 다음 loop에서 계산이 꼬였었다.
"""