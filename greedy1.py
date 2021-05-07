# 1이 될때까지 
# 첫 풀이

n = 25
k = 5
count = 0

while n > 1 :
  if n % k == 0:
    n /= k
  else :
    n -= 1
  count += 1
print(count)


#강의 풀이  > 타겟이라는 변수를 만들어 -1을 수행하는 과정을 한번에 처리 한다 시간 복잡도를 획기적으로 줄일 수 있는 테크닉

# N, K공백을 기준으로 구분하여 입력 받기
n, k = map(int, input().split())

result = 0

while True:
    # N이 K로 나누어 떨어지는 수가 될 때까지만 1씩 빼기
    target = (n // k) * k
    result += (n - target)
    n = target
    # N이 K보다 작을 때 (더 이상 나눌 수 없을 때) 반복문 탈출
    if n < k:
        break
    # K로 나누기
    result += 1
    n //= k

# 마지막으로 남은 수에 대하여 1씩 빼기
result += (n - 1)
print(result)