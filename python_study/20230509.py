
# import matplotlib.pyplot as plt

# fig,axs = plt.subplots(1,3, figsize=(9,3)) #가로 : 9cm / 세로 : 3cm

# axs[1].set_xticks([0,2,4,6])
# axs[1].set_yticks([0,5,10])

# axs[2].set_xticklabels(['A','B','C','D','E'])
# axs[2].set_yticks([0,1,2])
# axs[2].set_yticklabels(['a','b','c'])

# plt.show()

# import matplotlib.pyplot as plt

# fig,axs = plt.subplots(1,3, figsize=(9,3)) #9cm / 3cm


# plt.show()


# 회귀분석(Gradient Descent)

import numpy as np
import matplotlib.pyplot as plt

np.random.seed(0)
# y=4X+6식을 근사(w1=4,w=0.6). random. 값은 noise를 위해 만듦.
X = 2*np.random.rand(100,1)
y = 6+4*X+np.random.randn(100,1)

#X,y 데이터 셋 scatter plot으로 시각화
plt.scatter(X,y)

plt.show()
