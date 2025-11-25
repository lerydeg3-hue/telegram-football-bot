import requests
import time
import feedparser

# ---------------------------
# CONFIGURATION
# ---------------------------
TOKEN = "8285225937:AAEg5KqgkqE87HXVyfTp88bODUywKvQFmcM"   
# Mets ton token ici
CHAT_ID = "@InfosportFootballandbasketball"

# Flux RSS sélectionnés
RSS_FEEDS = [
    "https://www.lequipe.fr/rss/actu_rss.xml",
    "https://www.eurosport.fr/football/rss.xml"
]

# Pour éviter les doublons de publications
DEJA_PUBLIE = set()

# ---------------------------
# FONCTION D'ENVOI AU CANAL
# ---------------------------
def envoyer(message):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    requests.post(url, data={
        "chat_id": CHAT_ID,
        "text": message,
        "parse_mode": "Markdown"
    })

# ---------------------------
# BOUCLE INFINIE AUTOMATIQUE
# ---------------------------
while True:
    for RSS_URL in RSS_FEEDS:
        try:
            feed = feedparser.parse(RSS_URL)
            for article in feed.entries:
                if article.link not in DEJA_PUBLIE:
                    titre = article.title
                    lien = article.link

                    texte = f"📰 *{titre}*\n\n{lien}"
                    envoyer(texte)

                    DEJA_PUBLIE.add(article.link)  # mémorisé pour éviter doublons

        except Exception as e:
            print("Erreur :", e)

    time.sleep(120)  # vérifie toutes les 2 minutes
