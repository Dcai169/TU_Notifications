from requests import get
from bs4 import BeautifulSoup

def find_team_updates():
    url = "https://www.firstinspires.org/resource-library/frc/competition-manual-qa-system"
    r = get(url)
    html = r.text
    soup = BeautifulSoup(html, "html.parser")
    all_a = soup.body.find_all('a') # SoupStrainer("a")
    for a in all_a:
        try:
            if "Team Update" in a.string:
                return a.contents
        except TypeError:
            return None