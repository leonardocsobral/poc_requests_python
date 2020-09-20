import requests
import numpy as np
from numpy import random


class ApiRequests:

    # def __init__(self, status_code, response_json, response_utf):
    #     self.status_code = status_code
    #     self.response_json = response_json
    #     self.response_utf = response_utf

    # This Method is the easiest way to send a transaction through ACI
    def aci_transaction_post():
        url = "https://test.oppwa.com/v1/payments"

        payload = 'authentication.userId=8ac7a4ca66c593000166c5db24000091&authentication.password=B9hjxAzTz8' \
                  '&authentication.entityId=8ac7a4c7715ea88801715fe9a3900c15&amount=10&currency=BRL&paymentBrand=VISA' \
                  '&paymentType=DB&card.number=4066559930861909&card.holder=Corey%20Reinger&card.expiryMonth=10&card' \
                  '.expiryYear=2022&card.cvv=123&customer.merchantCustomerId=36742106816&merchantTransactionId=90f32647' \
                  '-f606-4f1a-818c-2a794ee9a9e9&customer.givenName=Hosea&customer.surname=Roberts&customer.email' \
                  '=Nakia_Tillman@yahoo.com&descriptor=Stone%20Descriptor&customParameters%5Bproduct%5D=Soap' \
                  '&customParameters%5Bmerchant_website%5D=www.ppro.com&recurringType=INITIAL&testMode=EXTERNAL&billing' \
                  '.state=SP&billing.city=Urielport&billing.country=CL&billing.street1=1031%20Wisozk%20Spur&billing' \
                  '.postcode=8980000&customer.ip=128.121.2.103&recurring.numberOfInstallments=3 '
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        print(response.text.encode('utf8'))
        print(response.json())

    def aci_transaction_post_improved():
        # API's URL
        url = "https://test.oppwa.com/v1/payments"
        # Authentication Data
        user = "8ac7a4ca66c593000166c5db24000091"
        pwd = "B9hjxAzTz8"
        channel = "8ac7a4c7715ea88801715fe9a3900c15"
        currency = "BRL"
        # Card Data
        brand = "VISA"
        cardNumber = "4066559930861909"
        cvv = "123"
        cardExpiryMonth = "10"
        cardExpiryYear = "2022"
        cardHolder = "LeoSobral"
        transactionType = "DB"
        # Customer Data
        taxId = "36742106816"
        amount = random.randint(100) + 1
        payload = {'authentication.userId': user, 'authentication.password': pwd, 'authentication.entityId': channel,
                   'amount': amount,
                   'currency': currency, 'paymentBrand': brand, 'paymentType': transactionType,
                   'card.number': 4066559930861909, 'card.holder': cardHolder,
                   'card.expiryMonth': cardExpiryMonth, 'card.expiryYear': cardExpiryYear, 'card.cvv': cvv,
                   'customer.merchantCustomerId': taxId,
                   'testMode': 'EXTERNAL'}

        headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        print(payload)
        response = requests.request("POST", url, headers=headers, data=payload)
        print(response.status_code)
        print(response.text.encode('utf8'))
        status_code = response.status_code
        response_json = response.json()


        # response_utf = (response.text.enconde('utf8')

        return response_json and status_code

    def healthcheckTest():
        r = requests.get('http://www.google.com')

        if r.status_code == 200:
            print('requests working')

    def aci_transaction_post_improved_craft_oriented_object(self):
        # API's URL
        url = "https://test.oppwa.com/v1/payments"
        # Authentication Data
        user = "8ac7a4ca66c593000166c5db24000091"
        pwd = "B9hjxAzTz8"
        channel = "8ac7a4c7715ea88801715fe9a3900c15"
        currency = "BRL"
        # Card Data
        brand = "VISA"
        cardNumber = "4066559930861909"
        cvv = "123"
        cardExpiryMonth = "10"
        cardExpiryYear = "2022"
        cardHolder = "LeoSobral"
        transactionType = "DB"
        # Customer Data
        taxId = "36742106816"
        amount = random.randint(100) + 1
        payload = {'authentication.userId': user, 'authentication.password': pwd, 'authentication.entityId': channel,
                   'amount': amount,
                   'currency': currency, 'paymentBrand': brand, 'paymentType': transactionType,
                   'card.number': 4066559930861909, 'card.holder': cardHolder,
                   'card.expiryMonth': cardExpiryMonth, 'card.expiryYear': cardExpiryYear, 'card.cvv': cvv,
                   'customer.merchantCustomerId': taxId,
                   'testMode': 'EXTERNAL'}

        headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }

        response = requests.request("POST", url, headers=headers, data=payload)
