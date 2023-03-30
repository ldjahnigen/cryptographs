import pandas as pd
import random
import datetime
import numpy as np

btcdata = "/home/louisj/Programs/cryptograph/btcdata.csv"
btcmdata = "/home/louisj/Programs/cryptograph/btcmdata.csv"
ethdata = "/home/louisj/Programs/cryptograph/ethdata.csv"
ethmdata = "/home/louisj/Programs/cryptograph/ethmdata.csv"

btc_data = pd.read_csv(btcdata)
btcm_data = pd.read_csv(btcmdata)
eth_data = pd.read_csv(ethdata)
ethm_data = pd.read_csv(ethmdata)

def incrementDate(date):
    year = date.split("-")[0]
    month = date.split("-")[1]
    day = date.split("-")[2]
    date = datetime.datetime(int(year), int(month), int(day))
    date += datetime.timedelta(days=1)
    date = "20" + date.strftime('%y-%m-%d')
    return date


mode = input("Enter dataframe to edit (btc, eth): ")
if mode == "btc":
    date = btc_data.loc[len(btc_data) - 1, "date"]
    openamount = btc_data.loc[len(btc_data) - 1, "open"]
    highamount = btc_data.loc[len(btc_data) - 1, "high"]
    lowamount = btc_data.loc[len(btc_data) - 1, "low"]
    closeamount = btc_data.loc[len(btc_data) - 1, "close"]
    volume = btc_data.loc[len(btc_data) - 1, "volume"]

    mu = 0
    sigma = 10

    while True:
        change_coef = np.random.normal(mu, sigma)
        if -50 <= change_coef <= 50:
            break

    change_coef = change_coef / 100

    date = incrementDate(date)
    openamount += (openamount * change_coef)
    highamount += (highamount * change_coef)
    lowamount += (lowamount * change_coef)
    closeamount += (closeamount * change_coef)
    volume += (volume * change_coef)

    data = {
        "date": date,
        "open": openamount,
        "high": highamount,
        "low": lowamount,
        "close": closeamount,
        "volume": volume 
        }
    btc_data.loc[len(btc_data)] = data
    btc_data.to_csv("btcdata.csv", index=False)


elif mode == "eth":
    date = eth_data.loc[len(eth_data) - 1, "date"]
    openamount = eth_data.loc[len(eth_data) - 1, "open"]
    highamount = eth_data.loc[len(eth_data) - 1, "high"]
    lowamount = eth_data.loc[len(eth_data) - 1, "low"]
    closeamount = eth_data.loc[len(eth_data) - 1, "close"]
    volume = eth_data.loc[len(eth_data) - 1, "volume"]

    mu = 0
    sigma = 10

    while True:
        change_coef = np.random.normal(mu, sigma)
        if -50 <= change_coef <= 50:
            break

    change_coef = change_coef / 100

    date = incrementDate(date)
    openamount += (openamount * change_coef)
    highamount += (highamount * change_coef)
    lowamount += (lowamount * change_coef)
    closeamount += (closeamount * change_coef)
    volume += (volume * change_coef)

    data = {
        "date": date,
        "open": openamount,
        "high": highamount,
        "low": lowamount,
        "close": closeamount,
        "volume": volume 
        }
    eth_data.loc[len(eth_data)] = data
    eth_data.to_csv("ethdata.csv", index=False)
