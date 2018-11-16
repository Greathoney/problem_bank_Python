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

def 적절한_소수_찾기(even,소수리스트):
    import itertools
    소수리스트_조합=itertools.combinations(소수리스트,2)
    for Check in 소수리스트_조합:
        if even==sum(Check):
            return Check
    return False

while True: #메뉴
    even=int(input('\n확인 할 짝수를 입력하세요. '))
    if even<=0 or even%2==1 or even==2:
        print('2보다 큰 짝수를 입력해 주세요.')
        continue

    소수리스트=소수생성기(even)
    a,b=적절한_소수_찾기(even,소수리스트)
    print('소수 ',a,'와(과) ',b,'로 ',even,'를 표현할 수 있습니다.',sep='')
