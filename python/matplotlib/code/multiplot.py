# # import matplotlib.pyplot as plt
# # plt.figure(1)                # the first figure
# # plt.subplot(211)             # the first subplot in the first figure
# # plt.plot([1, 2, 3])
# # plt.subplot(212)             # the second subplot in the first figure
# # plt.plot([4, 5, 6])
# #
# #
# # plt.figure(2)                # a second figure
# # plt.plot([4, 5, 6])          # creates a subplot(111) by default
# #
# # plt.figure(1)                # figure 1 current; subplot(212) still current
# # plt.subplot(211)             # make subplot(211) in figure1 current
# # plt.title('Easy as 1, 2, 3') # subplot 211 title
# # plt.show()
#
# import numpy as np
# import matplotlib.pyplot as plt
# from matplotlib import style
#
# style.use('ggplot')
# # Fixing random state for reproducibility
# np.random.seed(19680801)
#
# mu, sigma = 100, 15
# x = mu + sigma * np.random.randn(10000)
#
# # the histogram of the data
# n, bins, patches = plt.hist(x, 50, normed=1, facecolor='g', alpha=0.75)
#
#
# plt.xlabel('$\sigma_i=15$')
# plt.ylabel('Probability')
# plt.title('Histogram of IQ')
# plt.text(60, .025, r'$\mu=100,\ \sigma=15$')
# plt.axis([40, 160, 0, 0.03])
# # plt.grid(True)
# plt.show()
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
from collections import namedtuple


n_groups = 5

means_men = (20, 35, 30, 35, 27)
std_men = (2, 3, 4, 1, 2)

means_women = (25, 32, 34, 20, 25)
std_women = (3, 5, 2, 3, 3)

fig, ax = plt.subplots()

index = np.arange(n_groups)
bar_width = 0.35

opacity = 0.4
error_config = {'ecolor': '0.3'}

rects1 = ax.bar(index, means_men, bar_width,
                alpha=opacity, color='b',
                yerr=std_men, error_kw=error_config,
                label='Men')

rects2 = ax.bar(index + bar_width, means_women, bar_width,
                alpha=opacity, color='r',
                yerr=std_women, error_kw=error_config,
                label='Women')

ax.set_xlabel('Group')
ax.set_ylabel('Scores')
ax.set_title('Scores by group and gender')
ax.set_xticks(index + bar_width / 2)
ax.set_xticklabels(('A', 'B', 'C', 'D', 'E'))
ax.legend()

fig.tight_layout()
plt.show()
