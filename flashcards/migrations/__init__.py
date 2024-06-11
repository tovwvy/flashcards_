# myapp/migrations/0001_initial.py
from django.db import migrations, models

class Migration(migrations.Migration):

    initial = True

    dependencies = [
        # Specify dependencies if any
    ]

    operations = [
        migrations.CreateModel(
            name='FavoriteCard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('english', models.CharField(max_length=100)),
                ('ukrainian', models.CharField(max_length=100)),
            ],
        ),
    ]
