# Generated by Django 3.2.9 on 2021-12-07 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20211203_1608'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servico',
            name='icone',
            field=models.CharField(choices=[('lni-mobile', 'Mobile'), ('lni-rocket', 'Foguete'), ('lni-cog', 'Engrenagem'), ('lni-statis-up', 'Gráfico'), ('lni-users', 'Usuários'), ('lni-layers', 'Design')], max_length=13, verbose_name='Icone'),
        ),
    ]
