# calculator.py

def absolute(val):
    if val<0:
        return val * (-1)
    else:
        return val

if __name__=='__main__':
    print(absolute(-1))
    