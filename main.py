import os

from functions import *
from keys import *

if __name__ == "__main__":
    # Load the binance keys
    client = api.Binance_API(api_key=BINANCE_API_KEY, secret_key=BINANCE_SECRET_KEY)

    # Set the date and timeframes
    start_date = "2023-05-01"
    end_date = "2024-05-11"
    timeframe = "5m"

    # Create a list of pairs
    pairs = [
        "SOLBTC",
        "SOLUSDT",
    ]

    # Rip through the pairs
    for pair in pairs:
        # Create the path to save the data
        data_folder = os.path.join("data", "candles")
        data_path = os.path.join(data_folder, f"df_{timeframe}_{pair}.csv")
        os.makedirs(data_folder, exist_ok=True)

        # Collect the candles
        candles = get_candles_batched(client, symbol=pair, interval=timeframe, start_date=start_date, end_date=end_date, delay=0.4)

        # Convert the candles to a dataframe
        df = create_df(candles)

        # Visualise and save the data
        print(df)
        df.to_csv(data_path, index=False)
        plot_chart(df)

    # # Download spread data
    # candles1 = get_candles_batched(client, symbol=pair1, interval=timeframe, start_date=start_date, end_date=end_date, delay=0.4)
    # candles2 = get_candles_batched(client, symbol=pair2, interval=timeframe, start_date=start_date, end_date=end_date, delay=0.4)

    # df_spread = create_spread_df(candles1, candles2)
    # print(df_spread)
    # plot_chart(df_spread)
    # df_spread.to_csv(f"df_spread_{timeframe}_{pair1}_{pair2}.csv", index=False)
