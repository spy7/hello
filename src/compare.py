import re


class Compare:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def diff(self):
        a = re.sub(r"[\W\d_]", "", self.a.upper())
        b = re.sub(r"[\W\d_]", "", self.b.upper())
        fb = len(b)
        for x in b:
            if x in a:
                i = a.index(x)
                a = a[:i] + a[i+1:]
                fb -= 1
        da = (len(self.a) - len(a)) / len(self.a) * 50
        db = (len(self.b) - fb) / len(self.b) * 50
        return da + db
