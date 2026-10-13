class Calculator:
    def power(self, n, p):
        if n < 0 or p < 0:
            raise ValueError("n and p should be non-negative")
        return n ** p


if __name__ == '__main__':
    t = int(input())
    calc = Calculator()

    for _ in range(t):
        n, p = map(int, input().split())
        try:
            print(calc.power(n, p))
        except ValueError as e:
            print(e)
