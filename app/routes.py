from app import app
from crawlerTVS import scrating

resultados = scrating.jogos_de_hoje(format='json')


@app.route('/')
def index():
    return resultados
