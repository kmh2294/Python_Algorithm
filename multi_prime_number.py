import math

n = 1000 #2부터 1000까지 자연수중 소수판별
#소수인지 아닌지 값을 담을 배열초기화
array = [True for i in range(n + 1)]
#2부터 n의제곱근 까지의 모든 수를 확인하여
for i in range(2 , int(math.sqrt(n)) + 1):
    if array[i] == True : # i 가 소수인 경우 (남아있는경우)
        j = 2
        #i 를 제외한 배수를 모두 제거
        while i * j <= n :
            array[i * j] = False
            j += 1
#출력
for i in range(2 , n + 1):
    if array[i] :
        print(i , end=' ')

