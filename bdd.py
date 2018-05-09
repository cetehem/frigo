import configparser

NOM_FICHIER = 'stock.dat'

def ecrire_donnees(key, stock, masse, date):
    config = configparser.ConfigParser()
    config.read(NOM_FICHIER)


    config[key] = {}

    config[key] = {}
    config[key]['Stock'] = stock
    config[key]['Masse'] = masse
    config[key]['Date'] = date

    with open(NOM_FICHIER, 'w') as configfile:
        config.write(configfile)

ecrire_donnees('pdt', '128', '456', '2018-05-07')
ecrire_donnees('broc', '124', '455', '2018-05-06')
ecrire_donnees('cart', '124', '455', '2018-05-06')

