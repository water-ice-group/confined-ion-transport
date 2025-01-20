import matplotlib
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np

# plot settings
matplotlib.rcParams.update(matplotlib.rcParamsDefault)
smallsize = 10
largesize = 10
plt.rcParams.update({'font.size': largesize})
plt.rc('xtick', labelsize = smallsize, direction='in')
plt.rc('ytick', labelsize= smallsize, direction='in')
plt.rc('axes', labelsize = largesize)
plt.rc('axes', titlesize = largesize, linewidth=0.7)
plt.rc('legend', fontsize=largesize)
plt.rc('lines', markersize=8, linewidth=2)
plt.rc('legend', frameon=True,framealpha=1,)
plt.rcParams['figure.figsize'] = [3.25,3.25]
plt.rc('text', usetex=False)
plt.rcParams['text.latex.preamble']=[r"\usepackage{amsmath}"]
matplotlib.rcParams['mathtext.default'] = 'regular'
purple = '#9234eb'
green = '#3cb54a'
darkblue = '#003f5c'
lightblue = "#57b8ff"
colors = plt.get_cmap('Dark2')(range(6))

# load data
lij = np.load('data/lij.npy', allow_pickle=True)
lij_plotting = np.array([lij[0], lij[1], lij[4], lij[2] - lij[0], lij[3] - lij[1], lij[2] + lij[3] - 2*lij[4]])
lij_avg = np.mean(lij_plotting,axis=-1)
lij_err = np.std(lij_plotting,axis=-1)

lij_bulk = np.load('data/lij_bulk.npy', allow_pickle=True)
lij_plotting_bulk = np.array([lij_bulk[0], lij_bulk[1], lij_bulk[4], lij_bulk[2] - lij_bulk[0], lij_bulk[3] - lij_bulk[1], lij_bulk[2] + lij_bulk[3] - 2*lij_bulk[4]])
lij_avg_bulk = np.mean(lij_plotting_bulk,axis=-1)
lij_err_bulk = np.std(lij_plotting_bulk,axis=-1)

seps = [ 6.83, 9.25, 11.78, 14.62, 17.29]

# plot data
fig, axes = plt.subplots(1,3, figsize=(7,3.25),sharey=True,sharex=True)
labels=['$L^{++}_\mathrm{self}$', '$L^{--}_\mathrm{self}$', '$L^{+-}$', '$L^{++}_\mathrm{distinct}$', '$L^{--}_\mathrm{distinct}$', '$\kappa$']
markers = ['o','s','o','s','d','o']

lij_colors = [colors[2], colors[4], colors[3], colors[1], colors[0], darkblue]

# plot conductivity
plotting_indices = [5]
ax = axes[0]
for i in plotting_indices:
    ax.errorbar(seps, lij_avg[i], yerr=lij_err[i], marker='None', color=lij_colors[i], capsize=3, linestyle='None')
    ax.plot(seps, lij_avg[i],marker=markers[i], label=labels[i], color=lij_colors[i],markerfacecolor=matplotlib.colors.to_rgba(lij_colors[i],0.5), markersize=7, 
            markeredgecolor=lij_colors[i])
    ax.errorbar([19],lij_avg_bulk[i],yerr=lij_err_bulk[i],capsize=2,markerfacecolor='None',marker=markers[i],color=lij_colors[i],markersize=6)
    ax.set_ylabel('Transport coefficient (mS/cm)')

# plot self terms
plotting_indices = [0,1]
ax = axes[1]
for i in plotting_indices:
    ax.errorbar(seps, lij_avg[i], yerr=lij_err[i], marker='None', color=lij_colors[i], capsize=3, linestyle='None')
    ax.plot(seps, lij_avg[i],marker=markers[i], label=labels[i], color=lij_colors[i],markerfacecolor=matplotlib.colors.to_rgba(lij_colors[i],0.5), markersize=7, 
            markeredgecolor=lij_colors[i])
    ax.errorbar([19],lij_avg_bulk[i],yerr=lij_err_bulk[i],capsize=2,markerfacecolor='None',marker=markers[i],color=lij_colors[i],markersize=6)    # ax.grid('both')

# plot non-ideal terms
plotting_indices = [2,3,4]
ax = axes[2]
for i in plotting_indices:
    ax.errorbar(seps, lij_avg[i], yerr=lij_err[i], marker='None', color=lij_colors[i], capsize=3, linestyle='None')
    ax.plot(seps, lij_avg[i],marker=markers[i], label=labels[i], color=lij_colors[i],markerfacecolor=matplotlib.colors.to_rgba(lij_colors[i],0.5), markersize=7, 
            markeredgecolor=lij_colors[i])

    ax.errorbar([19],lij_avg_bulk[i],yerr=lij_err_bulk[i],capsize=2,markerfacecolor='None',marker=markers[i],color=lij_colors[i],markersize=6)

for ax in axes:
    ax.yaxis.set_minor_locator(ticker.MultipleLocator(25))  
    ax.grid(True, which='both', axis='y',linestyle='--')
    ax.grid(True, which='major', axis='x',linestyle='--')
    ax.set_xlabel('Slit height ($\AA$)')

plt.xlim(5.5,20)
print(ax.get_xlim())
x = np.arange(7,21,2)
new_labels = [str(label) if i != len(x)-1 else 'Bulk' for i, label in enumerate(x)]
plt.xticks(x, new_labels)

plt.ylim(-30,230)

plt.tight_layout()
plt.savefig('transport_coefficients.png',bbox_inches='tight',dpi=600)