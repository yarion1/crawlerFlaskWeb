from bs4 import BeautifulSoup
from urllib.request import urlopen
import json
import re
from dicttoxml import dicttoxml

_page = None


def get_html_page(cache):
    global _page

    if cache is False:
        _page = None
    if _page is None:
        html = urlopen('https://www.placardefutebol.com.br/')
        _page = BeautifulSoup(html, 'lxml')

    res = _page

    return res


def jogos_de_hoje(format='dict', cache=True):
    page = get_html_page(cache)
    titles = page.find_all('h3', class_='match-list_league-name')
    championships = page.find_all('div', class_='container content')
    del (titles[0])

    results = []

    for id, championship in enumerate(championships):
        matchs = championship.find_all('div', class_='row align-items-center content')

        for match in matchs:

            teams = match.find_all('div', class_='team-name')
            status = match.find('span', class_='status-name').text

            team_home = teams[0].text.strip()
            team_visitor = teams[1].text.strip()

            info = {
                'match': '{} x {}'.format(team_home, team_visitor),
                'status': status,
                'league': titles[id].text,
            }

            results.append(info)

    if format == 'json':
        return json.dumps(results)
    else:
        return results



