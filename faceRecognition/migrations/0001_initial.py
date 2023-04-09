# Generated by Django 4.1.7 on 2023-03-25 23:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UploadImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('image_name', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'uploadImage',
            },
        ),
        migrations.CreateModel(
            name='DetectResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('count', models.PositiveIntegerField()),
                ('upload_image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='faceRecognition.uploadimages')),
            ],
            options={
                'db_table': 'detectResult',
            },
        ),
    ]
