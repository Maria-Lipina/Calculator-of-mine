from random import randint


test = {
    1: 'q',
    2: 'w',
    3: 'e',
    4: 'r',
    5: 't'
}

rec = list(test.keys())
print(rec)
del test[rec[0]]
record = {(rec[-1]+1): 'y'}
test = test | record
print(test)

for i in range(10):
    rec = list(test.keys())
    del test[rec[0]]
    record = {(rec[-1]+1): randint(0, 100)}
    test = test | record
    print(test)
    print('---------')