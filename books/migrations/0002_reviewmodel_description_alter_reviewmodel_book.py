# Generated by Django 4.2.3 on 2023-08-04 12:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reviewmodel',
            name='description',
            field=models.CharField(choices=[('INTERESTING', 'Interesting'), ('SWEET', 'Sweet'), ('BORING', 'Boring')], default='Interesting', max_length=11),
        ),
        migrations.AlterField(
            model_name='reviewmodel',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='books.book'),
        ),
    ]
