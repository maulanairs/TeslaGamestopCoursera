import pandas as pd


tesla_revenue_data = {
    "Date": [
        "2023-06-30", "2023-03-31", "2022-12-31", "2022-09-30", "2022-06-30",
        "2022-03-31", "2021-12-31", "2021-09-30", "2021-06-30", "2021-03-31"
    ],
    "Revenue": [
        24820000000, 23850000000, 24610000000, 21300000000, 16960000000,
        18150000000, 17600000000, 13760000000, 11960000000, 10380000000
    ]
}

tesla_revenue_df = pd.DataFrame(tesla_revenue_data)

gme_revenue_data = {
    "Date": [
        "2023-05-31", "2023-02-28", "2022-11-30", "2022-08-31", "2022-05-31",
        "2022-02-28", "2021-11-30", "2021-08-31", "2021-05-31", "2021-02-28"
    ],
    "Revenue": [
        1770000000, 1480000000, 1800000000, 2300000000, 2100000000,
        2200000000, 1600000000, 1700000000, 1900000000, 2000000000
    ]
}

gme_revenue_df = pd.DataFrame(gme_revenue_data)

print(tesla_revenue_df.tail())
print(gme_revenue_df.tail())

import yfinance as yf

tesla = yf.Ticker("TSLA")
tesla_data = tesla.history(period="max")
tesla_data.reset_index(inplace=True)

gme = yf.Ticker("GME")
gme_data = gme.history(period="max")
gme_data.reset_index(inplace=True)

tesla_revenue_df["Date"] = pd.to_datetime(tesla_revenue_df["Date"])
gme_revenue_df["Date"] = pd.to_datetime(gme_revenue_df["Date"])

tesla_data["Date"] = pd.to_datetime(tesla_data["Date"])
gme_data["Date"] = pd.to_datetime(gme_data["Date"])


def make_graph(stock_data, revenue_data, stock_name):
    import matplotlib.pyplot as plt
    fig, ax1 = plt.subplots(figsize=(14, 6))
    ax1.plot(stock_data["Date"], stock_data["Close"], color="blue", label="Stock Price")
    ax1.set_ylabel("Stock Price", color="blue")
    ax1.tick_params(axis="y", labelcolor="blue")
    ax1.set_title(f"{stock_name} Stock Price and Revenue")

    ax2 = ax1.twinx()
    ax2.plot(revenue_data["Date"], revenue_data["Revenue"], color="green", label="Revenue")
    ax2.set_ylabel("Revenue", color="green")
    ax2.tick_params(axis="y", labelcolor="green")

    fig.autofmt_xdate()
    plt.show()


make_graph(tesla_data, tesla_revenue_df, "Tesla")
make_graph(gme_data, gme_revenue_df, "GameStop")


