import numpy as np
import random
import bitarray

class TaskGen:
    def __init__(self):
        self.names = ['anad', 'paul', 'carl', 'erne', 'gilb', 'juan', 'sant', 'roma']

    def generate(self, amount, training_data=True):
        return [self.generate_task(training_data) for _ in range(amount)]

    def generate_task(self, training_data):
        i = random.randint(0, len(self.names) - 1)
        name = self.names[i]
        if training_data:
            i = np.eye(len(self.names))[i]
            i = np.array([[item] for item in i])
        return (self.str_to_bits(name), i)

    def str_to_bits(self, string):
        bits = bitarray.bitarray()
        bits.frombytes(string.encode('utf-8'))
        return np.array([[1] if bit else [0] for bit in bits.tolist()])

    def generate_task_test(self):
        print (self.generate_task(False))

    def str_to_bits_test(self):
        print(self.str_to_bits('abcd'))
