# Generated by Django 2.1.7 on 2020-06-02 02:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cd',
            name='word',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.SearchWord', verbose_name='アーティスト名'),
        ),
    ]