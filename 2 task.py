from time import *
# 1 point
def words(list1):
    spisok=['Python', 'php', 'go', 'C']
    return print([i for i in list1.split() if i not in spisok])


words('Python fgfr  gfgf jhjh go C fggg')
# 2 point


def numbers(num):
    lit = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(list(filter(lambda x: x % num == 0, lit)))


numbers(2)
# 3 point


def cartege(*args):
    print(tuple(filter(lambda x: type(x) is str, args)))


cartege(3, 'gfgf', 5.0, True, 'fla', 'gro')


# 4 point


def deriv(list1, list2):
    print(list(filter(lambda x: x in list2, list1)))


deriv([3, 'gfgf', 5.0], ['fla', 'gro', 3, 'gfgf'])
# 5 point


def count_steps(num):
    for i in range(1, 15):
        if num < (1+i)*i/2:
            print(i - 1)
            break


count_steps(100)


# 6 point
def type_date(num):
    def relise(x, y, z):
        res = num(x, y, z)
        if type(res) is not int:
            raise Exception('Данный тип данных не целое число')
        else:
            return f'Результат вычислений: {res}'
    return relise


@type_date
def polinom(x, y, z):
    return x*z + y


print(polinom(1, 2, 3))


@type_date
def summator(x, y, z):
    return x**2 + y**4 + z**6


print(summator(1, 2, 3))


# 7 point
def try_2(num):
    for _ in range(0, 2):
        def func(x1):
            res = num(x1)
            if type(res) is not int:
                raise Exception('Данный тип данных не целое число')
            else:
                return f'Результат вычислений: {res}'
        return func


@try_2
def check1(x1):
    return x1**4 + x1**3 + x1**2 + x1 + 1


print(check1(1))


@try_2
def step(x):
    return x**2 + x**4 + x**6


#print(step(1))


# 8 point
elements = [(2, 12, "Mg"), (1, 11, "Na"), (1, 3, "Li"), (2, 4, "Be")]


def sort(list1):
    final_list =[]
    for i in range(1, 200):
        for j in list1:
            if j[1] == i:
                final_list.append(j)
    return final_list


print(sort(elements))


# 9 point


def time_programm(num):
    time_start = time()

    def func(list2):
        res = num(list2)
        return f'Результат вычислений получен за {time()-time_start} с'
    return func


@time_programm
def check1(list2):
     ae = list2*2000
     return [i*17/2 for i in ae]


print(check1([1.5, 0.1, 0.5, 0.6]))


@time_programm
def check2(x):
    '---'.join([j*1000000 for j in [i for i in x.split()]])

print(check2('Много Много Много слов слов для для времени времени расчета'))