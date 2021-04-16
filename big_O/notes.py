import time

nemo = ['nemo']


def find_Nemo(li):
    start = time.time()
    for i in range(len(li)):
        if li[i] == 'nemo':
            print('Found Nemo')
    end = time.time()
    print(end-start)


# find_Nemo(nemo)


def antoherFunction(input):
    a = 5  # O(1)
    b = 10  # O(1)
    c = 50  # O(1)
    for i in range(input):
        x = i + 1  # O(n)
        y = i + 2  # O(n)
        z = i + 3  # O(n)

    for j in range(input):
        p = j * 2  # O(n)
        q = j * 2  # O(n)

    whoIam = 'Don\'t know'  # O(1)

    # BigO(4 + 5n)=> O(n)


def logPairList(li):
    for i in range(len(li)):
        for j in range(len(li)):
            print(li[i], li[j])
    # O(n^2)


# logPairList([1, 2, 3, 4, 5, 6])


###### Space complexity #######
def booooo(n):
    for _ in range(len(n)):  # space complexity O(1)
        print('booo')


booooo([1, 2, 3, 4, 5])


def arrayOfHiNTimes(n):
    hi_array = []
    for i in range(len(n)):  # space complexity O(n)
        hi_array[i] = 'hi'
    return hi_array

# len(list) depends which language we are using, JS O(1) but assume
