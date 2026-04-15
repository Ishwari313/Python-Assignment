# Write a Python program to calculate the euclidean distance between 
#two points before and after applying feature scaling and explain the diffrence in results

import numpy as np
from sklearn.preprocessing import StandarScalar

p1 = np.array([25,20000])
p2 = np.array([35,80000])

# distance before scaling
dist_before = np.linalg.norm(p1-p2)

# Apply scaling
scaler = StandarScalar()
scaled = scaler.fit_transform(np.array([p1,p2]))

dist_after = np.linalg.norm(scaled[0]-scaled[1])

print("Distance Before Scaling:",dist_before)
print("Distance After Scaling:",dist_after)

