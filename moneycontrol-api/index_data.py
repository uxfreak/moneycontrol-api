import requests
from .utils import parse_curl

templated_curl_command_index = """
curl -H 'accept: */*' -H 'user-agent: moneycontrol/325 CFNetwork/1498.700.2 Darwin/23.6.0' -H 'accept-language: en-IN,en-GB;q=0.9,en;q=0.8' --compressed 'https://api.moneycontrol.com/mcapi/v1/indices/livemarket-indices/basic?ex={exchange}&frequency={frequency}&sortCol=&orderBy='
"""

def fetch_index_data(exchange, frequency):
    curl_command = templated_curl_command_index.format(
        exchange=exchange,
        frequency=frequency
    )

    url, headers = parse_curl(curl_command)

    response = requests.get(url, headers=headers)
    return response