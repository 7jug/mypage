import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient
import certifi
ca = certifi.where()
client = MongoClient('mongodb+srv://sparta:test@cluster0.7xyclcs.mongodb.net/Cluster0?retryWrites=true&w=majority', tlsCAFile=ca)
db = client.dbsparta

URL = "https://www.billboard-japan.com/charts/detail?a=hot100"
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get(URL, headers=headers)
soup = BeautifulSoup(data.text, 'html.parser')

print(soup)

songs = soup.select('#content2 > div > div.leftBox > table > tbody > tr')

for song in songs:
    rank = song.select_one('td>span').text
    artist = song.select_one('p.artist_name').text.strip()
    title = song.select_one('p.musuc_title').text.strip()
    print(rank,artist,title)

# movies = soup.select('#document_16l5w5x > main > div > div > section:nth-child(4) > table > tbody > tr')
# for movie in movies:
#     rank = movie.select_one('span').text
#     title = movie.select_one('h2 > a').text
#     date = movie.select_one('.time').text
#     doc = {
#         'title':title,
#         'rank':rank,
#         'date':date
#     }
#     db.movies.insert_one(doc)