import requests
from bs4 import BeautifulSoup

USER_ID = "1153590"
URL = f"https://www.beecrowd.com.br/judge/en/profile/{USER_ID}"

def fetch_stats():
    response = requests.get(URL)
    soup = BeautifulSoup(response.text, "html.parser")

    # Ranking
    rank = soup.select_one("div.profile-rank-position span.profile-rank-text").text.strip()

    # Solved problems
    solved = soup.select_one("div.profile-solved-number span").text.strip()

    # Streak
    streak = soup.select_one("div.profile-solved-streak span.profile-solved-streak-text").text.strip()

    return rank, solved, streak

def generate_svg(rank, solved, streak):
    svg = f"""
<svg xmlns="http://www.w3.org/2000/svg" width="400" height="80">
  <rect width="100%" height="100%" fill="#0f172a" rx="10"/>
  <text x="20" y="30" fill="#38bdf8" font-size="18" font-family="Arial">🐝 Beecrowd Stats</text>
  <text x="20" y="55" fill="#ffffff" font-size="14">Problems Solved: {solved} | 🔥 Streak: {streak} | 🏆 Rank: {rank}</text>
</svg>
"""
    with open("beecrowd-badge.svg", "w") as f:
        f.write(svg)

if __name__ == "__main__":
    rank, solved, streak = fetch_stats()
    generate_svg(rank, solved, streak)
