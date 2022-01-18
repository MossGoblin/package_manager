class Vector():
    def __init__(self, pos_x, pos_y, neg_x=0, neg_y=0):
        self.pos = (pos_x, pos_y)
        self.neg = (neg_x, neg_y)
        self.abs = (self.pos[0] + self.neg[0], self.pos[1], self.neg[1])

    def __str__(self):
        return f'(pos {self.pos[0]}, {self.pos[1]} : neg {self.neg[0]}, {self.neg[1]})'

    def set_positive(self, x, y):
        self.pos = (x, y)

    def set_negative(self, x, y):
        self.neg = (x, y)


class Composite():
    def __init__(self, v: Vector = None):
        self.vectors = [v]
        self.pos = [v.pos]
        self.neg = [v.neg]
        self.abs = [v.abs]

    def __str__(self):
        self_string = 'VECTORS\n'
        for vector in self.vectors:
            self_string = self_string + f'\t{vector}\n'
        self_string = self_string + '\nPOS:\n\t'
        for pos in self.pos:
            self_string = self_string + f'{pos}, '
        self_string = self_string + '\nNEG:\n\t'
        for neg in self.neg:
            self_string = self_string + f'{neg}, '
        return self_string

    def add_vector(self, v: Vector):
        if v.abs in self.abs:
            raise Exception('The vector is already in the composite')
        if v.neg in self.neg:
            raise Exception('The composite already has that negative')
        self.vectors.append(v)
        if v.pos in self.neg:
            self.neg.remove(v.pos)
        self.pos.append(v.pos)
        if v.neg not in self.pos:
            self.neg.append(v.neg)
        self.abs.append(v.abs)
