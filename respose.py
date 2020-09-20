from request import ApiRequests
import requests


class Responses():

    def response_pure(self):
        r = ApiRequests.aci_transaction_post_improved()
        print(r)
        if r.status.code == 200:
            print('response is being send properly')
        else:
            print('Take a look at the class request')

    def response_assertions(self):
        r = ApiRequests.aci_transaction_post_improved()
        assert r.status.code == 200
