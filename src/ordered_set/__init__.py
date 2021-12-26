
def set_and(self, other):
    _common = []
    for _item in self:
        if (_item in other):
            _common.append(_item)
    
    return type(self)(dict.fromkeys(
        _common
    ).keys())

def set_or(self, other):
    print ("YES")
    return type(self)(dict.fromkeys(
        (
            *self,
            *other,
        )
    ).keys())

def set_xor(self, other):
    _xors = []
    for _item in (*self, *other):
        if ((_item in self) ^ \
            (_item in other)):
            _xors.append(_item)

    return type(self)(dict.fromkeys(
        _xors
    ).keys())


class OrderedSet(tuple):
    __and__ = set_and
    __or__ = set_or
    __xor__ = set_xor

    def __repr__(self):
        return f"{type(self).__name__}({super().__repr__()})"

if __name__=="__main__":
    a = OrderedSet((2,1,3,5,4,5,9))
    b = OrderedSet((2,1,3,1,1,1,6,7,8,9))
    print (a ^ b)