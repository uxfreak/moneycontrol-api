
import uncurl
import requests
import time

def parse_curl(curl_command):
    context = uncurl.parse_context(curl_command)
    url = context.url
    headers = context.headers
    return url, headers

def convert_date_to_timestamp(date_str):
    return int(time.mktime(time.strptime(date_str, "%Y-%m-%d")))
