def main():
    S = input()
    A = 'abcdefghijklmnopqrstuvwxyz'

    for i in range(len(S)):
        if S[i] != A[i]:
            print(A[i] + 'to' + S[i])

if __name__ == '__main__':
    main()