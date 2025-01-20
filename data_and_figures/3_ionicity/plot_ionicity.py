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
seps = [ 6.83, 9.25, 11.78, 14.62, 17.29]
ionicity = np.load('data/ionicity.npy', allow_pickle=True)
ionicity_err = np.load('data/ionicity_err.npy', allow_pickle=True)
ionicity_bulk = np.load('data/ionicity_bulk.npy', allow_pickle=True)
ionicity_bulk_err = np.load('data/ionicity_bulk_err.npy', allow_pickle=True)

ion_pairing_avg = np.load('data/ion_pairing_fracs.npy', allow_pickle=True)
ion_pairing_err = np.load('data/ion_pairing_fracs_err.npy', allow_pickle=True)
ion_pairing_bulk_avg = np.load('data/ion_pairing_fracs_bulk.npy', allow_pickle=True)
ion_pairing_bulk_err = np.load('data/ion_pairing_fracs_bulk_err.npy', allow_pickle=True)

ion_pair_l_avg = np.load('data/ion_pair_diffusion_length.npy', allow_pickle=True)
ion_pair_l_err = np.load('data/ion_pair_diffusion_length_err.npy', allow_pickle=True)
ion_pair_l_bulk_avg = np.load('data/ion_pair_diffusion_length_bulk.npy', allow_pickle=True)
ion_pair_l_bulk_err = np.load('data/ion_pair_diffusion_length_bulk_err.npy', allow_pickle=True)

# plot ionicity

plt.figure(figsize=(3.25,1.5))

color=darkblue
plt.errorbar(seps, ionicity, ionicity_err, marker='None', color=color, capsize=3, linestyle='None')
plt.plot(seps, ionicity, 'o-', color=color,markerfacecolor=matplotlib.colors.to_rgba(color,0.5),markeredgecolor=color,markeredgewidth=1)

plt.errorbar([19],[ionicity_bulk],yerr=[ionicity_bulk_err],capsize=2,markerfacecolor='None',marker='o',color=color)

plt.xlim(6.2,20)
x = np.arange(7,21,4)
new_labels = [str(label) if i != len(x)-1 else 'Bulk' for i, label in enumerate(x)]
plt.xticks(x, new_labels)
plt.ylim(0.4,0.9)

plt.grid(linestyle='--')
plt.xlabel('Slit height ($\AA$)')
plt.ylabel('Ionicity')
plt.savefig('ionicity.png',bbox_inches='tight',dpi=300)

# plot ion pairing behavior

fig = plt.figure()
ax1 = fig.gca()

color=darkblue
ax1.errorbar(seps,ion_pair_l_avg,yerr=ion_pair_l_err, marker='None', color=color, capsize=3, linestyle='None')
ax1.plot(seps,ion_pair_l_avg,'o-', color=color, markerfacecolor=matplotlib.colors.to_rgba(color,0.5),markeredgecolor=color,markeredgewidth=1,
         label='tau')

ax1.errorbar([19],[ion_pair_l_bulk_avg],yerr=ion_pair_l_bulk_err, marker='None', color=color, capsize=3, linestyle='None')
ax1.plot([19],[ion_pair_l_bulk_avg],'o', color=color, markerfacecolor='None')

# ax1.set_ylim(0,30)
ax1.set_xlabel(f'Slit height ($\AA$)')
ax1.set_ylabel('Ion pair diffusion length ($\AA$)')
ax1.grid(linestyle='--')

ax1.set_xlim(6.2,20)
x = np.arange(7,21,2)
new_labels = [str(label) if i != len(x)-1 else 'Bulk' for i, label in enumerate(x)]
ax1.set_xticks(x, new_labels)

ax2 = ax1.twinx()
ax2.errorbar(seps[:],ion_pairing_avg[:,0], yerr = ion_pairing_err[:,0], marker='None', color=lightblue, capsize=3, linestyle='None')
ax2.plot(seps,ion_pairing_avg[:,0],'s-',markersize=7, color=lightblue, markerfacecolor=matplotlib.colors.to_rgba(lightblue,0.7),
         label='Ion pair fraction',markeredgecolor=lightblue,markeredgewidth=1)

ax2.errorbar([19],[ion_pairing_bulk_avg[0]],yerr=[ion_pairing_bulk_err[0]], marker='None', color=lightblue, capsize=3, linestyle='None')
ax2.plot([19],[ion_pairing_bulk_avg[0]],'s', color=lightblue, markerfacecolor='None')

ax2.set_ylabel('Ion pair fraction')
ax2.set_ylim(0,0.2)
ax1.set_ylim(0.75,2.2)
ax2.set_yticks(ax2.get_yticks()[::2])

plt.tight_layout()
plt.subplots_adjust(wspace=0.3)
plt.savefig('ion_pairing.png', format='png', dpi=600, bbox_inches='tight')