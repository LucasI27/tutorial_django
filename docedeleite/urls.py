from django.urls import path

from docedeleite.views import docedeleite, novodoce, leitecomgoiaba, aindatem, equipe

urlpatterns = [
    path('', docedeleite),
    path('novo-doce/', novodoce),
    path('leite-com-goiaba/', leitecomgoiaba),
    path('ainda-tem-doce/', aindatem),
    path('equipe/', equipe)
]
