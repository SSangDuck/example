n1, n2 , n3 = input().split()

for i in range(1, n+1) :
    if i%10==3 :
        print("X", end=' ')
    else :
        if i%10==6 :
            print("X", end=' ')
        else :
            if i%10==9 :
                print("X", end=' ')
            else :
                print(i, end=' ')
