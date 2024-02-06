def main() -> None:
    num_test_cases = int(input())
    for _ in range(num_test_cases):
        n = int(input())
        s = "ABACBC" + "ABC" * (n - 2)
        print(s)


if __name__ == "__main__":
    main()
