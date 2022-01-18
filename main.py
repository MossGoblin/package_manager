from toolbox.tools import *
from toolbox.objects import Unit, Composite

def main():
    a = Unit(1, 1, 1, 0)
    b = Unit(1, 1, 0, 1)
    ab = a *add* b
    print(ab)
    # c = Composite(a)
    # c.add_vector(b)
    c = a *cmb* b
    print(c)
    pass




if __name__ == "__main__":
    main()
