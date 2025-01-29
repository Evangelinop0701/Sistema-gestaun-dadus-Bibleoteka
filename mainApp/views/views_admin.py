from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout,authenticate
from mainApp.forms import *  # Explicitly import the form
from mainApp.models import * # Explicitly import the Livro model
from django.contrib import messages
import os
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.db.models import Count
import json
from django.conf import settings
from django.http import JsonResponse

# Create your views here.
def chek_login(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=uname, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, "Login ho susessu..!")
            return redirect('home')
        else:
            messages.success(request,"Username ou Password la los...!")

    return render(request, 'auth/login.html')

@login_required
def Logout(request):
    logout(request)
    messages.success(request, "Logout successful!")
    return render(request, 'auth/logout.html')


from django.db.models. functions import ExtractYear, ExtractMonth
from datetime import date, datetime
from calendar import month_name

@login_required
def index(request):
    # Count totals for models
    total_book = Livro.objects.count()
    total_ktg = Kategoira.objects.count()
    total_autor = AutorLivro.objects.count()
    total_editor = EditorLivro.objects.count()

    # Count books by category
    count_by_ktg = Livro.objects.values('id_kategoria', 'id_kategoria__kategoria').annotate(total=Count('id_kategoria'))

    # Count categories with returned books (status='Devolve')
    total_ktg_emp = Empresta.objects.filter(status='Devolve').values(
        'id_livro', 
        'id_livro__id_kategoria', 
        'id_livro__id_kategoria__kategoria', 
        'id_livro__naran_livro'
    ).annotate(total_emp=Count('id_livro'))


    
    ktg_devolve = []

    lv = Livro.objects.all()
    for l in lv:
        emp = Empresta.objects.filter(id_livro=l.id_livro, status='Devolve').count()
        ktg_devolve.append({
            'naran_ktg': l.naran_livro,
            'total': emp
        })

        
    
    # print(ktg_devolve)







    # Get distinct years from 'data_empresta'
    unique_years = Empresta.objects.annotate(
        year=ExtractYear('data_empresta')
    ).values_list('year', flat=True).distinct().order_by('year')

    # Get the current year and filter data for this year
    current_year = date.today().year
    result = Empresta.objects.filter(data_empresta__year=current_year).values(
        'id_livro__naran_livro'
    ).annotate(count=Count('id_livro')).order_by('-count')


    # Calculate the total count of borrowed books for the year
    total_count = sum(item['count'] for item in result)

    # Format the result with percentages
    formatted_result = [
        {
            'naran_livro': item['id_livro__naran_livro'],
            'total': item['count'],
            'percentage': round((item['count'] / total_count) * 100, 2) if total_count > 0 else 0,
        }
        for item in result
    ]
    # print(formatted_result)

    

    json_file_path = os.path.join(settings.BASE_DIR, 'json_files', 'bar_chart_data.json')
    if not os.path.exists(os.path.dirname(json_file_path)):
        os.makedirs(os.path.dirname(json_file_path))

    with open(json_file_path, 'w') as json_file:
        json.dump(formatted_result, json_file, indent=4)

    


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
        'current_date': current_year,
    }
    return render(request, 'home.html', context)

# ====================================================== Model Livro============================
@login_required
def livro_list(request, id_kategoria):  
    dados_livro = Livro.objects.all().filter(id_kategoria=id_kategoria)

    context = {
        'title': 'Dados Livro',
        'sub_title': 'Dadus Livro',
        'livros': dados_livro,
        'id_ktg': id_kategoria  
    }
    return render(request, 'module/mod_livro/v_livro.html', context)
@login_required
def add_livro(request):  
    if request.method == 'POST':
        form = FormLivro(request.POST)  
        if form.is_valid():
            id_kategoria = request.POST.get('id_kategoria')
            form.save()
            messages.success(request, "Aumenta dados ho sucessu..!")
            return redirect('livro_list',id_kategoria)  
    else:
        form = FormLivro()  

    context = {
        'title': 'Aumenta Dadus Livro',
        'sub_title': 'Aumenta Dadu Livro',
        'form': form,
    }
    return render(request, 'module/mod_livro/add_livro.html', context)

@login_required
def delete_livro(request, pk, id_ktg):
	delete_it = Livro.objects.get(id_livro=pk)
	delete_it.delete()
	messages.success(request, "Hamos dados ho sucessu..!")
	return redirect('livro_list', id_ktg)
@login_required
def update_livro(request, pk): 
    livro = get_object_or_404(Livro, id_livro=pk) 
    if request.method == 'POST':
        form = FormLivro(request.POST, instance=livro) 
        if form.is_valid():
            id_kategoria = request.POST.get('id_kategoria')
            form.save()  
            messages.success(request, "Hadia dados ho sucessu..!")
            return redirect('livro_list', id_kategoria)  
    else:
        form = FormLivro(instance=livro)  

    context = {
        'title': 'Update dadus Livro',
        'sub_title': 'Hadia dadus Livro',
        'form': form,
    }
    return render(request, 'module/mod_livro/update_livro.html', context)





# ========================MOdel Kategorai=============

@login_required
def Kategoria(request):
    ktg = Kategoira.objects.all()
    autor = AutorLivro.objects.count()
    edior = EditorLivro.objects.count()
    context = {
        'title': 'Kategorai Livro',
        'sub_title': 'Kategoria Livros',
        'ktg': ktg,
        'total_autor': autor,
        'total_edito': edior,
        
    }

    return render(request, 'module/mod_kategoria/kategoria.html', context)

@login_required
def add_kategoria(request):
    if request.method == 'POST':
        form = FormCategoria(request.POST)  
        if form.is_valid():
            form.save()
            messages.success(request, "Aumenta dados ho sucessu..!")
            return redirect('kategoria_livro')  
    else:
        form = FormCategoria()  

        context = {
            'title': 'Aumenta Dadus Kategoria',
            'sub_title': 'Aumenta Dadu Kategoria',
            'form': form,
        }
    return render(request, 'module/mod_kategoria/add_ktg.html', context)
@login_required
def updata_ktg(request, id_ktg):
     ktg = get_object_or_404(Kategoira, id_kategoria=id_ktg) 
     if request.method == 'POST':
        form = FormCategoria(request.POST, instance=ktg) 
        if form.is_valid():
            form.save()  
            messages.success(request, "Hadia dados ho sucessu..!")
            return redirect('kategoria_livro')  
     else:
        form = FormCategoria(instance=ktg)  

     context = {
        'title': 'Update dadus Kategoria',
        'sub_title': 'Hadia dadus Kategoria',
        'form': form,
     }
     return render(request, 'module/mod_kategoria/update_ktg.html', context)
@login_required
def delete_ktg(request, id_ktg):
	delete_it = Kategoira.objects.get(id_kategoria=id_ktg)
	delete_it.delete()
	messages.success(request, "Hamos dados ho sucessu..!")
	return redirect('kategoria_livro')


# =========================== Mod Staff ======================

@login_required
def show_staff(request):
    staff = Staff.objects.select_related('id_suku').all()
    context = {
        'title': 'Dados Staff',
        'sub_title': 'Dadus Staff',
        'data': staff,
     }
    
    return render(request, 'module/mod_staff/staff.html',context)

@login_required
def detallu_staff(request, id_staff):
    staff = get_object_or_404(Staff, id_staff=id_staff)
    context = {
        'title': 'Detallu Staff',
        'sub_title': 'Detallu Staff',
        'detallu': staff
     }
    
    return render(request, 'module/mod_staff/detallu_staff.html', context)
@login_required
def add_staff(request):
    form = FormStaff(request.POST, request.FILES)  
    if form.is_valid():
            messages.success(request, "Aumenta dados ho sucessu..!")
            form.save()
            return redirect('staff')  
    else:
        form = FormStaff()
    context = {
            'title': 'Add dados Staff',
            'sub_title': 'Aumenta dados Staff',
            'form': form
    }
    return render(request, 'module/mod_staff/add_staff.html', context)
@login_required
def delete_staff(request, id_staff,):
    delete_it = get_object_or_404(Staff, id_staff=id_staff)

    if delete_it.foto and os.path.isfile(delete_it.foto.path):
        os.remove(delete_it.foto.path)
    delete_it.delete()
    messages.success(request, "Hamos dados ho sucessu..!")
    return redirect('staff')


@login_required
def update_staff(request, id_staff):
    staff = get_object_or_404(Staff, id_staff=id_staff)
    if request.method == 'POST':
        form = FormStaff(request.POST, request.FILES, instance=staff)
        if 'foto' in request.FILES:
            if staff.foto and os.path.isfile(staff.foto.path):
                os.remove(staff.foto.path)

        if form.is_valid():
            form.save()
        messages.success(request, "Hadia dados ho Sucessu...!")
        if request.user.groups.name == "admin":
            return redirect('staff')
        else:
             return redirect('home')
    else:
        form = FormStaff(instance=staff)

    context = {
        'title': 'Update Staff Data',
        'sub_title': 'Hadia dados Staff',
        'form': form,
        'data': staff,
    }

    return render(request, 'module/mod_staff/update_staff.html', context)


# =================================Kleinte view===============================
@login_required
def show_kliente(request):
    kliente = Kliente.objects.select_related('id_suku').all()
    context = {
        'title': 'Dadus Kliente',
        'sub_title': 'Dadus Kliente',
        'data': kliente,
     }
    
    return render(request, 'module/mod_kliente/kliente.html',context)

@login_required
def add_kliente(request):
    if request.method == 'POST':
        form = FormCliente(request.POST)  
        if form.is_valid():
            messages.success(request, "Aumenta dados ho sucessu..!")
            form.save()
            return redirect('kliente')  
    else:
        form = FormCliente() 
    context = {
        'title': 'Hadia dadus Kliente',
        'sub_title': 'Hadia dadus Kliente',
        'form': form,
     }
    
    return render(request, 'module/mod_kliente/add_kliente.html',context)

@login_required
def update_kliente(request, id_kliente):
    kliente = get_object_or_404(Kliente, id_kliente=id_kliente)
    if request.method == 'POST':
        form = FormCliente(request.POST, instance=kliente )
        if form.is_valid():
            form.save()
        messages.success(request, "Hadia dados ho Successu...!")
        return redirect('kliente')
    else:
        form = FormCliente(instance=kliente)

    context = {
        'title': 'Update Staff Data',
        'sub_title': 'Hadia dados Staff',
        'form': form,
        'data': kliente,
    }

    return render(request, 'module/mod_kliente/update_kliente.html',context)

@login_required
def delete_kliente(request, id_kliente,):
    delete_it = get_object_or_404(Kliente, id_kliente=id_kliente)
    delete_it.delete()
    messages.success(request, "Hamos dados ho sucessu..!")
    return redirect('kliente')


# =======================Empresta========================
@login_required
def show_empresta_base_kliente(request):

    kliente_data = []
    kliente = Kliente.objects.all()
    for kl in kliente:
        emp_kliente = Empresta.objects.filter(id_kliente=kl.id_kliente).count()
        kliente_data.append({
            'id_kliente': kl.id_kliente,
            'naran_kliente': kl.naran_kliente,
            'total_emp': emp_kliente
        })



    data = {
        'title': 'Dadus Kliente Empresta',
        'sub_title': 'Dadus Empresta',
        'data': kliente_data
    }
    return render(request, 'module/mod_empresta/kliente_emp.html',data)

@login_required
def show_empresta(request, id_kliente):
    empresta = Empresta.objects.filter(id_kliente=id_kliente)
    kli = get_object_or_404(Kliente, id_kliente=id_kliente)
    kli_name = kli.naran_kliente
    data_now = timezone.now().date()
    for emp in empresta:
        if emp.status == 'Devolve':
            obj = get_object_or_404(Empresta, id_empresta=emp.id_empresta)
            obj.status = 'Devolve'
            obj.save()
        elif emp.status == 'Empresta':
            if emp.data_devolve > data_now:
                obj = get_object_or_404(Empresta, id_empresta=emp.id_empresta)
                obj.loron_tarde = None
                obj.multa = None
                obj.status = 'Empresta'
                obj.save()
            elif emp.data_devolve == data_now:
                obj = get_object_or_404(Empresta, id_empresta=emp.id_empresta)
                obj.loron_tarde = None
                obj.multa = None
                obj.status = 'Empresta'
                obj.save()
            else:
                day1 = emp.data_devolve  # No need for strptime, it's already a date object
                day2 = data_now
                difference = day2 - day1
                tarde = difference.days
                obj = get_object_or_404(Empresta, id_empresta=emp.id_empresta)
                obj.loron_tarde = tarde
                obj.multa = tarde * 0.25
                obj.status = 'Tarde'
                obj.save()
    context = {
        'title': 'Dadus Empresta',
        'sub_title': 'Dadus Empresta',
        'data': empresta,
        'kl_name': kli_name
    }
    
    return render(request, 'module/mod_empresta/empresta.html',context)

@login_required
def chek_empresta(request, id_kliente):
    cliente = get_object_or_404(Kliente, id_kliente=id_kliente)
    detallu_emp = Empresta.objects.filter(id_kliente=id_kliente)
    context = {
         'title': 'Detallu Empresta husi Kliente',
         'sub_title': 'Dadus Empresta',
         'det_emp' : detallu_emp,
         'client_name': cliente.naran_kliente
    }

    return render(request, 'module/mod_empresta/detallu_emp.html', context)



@login_required
def add_empresta(request):
    if request.method == 'POST':

        id_livro = request.POST.get('id_livro')
        livro = get_object_or_404(Livro, id_livro=id_livro)
        id_kl = request.POST.get('id_kliente')
        if livro.stock_livro > 0 :
            stok_menus = livro.stock_livro - 1
            livro.stock_livro = stok_menus
            livro.save()
            form = FormEmpresta(request.POST)
            if form.is_valid():
                messages.success(request, "Aumenta dados ho sucessu..!")
                form.save()
                return redirect('empresta',id_kl)
        else:
            messages.success(request, "Stock Livro hotu.....!")
            form =FormEmpresta()
    else:
        form =FormEmpresta()

    context = {
        'title': 'Aumenta dados Empresta',
        'sub_title': 'Aumenta dados Empresta',
        'form': form,
    }
    
    return render(request, 'module/mod_empresta/add_emp.html',context)
@login_required
def update_empresta(request, id_empresta):
    emp = get_object_or_404(Empresta, id_empresta=id_empresta)
    if request.method == 'POST':
        form = FormEmpresta(request.POST, instance=emp)
        id_kl = request.POST.get('id_kliente')
        if form.is_valid():
            data_now = timezone.now().date()
            data_devolve = form.cleaned_data.get('data_devolve')  # Use `cleaned_data` to get validated form data
            if data_devolve and data_devolve > data_now:
                emp.status = 'Empresta'
                emp.multa = 0
                emp.loron_tarde = 0
                emp.save()
            form.save()  # Save the form to update the model instance
            messages.success(request, "Hadia dados ho sucessu..!")
            return redirect('empresta',id_kl)
    else:
        form =FormEmpresta(instance=emp)

    context = {
        'title': 'Hadia dados Empresta',
        'sub_title': 'Hadia dados Empresta',
        'form': form,
    }
    
    return render(request, 'module/mod_empresta/update_empresta.html',context)

@login_required
def delete_empresta(request, id_empresta, id_livro, id_kliente):
    delete_it = get_object_or_404(Empresta, id_empresta=id_empresta)
    if delete_it.status == "Empresta" or  delete_it.status == "Tarde":
        obj_livro = get_object_or_404(Livro, id_livro=id_livro)
        obj_livro.stock_livro = obj_livro.stock_livro + 1
        obj_livro.save()

    delete_it.delete()
    messages.success(request, "Hamos dados ho sucessu..!")
    return redirect('empresta', id_kliente)

@login_required
def update_estatus(request, id_empresta,id_livro, id_kliente):
    obj = get_object_or_404(Empresta, id_empresta=id_empresta)
    obj.status = 'Devolve'
    obj.save()
    obj_livro = get_object_or_404(Livro, id_livro=id_livro)
    # print(obj_livro)
    obj_livro.stock_livro = obj_livro.stock_livro + 1
    obj_livro.save()
    messages.success(request, "Livro devolve Ona..!")
    return redirect('empresta', id_kliente)


@login_required
def kansela_status(request, id_empresta, id_livro, id_kliente):
    obj = get_object_or_404(Empresta, id_empresta=id_empresta)
    if obj.data_devolve > timezone.now().date():
        obj.status = 'Empresta'
        obj.save()
        obj_livro = get_object_or_404(Livro, id_livro=id_livro)
        obj_livro.stock_livro = obj_livro.stock_livro - 1
        obj_livro.save()
    elif obj.data_devolve == timezone.now().date():
        obj.status = 'Empresta'
        obj.save()
        obj_livro = get_object_or_404(Livro, id_livro=id_livro)
        obj_livro.stock_livro = obj_livro.stock_livro - 1
        obj_livro.save()
    else:
        obj.status = 'Tarde'
        obj.save()
    messages.success(request, "Ita Kansela Ona Livro..!")
    return redirect('empresta', id_kliente)


# ========================View autor===================================

@login_required
def autor_livro(request):
    autor = AutorLivro.objects.all()
    context = {
        'title': 'Autor ba Livor',
        'sub_title': 'Autor ba Livro',
        'autor': autor
    }

    return render(request, 'module/mod_autor/autor.html', context)
    
@login_required
def add_autor(request):
    if request.method == 'POST':
        form = FormAutor(request.POST)
        if form.is_valid():
            messages.success(request,'Aumenta dadus ho Susesu')
            form.save()
        return redirect('autor_livro')
    else:
        form = FormAutor()
        context = {
            'title': 'Aumenta dados Autor',
            'sub_title': 'Aumenta dados Autor',
            'form': form
        }
    return render(request, 'module/mod_autor/add_autor.html', context)

@login_required
def update_autor(request, id_autor):
    autor = get_object_or_404(AutorLivro, id_autor=id_autor)
    if request.method == 'POST':
        form = FormAutor(request.POST, instance=autor)
        if form.is_valid():
            messages.success(request,'Hadia dadus ho Susesu.....!')
            form.save()
        return redirect('autor_livro')
    else:
        form = FormAutor(instance=autor)
        context = {
            'title': 'Hadia dados Autor',
            'sub_title': 'Hadia dados Autor',
            'form': form
        }
    return render(request, 'module/mod_autor/update_autor.html', context)
@login_required
def delete_autor(request, id_autor):
    autor = get_object_or_404(AutorLivro, id_autor=id_autor)
    autor.delete()
    messages.success(request, 'Hamos dados ho susesu')
    return redirect('autor_livro')


# ===========================view editor========================

@login_required
def editor_livro(request):
    editor = EditorLivro.objects.all()
    context = {
        'title': 'Dados Editor',
        'sub_title': 'Dados Editor',
        'editor' : editor
    }

    return render(request, 'module/mod_editor/editor.html', context)

@login_required
def add_editor(request):
    if request.method == 'POST':
        form = FormEditor(request.POST)
        if form.is_valid():
            messages.success(request,'Aumenta dadus ho Susesu')
            form.save()
        return redirect('editor_livro')
    else:
        form = FormEditor()
        context = {
            'title': 'Aumenta dados Editor',
            'sub_title': 'Aumenta dados Editor',
            'form': form,
            'btn' : 'Rai dadus'
        }
    return render(request, 'module/mod_editor/add_editor.html', context)
@login_required
def update_editor(request, id_editor):
    editor = get_object_or_404(EditorLivro, id_editor=id_editor)
    if request.method == 'POST':
        form = FormEditor(request.POST, instance=editor)
        if form.is_valid():
            messages.success(request,'Hadia dadus ho Susesu..!')
            form.save()
        return redirect('editor_livro')
    else:
        form = FormEditor(instance=editor)
        context = {
            'title': 'Aumenta dados Editor',
            'sub_title': 'Aumenta dados Editor',
            'form': form,
            'btn': 'update'
        }
    return render(request, 'module/mod_editor/add_editor.html', context)
@login_required
def delete_editor(request, id_editor):
    editor = get_object_or_404(EditorLivro, id_editor=id_editor)
    editor.delete()
    messages.success(request, 'Hamos dados ho Susesu..!')
    return redirect('editor_livro')


# ==================== view mps ====================
@login_required
def mun(request):
    if request.method == 'POST':
        form = FormMun(request.POST)
        if form.is_valid():
            messages.success(request,'Aumenta dadus ho Susesu')
            form.save()
        return redirect('origin')
    else:
        form = FormMun()
        context = {
            'title': 'Origin',
            'sub_title': 'Munisipiu',
            'form': FormMun(),
            'title_form': 'Aumenta Munisipiu'
        }
    return render(request, 'module/origin/origin.html', context)
    
# ========
@login_required
def origin(request):
    mun = Municipio.objects.all()
    context = {
        'title': 'Origin',
        'sub_title': 'Munisipiu',
        'data':  mun,
        'form': FormMun(),
        'title_form': 'Aumenta Munisipiu',
        'btn':'Rai dadus'
    }
    return render(request, 'module/origin/origin.html', context)
@login_required
def update_mun(request, id_mun):
    mun = get_object_or_404(Municipio, id_mun=id_mun)
    if request.method == 'POST':
        form = FormMun(request.POST, instance=mun)
        if form.is_valid():
            messages.success(request,'Hadia dadus ho Susesu.....!')
            form.save()
        return redirect('origin')
    else:
        form = FormMun(instance=mun)
        mun2 = Municipio.objects.all()
        context = {
            'title': 'Update Munisipiu',
            'sub_title': 'Hadia dados munisipiu',
            'data':  mun2,
            'form': FormMun(instance=mun),
            'btn':'Update'
        }
    return render(request, 'module/mod_mun/update_mun.html', context)

@login_required
def delete_mun(request, id_mun):
    mun = get_object_or_404(Municipio, id_mun=id_mun)
    mun.delete()
    messages.success(request, 'Hamos dadus ho susessu...!')
    return redirect('origin')

@login_required
def postu(request):
    postu = Postu.objects.all()
    context ={
        'title': 'Origin',
        'sub_title': 'Postu Admistrativo',
        'title_form': 'Aumenta Munisipiu',
        'data' : postu
    }
    return render(request, 'module/mod_postu/postu.html', context)
@login_required
def add_postu(request):
    if request.method == 'POST':
        form = FormPostu(request.POST)
        if form.is_valid():
            messages.success(request, 'Aumenta dadus ho Susessu...!')
            form.save()
            return redirect('postu')
    context = {
        'title': 'Aumenta Postu admistrativo',
        'sub_title': 'Aumenta Postu Admistrativo',
        'form': FormPostu(),
        'btn': 'Rai dadus'
    }
    return render(request, 'module/mod_postu/add_postu.html', context)
@login_required
def update_postu(request, id_postu):
    postu = get_object_or_404(Postu, id_postu=id_postu)
    if request.method == 'POST':
        form = FormPostu(request.POST, instance=postu)
        if form.is_valid():
            messages.success(request, 'Hadia dadus ho Susessu...!')
            form.save()
            return redirect('postu')
    context = {
        'title': 'Hadia Postu admistrativo',
        'sub_title': 'Hadia Postu Admistrativo',
        'form': FormPostu(instance=postu),
        'btn': 'Update'
    }
    return render(request, 'module/mod_postu/add_postu.html', context)

@login_required
def delete_postu(request, id_postu):
    mun = get_object_or_404(Postu, id_postu=id_postu)
    mun.delete()
    messages.success(request, 'Hamos dadus ho susessu...!')
    return redirect('postu')



# =========================================

@login_required
def suku(request):
    data = Suku.objects.all()
    context = {
        'title': 'Dadus SUku',
        'sub_title': 'Dadus Suku',
        'data': data,
    }

    return render(request, 'module/mod_suku/suku.html', context)
@login_required
def add_suku(request):
    if request.method == 'POST':
        form = FormSuku(request.POST)
        if form.is_valid():
            messages.success(request, 'Aumenta dadus ho Susessu...!')
            form.save()
            return redirect('suku')
    context = {
        'title': 'Aumenta Suku',
        'sub_title': 'Aumenta Suku',
        'form': FormSuku(),
        'btn': 'Rai dadus'
    }
    return render(request, 'module/mod_suku/add_suku.html', context)
@login_required
def update_suku(request, id_suku):
    suku = get_object_or_404(Suku, id_suku=id_suku)
    if request.method == 'POST':
        form = FormSuku(request.POST, instance=suku)
        if form.is_valid():
            messages.success(request, 'Hadia dadus ho Susessu...!')
            form.save()
            return redirect('suku')
    context = {
        'title': 'Hadia Suku',
        'sub_title': 'Hadia Suku',
        'form': FormSuku(instance=suku),
        'btn': 'Update'
    }
    return render(request, 'module/mod_suku/add_suku.html', context)

@login_required
def delete_suku(request, id_suku):
    mun = get_object_or_404(Suku, id_suku=id_suku)
    mun.delete()
    messages.success(request, 'Hamos dadus ho susessu...!')
    return redirect('suku')

@login_required
def update_stock(request, id_livro):
    mun = get_object_or_404(Livro, id_livro=id_livro)