import pandas as pd
import numpy as np

dataset = pd.read_csv('MachineLearning/watermelon_3.csv', delimiter=",")

print(dataset)

# process the dataset
dataset = np.array(dataset)
m, n = np.shape(dataset)

