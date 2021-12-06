# Generated by Django 3.2.9 on 2021-12-06 22:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('message', models.JSONField(blank=True, null=True, verbose_name='содержимое сообщения (JSON)')),
                ('send_message', models.BooleanField(default=False)),
                ('create_at', models.IntegerField()),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'Groups User',
            },
        ),
    ]
