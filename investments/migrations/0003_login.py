# Generated by Django 4.1.2 on 2022-10-18 23:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('investments', '0002_alter_registry_descricao'),
    ]

    operations = [
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, null=True)),
                ('sobrenome', models.CharField(max_length=100, null=True)),
                ('email', models.CharField(max_length=200, null=True)),
                ('senha', models.CharField(max_length=30, null=True)),
            ],
        ),
    ]