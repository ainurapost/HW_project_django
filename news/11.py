# class Rate:
#     def __init__(self):
#         self.rating_sum = 0
#         self.users_count = 0
#
#     def set_rate(self, user, score):
#         self.rating_sum += score
#         self.users_count += 1
#
#     def get_rate(self):
#         print(self.rating_sum / self.users_count)
#
#
# if __name__ == '__main__':
#     r = Rate()
#     r.set_rate(1, 5)
#     r.get_rate()
#     r.set_rate(1, 7)
#     r.get_rate()
#     r.set_rate(1, 2)
#     r.get_rate()


# def func(x):
#     list = []
#     for i in x:
#         if i.isdigit():
#             list.append(i)
#
#     print(list)



# l1 = [[18,12,15,2],[13,14,15,3,15],[1,0]]
# words(l1) #много слов
# l2 = [[13,9,17],[16,17,9,2,5,19],[1,0]]
# words(l2) #привет мир


# element 'i' is searched
# index of the first 'i' is returned
# index = vowels.index('i')


# def words(mylist):
#     a = "абвгдеёжзийклмнопрcтуфхцчшщъыьэюя"
#     l= ''
#     order= mylist[-1]
#     # for k in order:
#     for i in mylist[-1]:
#         for j in mylist[i]:
#             l=l+a[j]
#         l+=' '
#     print(l)
#
#
# l2 = [[13,9,17],[16,17,9,2,5,19],[1,0]]
# l1 = [[18,12,15,2],[13,14,15,3,15],[1,0]]
# words(l2)
#
#








# def func(x):
#     list= []
#     for i in range(1, x):
#         list.append(str(i))
#     print(list)
#     print(''.join(list))
#
#
# func(6)


# s = sorted('Sorting1234')
s = sorted(input(''))

def f(s):
    l = []
    for i in s:
        if i.islower():
            l.append(i)
    for i in s:
        if i.isupper():
            l.append(i)
    for i in s:
        if i.isdigit():
            if int(i) % 2 > 0:
                l.append(i)
    for i in s:
        if i.isdigit():
            if int(i) % 2 == 0:
                l.append(i)
    print(''.join(l))


f(s)
