N = 5
x = 2
while N > 0:
    for i in range(2, x):

        if x%i==0:

            break

    else:
        print(x)
        N -= 1
    x += 1