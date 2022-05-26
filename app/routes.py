from app import app
from crawlerTVS import scrating



@app.route('/')
def index():
    return scrating.jogos_de_hoje(format='json', cache=False)
