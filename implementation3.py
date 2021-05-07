#문자열 재정렬 문제

n = 'K1KA5CB7'

sum = 0
result = []

for i in n:
  if i.isalpha():
    result.append(i)
  else : 
    sum += int(i)

result.sort()
print(''.join(result) + str(sum))

##강의 풀의 >>>>>> 마지막에 숫자가 0일수도있음을 확인하고 결과 배열에 한번에 붙혀 join 시키면 되는거였다.


data = input()
result = []
value = 0

# 문자를 하나씩 확인하며
for x in data:
    # 알파벳인 경우 결과 리스트에 삽입
    if x.isalpha():
        result.append(x)
    # 숫자는 따로 더하기
    else:
        value += int(x)

# 알파벳을 오름차순으로 정렬
result.sort()

# 숫자가 하나라도 존재하는 경우 가장 뒤에 삽입
if value != 0:
    result.append(str(value))

# 최종 결과 출력(리스트를 문자열로 변환하여 출력)
print(''.join(result))