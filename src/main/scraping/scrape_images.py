import os
import requests
from bs4 import BeautifulSoup

# Basisspeicherverzeichnis
SAVE_DIR = 'Cars_Dataset/Fiat/500'

# URL der Webseite
URL = 'https://stock.adobe.com/ch_de/search/images?filters%5Bcontent_type%3Aphoto%5D=1&filters%5Bcontent_type%3Aillustration%5D=0&filters%5Bcontent_type%3Azip_vector%5D=0&filters%5Bcontent_type%3Aimage%5D=1&filters%5Breleases%3Ais_exclude%5D=1&filters%5Billustrative%5D=exclude&k=fiat+500&order=relevance&price%5B%24%5D=1&safe_search=1&search_type=filter-select&limit=100&search_page=1&get_facets=1'

# Funktion zum Scraping der Bilder
def fetch_image_urls(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    response = requests.get(url, headers=headers)
    response.raise_for_status()  # Sicherstellen, dass die Anfrage erfolgreich war
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Extrahiere Bild-URLs aus den img-Elementen mit .jpg-Endung
    image_urls = []
    for img in soup.find_all('img'):
        image_url = img.get('src')
        if image_url and image_url.endswith('.jpg'):
            image_urls.append(image_url)
    
    return image_urls

# Funktion zum Herunterladen der Bilder
def download_images(image_urls, save_dir):
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
    
    for i, url in enumerate(image_urls):
        try:
            response = requests.get(url)
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            print(f"Error downloading {url}: {e}")
            continue
        
        file_extension = url.split('.')[-1].split('?')[0]  # Extrahiere die Dateierweiterung
        file_path = os.path.join(save_dir, f'image_{i}.{file_extension}')
        with open(file_path, 'wb') as f:
            f.write(response.content)
        print(f'Downloaded {url} to {file_path}')

if __name__ == "__main__":
    image_urls = fetch_image_urls(URL)
    download_images(image_urls, SAVE_DIR)
    print('Finished downloading images.')
