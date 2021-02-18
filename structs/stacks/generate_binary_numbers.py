from implementation import Queue

"""Implement a function find_bin(n) which will generate binary numbers from 11 till nn in the form of a string using a
 queue. The MyQueue() and MyStack() classes are provided in all of these challenges. An illustration is also provided 
 for your understanding."""


# Time complexity O(n^2)
def gen_bin(n):
    q = Queue()
    q.enqueue('1')
    result = []
    # O(n)
    for i in range(n):
        # O(n)
        ele = q.dequeue()
        print(i, ele)
        result.append(str(ele))
        str1 = result[i] + '0'
        str2 = result[i] + '1'

        q.enqueue(str1)
        q.enqueue(str2)

    return result


def main():
    result = gen_bin(1)
    print(result)

    result = gen_bin(3)
    print(result)

    # result = gen_bin(10)
    # print(result)
    #
    # result = gen_bin(50)
    # print(result)


main()
