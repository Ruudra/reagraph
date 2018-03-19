import matplotlib.pyplot as plt
import numpy as np

x, y = np.loadtxt('insert_text_file_here.txt', delimiter=',', unpack=True)
plt.scatter(x,y,  label='insert_label_here', s=500, marker="x")


plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.title('insert_title_here')
plt.savefig("value{y}.png".format(y=y))
plt.show()
