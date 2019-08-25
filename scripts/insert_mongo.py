import time

import pandas as pd
import requests

df = pd.read_excel('4250.xlsx', header=None)
for i in df.to_dict('records'):
    for k, v in i.items():
        requests.post('http://127.0.0.1:5000', data={'ci': v})
        time.sleep(1)
