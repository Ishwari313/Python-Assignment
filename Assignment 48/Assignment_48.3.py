# Write  python progrm using standardScalar to perform featue scaling on the follwing dataset

#[[25,20000]
 #[30,40000]
 #[35,80000]]
# print the scaled dataset

from sklearn.preprocessing import StandardScaler
import numpy as np

dataset = np.array([[25, 20000],
                    [30, 40000],
                    [35, 80000]])

scaler = StandardScaler()
scaled_data = scaler.fit_transform(dataset)

print("Scaled Dataset:\n", scaled_data)