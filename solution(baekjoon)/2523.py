# 문제
# 예제를 보고 규칙을 유추한 뒤에 별을 찍어 보세요.

# 입력
# 첫째 줄에 N(1 ≤ N ≤ 100)이 주어진다.

# 출력
# 첫째 줄부터 2×N-1번째 줄까지 차례대로 별을 출력한다.

# 예제 입력 1
# 3

# 예제 출력 1
# *
# **
# ***
# **
# *




num = int(input())

lis = []
order = list(range(1,num))
lis = lis + order
lis.append(num)
order.reverse()
lis = lis + order

for i in lis:
    
    print('*' * i)