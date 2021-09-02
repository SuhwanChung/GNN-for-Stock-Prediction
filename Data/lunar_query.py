
import argparse
import urllib.request
import json
import pandas as pd


def query(args):
    path = args.credential

    with open(path) as f:
        key = f.read().split('\n')[0]

    url = f"https://api.lunarcrush.com/v2?data=assets&key={key}&symbol=BTC&interval=day&data_points={365*2}"

    response = urllib.request.urlopen(url)
    data = json.load(response)

    data = pd.DataFrame(data['data'][0]['timeSeries']).to_csv('./stockdata.csv')

    return




if __name__ == '__main__':

    parser = argparse.ArgumentParser(description="Save stock data")
    parser.add_argument(
        "--credential", type=str, help='Credential for LunarCrush API'
    )
    args = parser.parse_args()

    query(args)

