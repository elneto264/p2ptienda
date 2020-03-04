<<<<<<< HEAD
# Generated by Django 2.2.10 on 2020-03-04 15:18
=======
# Generated by Django 2.2.10 on 2020-03-04 15:13
>>>>>>> 91121a0198156801b0df7fff46094ed008c79612

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomCat', models.CharField(max_length=70)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=20, null=True)),
                ('precio', models.IntegerField(null=True)),
                ('descripcion', models.CharField(max_length=250, null=True)),
                ('producto_fields', models.ImageField(upload_to='static/img')),
                ('fkCategoria', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='p2pApp.Categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Carrito',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('cantidad', models.IntegerField(default=1)),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='p2pApp.Producto')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
