# Generated by Django 4.2.16 on 2024-09-28 20:25

from django.db import migrations
import log.crypto


class Migration(migrations.Migration):

    dependencies = [
        ('log', '0003_alter_event_bio_alter_event_event_alter_event_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='bio',
            field=log.crypto.EncryptedField(null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='name',
            field=log.crypto.EncryptedField(null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='password',
            field=log.crypto.EncryptedField(null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='prompt',
            field=log.crypto.EncryptedField(null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='response',
            field=log.crypto.EncryptedField(null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='username',
            field=log.crypto.EncryptedField(null=True),
        ),
    ]
