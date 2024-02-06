def main():
    S = int(input())

    if S % 2 == 0:
        ans = '1' * (S // 2)
        print(ans)
    else:
        ans = '7' + ('1' * ((S // 2) - 1))
        print(ans)

    print('1' * (S // 2) if S % 2 == 0 else '7' + ('1' * ((S // 2) - 1)))

if __name__ == '__main__':
    main()