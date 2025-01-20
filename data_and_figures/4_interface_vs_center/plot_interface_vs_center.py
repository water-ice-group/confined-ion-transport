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
diff = np.load('data/diffusion.npy', allow_pickle=True)
diff_avg = np.mean(diff,axis=-1)
diff_err = np.std(diff,axis=-1)

diff_center = np.load('data/diffusion_center.npy', allow_pickle=True)
diff_interface = np.load('data/diffusion_interface.npy', allow_pickle=True)
water_diff_interface = diff_interface[0]
cat_diff_interface = diff_interface[1]
an_diff_interface = diff_interface[2]
water_diff_center = diff_center[0]
cat_diff_center = diff_center[1]
an_diff_center = diff_center[2]
water_diff = diff_avg[0]
cat_diff = diff_avg[1]
an_diff = diff_avg[2]
water_diff_err = diff_err[0]
cat_diff_err = diff_err[1]
an_diff_err = diff_err[2]

[nao_coord_int, nao_coord_center] = np.load('data/nao_coord_int_vs_center.npy', allow_pickle=True)
[clh_coord_int, clh_coord_center] = np.load('data/clh_coord_int_vs_center.npy', allow_pickle=True)
[nao_coord_int_err, nao_coord_center_err] = np.load('data/nao_coord_int_vs_center_err.npy', allow_pickle=True)
[clh_coord_int_err, clh_coord_center_err] = np.load('data/clh_coord_int_vs_center_err.npy', allow_pickle=True)
nao_coord = np.load('data/nao_coord.npy', allow_pickle=True)
clh_coord = np.load('data/clh_coord.npy', allow_pickle=True)
nao_coord_avg = np.mean(nao_coord, axis=1)
nao_coord_err = np.std(nao_coord, axis=1)
clh_coord_avg = np.mean(clh_coord, axis=1)
clh_coord_err = np.std(clh_coord, axis=1)

nao_l_total = np.load('data/nao_diffusion_length.npy', allow_pickle=True)
clo_l_total = np.load('data/clo_diffusion_length.npy', allow_pickle=True)
nao_l_avg = np.mean(nao_l_total,axis=-1)[-1]
nao_l_err = np.std(nao_l_total,axis=-1)[-1]
clo_l_avg = np.mean(clo_l_total,axis=-1)[-1]
clo_l_err = np.std(clo_l_total,axis=-1)[-1]
nao_l_center = np.load('data/nao_l_center.npy', allow_pickle=True)
clo_l_center = np.load('data/clo_l_center.npy', allow_pickle=True)
nao_l_center_avg = np.mean(nao_l_center,axis=-1)
nao_l_center_err = np.std(nao_l_center,axis=-1)
clo_l_center_avg = np.mean(clo_l_center,axis=-1)
clo_l_center_err = np.std(clo_l_center,axis=-1)
nao_l_interface= np.load('data/nao_l_interface.npy', allow_pickle=True)
clo_l_interface = np.load('data/clo_l_interface.npy', allow_pickle=True)
nao_l_interface_avg = np.mean(nao_l_interface,axis=-1)
nao_l_interface_err = np.std(nao_l_interface,axis=-1)
clo_l_interface_avg = np.mean(clo_l_interface,axis=-1)
clo_l_interface_err = np.std(clo_l_interface,axis=-1)

# plot interfacial vs central diffusion
colors2 = ["#1d689a","#57b8ff","#09bc8a","#c2c6cc","#e87461",'k']
lightblue = "#57b8ff"
x_labels = ['Water', 'Na$^+$', 'Cl$^-$']
x = np.arange(len(x_labels))
y_interface = np.array([np.mean(water_diff_interface),np.mean(cat_diff_interface),np.mean(an_diff_interface)])*1e5
yerr_interface = np.array([np.std(water_diff_interface),np.std(cat_diff_interface),np.std(an_diff_interface)])*1e5
y_center = np.array([np.mean(water_diff_center),np.mean(cat_diff_center),np.mean(an_diff_center)])*1e5
yerr_center = np.array([np.std(water_diff_center),np.std(cat_diff_center),np.std(an_diff_center)])*1e5
y_total = np.array([water_diff[-1],cat_diff[-1],an_diff[-1]])*1e5
yerr_total = np.array([water_diff_err[-1],cat_diff_err[-1],an_diff_err[-1]])*1e5

bar_width = 0.2

fig, ax = plt.subplots(figsize=[4,2.5])
ax.bar(x-bar_width, y_interface, bar_width, yerr=yerr_interface, label='Interface', color=lightblue, capsize=2, zorder=3, edgecolor='k')
ax.bar(x, y_center, bar_width, yerr=yerr_center, label='Center', color=colors[0], capsize=2, zorder=3, edgecolor='k')
ax.bar(x+bar_width, y_total, bar_width, yerr=yerr_total, label='Total', color=colors2[3], capsize=2, zorder=3, edgecolor='k')

ax.set_xticks(x)
ax.set_xticklabels(x_labels)
ax.set_ylabel('Diffusion coefficient\n(10$^{-5}$ cm$^2$/s)')
ax.set_ylim(2,7)
ax.legend(frameon=True,framealpha=1, edgecolor='k', loc='upper right', bbox_to_anchor=(1, 0.97))
ax.grid(linestyle='--', zorder=0)
fig.savefig('bulk_vs_interface_diffusion_1729.png', format='png', dpi=300, bbox_inches='tight')

# plot interfacial vs central diffusion length
x_labels = ['Na-O', 'Cl-O']
x = np.arange(len(x_labels))
y_total = np.array([nao_l_avg, clo_l_avg])
yerr_total = np.array([nao_l_err, clo_l_err])
y_interface = np.array([nao_l_interface_avg, clo_l_interface_avg])
yerr_interface = np.array([nao_l_interface_err, clo_l_interface_err])
y_center = np.array([nao_l_center_avg, clo_l_center_avg])
yerr_center = np.array([nao_l_center_err , clo_l_center_err])

lightblue = "#57b8ff"
bar_width = 0.25

fig, ax = plt.subplots(figsize=[2,2])
ax.bar(x, y_center, bar_width, yerr=yerr_center, label='Center', color=colors[0], capsize=2, zorder=3, edgecolor='k')
ax.bar(x-bar_width, y_interface, bar_width, yerr=yerr_interface, label='Interface', color=lightblue, capsize=2, zorder=3, edgecolor='k')
ax.bar(x+bar_width, y_total, bar_width, yerr=yerr_total, label='Total', color="#c2c6cc", capsize=2, zorder=3, edgecolor='k')

ax.set_xticks(x)
ax.set_xticklabels(x_labels)
ax.set_ylabel('$\\mathcal{L}_{Ion-Water}$ ($\AA$)')
ax.set_ylim(0.5,2.3)
ax.grid(linestyle='--', zorder=0)
fig.tight_layout()
fig.savefig('bulk_vs_interface_diffusionLengths.png', format='png', dpi=300, bbox_inches='tight')

# plot interfacial vs central coordination
x_labels = ['Na-O', 'Cl-H']
x = np.arange(len(x_labels))
y_total = np.array([nao_coord_avg[-1], clh_coord_avg[-1]])
yerr_total = np.array([nao_coord_err[-1], clh_coord_err[-1]])
y_center = np.array([nao_coord_center[-1], clh_coord_center[-1]])
yerr_center = np.array([nao_coord_center_err[-1], clh_coord_center_err[-1]])
y_interface = np.array([nao_coord_int[-1], clh_coord_int[-1]])
yerr_interface = np.array([nao_coord_int_err[-1], clh_coord_int_err[-1]])

bar_width = 0.25

fig, ax = plt.subplots(figsize=[2,2])
ax.bar(x, y_center, bar_width, yerr=yerr_center, label='Center', color=colors[0], capsize=2, zorder=3, edgecolor='k')
ax.bar(x-bar_width, y_interface, bar_width, yerr=yerr_interface, label='Interface', color=lightblue, capsize=2, zorder=3, edgecolor='k')
ax.bar(x+bar_width, y_total, bar_width, yerr=yerr_total, label='Total', color="#c2c6cc", capsize=2, zorder=3, edgecolor='k')

ax.set_xticks(x)
ax.set_xticklabels(x_labels)
ax.set_ylabel('Coordination number')
ax.set_ylim(4.5,6.5)
ax.set_xlim(-0.55,1.55)
ax.grid(linestyle='--', zorder=0)
fig.tight_layout()
fig.savefig('bulk_vs_interface_coorindation_1729.png', format='png', dpi=300, bbox_inches='tight')