import configparser
from pathlib import Path
from relojjuego import *
from equipo import *
from partido import *
from scoreboard import *
from apiGetter import *
from recolectorESPN import *
from mastodon import Mastodon
from datetime import datetime

def getConfig():
    directorioMain = Path(__file__).resolve().parent
    configPath = str(directorioMain) + "/config.conf"
    config = configparser.ConfigParser()
    config.read(configPath)
    return config

def esHoraDePublicar():
    horaPublicar=False

    if datetime.now().minute == 0:
        horaPublicar=True

    return horaPublicar
    
# Publicar en Mastodon
def publicarMastodon(scorebrd):
    # Cargar config
    config = getConfig()
    mastodonToken = config['MASTODON']['ACCESS_TOKEN']
    mastodonUrlAPI = config['MASTODON']['API_BASE_URL']
    mastodonTam = int(config['MASTODON']['MAX_TAM_TOOT'])
    
    # mastodon.online tiene 500 caracteres por toot. Se Divide el texto por algo mas pequeno y si hace falta pongo varios toots. El tamano de division esta en el fichero de config
    scorebrdStrSplit = scorebrd.divideScoreboard(mastodonTam)
    
    mastodon = Mastodon(access_token = mastodonToken,api_base_url = mastodonUrlAPI)

    primero=True
    for t in scorebrdStrSplit:
        if primero:
            if scorebrd.necesitaContentWarning():
                toot=mastodon.status_post(t,spoiler_text=scorebrd.getEncabezado())
            else:
                toot=mastodon.status_post(t)
            ##print("Publicando sin respuesta")
            ##print(t)
            primero=False
        else:
            if scorebrd.necesitaContentWarning():
                toot=mastodon.status_post(t, in_reply_to_id = toot["id"], spoiler_text=scorebrd.getEncabezado())
            else:
                toot=mastodon.status_post(t, in_reply_to_id = toot["id"])
            ##print("Publicando como respuesta")
            ##print(t)
    
def main():
    
    # Cargar configuracion
    config = getConfig()
    urlAPI = config['API']['API_URL_SCB']
    mastodonPublicar = config['MASTODON'].getboolean('TOOTEAR')

    # Creacion dek apigetter y obtener el doct a partir del json
    ag = ApiGetter(urlAPI, 10)
    datos=ag.obtenerDatosAPI()

    # Traducir la info y generar todos los objetos
    reco=RecolectorESPN(datos)
    ##reco.imprimeInfo()
    scorebrd=reco.generaScoreboard()
    scorebrdStr=scorebrd.__str__()

    # Solo para debug
    #if scorebrd.hayPartidoEnCurso():
    #    print("DEBUG: Hay partidos en curso")
    #else:
    #    print("DEBUG: NO hay partidos en juego")

    #if scorebrd.hayPartidoAcabado():
    #    print("DEBUG: Hay partidos en Acabados")
    #else:
    #    print("DEBUG: NO hay partidos en acabados")

    #print("Es necesario CW: "+str(scorebrd.necesitaContentWarning()))
    #print(datetime.now().minute)
    #print("DEBUG: Partidos sin comenzar ")
    #for ps in scorebrd.partidosSinComenzar:
    #    print(ps)

    #print("¿Es hora de publicar? "+str(esHoraDePublicar()))

    # Publicar si: El fichero de config tiene publicar a True y si hay partidos en curso y si es hora en punto.
    if mastodonPublicar:
        publicarMastodon(scorebrd)

    ## Solo Para Debug
    #print(scorebrd)
    #print(mastodonPublicar)
    #print(type(mastodonPublicar))

    txtScore=scorebrd.__str__()
    print(txtScore)
    print(f"Total caracteres: {len(txtScore)}")

    #print(len(scorebrdStrSplit))
    
if __name__=="__main__":
    main()
