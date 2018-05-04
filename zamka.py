

def main():
    L = int(input())
    D = int(input())
    X = int(input())

    def calc_digits(num):
        result = 0
        for i in range(0,len(str(num))):
            result +=  int(str(num)[i])
        return result


    def winner(L,D,X):
        N = []
        for n in range(L,D+1):

            if calc_digits(n) == X:
                N.append(n)
        print(min(N))
        print(max(N))

    winner(L,D,X)


if __name__ == "__main__":
    main()

