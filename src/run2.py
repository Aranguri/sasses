import mnist_loader
import network2
from task_gen import TaskGen
import numpy as np

training_data2, validation_data2, test_data2 = mnist_loader.load_data_wrapper()
task_gen = TaskGen()
training_data = task_gen.generate(1000)
validation_data = task_gen.generate(1000, False)
'''
print training_data2[0][1]
print training_data[0][1]

print validation_data2[0][1]
print validation_data[0][1]
'''
net = network2.Network([32, 30, 8])
net.SGD(training_data, 30, 10, 0.005, lmbda = 5.0,
evaluation_data=validation_data, monitor_evaluation_accuracy=True)
