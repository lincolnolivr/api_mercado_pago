# %%
import os
import json
import requests
import pandas as pd
from dotenv import load_dotenv

# %%
env_path = os.path.join(os.path.dirname(__file__),'.env')
load_dotenv(dotenv_path=env_path)

token = os.getenv('MERCADO_PAGO_TEST_TOKEN_SECRET')

# %%

def get_reports(token):
    headers = { 
        'accept': 'application/json',
        'Authorization': f'Bearer {token}' 
    }

    response = requests.get('https://api.mercadopago.com/v1/account/settlement_report/list', headers=headers)
    return response.content

def get_report(token, report_name):
    headers = {
    'Authorization': f'Bearer {token}'
    }

    response = requests.get(f'https://api.mercadopago.com/v1/account/settlement_report/{report_name}', headers=headers)
    return response.content

# %%
reports = get_reports(token).decode('utf-8')
reports = json.loads(reports)
df = pd.DataFrame(reports)

# %%
last_report = get_report(token, df['file_name'][0]).decode('utf-8')

# Check how to make the last report to Data frame as it is text
# data = pd.DataFrame(last_report)


# %%
