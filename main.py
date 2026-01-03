# main.py
import heapq


def min_total_cost(cables):
    # копія
    cables = cables[:]

    if len(cables) < 2:
        return 0

    heapq.heapify(cables)  # мін-купа
    total = 0

    while len(cables) > 1:
        a = heapq.heappop(cables)
        b = heapq.heappop(cables)
        s = a + b
        total += s
        heapq.heappush(cables, s)

    return total

def main():
    cables = [4, 3, 2, 6]
    print("Мінімальні витрати:", min_total_cost(cables)) # 29


if __name__ == "__main__":
    main()