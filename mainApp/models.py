from django.db import models
from django.core.validators import FileExtensionValidator
from django.core.validators import MinValueValidator, MaxValueValidator
import datetime
import uuid
from django.contrib.auth.models import User
# Create your models here.


# class CustumeUser(AbstractUser):
#     phone_number = models.CharField(max_length=15, blank=True,null=True)
#     def __str__(self):
#         return self.username

class Municipio(models.Model):
    id_mun = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    mun = models.CharField(max_length=100)

    def __str__(self):
        return self.mun

# Table: Postu
class Postu(models.Model):
    id_postu = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    naran_postu = models.CharField(max_length=100)
    id_mun = models.ForeignKey(Municipio, related_name='postus', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.id_mun.mun}-{self.naran_postu}"
# Table: Suku
class Suku(models.Model):
    id_suku = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    naran_suku = models.CharField(max_length=50)
    id_postu = models.ForeignKey(Postu, related_name='sukus', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.id_postu.id_mun.mun}-{self.id_postu.naran_postu}-{self.naran_suku}"

class AutorLivro(models.Model):
    SEXO_CHOICES = [
        ('Mane', 'Mane'),
        ('Feto', 'Feto'),
    ]
    
    id_autor = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    naran_autor = models.CharField(max_length=225)
    sexu = models.CharField(max_length=5, choices=SEXO_CHOICES)  # increased to 5 to match 'Mane'
    data_moris = models.DateField()
    nasionalidade = models.CharField(max_length=200)
    espesialidade = models.TextField()

    def __str__(self):
        return self.naran_autor


class EditorLivro(models.Model):
    SEXO_CHOICES = [
        ('Mane', 'Mane'),
        ('Feto', 'Feto'),
]

    id_editor = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    naran_editor = models.CharField(max_length=225)
    sexu = models.CharField(max_length=4, choices=SEXO_CHOICES)
    data_moris = models.DateField()
    nasionalidade = models.CharField(max_length=200)
    espesialidade = models.TextField()

    def __str__(self):
        return self.naran_editor

class Kategoira(models.Model):
    id_kategoria = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    kategoria = models.CharField(max_length=50)

    def __str__ (self):
        return str(self.kategoria)

class Livro(models.Model):
    def year_choices():
        return [(r, r) for r in range(1900, datetime.datetime.now().year + 1)]
    
    # current_year = datetime.datetime.now().year

    id_livro = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    naran_livro = models.CharField(max_length=225)
    id_autor = models.ForeignKey(AutorLivro, related_name='autor_livro', on_delete=models.CASCADE)
    stock_livro = models.IntegerField()
    no_isbn = models.CharField(max_length=225)
    data_tama = models.DateField()
    # tinan_publikasaun = models.IntegerField(
    #     validators=[
    #         MinValueValidator(1800),  # Minimum year allowed
    #         MaxValueValidator(current_year),  # Maximum year allowed
    #     ]
    # )
    tinan_publikasaun = models.IntegerField(choices=year_choices())
    id_editor = models.ForeignKey(EditorLivro, related_name='editor_livro', on_delete=models.CASCADE)
    id_kategoria = models.ForeignKey(Kategoira, related_name='kategorias_livro', on_delete=models.CASCADE)

    def __str__(self):
       return self.naran_livro


class Staff(models.Model):
    SEXO_CHOICES = [
        ('Mane', 'Mane'),
        ('Feto', 'Feto'),
    ]

    STADU_CIVIL = [
        ('Solteiro', 'Solteiro'),
        ('Kassadu', 'Kassadu'),
        ('Diborsiadu', 'Diborsiadu'),
        ('Barlakeadu', 'Barlakeadu')
    ]

    id_staff = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    naran_staff = models.CharField(max_length=225, blank=True, null=True)
    sexu = models.CharField(max_length=4, choices=SEXO_CHOICES, blank=True, null=True)
    data_moris = models.DateField(blank=True, null=True)
    id_suku = models.ForeignKey(Suku, related_name='staff', on_delete=models.CASCADE, blank=True, null=True)
    endereso = models.CharField(max_length=225, blank=True, null=True)
    no_tlf = models.CharField(max_length=20, blank=True, null=True)
    estadu_sivil = models.CharField(max_length=15, default='', choices=STADU_CIVIL,blank=True, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null= True)
    foto = models.ImageField(
        upload_to='foto_staff/',
        validators=[FileExtensionValidator(allowed_extensions=['png', 'jpg', 'jpeg'])],
        null=True,
        blank=True,
        default='default.png'
    )
    def __str__(self):
        # return f"{self.user.username} Profile"
        return f"{self.naran_staff}"
    

class Kliente(models.Model):
    SEXO_CHOICES = [
        ('Mane', 'Mane'),
        ('Feto', 'Feto'),
]

    STADU_CIVIL = [
        ('Solteiro', 'Solteiro'),
        ('Kassadu', 'Kassadu'),
        ('Diborsiadu', 'Diborsiadu'),
        ('Barlakeadu', 'Barlakeadu')
]
    id_kliente = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    naran_kliente = models.CharField(max_length=225)
    sexu = models.CharField(max_length=4, choices=SEXO_CHOICES)
    data_moris = models.DateField()
    id_suku = models.ForeignKey(Suku, related_name='kliente_suku', on_delete=models.CASCADE)
    hela_fatin = models.CharField(max_length=225)
    estadu_sivil = models.CharField(max_length=15, choices=STADU_CIVIL)
    no_tlf = models.CharField(max_length=20)

    def __str__(self):
        return self.naran_kliente


class Empresta(models.Model):
    STATUS_EMP = [
        ('Empresta', 'Empresta'),
        ('Devolve', 'Devolve'),
        ('Tarde', 'Tarde'),
]
    id_empresta = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    id_kliente = models.ForeignKey('Kliente', related_name='kliente_empresta', on_delete=models.CASCADE)
    id_staff = models.ForeignKey('Staff', related_name='staff_responsavel', on_delete=models.CASCADE)  # Corrected spelling
    data_empresta = models.DateField()
    data_devolve = models.DateField()
    loron_tarde = models.IntegerField(null=True, blank=True)  # Ensure proper spacing around `=`
    multa = models.FloatField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_EMP, null=True, blank=True, default='Empresta')
    id_livro = models.ForeignKey('Livro', related_name='empresta', on_delete=models.CASCADE)

    def __str__(self):
        return f"Empresta({self.id_kliente})"
