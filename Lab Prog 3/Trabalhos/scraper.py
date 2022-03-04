
from bs4 import BeautifulSoup
import requests

class Filme:
    def __init__(self,titulo,autor,nota):
        self.titulo = titulo
        self.autor = autor
        self.nota = nota


req = requests.get('https://www.imdb.com/chart/top/')

soup = BeautifulSoup(req.content,'html.parser')
lista_titulos = []

for element in soup.find_all("td","titleColumn"):
    lista_titulos.append(element.a.string)

lista_autores = []
for element in soup.find_all("td","titleColumn"):
    lista_autores.append(element.a["title"])

lista_notas = []
for element in soup.find_all("td","ratingColumn imdbRating"):
    lista_notas.append(element.strong.string)

lista_filmes = []
for i in range(0,len(lista_titulos)):
    lista_filmes.append(Filme(lista_titulos[i],lista_autores[i],lista_notas[i]))

##visualização

print("Top " + str(5) + " filmes:\n")

for i in range(0,4):
    print("Título: " + lista_filmes[i].titulo)
    print("Autor: " + lista_filmes[i].autor)
    print("Nota: " + lista_filmes[i].nota)

    print("\n")