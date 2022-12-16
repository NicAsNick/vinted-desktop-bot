"""
import configparser

config = configparser.ConfigParser()
config['USER'] = {'Pseudo': 'Nelphax','Key': '234098230498'}


with open('example.ini', 'w') as configfile:
   config.write(configfile)

"""
fichier = open("user/data.txt", "r")
print(fichier.readlines())
fichier.close()


links = ['https://google.fr\n', 'https://vinted.fr']
fichier = open("user/data.txt", "w")

for link in links:
   fichier.write(link)
fichier.close()


for link in links:
   print(link.replace("\n",""))