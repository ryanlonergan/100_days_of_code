from bs4 import BeautifulSoup
import requests

response = requests.get('https://news.ycombinator.com/news')
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, 'html.parser')
articles = soup.find_all(name='a', class_='storylink')

# article_texts, article_links = [], []
# for article_tag in articles:
#     text = article_tag.text
#     article_texts.append(text)
#     link = article_tag.get('href')
#     article_links.append(link)

# List comprehension is much, much shorter - compare with above
article_texts = [article_tag.text for article_tag in articles]
article_links = [article_tag.get('href') for article_tag in articles]

# List comprehension to parse upvote scores with error exception if no score exists
subtexts = soup.find_all(name="td", class_="subtext")
article_upvotes = [0 if sub.find(class_="score") is None else int(sub.find(class_="score").text.split()[0]) for sub in subtexts]

# finding index of article with highest score
largest_ind = article_upvotes.index(max(article_upvotes))

print(article_texts[largest_ind], article_links[largest_ind], article_upvotes[largest_ind], 'Votes')

# From here, can decide what to do with information, such as sending an sms or email with the most popular article
# every day, putting the lists into a dict or dataframe to sort, etc.
