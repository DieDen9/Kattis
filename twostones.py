

def main():
    n = int(input())

    def winner(n):
        if n %2 ==0:
            print("Bob")
        else:
            print("Alice")

    winner(n)

if __name__ == "__main__":
    main()

