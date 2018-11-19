print('2진수를 모두 뽑아내는 프로그램')
num=int(input('몇 자리의 모든 이진수를 출력할까요?'))
for a in range(2**num,2**(num+1)):
    b=bin(a)
    b=b.replace('0b1','')
    print(b)
    
