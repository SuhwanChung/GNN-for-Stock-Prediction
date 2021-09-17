## Usage
Simply run the below command with optional arguments ```--in-ticker-csv [path-to-csv]``` and  ```--out-csv [path-to-output]```.  If they are not provided, the default will be used. Please see the .py script for details.
```$ ./read_yahoo_stock_data.py```

## Result files
```sp500_prices_adjclose_30_09_16_30_09_21.csv```

## Log when downloading stock prices for S&P 500
```
$ ./read_yahoo_stock_data.py 
 13%|█████▎                                    | 64/505 [00:26<03:36,  2.04it/s]Skipping for symbols ['BRK.B'] as their yahoo queries are not responding
 16%|██████▌                                   | 79/505 [01:49<03:59,  1.78it/s]Skipping for symbols ['BF.B'] as they don't have the price info for all the dates
 18%|███████▍                                  | 89/505 [01:54<03:42,  1.87it/s]Skipping for symbols ['CARR'] as they don't have the price info for all the dates
 26%|██████████▍                              | 129/505 [02:15<02:53,  2.17it/s]Skipping for symbols ['CTVA'] as they don't have the price info for all the dates
 31%|████████████▌                            | 155/505 [02:31<03:43,  1.57it/s]Skipping for symbols ['DOW'] as they don't have the price info for all the dates
 40%|████████████████▍                        | 202/505 [03:01<03:22,  1.50it/s]Skipping for symbols ['FOXA'] as they don't have the price info for all the dates
 40%|████████████████▍                        | 203/505 [03:01<02:49,  1.78it/s]Skipping for symbols ['FOX'] as they don't have the price info for all the dates
 49%|████████████████████                     | 247/505 [03:31<03:03,  1.41it/s]Skipping for symbols ['IR'] as they don't have the price info for all the dates
 56%|██████████████████████▊                  | 281/505 [03:54<02:45,  1.36it/s]Skipping for symbols ['LW'] as they don't have the price info for all the dates
 63%|█████████████████████████▋               | 317/505 [04:19<02:15,  1.39it/s]Skipping for symbols ['MRNA'] as they don't have the price info for all the dates
 70%|████████████████████████████▉            | 356/505 [04:47<01:56,  1.28it/s]Skipping for symbols ['OGN'] as they don't have the price info for all the dates
 71%|████████████████████████████▉            | 357/505 [04:48<01:27,  1.69it/s]Skipping for symbols ['OTIS'] as they don't have the price info for all the dates
100%|█████████████████████████████████████████| 505/505 [06:50<00:00,  1.23it/s]
Done writing all company stock prices to file.

```
