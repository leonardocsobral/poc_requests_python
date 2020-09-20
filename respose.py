from request import Requests


def responseAssertions():

    r = Requests.aciTransactionPostImproved()
    print(r)
    if r == 200:
        print ('')
    else:
        print('n')
