import requests
from bs4 import BeautifulSoup
import re


def artist_search(artist):
    #TODO: Add error catching for invalid artist
    base_url = "https://api.genius.com"
    headers = {'Authorization': 'Bearer ' + 'O7jw2UWwqHpu8BX3-ophJywcdKK7T3ITq_f6AOVqvVZIZxr4l5K3CvFBZkPCyWU_'}
    search_url = base_url + '/search'
    data = {'q': artist}
    response = requests.get(search_url, data=data, headers=headers)
    return response.json()

def request_song_info():
    base_url = "https://api.genius.com"
    headers = {'Authorization': 'Bearer ' + 'O7jw2UWwqHpu8BX3-ophJywcdKK7T3ITq_f6AOVqvVZIZxr4l5K3CvFBZkPCyWU_'}
    search_url = base_url + '/search'
    data = {'q': 'gucci gang'}
    response = requests.get(search_url, data=data, headers=headers)
    return response.json()

def get_lyrics(url):
    page = requests.get(url)
    html = BeautifulSoup(page.text, 'html.parser')
    lyrics = html.find('div', class_='lyrics')
    print(lyrics.get_text())

def mask_lyrics(url):
    page = requests.get(url)
    html = BeautifulSoup(page.text, 'html.parser')
    pre_lyrics = html.find('div', class_='lyrics').get_text()
    lyrics = re.sub(r"\[.*\]", "", pre_lyrics).strip()


if __name__ == '__main__':
    mask_lyrics('https://genius.com/Drake-hold-on-were-going-home-lyrics')
    # artist = input("Choose an artist: ")
    # songs = artist_search(artist)
    # hits = songs['response']['hits']
    # num_to_song = {}
    # for i in range(len(hits)):
    #     title = hits[i]['result']['title']
    #     print("{}: {}".format(i, title))
    #     num_to_song[i] = {'title': title, 'url': hits[i]['result']['url']}
    # #TODO: implement checking for non-ints and out of range ints being put in
    # num = int(input("Which song would you like? Insert the respective number: "))
    # song = num_to_song[num]
    # print(song['title'])
    # get_lyrics(song['url'])
    # mask_lyrics(song['url'])
