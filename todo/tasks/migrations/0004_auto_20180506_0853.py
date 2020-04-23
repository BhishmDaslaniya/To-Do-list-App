

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0003_task_complete'),
    ]

    operations = [
        migrations.CreateModel(
            name='Username',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='task',
            name='priority',
            field=models.CharField(choices=[('adanger', 'Priority 1'), ('bwarning', 'Priority 2'), ('csuccess', 'Priority 3'), ('dprimary', 'Priority 4')], default='adanger', max_length=30),
        ),
    ]
