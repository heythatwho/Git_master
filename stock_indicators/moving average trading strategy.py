# moving average trading strategy
import datetime as dt
import matplotlib.pyplot as plt
import pandas_datareader as web

print("for Issac's Group Only, hummmm, happy trading! ")

plt.style.use("dark_background")

ma_1 = int(input("input short term SMA"))
ma_2 = int(input("input longer term SMA"))

stock = input("what stock do you want to check?")

start=dt.datetime.now()- dt.timedelta(days=363*3) #past 3 year
end=dt.datetime.now()

data=web.DataReader(stock, "yahoo", start, end)
# print(data)

data[f"SMA_{ma_1}"] = data["Adj Close"].rolling(window=ma_1).mean()
data[f"SMA_{ma_2}"] = data["Adj Close"].rolling(window=ma_2).mean()

data= data.iloc[ma_2:]

plt.plot(data["Adj Close"], label="Share Price", color="lightgray")
plt.plot(data[f"SMA_{ma_1}"], label=f"SMA_{ma_1}", color="orange")
plt.plot(data[f"SMA_{ma_2}"], label=f"SMA_{ma_2}",color="purple")
plt.legend(loc="upper left")
plt.show()

buy_signals =[]
sell_signals =[]
trigger = 0

for x in range(len(data)):
	if data[f"SMA_{ma_1}"].iloc[x] > data[f"SMA_{ma_2}"].iloc[x] and trigger !=1:
		buy_signals.append(data["Adj Close"].iloc[x])
		sell_signals.append(float("nan"))
		trigger = 1
	elif data[f"SMA_{ma_1}"].iloc[x] < data[f"SMA_{ma_2}"].iloc[x] and trigger !=-1:
		buy_signals.append(float("nan"))
		sell_signals.append(data["Adj Close"].iloc[x])
		trigger= -1
	else:
		buy_signals.append(float("nan"))
		sell_signals.append(float("nan"))

data["Buy Signals"]=buy_signals
data["Sell Signals"]=sell_signals

print(data)

plt.plot(data["Adj Close"], label="Share Price", alpha=0.5)
plt.plot(data[f"SMA_{ma_1}"], label=f"SMA_{ma_1}", color="orange", linestyle="--")
plt.plot(data[f"SMA_{ma_2}"], label=f"SMA_{ma_2}",color="purple", linestyle="--")
plt.scatter(data.index, data["Buy Signals"],label="Buy Signals", marker="^", color="#00ff00", lw=3)
plt.scatter(data.index, data["Sell Signals"],label="Sell Signals", marker="v", color="#ff0000", lw=3)
plt.legend(loc="upper left")
plt.show()


