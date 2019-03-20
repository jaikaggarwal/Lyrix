import requests
from bs4 import BeautifulSoup


def request_song_info():
    base_url = "https://api.genius.com"
    headers = {'Authorization': 'Bearer ' + 'O7jw2UWwqHpu8BX3-ophJywcdKK7T3ITq_f6AOVqvVZIZxr4l5K3CvFBZkPCyWU_'}
    search_url = base_url + '/search'
    data = {'q': 'Drake'}
    response = requests.get(search_url, data=data, headers=headers)
    return response.json()

def get_lyrics(url):
    page = requests.get(url)
    html = BeautifulSoup(page.text, 'html.parser')
    lyrics = html.find('div', class_='lyrics')
    print(lyrics.get_text())



if __name__ == '__main__':
    get_lyrics('https://genius.com/Drake-0-to-100-the-catch-up-lyrics')
    # x = request_song_info()
    # for hit in x['response']['hits']:
    #     print(hit['result']['url'])