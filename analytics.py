import pandas as pd
import os
import csv

# identify last csv file in directory
path = os.path.join(os.getcwd(), 'olx', 'data', 'electronics')

csvs = list(filter(lambda x: '.csv' in x, os.listdir(path)))
last_csv = max(csvs)

df = pd.read_csv(os.path.join(path, last_csv))

mean_prices = {
    "iphone 8": 0,
    "iphone 8 plus": 0,
    "iphone x": 0,
    "iphone xs": 0,
    "iphone xs max": 0,
    "iphone xr": 0,
    "iphone 11": 0,
    "iphone 11 pro": 0,
    "iphone 11 pro max": 0,
    "iphone 12": 0,
    "iphone 12 pro": 0,
    "iphone 12 pro max": 0,
}

bargains = pd.DataFrame(columns=df.columns)

for phone in mean_prices:
    listings = df[df['title'].str.lower().str.contains(phone, regex=False)]
    mean_prices[phone] = listings['price'].mean()

    cheap_listings = listings[listings['price'] < mean_prices[phone]]
    bargains = bargains.append(cheap_listings, ignore_index=True)

print(bargains.head())

bargains.to_csv(os.path.join(path, 'bargains', last_csv[:-4]+'_cheap.csv'), index=False)

mean_csv = [{'model': key, 'mean_price': value} for key, value in mean_prices.items()]
with open(os.path.join(path, 'mean_prices', f'mean_{last_csv[:-4]}.csv'), 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=['model', 'mean_price'])
    writer.writeheader()
    writer.writerows(mean_csv)