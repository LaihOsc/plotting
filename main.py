import numpy as np
import matplotlib.pyplot as plt

grades = np.array(['L', 'E', 'M', 'C', 'B', 'A', 'I'])
percent = np.array([5, 15, 20, 24, 20, 11, 5])

plt.bar(grades, percent)
plt.title('Grade Distribution')
plt.xlabel('Grade')
plt.ylabel('Percent')
plt.show()
