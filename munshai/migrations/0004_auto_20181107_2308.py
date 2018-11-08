# Generated by Django 2.1.2 on 2018-11-07 23:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('viewflow', '0008_merge'),
        ('munshai', '0003_document_client_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(default='', max_length=140, verbose_name='email')),
                ('client_id', models.ForeignKey(db_column='client_id', on_delete=django.db.models.deletion.CASCADE, to='munshai.Client', verbose_name='client')),
            ],
        ),
        migrations.CreateModel(
            name='HelloWorldProcess',
            fields=[
                ('process_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='viewflow.Process')),
                ('text', models.CharField(max_length=150)),
                ('approved', models.BooleanField(default=False)),
                ('upload', models.FileField(upload_to='documents/')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('viewflow.process',),
        ),
        migrations.AlterField(
            model_name='document',
            name='document_type',
            field=models.CharField(choices=[('ledger', 'LEDGER'), ('far', 'FAR')], default='ledger', max_length=140, verbose_name='Document Type'),
        ),
    ]
