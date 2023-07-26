import csv
import requests
from bs4 import BeautifulSoup
from tqdm import tqdm

def scrape_game_data(url):
    game_list = []
    page_num = 1

    while True:
        page_url = f"{url}?page={page_num}"
        response = requests.get(page_url)
        if response.status_code != 200:
            break

        soup = BeautifulSoup(response.content, 'html.parser')
        games_on_page = soup.find_all('div', class_='game_cell')

        if not games_on_page:
            break

        # Use tqdm to create a progress bar
        for game in tqdm(games_on_page, desc=f"Scraping page {page_num}"):
            game_name = game.find('a', class_='title game_link').text.strip()

            # Extracting game author
            game_author_element = game.find('div', class_='game_author').find('a')
            game_author = game_author_element.text.strip() if game_author_element else 'N/A'

            game_price_element = game.find('div', class_='price_value')
            game_price = game_price_element.text.strip() if game_price_element else 'N/A'

            game_genre_element = game.find('div', class_='game_genre')
            game_genre = game_genre_element.text.strip() if game_genre_element else 'N/A'

            # Extracting game rating
            game_rating_element = game.find('div', class_='game_rating')
            game_rating = game_rating_element['title'] if game_rating_element else 'N/A'

            game_url = game.find('a', class_='title game_link')['href']

            game_list.append((game_name, game_author, game_price, game_genre, game_rating, game_url))

        page_num += 1

    return game_list

def save_to_csv(data, filename):
    with open(filename, 'w', newline='', encoding='utf-8-sig') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(["Game_Name", "Game_Author", "Game_Price", "Game_Genre", "Game_Rating", "Game_URL"])
        for game in data:
            csv_writer.writerow(game)

if __name__ == "__main__":
    url = "https://itch.io/games/top-rated/made-with-pico-8"
    game_data = scrape_game_data(url)
    if game_data:
        csv_filename = "Pico8_games_toprated.csv"
        save_to_csv(game_data, csv_filename)
        print(f"Data scraped successfully and saved to {csv_filename}.")
