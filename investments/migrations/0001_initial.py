# Generated by Django 4.1.1 on 2022-09-23 20:38

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Registry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=255, null=True)),
                ('escolha', models.CharField(choices=[('expense', 'Despesa'), ('revenue', 'Receita')], max_length=50, null=True)),
                ('data_entrada', models.DateTimeField(default=django.utils.timezone.now, null=True)),
                ('quantia', models.FloatField()),
                ('categoria', models.CharField(choices=[('Comida e Bebida', 'Comida e Bebida'), ('Compras', 'Compras'), ('Habilitacao', 'Habilitacao'), ('Transporte', 'Transporte'), ('Veiculo', 'Veiculo'), ('Vida e Entretenimento', 'Vida e Entretenimento'), ('Comunicacao, PC', 'Comunicacao, PC'), ('Despesas Financeiras', 'Despesas Financeiras'), ('Investimentos', 'Investimentos'), ('Renda', 'Renda'), ('Outro', 'Outro')], max_length=200, null=True)),
            ],
        ),
    ]
