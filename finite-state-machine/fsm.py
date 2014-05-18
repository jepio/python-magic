import numpy as np


class Fsm(object):
    """
    A base class for all FSM.
    """
    def __init__(self):
        self.out = []


class MyMachine(Fsm):
    """
    A machine that searches for the sequence '011' and when it finds one it
    outputs '1' else '0'.
    """

    def __init__(self):
        self.bit1 = [0, 0]
        self.bit0 = [0, 0]
        super(MyMachine, self).__init__()

    def out_log(self):
        self.out.append(int(self.bit1[0] and not self.bit0[0]))

    def bit1_log(self, a):
        self.bit1[1] = a and self.bit0[0]

    def bit0_log(self, a):
        self.bit0[1] = not a or self.bit0[0] and not self.bit1[0]

    def shift(self):
        self.bit1[0] = self.bit1[1]
        self.bit0[0] = self.bit0[1]

    def run(self, insequence):
        for bit in insequence:
            self.out_log()
            self.bit1_log(bit)
            self.bit0_log(bit)
            self.shift()
        return self.out


if __name__ == "__main__":
    machine = MyMachine()
    input = np.random.randint(2, size=128).tolist()
    output = machine.run(input)
    input = ''.join(map(str, input))
    output = ''.join(map(str, output))
    print('In:')
    print(input)
    print('Out:')
    print(output)
