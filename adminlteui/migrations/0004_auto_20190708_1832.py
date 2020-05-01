# Generated by Django 2.2.3 on 2019-07-08 10:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [('django_admin_settings', '0003_menu'),]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='content_type',
            field=models.ForeignKey(
                blank=True,
                help_text='use for permission control.',
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to='contenttypes.ContentType',
                verbose_name='ContentType'
            ),
        ),
        migrations.AlterField(
            model_name='menu',
            name='link',
            field=models.CharField(
                blank=True,
                help_text='support admin:index or /admin/ or http://',
                max_length=255,
                null=True,
                verbose_name='Link'
            ),
        ),
        migrations.AlterField(
            model_name='menu',
            name='link_type',
            field=models.IntegerField(
                choices=[(0, 'Internal'), (1, 'External'), (3, 'Divide')], default=0, verbose_name='Link Type'
            ),
        ),
    ]
