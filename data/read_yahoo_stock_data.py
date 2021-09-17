#!/usr/bin/env python3

import argparse

import pandas as pd
from yahoofinancials import YahooFinancials
from shutil import copyfile
from tqdm import tqdm


def main(in_ticker_csv, out_csv):
    output_file_path = out_csv
    temp_file_path = output_file_path + '.temp'
    date_error_msg = 'Dates are not aligned when adding new company stock prices!\n' + \
                 'Date in file: {}, Date to add: {}'

    # Read company symbols
    sp_df = pd.read_csv(in_ticker_csv, encoding = 'unicode_escape')
    sp_500_symbols = sp_df.Ticker.values.tolist()

    # Prepare the file to write stock prices
    symbol_subset = sp_500_symbols[:4]
    history = YahooFinancials(symbol_subset)
    data = history.get_historical_price_data(start_date='2016-09-30',
                                                  end_date='2021-09-30',
                                                  time_interval='daily')
    prices_df = pd.DataFrame({
        a: {x['formatted_date']: x['adjclose'] for x in data[a]['prices']} for a in symbol_subset
    })
    with open(output_file_path, 'w') as wf:
        wf.write(','.join(['date']) + '\n')
        for index, row in prices_df.iterrows():
            wf.write(','.join([index]) + '\n')
    date_count = len(prices_df.index)

    # Write stock prices of a sebset of companies at a time, or it may hang
    batch_size = 1
    for i in tqdm(range(0, len(sp_500_symbols), batch_size)):
        # Query a subset of companies only
        symbol_subset = sp_500_symbols[i:i+batch_size]
        history = YahooFinancials(symbol_subset)
        data = history.get_historical_price_data(start_date='2016-09-30',
                                                      end_date='2021-09-30',
                                                      time_interval='daily')
        try:
            prices_df = pd.DataFrame({
                a: {x['formatted_date']: x['adjclose'] for x in data[a]['prices']} for a in symbol_subset
            })
        except:
            print('Skipping for symbols {} as their yahoo queries are not responding'.format(symbol_subset))
            continue

        new_data_to_add = list(prices_df.iterrows())
        if len(new_data_to_add) != date_count:
            print('Skipping for symbols {} as they don\'t have the price info for all the dates'.format(symbol_subset))
            continue
        
        copyfile(output_file_path, temp_file_path)
        with open(temp_file_path, 'r') as rf, open(output_file_path, 'w') as wf:
            for i2, line in enumerate(rf.readlines()):
                # Add more company symbols to the file
                if i2 == 0:
                    wf.write(line[:-1] + ',' + ','.join(symbol_subset) + '\n')
                # For each new company, add their stock prices
                else:
                    assert line[:-1].split(',')[0] == new_data_to_add[i2-1][0], date_error_msg.format(line[:-1].split(',')[0], new_data_to_add[i2-1][0])
                    wf.write(line[:-1] + ',' + ','.join([str(t) for t in new_data_to_add[i2-1][1].values.tolist()]) + '\n')

    print('Done writing all company stock prices to file.')


# CLI
parser = argparse.ArgumentParser(description='Convert CTM to text file')

parser.add_argument('--in-ticker-csv', type = str, required = False, default = 'S&P 500 tickers.csv')
parser.add_argument('--out-csv', type = str, required = False, default = 'sp500_prices_adjclose_30_09_16_30_09_21.csv')


if __name__ == '__main__':
    args = parser.parse_args()
    main(args.in_ticker_csv, args.out_csv)