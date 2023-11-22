import matplotlib.pyplot as plt
fig, ax= plt.subplots()
Gause= [70, 143, 196, 316, 335, 423, 407, 373, 503, 446, 532, 491, 487, 426, 436, 297, 487, 755]
Actual= [2, 124, 257, 310, 313, 302, 364, 525, 458, 499, 284, 539, 590, 614, 714, 656, 670, 572]
ax.plot (Gause, Actual, color= "green", lw=3, ls="-.")
ax.set_title("Data Of Calories")
plt.show();
