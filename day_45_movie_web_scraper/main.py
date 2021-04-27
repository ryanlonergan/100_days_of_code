from bs4 import BeautifulSoup
import requests

response = requests.get('https://www.hollywoodreporter.com/lists/100-best-films-ever-hollywood-favorites-818512')
top_movies = response.text

soup = BeautifulSoup(top_movies, 'html.parser')
movies = soup.find_all(name='li', class_='list-item list-item--ordered has-imagetype-')

movie_titles = [movie.find(class_='list-item__title').text for movie in movies]
movie_ranks = [movie.find(class_='list-item__index').text for movie in movies]

# Reverse list order
titles, ranks = movie_titles[::-1], movie_ranks[::-1]

# Writes the list to a text file
with open('movies.txt', mode='w') as file:
    for title in titles:
        file.write(f'{ranks[titles.index(title)]}) {title}\n')
