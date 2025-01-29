from django.contrib import admin
from django.urls import path
from . import views 

urlpatterns = [
    path('home/', views.index, name='home'),
    path('logout/', views.Logout, name='logout'),
    path('livro_list/<str:id_kategoria>', views.livro_list, name='livro_list'),
    path('add/', views.add_livro, name='add'),
    path('delete_livro/<str:pk>/<str:id_ktg>', views.delete_livro, name='delete_livro'),
    path('update_livro/<str:pk>', views.update_livro, name='update_livro'),

    # Urls Kategorai
    path('kategoria_livro/', views.Kategoria, name='kategoria_livro'),
    path('add_ktg/', views.add_kategoria, name='add_ktg'),
    path('update_ktg/<str:id_ktg>', views.updata_ktg, name='update_ktg'),
    path('delete_ktg/<str:id_ktg>', views.delete_ktg, name='delete_ktg'),

    # Urls Staff

    path('staff/', views.show_staff, name='staff'),
    path('detallu_staff/<str:id_staff>', views.detallu_staff, name='detallu_staff'),
    path('add_staff/', views.add_staff, name='add_staff'),
    path('update_staff/<str:id_staff>', views.update_staff, name='update_staff'),
    path('delete_staff/<str:id_staff>', views.delete_staff, name='delete_staff'),

# url Staff
    path('kliente/', views.show_kliente, name='kliente'),
    path('add_kliente/', views.add_kliente, name='add_kliente'),
    path('update_kliente/<str:id_kliente>', views.update_kliente, name='update_kliente'),
    path('delete_kliente/<str:id_kliente>', views.delete_kliente, name='delete_kliente'),

# empresta
    path('kliente-empresta/', views.show_empresta_base_kliente, name='kliente-empresta'),
    path('empresta/<str:id_kliente>', views.show_empresta, name='empresta'),
    path('add_empresta/', views.add_empresta, name='add_empresta'),
    path('update_empresta/<str:id_empresta>', views.update_empresta, name='update_empresta'),
    path('delete_empresta/<str:id_empresta>/<str:id_livro>/<str:id_kliente>', views.delete_empresta, name='delete_empresta'),
    path('update_estatus/<str:id_empresta>/<str:id_livro>/<str:id_kliente>', views.update_estatus, name='update_estatus'),
    path('kansela_status/<str:id_empresta>/<str:id_livro>/<str:id_kliente>', views.kansela_status, name='kansela_status'),

    path('chek-empresta/<str:id_kliente>', views.chek_empresta, name='chek-empresta'),


# autor
    path('autor_livro/', views.autor_livro, name='autor_livro'),
    path('add_autor/', views.add_autor, name='add_autor'),
    path('update_autor/<str:id_autor>', views.update_autor, name='update_autor'),
    path('delete_autor/<str:id_autor>', views.delete_autor, name='delete_autor'),
# editor
    path('editor_livro/', views.editor_livro, name='editor_livro'),
    path('add_editor/', views.add_editor, name='add_editor'),
    path('update_editor/<str:id_editor>', views.update_editor, name='update_editor'),
    path('delete_editor/<str:id_editor>', views.delete_editor, name='delete_editor'),
# mun
    path('mun/', views.mun, name='mun'),
    path('update_mun/<str:id_mun>', views.update_mun, name='update_mun'),
    path('delete_mun/<str:id_mun>', views.delete_mun, name='delete_mun'),


# url 
    path('origin/', views.origin, name='origin'),
# usrl suku
    path('suku/', views.suku, name='suku'),
    path('add_suku/', views.add_suku, name='add_suku'),
    path('update_suku/<str:id_suku>', views.update_suku, name='update_suku'),
    path('delete_suku/<str:id_suku>', views.delete_suku, name='delete_suku'),
# url postu
    path('postu/', views.postu, name='postu'),
    path('add_postu/', views.add_postu, name='add_postu'),
    path('update_postu/<str:id_postu>', views.update_postu, name='update_postu'),
    path('delete_postu/<str:id_postu>', views.delete_postu, name='delete_postu'),


#dash_url
    path('detallu-livro-ktg/<str:id_ktg>', views.detallho_livro_ktg, name='detallu-livro-ktg'),
    path('emp-dev/<str:id_ktg>/<str:id_livro>', views.devolve_emp, name='emp-dev'),
    path('home-page/<int:year_id>', views.home_page, name='home-page'),



]
