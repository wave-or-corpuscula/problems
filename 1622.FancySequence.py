# https://leetcode.com/problems/fancy-sequence/description/?envType=daily-question&envId=2026-03-15


MOD = 10 ** 9 + 7

ADD_OP = "add"
MULT_OP = "mult"

class Fancy:

    def __init__(self):
        self._seq = []
        self._add = 0
        self._mul = 1
        
    def append(self, val: int) -> None:
        self._seq.append(self._inverse(val))

    def _inverse(self, x):
        return ((x - self._add) * pow(self._mul, MOD - 2, MOD)) % MOD
        
    def addAll(self, inc: int) -> None:
        self._add = (self._add + inc) % MOD
        
    def multAll(self, m: int) -> None:
        self._mul = (self._mul * m) % MOD
        self._add = (self._add * m) % MOD

    def getIndex(self, idx: int) -> int:
        if idx >= len(self._seq):
            return -1
        return (self._seq[idx] * self._mul + self._add) % MOD
        
        

        

if __name__ == "__main__":
    obj = Fancy()

    # Your Fancy object will be instantiated and called as such:
    val = 1
    inc = 10
    m = 4
    idx = 1
    obj = Fancy()
    obj.append(1)
    print(obj._seq)
    obj.append(2)
    print(obj._seq)
    obj.append(3)
    print(obj._seq)
    obj.addAll(inc)
    print(obj._seq)
    obj.multAll(m)
    print(obj._seq)
    param_4 = obj.getIndex(idx)
    print(param_4)