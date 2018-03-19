import random
import numpy as np

full_data = range(10000)

sample_data = np.random.choice(full_data, size=1000, replace=False).tolist()

def bootstrapping(sample_data, n):
    bs_var = []
    for i in range(n):
        sample = [random.choice(sample_data) for _ in sample_data]
        bs_var.append(np.var(sample))
    return(np.mean(bs_var))

def jackknife(sample_data):
    n = len(sample_data)
    jk_var = []
    for i in range(n):
        sample = sample_data[:i] + sample_data[(i+1):]
        jk_var.append(np.var(sample))
    return(np.mean(jk_var))

true_var = np.var(full_data)
sample_bs_var = np.var(sample_data) - (bootstrapping(sample_data, 1000) - np.var(sample_data))
sample_jk_var = np.var(sample_data) - (1000 - 1) * (jackknife(sample_data) - np.var(sample_data))
print(true_var)
print(np.var(sample_data))
print(sample_bs_var)
print(sample_jk_var)
