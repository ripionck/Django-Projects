# Generated by Django 4.2.7 on 2023-12-08 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('taskTitle', models.CharField(max_length=50)),
                ('taskDescription', models.TextField()),
                ('isCompleted', models.BooleanField(default=False)),
                ('taskAssignDate', models.DateTimeField(auto_now_add=True)),
                ('categories', models.ManyToManyField(to='category.taskcategory')),
            ],
        ),
    ]