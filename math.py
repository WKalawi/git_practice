import matplotlib.pyplot as plt

fig, (ax1,ax2)= plt.subplots(figsize=(10,4), ncols=2)
Gause= [70, 143, 196, 316, 335, 423, 407, 373, 503, 446, 532, 491, 487, 426, 436, 297, 487, 755]
Actual= [2, 124, 257, 310, 313, 302, 364, 525, 458, 499, 284, 539, 590, 614, 714, 656, 670, 572]
x=range(len(Gause))
ax1.bar(x, Gause, color="blue")
ax2.bar(x, Actual, color="green")
plt.show();