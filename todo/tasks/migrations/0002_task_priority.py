

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='priority',
            field=models.CharField(choices=[('danger', 'Priority 1'), ('warning', 'Priority 2'), ('success', 'Priority 3'), ('primary', 'Priority 4')], default='danger', max_length=30),
        ),
    ]
