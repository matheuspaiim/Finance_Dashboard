from django.db import migrations, models
from django import forms


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=255, null=True)),
                ('selecao', models.CharField(max_length=30, null=True)),
                ('data_entrada', models.DateTimeField(auto_now_add=True, null=True)),
                ('quantia', models.FloatField()),
            ],
        ),
    ]
