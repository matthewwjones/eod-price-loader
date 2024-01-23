# eod-price-loader
Simple utility for grabbing EOD prices from EOD HD.

## Requirements

1. Create a file in the root called `api-config.txt` and add:
```bash
  api_token=<Your API token from EOD HD>
```

2. Create a file in the root called `instrument-codes.txt` and add a list of instruments that you're interested in 
collecting prices for, one per line with a format recognised by EOD HD.  You can 
[look these up here](https://eodhd.com/financial-apis/), for example:

```bash
    ISF.LSE
    CUKS.LSE
```
