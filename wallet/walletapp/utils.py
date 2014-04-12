from django.conf import settings
import requests
import simplejson as json

def make_payment(user, value):
    data = {
        "payment": {
            "client": {
                "name": " ".join([]),
                "email": user,
                "address": {
                     "country": "pt",
                     "address": "some street",
                     "city": "lisboa",
                     "postalcode": "1100-000"
                }
            },
            "amount": value/100.0,
            "currency": "EUR",
            "items": [],
        },
        "url_confirm": "https://codingbooster.herokuapp.com",
        "url_cancel": "https://codingbooster.herokuapp.com"}
    url = "https://services.wallet.codebits.eu/api/v2/checkout"
    headers = {
        "Authorization": "WalletPT "+settings.WALLET_MER_ID,
        'content-type': 'application/json'
    }
    payload = json.dumps(data)
    response = requests.post(url, data=payload, headers=headers)
    return response
