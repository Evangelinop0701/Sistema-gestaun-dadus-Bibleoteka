# Generated by Django 5.1.3 on 2024-12-07 13:32

import django.core.validators
import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AutorLivro',
            fields=[
                ('id_autor', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('naran_autor', models.CharField(max_length=225)),
                ('sexu', models.CharField(choices=[('Mane', 'Mane'), ('Feto', 'Feto')], max_length=5)),
                ('data_moris', models.DateField()),
                ('nasionalidade', models.CharField(max_length=200)),
                ('espesialidade', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='EditorLivro',
            fields=[
                ('id_editor', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('naran_editor', models.CharField(max_length=225)),
                ('sexu', models.CharField(choices=[('Mane', 'Mane'), ('Feto', 'Feto')], max_length=4)),
                ('data_moris', models.DateField()),
                ('nasionalidade', models.CharField(max_length=200)),
                ('espesialidade', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Kategoira',
            fields=[
                ('id_kategoria', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('kategoria', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Kliente',
            fields=[
                ('id_kliente', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('naran_kliente', models.CharField(max_length=225)),
                ('sexu', models.CharField(choices=[('Mane', 'Mane'), ('Feto', 'Feto')], max_length=4)),
                ('data_moris', models.DateField()),
                ('hela_fatin', models.CharField(max_length=225)),
                ('estadu_sivil', models.CharField(choices=[('Solteiro', 'Solteiro'), ('Kassadu', 'Kassadu'), ('Diborsiadu', 'Diborsiadu'), ('Barlakeadu', 'Barlakeadu')], max_length=15)),
                ('no_tlf', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Municipio',
            fields=[
                ('id_mun', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('mun', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Livro',
            fields=[
                ('id_livro', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('naran_livro', models.CharField(max_length=225)),
                ('stock_livro', models.IntegerField()),
                ('no_isbn', models.CharField(max_length=225)),
                ('data_tama', models.DateField()),
                ('tinan_publikasaun', models.IntegerField(choices=[(1900, 1900), (1901, 1901), (1902, 1902), (1903, 1903), (1904, 1904), (1905, 1905), (1906, 1906), (1907, 1907), (1908, 1908), (1909, 1909), (1910, 1910), (1911, 1911), (1912, 1912), (1913, 1913), (1914, 1914), (1915, 1915), (1916, 1916), (1917, 1917), (1918, 1918), (1919, 1919), (1920, 1920), (1921, 1921), (1922, 1922), (1923, 1923), (1924, 1924), (1925, 1925), (1926, 1926), (1927, 1927), (1928, 1928), (1929, 1929), (1930, 1930), (1931, 1931), (1932, 1932), (1933, 1933), (1934, 1934), (1935, 1935), (1936, 1936), (1937, 1937), (1938, 1938), (1939, 1939), (1940, 1940), (1941, 1941), (1942, 1942), (1943, 1943), (1944, 1944), (1945, 1945), (1946, 1946), (1947, 1947), (1948, 1948), (1949, 1949), (1950, 1950), (1951, 1951), (1952, 1952), (1953, 1953), (1954, 1954), (1955, 1955), (1956, 1956), (1957, 1957), (1958, 1958), (1959, 1959), (1960, 1960), (1961, 1961), (1962, 1962), (1963, 1963), (1964, 1964), (1965, 1965), (1966, 1966), (1967, 1967), (1968, 1968), (1969, 1969), (1970, 1970), (1971, 1971), (1972, 1972), (1973, 1973), (1974, 1974), (1975, 1975), (1976, 1976), (1977, 1977), (1978, 1978), (1979, 1979), (1980, 1980), (1981, 1981), (1982, 1982), (1983, 1983), (1984, 1984), (1985, 1985), (1986, 1986), (1987, 1987), (1988, 1988), (1989, 1989), (1990, 1990), (1991, 1991), (1992, 1992), (1993, 1993), (1994, 1994), (1995, 1995), (1996, 1996), (1997, 1997), (1998, 1998), (1999, 1999), (2000, 2000), (2001, 2001), (2002, 2002), (2003, 2003), (2004, 2004), (2005, 2005), (2006, 2006), (2007, 2007), (2008, 2008), (2009, 2009), (2010, 2010), (2011, 2011), (2012, 2012), (2013, 2013), (2014, 2014), (2015, 2015), (2016, 2016), (2017, 2017), (2018, 2018), (2019, 2019), (2020, 2020), (2021, 2021), (2022, 2022), (2023, 2023), (2024, 2024)])),
                ('id_autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='autor_livro', to='mainApp.autorlivro')),
                ('id_editor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='editor_livro', to='mainApp.editorlivro')),
                ('id_kategoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='kategorias_livro', to='mainApp.kategoira')),
            ],
        ),
        migrations.CreateModel(
            name='Postu',
            fields=[
                ('id_postu', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('naran_postu', models.CharField(max_length=100)),
                ('id_mun', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='postus', to='mainApp.municipio')),
            ],
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id_staff', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('naran_staff', models.CharField(blank=True, max_length=225, null=True)),
                ('sexu', models.CharField(blank=True, choices=[('Mane', 'Mane'), ('Feto', 'Feto')], max_length=4, null=True)),
                ('data_moris', models.DateField(blank=True, null=True)),
                ('endereso', models.CharField(blank=True, max_length=225, null=True)),
                ('no_tlf', models.CharField(blank=True, max_length=20, null=True)),
                ('estadu_sivil', models.CharField(blank=True, choices=[('Solteiro', 'Solteiro'), ('Kassadu', 'Kassadu'), ('Diborsiadu', 'Diborsiadu'), ('Barlakeadu', 'Barlakeadu')], default='', max_length=15, null=True)),
                ('foto', models.ImageField(blank=True, default='default.png', null=True, upload_to='foto_staff/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['png', 'jpg', 'jpeg'])])),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Empresta',
            fields=[
                ('id_empresta', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('data_empresta', models.DateField()),
                ('data_devolve', models.DateField()),
                ('loron_tarde', models.IntegerField(blank=True, null=True)),
                ('multa', models.FloatField(blank=True, null=True)),
                ('status', models.CharField(blank=True, choices=[('Empresta', 'Empresta'), ('Devolve', 'Devolve'), ('Tarde', 'Tarde')], default='Empresta', max_length=20, null=True)),
                ('id_kliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='kliente_empresta', to='mainApp.kliente')),
                ('id_livro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='empresta', to='mainApp.livro')),
                ('id_staff', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='staff_responsavel', to='mainApp.staff')),
            ],
        ),
        migrations.CreateModel(
            name='Suku',
            fields=[
                ('id_suku', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('naran_suku', models.CharField(max_length=50)),
                ('id_postu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sukus', to='mainApp.postu')),
            ],
        ),
        migrations.AddField(
            model_name='staff',
            name='id_suku',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='staff', to='mainApp.suku'),
        ),
        migrations.AddField(
            model_name='kliente',
            name='id_suku',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='kliente_suku', to='mainApp.suku'),
        ),
    ]
