class Fsm:
    def __init__(self):
        self.bit1 = [0, 0]
        self.bit0 = [0, 0]
        self.out  = []

    def out_log(self):
        self.out.append(int(self.bit1[0] and not self.bit0[0]))

    def bit1_log(self,a):
        self.bit1[1]=a and self.bit0[0]

    def bit0_log(self,a):
        self.bit0[1]=not a or self.bit0[0] and not self.bit1[0]

    def loop(self, insequence):
        for bit in insequence:
            self.out_log()
            self.bit1_log(bit)
            self.bit0_log(bit)
            self.bit1[0] = self.bit1[1]
            self.bit0[0] = self.bit0[1]
        return self.out

a = Fsm()
import numpy as np

#sequence = [0,0,0,0,1,0,1,0,1,0,1,0,1,1,1,0,1,0,0,0,0]
sequence = np.random.randint(2,size=128).tolist()
b = a.loop(sequence)


for i in range(128):
    print(sequence[i],b[i])

"""
print('in:')
sequence = ''.join(map(str,sequence))
print(sequence)
b = ''.join(map(str,b))
print('out:')
print(b)
"""