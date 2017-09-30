import urllib.request, os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(os.path.dirname(BASE_DIR))
SERVER_DIR = os.path.dirname(BASE_DIR)


def Exchange_Rate(amount, currency_from, currency_to):

    # create url
    url = 'https://finance.google.com/finance/converter?a={0}&from={1}&to={2}'
    url = url.format(amount, currency_from, currency_to)

    # get html
    fp = urllib.request.urlopen(url)
    html = fp.read().decode('ISO-8859-1')
    fp.close()

    # parse html
    html = html[html.find('span'):html.rfind('span')]
    price = html[html.find('>'):html.rfind('<')]
    price = float(price[1:-4])

    return '{0:.2f}'.format(price)


eur = Exchange_Rate(1, 'PLN', 'EUR')
gbp = Exchange_Rate(1, 'PLN', 'GBP')

file = open(SERVER_DIR + '/manage/setting/data/_exchange_rate', 'w')
file.write('PLN:1\n')
file.write('EUR:{0}\n'.format(eur))
file.write('GBP:{0}'.format(gbp))