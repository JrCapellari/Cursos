import urllib
import urllib.request


def pudim(msg):
    try:
        site = urllib.request.urlopen(msg)
        print('O site pudim.com.br esta acessível no momento')
    except:
        print('O site pudim NÃO esta acessível')


pudim('http://www.pudim.com.br')
