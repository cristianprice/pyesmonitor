import requests
import json


def poll_stats(host, port=9200, protocol='http', url='/_nodes/stats', headers={}, auth=None, json=True):
    full_url = f'{protocol}://{host}:{port}{url}'
    r = requests.get(full_url, headers=headers,
                     auth=auth, timeout=5)

    return r.content.decode('utf-8') if json else r.json()
