import sys

num = int(input())

def 소수생성기(even): # 2부터 n까지의 소수를 리스트로 반환합니다.
    소수리스트=[1,2]
    for num in range(3,even+1):
        check=True
        for 소수 in 소수리스트:
            if not 소수==1:
                if num%소수==0: #소수가 아니면 참
                    check=False
        if check:
            소수리스트.append(num)

    return 소수리스트  #[2,3,5,7,...,n보다 작은 가장 큰 소수]

import math
소수리스트 = 소수생성기(int(math.sqrt(num)))

for 소수 in 소수리스트:
    if num % 소수 == 0:
        print('아님')

print("마즘")
