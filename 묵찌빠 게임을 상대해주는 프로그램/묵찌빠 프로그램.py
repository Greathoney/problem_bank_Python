import random

def 판정(너, 상대):
    if 너=='묵':
        if 상대=='묵':
            승패='Draw'
        elif 상대=='찌':
            승패='Win'
        else:
            승패='Lose'
    elif 너=='찌':
        if 상대=='묵':
            승패='Lose'
        elif AI=='찌':
            승패='Draw'
        else:
            승패='Win'
    elif 너=='빠':
        if 상대=='묵':
            승패='Win'
        elif 상대=='찌':
            승패='Lose'
        else:
            승패='Draw'
    return 승패

묵찌빠=['묵','찌','빠']
print('Notice: 입력은 묵, 찌, 빠만 가능합니다!!')
너=input('묵, 찌, ...')
상대=random.choice(묵찌빠)
print(상대)
승패 = 판정(너, 상대)

while 승패=='Draw':
    너=input('비겼네... 다시! 묵 찌...')
    상대=random.choice(RSP)
    print(상대)
    승패 = 판정(너, 상대)

while 승패!='Draw':
    if 승패=='Win':
        상황='Win'
        print('너의 주도권! ',너,'에',너,'에...', end='')
        너=input()
        상대=random.choice(묵찌빠)
        print(상대)
        승패 = 판정(너, 상대)
    elif 승패=='Lose':
        상황='Lose'
        print('상대의 주도권! ',상대,'에',상대,'에...',end='')
        너=input()
        상대=random.choice(묵찌빠)
        print(상대)
        승패 = 판정(너, 상대)

if 상황=='Win':
    print('축하합니다! 당신이 이겼습니다!')
else:
    print('분발하세요...')
