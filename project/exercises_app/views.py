from django.http import HttpResponse
from django.shortcuts import render

from exercises_app.models import Album, Band


def articles(request):
    articles = Aricles.object.filter(status='published')
    html = """
    <html>
    <body>
    """
    for article in articles:
        html += '<p>'
        html += f'{article.author}: <strong>{article.title}</strong>, {article.date_added}<br/>'
        html += '</p>'

    html += """
    </body>
    </html>
    """
    return HttpResponse(html)

def show_band(request, band_id):
    band = Band.objects.get(id=band_id)
    albums = Album.objects.filter(band=band)
    return render(request, 'bands.jinja2', context={'albums': albums, 'band': band})