#상하좌우 여행가문제
#첫 풀이
n = 5
data = ["R","R","R","U","D","D"]
x , y = 1 , 1
dx = [0,0,1,-1] #동서남북
dy = [1,-1,0,0]
ds = ["R","L","D","U"]

for i in data:
  a = ds.index(i)
  nx = x + dx[a]
  ny = y + dy[a]
  if nx > n or nx < 1 or ny > n or ny < 1:
    continue
  else :
    x = nx
    y = ny
print(str(x)+" "+str(y))

#강의 풀이 >> 
# N 입력받기
n = int(input())
x, y = 1, 1
plans = input().split()

# L, R, U, D에 따른 이동 방향
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

# 이동 계획을 하나씩 확인
for plan in plans:
    # 이동 후 좌표 구하기
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    # 공간을 벗어나는 경우 무시
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    # 이동 수행
    x, y = nx, ny

print(x, y)