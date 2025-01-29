from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from mainApp.models import *
from django.db.models import Count

@login_required
def detallho_livro_ktg(request, id_ktg):
    ktg = get_object_or_404(Kategoira, id_kategoria=id_ktg)
    dadus_livro = Livro.objects.filter(id_kategoria__id_kategoria= ktg.id_kategoria)
    print(dadus_livro)
    name_ktg = ktg.kategoria
    context = {
        'title': 'Sistema Gestaun Dadus Bibleoteka',
        'sub_title': 'Dadus livro husi Kategoria ',
        'name_ktg': name_ktg,
        'data_livro': dadus_livro

    }
    return render(request, 'module/mod_dash/detallu_livro_ktg.html', context)

@login_required
def devolve_emp(request, id_ktg, id_livro):
    ktg = get_object_or_404(Kategoira, id_kategoria=id_ktg)
    name_ktg = ktg.kategoria

    emp = Empresta.objects.filter(status ='Devolve', id_livro=id_livro)

    # print(emp)
    context = {
        'title': 'Sistema Gestaun Dadus Bibleoteka',
        'sub_title': 'Dadus livro husi Kategoria',
        'emp_dv': emp,
        'name_ktg': name_ktg,
    }

    return render(request, 'module/mod_dash/detallu_dev_emp.html',context)



from django.db.models. functions import ExtractYear, ExtractMonth
from datetime import date, datetime
from calendar import month_name

@login_required
def home_page(request, year_id):
    total_book = Livro.objects.count()
    total_ktg = Kategoira.objects.count()
    total_autor = AutorLivro.objects.count()
    total_editor = EditorLivro.objects.count()
    count_by_ktg = Livro.objects.values('id_kategoria','id_kategoria__kategoria','id_kategoria').annotate(total=Count('id_kategoria'))


    total_ktg_emp = Empresta.objects.filter(status='Devolve').values('id_livro','id_livro__id_kategoria','id_livro__id_kategoria__kategoria','id_livro__naran_livro').annotate(total_emp=Count('id_livro__id_kategoria'))


    unique_years = Empresta.objects.annotate(year=ExtractYear('data_empresta')).values_list('year', flat=True).distinct().order_by('year')
    # print(unique_years)


    result = (
        Empresta.objects.filter(data_empresta__year=year_id)   # Extract the month from the date field
        .values('id_livro__naran_livro')  # Group by month
        .annotate(count=Count('id_livro'))
    )
    
    total_count = sum(item['count'] for item in result)

    formatted_result = [
        {
         'naran_livro': item['id_livro__naran_livro'],
         'total': item['count'],
         'percentage': (item['count'] / total_count) * 100  if total_count > 0 else 0,
        }
        
        for item in result
    ]
    tinan = date(year_id, 1,1)
    data = tinan.year
    # print(data)
    context = {
        'title': 'Sistema Gestaun Dadus Bibleoteka',
        'total_livro': total_book,
        'total_ktg': total_ktg,
        'total_autor': total_autor,
        'total_editor': total_editor,
        'count_by_ktg': count_by_ktg,
        'count_emp': total_ktg_emp,
        'year_emp': unique_years,
        'fulan': formatted_result,
        'tinan': data,
    }
    print(formatted_result)
    return render(request, 'module/mod_dash/home.html', context)