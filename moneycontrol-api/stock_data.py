import requests
from .utils import parse_curl, convert_date_to_timestamp

templated_curl_command_stock = """
curl -H 'accept: */*' -H 'user-agent: moneycontrol/325 CFNetwork/1498.700.2 Darwin/23.6.0' -H 'accept-language: en-IN,en-GB;q=0.9,en;q=0.8' --compressed 'https://priceapi.moneycontrol.com/techCharts/mcApp/history?symbol={symbol}&resolution={resolution}&from={from_timestamp}&to={to_timestamp}&firstCall=true'
"""

def fetch_historical_data(symbol, resolution, from_date, to_date):
    from_timestamp = convert_date_to_timestamp(from_date)
    to_timestamp = convert_date_to_timestamp(to_date)

    curl_command = templated_curl_command_stock.format(
        symbol=symbol,
        resolution=resolution,
        from_timestamp=from_timestamp,
        to_timestamp=to_timestamp
    )

    url, headers = parse_curl(curl_command)

    response = requests.get(url, headers=headers)
    return response