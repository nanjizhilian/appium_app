import time
from tqdm import tqdm

# for i in tqdm(range(100)):
#     time.sleep(0.1)
#     pass

def test(number):
    ret = 4
    for i in range(ret):
        print(i)
        sum = number * i - 1
        if i == 0:
            break
    print(sum)


if __name__ == "__main__":
    test(5)


    # for i in tqdm(range(100)):
    #     time.sleep(0.1)
    #     pass


