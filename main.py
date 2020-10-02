import matplotlib.pyplot as plt


def trap_water(arr, n):
    water_blocks = [0] * n
    left = [0] * n
    right = [0] * n
    water = 0
    left[0] = arr[0]
    for i in range(1, n):
        left[i] = max(left[i - 1], arr[i])

    right[n - 1] = arr[n - 1]
    for i in range(n - 2, -1, -1):
        right[i] = max(right[i + 1], arr[i])

    for i in range(0, n):
        water += min(left[i], right[i]) - arr[i]
        water_blocks[i] = min(left[i], right[i]) - arr[i]

    fig = plt.figure(figsize=(10, 5))
    plt.title('Rain water trapping')
    plt.xlabel('Block')
    plt.ylabel('Height of Block')
    blocks = [i for i in range(0, n)]
    blocks_heights = arr
    positions = [i for i in range(0, n)]

    plt.bar(positions, water_blocks, width=1, color="blue", bottom=blocks_heights)
    plt.bar(positions, blocks_heights, width=1, color="black")
    plt.xticks(positions, blocks)
    plt.yticks(blocks_heights)
    plt.show()

    return water


if __name__ == '__main__':
    tc = int(input("Enter number of testcases:"))
    while tc:
        n = int(input("Enter number of blocks:"))
        arr = [int(i) for i in input().split()]
        for i in range(0, n):
            print(arr[i])
        print("Maximum units of water that can be accumulated is", trap_water(arr, n))
        tc -= 1
