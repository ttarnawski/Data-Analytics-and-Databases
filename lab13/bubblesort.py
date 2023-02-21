from copy import deepcopy


def bubblesort(l: list = None) -> list:
    if l is None:
        l = []
        return l
    else:
        if isinstance(l, list):
            for item in l:
                if isinstance(item, (int, float)):
                    continue
                else:
                    raise TypeError('Invalid value type')
            
            l = deepcopy(l)
            n = len(l)
            while n > 1:
                for i in range(1, n):
                    if l[i - 1] > l[i]:
                        l[i - 1], l[i] = l[i], l[i - 1]
                n = n - 1
            return l
        else:
            raise TypeError('Invalid value type')