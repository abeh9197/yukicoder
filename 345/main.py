
def main():
    S = input()
    C1 = 0
    W1 = 0
    W2 = 0
    chiwawa = []

    for i in range(len(S)):
        if S[i] == 'c':
            C1 = i
            for j in range(C1 + 1, len(S)):
                if S[j] == 'w':
                    W1 = j
                    for k in range(W1 + 1, len(S)):
                        if S[k] == 'w':
                            W2 = k
                            chiwawa.append(W2 - C1 + 1) 
                            break
    if len(chiwawa) <= 0:
        print(-1)
    else:
        print(min(chiwawa))


if __name__ == '__main__':
    main()


    