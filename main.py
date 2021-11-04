print("오징어 게임에 오신 것을 환영합니다.")
print("이번 게임은 다리 건너기입니다.")
print("왼쪽 혹은 왼쪽 중에 선택하세요")

import random
br = random.randint(1, 2)
a = 0
dir = ["", "왼쪽", "오른쪽"]
print("1번은 왼쪽 2번은 오른쪽")

while a < 10 :
    while 1 :
        choice = int(input("1.왼쪽 2.오른쪽 : "))
        if choice == 1 or choice == 2 :
            break
        else :
            print("1과 2 중에 입력하세요!")
            continue
    print("{}으로 점프".format(dir[choice]))
    if choice == br :
        print("같은 방향을 선택했습니다.")
        print("생존입니다.")
        a += 1
    else :
        print("강화유리는 {}입니다.".format(dir[br]))
        print("으아아아악~")
        break

