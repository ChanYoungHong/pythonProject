import sys

def main():
    N, L, W, H = map(int, sys.stdin.readline().split())
    start = 0
    end = 1000000000
    for _ in range(10000):
        mid = (start + end) / 2
        if (L // mid) * (W // mid) * (H // mid) < N:
            end = mid
        else:
            start = mid
    print(start)

if __name__ == "__main__":
    main()
