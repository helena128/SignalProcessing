class InputClass(object):
    def __init__(self, val=0):
        self._val = int(val) & 1023

    def __add__(self, val):
        if isinstance(val, Integer):
            return Integer(self._val + val._val)
        return self._val + val

    def __iadd__(self, val):
        self._val += val
        return self

    def __str__(self):
        return str(self._val)

    def __repr__(self):
        return 'Integer(%s)' % self._val

test = InputClass(5);
print(test);

test1 = InputClass(1025);
print(test1);
