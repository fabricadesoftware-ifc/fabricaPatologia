# Generated by Django 2.2 on 2019-05-09 16:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('laudosMedvet', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bairromodel',
            old_name='cod_cidade',
            new_name='id_cidade',
        ),
        migrations.RenameField(
            model_name='cidademodel',
            old_name='regiao_estado',
            new_name='id_regiao_estado',
        ),
        migrations.RenameField(
            model_name='estadomodel',
            old_name='regiao_federal',
            new_name='id_regiao_federal',
        ),
        migrations.RenameField(
            model_name='regiaoestadomodel',
            old_name='estado',
            new_name='id_estado',
        ),
        migrations.RenameField(
            model_name='ruamodel',
            old_name='cod_bairro',
            new_name='id_bairro',
        ),
    ]