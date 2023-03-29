import pandas as pd
import matplotlib.pyplot as plt
import mplfinance as mpf

# define some constants
btcdataset_path = "/home/louisj/Programs/cryptograph/btcdata.csv"
ethdataset_path = "/home/louisj/Programs/cryptograph/ethdata.csv"
btcmdataset_path = "/home/louisj/Programs/cryptograph/btcmdata.csv"
ethmdataset_path = "/home/louisj/Programs/cryptograph/ethmdata.csv"
update_interval = 60

# read data from csv files
btcdata = pd.read_csv(btcdataset_path, index_col=0, parse_dates=True)
ethdata = pd.read_csv(ethdataset_path, index_col=0, parse_dates=True)
btcmdata = pd.read_csv(btcmdataset_path, index_col=0, parse_dates=True)
ethmdata = pd.read_csv(ethmdataset_path, index_col=0, parse_dates=True)

# define graph appearances
colors = mpf.make_marketcolors(
    up='g',
    down='r',
    inherit=True
)
style = mpf.make_mpf_style(marketcolors=colors)
plt.rcParams['toolbar'] = 'None'

# create plots
fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(12,8))
plt.subplots_adjust(top=0.975, bottom=0.08)

# add data in the proper format
mpf.plot(btcdata, type='candle', style=style, ax=axes[0,0], volume=False)
mpf.plot(ethdata, type='candle', style=style, ax=axes[0,1], volume=False)
mpf.plot(btcmdata, type='line', style=style, ax=axes[1,0], volume=False)
mpf.plot(ethmdata, type='line', style=style, ax=axes[1,1], volume=False)

# add titles and grids
axes[0, 0].set_title('Bitcoin Price')
axes[0, 1].set_title('Ethereum Price')
axes[1, 0].set_title('Bitcoin Market Cap')
axes[1, 1].set_title('Ethereum Market Cap')
axes[0, 0].grid()
axes[0, 1].grid()
axes[1, 0].grid()
axes[1, 1].grid()

plt.show()
