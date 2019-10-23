# Generated by Django 2.1.1 on 2018-12-05 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iris', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='iris',
            name='petal_length',
            field=models.DecimalField(decimal_places=1, help_text='cm', max_digits=3, verbose_name='Petal Length'),
        ),
        migrations.AlterField(
            model_name='iris',
            name='petal_width',
            field=models.DecimalField(decimal_places=1, help_text='cm', max_digits=3, verbose_name='Petal Width'),
        ),
        migrations.AlterField(
            model_name='iris',
            name='sepal_length',
            field=models.DecimalField(decimal_places=1, help_text='cm', max_digits=3, verbose_name='Sepal Length'),
        ),
        migrations.AlterField(
            model_name='iris',
            name='sepal_width',
            field=models.DecimalField(decimal_places=1, help_text='cm', max_digits=3, verbose_name='Sepal Width'),
        ),
        migrations.AlterField(
            model_name='iris',
            name='species',
            field=models.CharField(choices=[('setosa', 'Iris Setosa'), ('virginica', 'Iris Virginica'), ('versicolor', 'Iris Versicolor')], help_text='choose one', max_length=30, verbose_name='Species'),
        ),
    ]