a = [4.7, 3.2, 1.3, 0.2, 'setosa']
b = [7.0, 3.2, 4.7, 1.4, 'versicolor']
c = [7.6, 3.0, 6.6, 2.1, 'virginica']

a.insert(0, b.pop())
b.append(a.pop())
del c[4]

print(f'a = {a}')
# a = ['versicolor', 4.7, 3.2, 1.3, 0.2]

print(f'b = {b}')
# b = [7.0, 3.2, 4.7, 1.4, 'setosa']

print(f'c = {c}')
# c = [7.6, 3.0, 6.6, 2.1]