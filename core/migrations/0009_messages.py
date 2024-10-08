# Generated by Django 4.1.7 on 2023-10-26 18:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_forums'),
    ]

    operations = [
        migrations.CreateModel(
            name='Messages',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('message', models.CharField(max_length=1024, verbose_name='Message')),
                ('receiver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='receiverr', to='core.forums')),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='senderr', to='core.users')),
            ],
        ),
    ]
