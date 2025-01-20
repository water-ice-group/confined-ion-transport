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
densities = np.load('data/densities.npy', allow_pickle=True)

diff = np.load('data/diffusion.npy', allow_pickle=True)
diff_avg = np.mean(diff,axis=-1)
diff_err = np.std(diff,axis=-1)
diff_bulk = np.load('data/diffusion_bulk.npy', allow_pickle=True)
diff_avg_bulk = np.mean(diff_bulk,axis=-1)
diff_err_bulk = np.std(diff_bulk,axis=-1)

clo_l = np.load('data/clo_diffusion_length.npy', allow_pickle=True)
clo_l_avg = np.mean(clo_l,axis=-1)
clo_l_err = np.std(clo_l,axis=-1)
nao_l = np.load('data/nao_diffusion_length.npy', allow_pickle=True)
nao_l_avg = np.mean(nao_l,axis=-1)
nao_l_err = np.std(nao_l,axis=-1)
clo_l_bulk = np.load('data/clo_diffusion_length_bulk.npy', allow_pickle=True)
clo_l_bulk_avg = np.mean(clo_l_bulk,axis=-1)
clo_l_bulk_err = np.std(clo_l_bulk,axis=-1)
nao_l_bulk = np.load('data/nao_diffusion_length_bulk.npy', allow_pickle=True)
nao_l_bulk_avg = np.mean(nao_l_bulk,axis=-1)
nao_l_bulk_err = np.std(nao_l_bulk,axis=-1)

# plot diffusion coefficients and density vs H
diff_names = ['Water','Na','Cl']
markers = ['o','s','^']
diff_colors = [darkblue,purple,green]
fig, axs = plt.subplots(1, 1, figsize=(3.5, 3.25), sharey=False)

color=darkblue
x = seps
ax2 = axs.twinx()
y = 1/densities
lns2 = ax2.plot(x, y,'--',color=color, alpha=0.5,
        marker='d',markersize=7, label='1/$\mathit{\\rho}$')

dens_bulk = 1.0489361348525736
ax2.plot([19], 1/dens_bulk,color=color,alpha=0.5,marker='d',markersize=6)
ax2.set_ylabel('1/($\mathit{\\rho}$ (g/cm$^3$))')

for l in range(3):
    ax = axs
    y = diff_avg[l]*1e5
    yerr = diff_err[l]*1e5
    x = seps
    color=diff_colors[l]
    ax.errorbar(x,y, yerr = yerr, marker='None', color=color, capsize=3, linestyle='None')
    
    ax.errorbar([19],diff_avg_bulk[l]*1e5,yerr=diff_err_bulk[l]*1e5,capsize=2,markerfacecolor='None',marker=markers[l],color=diff_colors[l],markersize=6)
    
    ax.grid('both',linestyle='--')

    if l == 0:
        lns1 = ax.plot(x,y,color=color,
            marker=markers[l],markersize=7, label='$\mathit{D}$' +f'$_\mathrm{{{diff_names[l]}}}$',markeredgecolor=color,markeredgewidth=1)
        lns = lns1

    else:
        lns1 = ax.plot(x,y,color=color,
            marker=markers[l],markersize=7, label='$\mathit{D}$' + f'$_\mathrm{{{diff_names[l]}}}$',markerfacecolor=matplotlib.colors.to_rgba(color,0.5),markeredgecolor=color,markeredgewidth=1)
        lns+= lns1

ax.set_xlabel('Slit height ($\AA$)')
ax.set_ylabel('Diffusion coefficient (10$^{-5}$ cm$^2$/s)')

lns += lns2

labs = [l.get_label() for l in lns]
leg = ax.legend(lns, labs, frameon=True,framealpha=1)
leg.get_frame().set_edgecolor('k')

plt.xlim(6.2,20)
print(ax.get_xlim())
x = np.arange(7,21,2)
new_labels = [str(label) if i != len(x)-1 else 'Bulk' for i, label in enumerate(x)]
plt.xticks(x, new_labels)

plt.tight_layout()
ax.set_ylim(0,8.65)
ax2.set_ylim(0.7,1.1)
plt.savefig('diffusion_density.png', format='png', dpi=300, bbox_inches='tight')

# plot diffusion lengths
fig = plt.figure(figsize=(3,3.25))
ax1 = fig.gca()

color=purple
x = seps
y = nao_l_avg
yerr = nao_l_err
ax1.errorbar(x,y,yerr=yerr, marker='None', color=color, capsize=3, linestyle='None')
ax1.plot(x,y,'s-', color=color, markerfacecolor=matplotlib.colors.to_rgba(color,0.5),markeredgecolor=color,markeredgewidth=1)

ax1.plot([19],[nao_l_bulk_avg],'s', color=color, markerfacecolor='None')
ax1.errorbar([19],[nao_l_bulk_avg],yerr=nao_l_bulk_err, marker='None', color=color, capsize=3, linestyle='None')

color=green
y = clo_l_avg
yerr = clo_l_err
ax1.errorbar(x,y,yerr=yerr, marker='None', color=color, capsize=3, linestyle='None')
ax1.plot(x,y,'o-', color=color, markerfacecolor=matplotlib.colors.to_rgba(color,0.5),markeredgecolor=color,markeredgewidth=1)

ax1.plot([19],[clo_l_bulk_avg],'s', color=color, markerfacecolor='None')
ax1.errorbar([19],[clo_l_bulk_avg],yerr=clo_l_bulk_err, marker='None', color=color, capsize=3, linestyle='None')

ax1.set_xlim(6.2,20)
x = np.arange(7,21,2)
new_labels = [str(label) if i != len(x)-1 else 'Bulk' for i, label in enumerate(x)]
ax1.set_xticks(x, new_labels)

ax1.set_ylim(0.7,3.5)
ax1.set_xlabel(f'Slit height ($\AA$)')
ax1.set_ylabel('$\mathcal{L}_{Ion-Water}$ ($\AA$)')
ax1.grid(linestyle='--')

plt.tight_layout()
plt.savefig('solvation_diffusion_lengths.png', format='png', dpi=600, bbox_inches='tight')