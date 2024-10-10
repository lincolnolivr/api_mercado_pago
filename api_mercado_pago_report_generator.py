# %%
import os
import requests
from dotenv import load_dotenv

env_path = os.path.join(os.path.dirname(__file__),'.env')
load_dotenv(dotenv_path=env_path)

token = os.getenv('MERCADO_PAGO_TEST_TOKEN_SECRET')

def get_reports(token):
    headers = { 
        'accept': 'application/json',
        'Authorization': f'Bearer {token}' 
    }

    response = requests.get('https://api.mercadopago.com/v1/account/settlement_report/list', headers=headers)
    return response.content

# %%

headers = {
    'Authorization': f'Bearer {token}'
}

response = requests.get('https://api.mercadopago.com/v1/account/settlement_report/settlement-report-450494286-2021-04-24-200025.csv', headers=headers)
print(f'Status: {response.status_code}')
print(response.content)
# %%
