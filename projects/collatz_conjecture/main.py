import matplotlib.pyplot as plt

def n(num: int) -> list:
    _n = [num]
    while num > 1:
        if num % 2:
            # num is odd
            num = num * 3 + 1
        else:
            # num is even
            num = int(num/2)
        _n.append(num)
    return _n

if __name__ == "__main__":
    y = []
    p = plt
    for x in range(4,41,2):
        z = n(x)
        if max(z) > 1:
            y.append(z)
            p.plot(z)

    p.title("Collatz Conjecture", loc="center")
    p.ylabel('Step Value')
    p.xlabel('Step Count')
    p.show()