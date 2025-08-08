from flask import Flask, jsonify
import requests
from bs4 import BeautifulSoup
 
app = Flask(__name__)
 
@app.route("/")
def live_scores():
    url = "https://www.cricbuzz.com/cricket-match/live-scores/recent-matches"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
 
    matches_data = []
    matches = soup.find_all('div', class_="cb-lv-main")
 
    for match in matches:
        tour_tag = match.find('h2', class_="cb-lv-grn-strip")
        tour = tour_tag.text.strip() if tour_tag else "N/A"
 
        teams = match.find_all('h3', class_="cb-lv-scr-mtch-hdr")
        teams_list = [t.text.strip() for t in teams]
 
        score_tag = match.find('div', class_="cb-scr-wll-chvrn")
        score = score_tag.text.strip() if score_tag else "N/A"
 
        matches_data.append({
            "tour": tour,
            "teams": teams_list,
            "score": score
        })
 
    return jsonify(matches_data)
 
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
