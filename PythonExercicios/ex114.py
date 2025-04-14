#Verificar se site pudim está acesível
import urllib
import urllib.request

try:
    site = urllib.request.urlopen('https://www.twitch.tv')
except:
    print('Não-disponível')
else:
    print('DISPONÍVEL')

#Por algum motivo, pudim não funcionou
