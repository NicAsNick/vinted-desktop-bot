import eel
import requests
from bs4 import BeautifulSoup
import time
import random
import json


fichier = open("user/data.txt", "r")
file_links = fichier.readlines()
links = []
for link in file_links:
    links.append(link.replace("\n",""))
    
fichier.close()

eel.init("web")  
eel.start("index.html", block=False)

@eel.expose
def task(name,link):
    links.append((link + ";" + name))
    with open(f'user/data.txt', 'a+') as f:
        f.write('\n' + link + ';' + name)
    sendTask()


@eel.expose
def actualisation():
    sendTask()

def sendTask():
    for link in links:
        title_link = link.split(";")[1]
        vinted_link = link.split(";")[0]
        print(title_link,vinted_link)
        eel.addText(title_link,vinted_link)




products = []
count = 0
linkCount = 0
while True:  
    
    try:

        if linkCount > (len(links) - 1):
            linkCount = 0

        headers = {"User-Agent":"Mozilla/5.0"}
        r = requests.get(links[linkCount], headers=headers)
        page = r.content
        soup = BeautifulSoup(page, 'html.parser')
        data = soup.find(
            "script", {"data-js-react-on-rails-store": "MainStore"})
        
        data = str(data)[str(data).find("{"): str(data).find("</script>")]
        
        jsonData = json.loads(data)
        
        try:
            x = jsonData["items"]["catalogItems"]["byId"].values()
        except:
            print("erreur json : ", jsonData)
        
        
        produits = []
        for val in x:
            produits.append(val)

        for produit in produits:

            if count < len(links):

                id = produit["id"]
                products.append(id)

            if count > len(links):
                id = produit["id"]

                if id not in products:
                    print("Nouveau produit disponible")
                    try:
                        url = produit["url"]
                    except:
                        url = links[linkCount]

                    try:
                        name = produit["title"]
                    except:
                        name = "No title found"
                        break
                    
                    try:
                        size = produit["size_title"]
                    except:
                        size = "No size information"

                    try:
                        brand = produit["brand_title"]
                    except:
                        brand = "No brand information"

                    try:
                        price = (produit["price"] + produit["currency"])
                    except:
                        price = "No price information"

                    try:
                        image = produit["photo"]["url"]
                    except:
                        image = "[LINK OFF IMAGE YOU WANT]"
                        
                    countUrl = links[linkCount]


                    try:
                        eel.addArticle(name,url,brand,size,price,image,"now")
                        print("Webhook envoyé !")
                    except:
                        print("Impossible d'envoyé le webhook")
                    

                    time.sleep(5)
                    products.append(id)

        print("script all shoes spam is running", count,
              ", Heure :", time.strftime('%Hh%M'))
        count += 1
        linkCount += 1
        time.sleep(random.randint(0, 10))

    except ConnectionResetError:
        print("Erreur de Connexion")
        console = "Erreur de connexion"
        time.sleep(3)
        pass

    eel.sleep(1)
