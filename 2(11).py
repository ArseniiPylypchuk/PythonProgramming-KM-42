# ВАШ КОД ТУТ
def rrange(begin ,end , step):
    if step==0:
        return []
    elif begin >= end and step>0:
        return []
    elif begin<=end and step<0:
        return []
    else:
        return [begin]+ rrange(begin+step, end, step)


# ПЕРЕВІРКА

x = rrange(1, 10, 1)
y = rrange(10, 1, -1)
z = rrange(10, 1, 1)
#print(x, y, z)

assert x == list(range(1, 10)), 'Failed test for simple range'
assert y == list(range(10, 1, -1)), 'Failed test for reverse range'
assert z == list(range(10, 1, 1)), 'Failed test for empty range'
print('All tests good!')