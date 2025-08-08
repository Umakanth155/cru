import requests
from bs4 import BeautifulSoup
 
url = "https://www.cricbuzz.com/cricket-match/live-scores/recent-matches"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
 
matches = soup.find_all('div', class_="cb-lv-main")
for match in matches:
    tour = match.find('h2', class_="cb-lv-grn-strip").text.strip()
    teams = match.find_all('h3', class_="cb-lv-scr-mtch-hdr")
    score = match.find('div', class_="cb-scr-wll-chvrn").text.strip()
 
    print(f"Tour: {tour}")
    print(f"Teams/Match: {[t.text.strip() for t in teams]}")
    print(f"Score: {score}\n")
