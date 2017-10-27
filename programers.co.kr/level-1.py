def gcdlcm(a, b):
    def gcd(a, b):
        if b == 0:
            return a
        return gcd(b, a % b)

    def lcm(a, b, gcd_ab=None):
        gcd_ab = gcd_ab if gcd_ab is not None else gcd(a, b)

        return int(a * b / gcd_ab)

    gcd_ab = gcd(a, b)
    lcm_ab = lcm(a, b, gcd_ab)
    answer = [gcd_ab, lcm_ab]

    return answer


print(gcdlcm(3, 12))

#########################


def rm_small(mylist):
    if len(mylist) <= 1:
        return []
    m = min(mylist)

    return [x for x in mylist if x != m]
    # return list(filter(lambda x: x != m, mylist))


# 아래는 테스트로 출력해 보기 위한 코드입니다.
my_list = [4, 3, 2, 1]
print("결과 {} ".format(rm_small(my_list)))

#########################


def sumMatrix(A, B):
    answer = []

    # Using map
    # for row_a, row_b in zip(A, B):
    #     row = list(map(lambda x: x[0]+x[1], zip(row_a, row_b)))
    #    answer.append(row)

    # 7. Use List Comprehensions Instead of map and filter
    # But, Two Expressions in List Comprehesions
    # answer = [[a + b for a, b in zip(row_a, row_b)]
    #           for row_a, row_b in zip(A, B)]


    # 8. Avoid More Than Two Expressions in List Comprehensions
    for row_a, row_b in zip(A, B):
        row = [a+b for a, b in zip(row_a, row_b)]
        answer.append(row)

    return answer


# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(sumMatrix([[1, 2], [2, 3]], [[3, 4], [5, 6]]))


#########################


def sum_digit(number):
    '''number의 각 자릿수를 더해서 return하세요'''
    return sum([int(n) for n in str(number)])

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print("결과 : {}".format(sum_digit(123)));


#########################


def sumDivisor(num):
    answer = num

    divisor = 1
    while num//2 >= divisor:
        if num%divisor == 0:
            answer += divisor
        divisor += 1

    # return num + sum([x for x in range(1, num//2 + 1) if num%x == 0])

    return answer


print(sumDivisor(12))


#########################


def string_middle(str):
    l = len(str)
    # if l%2 == 0:
    #     # return str[l//2-1 : l//2+1]
    #     return str[l//2 - 1] + str[l//2]
    # else:
    #     return str[l//2]

    return str[l // 2] if l % 2 != 0 else str[l // 2 - 1] + str[l // 2]
    # return str[(len(str)-1)//2:len(str)//2+1]


print(string_middle("poa"))


#########################


def printTriangle(num):
    s = ['*'*i for i in range(1, num+1)]
    s = '\n'.join(s) + '\n'

    return s
    # return '\n'.join(['*'*i for i in range(1, num+1)]) + '\n'


print(printTriangle(3))


#########################


import re


def no_continuous(s):
    regex = r"(\d)\1{0,}"

    return re.findall(regex, s)

    # return [s[0]] + [s[i] for i in range(1, len(s)) if s[i] != s[i-1:i]]
    # return [s[i] for i in range(len(s)) if s[i] != s[i-1:i]]


# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(no_continuous("1133303"))


#########################


# https://www.andreagrandi.it/2015/08/31/understanding-python-decorators-optimizing-a-recursive-fibonacci-implementation/

import timeit


def deco(func):
    cache = {}

    def decorated_func(*args):
        if args in cache:
            return cache[args]
        else:
            cache[args] = func(*args)
            return cache[args]

    return decorated_func

@deco
def fibonacci(num):
    if num == 0 or num == 1:
        return num

    return fibonacci(num - 1) + fibonacci(num - 2)


# 아래는 테스트로 출력해 보기 위한 코드입니다.
t1 = timeit.Timer("fibonacci(40)", "from __main__ import fibonacci")
print(t1.timeit(1))
# print(fibonacci(40))


#########################


def evenOrOdd(num):
    s = "Even" if num % 2 == 0 else "Odd"
    # num % 2 and "Odd" or "Even"

    return s


# 아래는 테스트로 출력해 보기 위한 코드입니다.
print("결과 : " + evenOrOdd(3))
print("결과 : " + evenOrOdd(2))


