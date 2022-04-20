import re


class Compare:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def diff(self):
        a = re.sub(r"[\W\d_]", "", self.a.upper())
        b = re.sub(r"[\W\d_]", "", self.b.upper())
        la = len(a)
        lb = fb = len(b)
        for x in b:
            if x in a:
                i = a.index(x)
                a = a[:i] + a[i+1:]
                fb -= 1
        da = (la - len(a)) / la * 50
        db = (lb - fb) / lb * 50
        return 100 - (da + db)
