from toolbox.tools import *
from toolbox.vectors import Vector, Composite

def main():
    a = Vector(1, 1, 0, 0)
    b = Vector(1, 1, 1, 1)
    ab = a *add* b
    print(ab)
    c = Composite(a)
    c.add_vector(b)
    print(c)
    pass




if __name__ == "__main__":
    main()
