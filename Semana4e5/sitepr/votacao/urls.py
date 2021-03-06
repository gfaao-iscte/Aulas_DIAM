from django import path
from . import views

app_name = 'votacao'
urlpatterns = [
      # ex: votacao/
     path("", views.index, name='index'),
     # ex: votacao/1
     path("<int:questao_id>", views.detalhe, name='detalhe'),
     # ex: votacao/3/resultados
     path('<int:questao_id>/resultados', views.resultados, name='resultados'),
     # ex: votacao/5/voto
     path('<int:questao_id>/voto', views.voto, name='voto'),
     # ex: votacao/criarquestão
     path("criarquestao", views.criarquestao, name='criarquestao'),
     path("gravarquestao", views.gravarquestao, name='gravarquestao'),
     path('<int:questao_id>/criaropcao', views.criaropcao, name='criaropcao'),
     path('<int:questao_id>/gravaropcao', views.gravaropcao, name='gravaropcao'),

]