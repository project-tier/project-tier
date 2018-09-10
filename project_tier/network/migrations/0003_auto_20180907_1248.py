# Generated by Django 2.0.4 on 2018-09-07 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0002_auto_20180906_1829'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='person',
            options={'verbose_name': 'Person', 'verbose_name_plural': 'People'},
        ),
        migrations.AlterField(
            model_name='person',
            name='fellowship_year',
            field=models.CharField(blank=True, choices=[(2010, '2010–2011'), (2011, '2011–2012'), (2012, '2012–2013'), (2013, '2013–2014'), (2014, '2014–2015'), (2015, '2015–2016'), (2016, '2016–2017'), (2017, '2017–2018'), (2018, '2018–2019')], default='', max_length=20),
        ),
    ]