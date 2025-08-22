import random


print('시작 번호와 끝 번호를 입력 하시면 랜덤한 숫자가 주어집니다!')
try:
    while True:
        start = int(input('시작 숫자를 입력:'))
        end = int(input('끝 숫자를 입력:'))
        if start > end :
            print('시작 숫자는 끝 숫자보다 클 수 없습니다:')
            continue
        else:
            break
except:
    print('숫자를 정확히 입력하세요.')

randnum = random.randint(start, end)

print(randnum)

a=0

while True:
    num = int(input('정답을 입력:'))
    a+=1
    if randnum == num :
        print(f'🎉{a}번 시도 하였습니다! 정답은 {num}입니다. 축하합니다!🎉')
        break
    else:
        if num > randnum:
            print(f'정답은 {num}보다 작습니다.')
            continue
        else:
            print(f'정답은 {num}보다 큽니다.')
            continue
