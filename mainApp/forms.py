from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import *


class FormLivro(forms.ModelForm):
    class Meta:
        model = Livro
        fields = '__all__'

        labels = {
            'naran_livro': 'Naran Livro',
            'id_autor': 'Autor do Livro',
            'no_isbn': 'Numeru ISBN',
            'id_editor': 'Editor Livro',
            'id_kategoria': 'Kategoria Livro',
        }
        widgets = {
            'data_tama': forms.DateInput(attrs={'type': 'date'}),  
            'naran_livro': forms.TextInput(attrs={'placeholder': 'Prense...'}),  
            'no_isbn': forms.TextInput(attrs={'placeholder': 'Prense...', 'type':'number'}),  
            'stock_livro': forms.TextInput(attrs={'placeholder': 'Prense...', 'type':'number'}),  
            
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_class = 'form-horizontal'


class FormCategoria(forms.ModelForm):
    class Meta:
        model = Kategoira
        fields = '__all__'

        widgets = {
                'data_tama': forms.TextInput(attrs={'placeholder': 'Prense...'}),  
            }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_class = 'form-horizontal'


class FormStaff(forms.ModelForm):
    # user_created = forms.ModelChoiceField(queryset=User.objects.all(),required=False)
    class Meta:
        model = Staff
        fields = ['naran_staff', 'data_moris','endereso','no_tlf','sexu', 'id_suku','estadu_sivil','foto']
        labels = {
            'id_suku': 'Suku',
        }

        # user_created = forms.ModelChoiceField(queryset=User.objects.all(),required=False)
    
        widgets = {
                'id_suku': forms.Select(attrs={'class': 'form-control', 'id':'select'}),  
                'data_moris': forms.DateInput(attrs={'type': 'date'}),  
                'naran_staff': forms.TextInput(attrs={'placeholder': 'Prense...'}),  
                'endereso': forms.TextInput(attrs={'placeholder': 'Prense...'}),  
                'no_tlf': forms.TextInput(attrs={'placeholder': 'Prense...'}),  
            }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_class = 'form-horizontal'


class FormCliente(forms.ModelForm):
    class Meta:
        model = Kliente
        fields =  '__all__'
        labels = {
            'id_suku':'Originalidade',
            'no_tlf':'Numeru Telfone'
        }

        widgets = {
                'id_suku': forms.Select(attrs={'class': 'form-control', 'id':'select'}),  
                'data_moris': forms.DateInput(attrs={'type': 'date'}),  
                'naran_kliente': forms.TextInput(attrs={'placeholder': 'Prense...'}),  
                'hela_fatin': forms.TextInput(attrs={'placeholder': 'Prense...'}),  
                'no_tlf': forms.TextInput(attrs={'placeholder': 'Prense...'}),  
            }
       


class FormEmpresta(forms.ModelForm):
    class Meta:
        model = Empresta
        fields = ('id_kliente','id_staff','data_empresta','data_devolve','id_livro')

        labels = {
            'id_kliente': 'Naran Kiente',
            'id_staff': 'Naran Estaff',
            'data_empresta': 'Data Empresta',
            'data_devolve': 'Data Devolve',
            'id_livro': 'Naran Livro',
        }

        widgets = {
                'data_empresta': forms.DateInput(attrs={'type': 'date'}),
                'data_devolve': forms.DateInput(attrs={'type': 'date'}),
            }
        

class FormAutor(forms.ModelForm):
    class Meta:
        model = AutorLivro
        fields = '__all__'

        widgets = {
                'espesialidade': forms.Textarea(attrs={'cols':'2','rows':'2', 'placeholder': 'Prense...'}),
                'nasionalidade': forms.TextInput(attrs={'placeholder': 'Prense...'}),
                'naran_autor': forms.TextInput(attrs={'placeholder': 'Prense...'}),
                'data_moris': forms.TextInput(attrs={'type':'date'}),
            }
        

class FormEditor(forms.ModelForm):
    class Meta:
        model = EditorLivro
        fields = '__all__'

        widgets = {
                'espesialidade': forms.Textarea(attrs={'cols':'2','rows':'2', 'placeholder': 'Prense...'}),
                'nasionalidade': forms.TextInput(attrs={'placeholder': 'Prense...'}),
                'naran_editor': forms.TextInput(attrs={'placeholder': 'Prense...'}),
                'data_moris': forms.TextInput(attrs={'type':'date'}),
            }
        
class FormMun(forms.ModelForm):
    class Meta:
        model = Municipio
        fields = '__all__'
        labels ={
            'mun':'Munisipiu'
        }
        widgets = {
            'mun': forms.TextInput(attrs={'placeholder': 'Prense...'})
        }
        

class FormPostu(forms.ModelForm):
    class Meta:
        model =Postu
        fields = '__all__'
        labels = {
            'id_mun': 'Munispiu'
        }

        widgets = {
            'naran_postu': forms.TextInput(attrs={'placeholder':'Prense...'})
        }

    
class FormSuku(forms.ModelForm):
    class Meta:
        model =Suku
        fields = '__all__'
        labels = {
            'id_postu': 'Postu admistrativo'
        }

        widgets = {
            'naran_suku': forms.TextInput(attrs={'placeholder':'Prense...'})
        }        
        