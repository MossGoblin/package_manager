from infix import mul_infix
from objects import Unit, Composite

# OPERATIRS

@mul_infix
def add(a: Unit, b:Unit):
    res_pos_x = a.pos[0] + b.pos[0]
    res_pos_y = a.pos[1] + b.pos[1]
    res_neg_x = a.neg[0] + b.neg[0]
    res_neg_y = a.neg[1] + b.neg[1]
    res = Unit(res_pos_x, res_pos_y, res_neg_x, res_neg_y)
    return res

@mul_infix
def cmb(a: Unit, b:Unit):
    res = Composite(a)
    res.add_vector(b)
    return res
