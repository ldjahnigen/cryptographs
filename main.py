import pandas as pd
import matplotlib.pyplot as plt
import mplfinance as mpf

btcdataset_path = "/home/louisj/Programs/cryptograph/btcdata.csv"
ethdataset_path = "/home/louisj/Programs/cryptograph/ethdata.csv"
btcmdataset_path = "/home/louisj/Programs/cryptograph/btcmdata.csv"
ethmdataset_path = "/home/louisj/Programs/cryptograph/ethmdata.csv"
update_interval = 60

btcdata = pd.read_csv(btcdataset_path, index_col=0, parse_dates=True)
ethdata = pd.read_csv(ethdataset_path, index_col=0, parse_dates=True)
btcmdata = pd.read_csv(btcmdataset_path, index_col=0, parse_dates=True)
ethmdata = pd.read_csv(ethmdataset_path, index_col=0, parse_dates=True)
colors = mpf.make_marketcolors(
    up='g',
    down='r',
    inherit=True
)

style = mpf.make_mpf_style(base_mpl_style="seaborn-darkgrid",
    marketcolors=colors,
    rc={
    "axes.facecolor": "#131722",
    "figure.facecolor": "#131722",
    "grid.color": "#8699a4",
    "xtick.color": "#8699a4",
    "ytick.color": "#8699a4",
    "axes.labelcolor": "#8699a4",
    "axes.edgecolor": "#8699a4",
    "axes.grid": True,
    "axes.spines.top": False,
    "axes.spines.right": False,
    "axes.spines.bottom": True,
    "axes.spines.left": True,
    "grid.linewidth": 0.5,
    "xtick.bottom": True,
    "xtick.direction": "in",
    "xtick.top": False,
    "ytick.direction": "in",
    "ytick.left": True,
    "ytick.right": False,
    })


fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(12,8))

plt.subplots_adjust(top=0.97)

mpf.plot(btcdata, type='candle', style=style, ax=axes[0,0], volume=False)
mpf.plot(ethdata, type='candle', style=style, ax=axes[0,1], volume=False)
mpf.plot(btcmdata, type='line', style=style, ax=axes[1,0], volume=False)
mpf.plot(ethmdata, type='line', style=style, ax=axes[1,1], volume=False)

axes[0, 0].set_title('Bitcoin Price')
axes[0, 1].set_title('Ethereum Price')
axes[1, 0].set_title('Bitcoin Market Cap')
axes[1, 1].set_title('Ethereum Market Cap')

plt.show()
