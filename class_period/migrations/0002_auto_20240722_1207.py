from django.db import migrations, models
import django.db.models.deletion

class Migration(migrations.Migration):

    dependencies = [
        ('class_period', '0001_initial'),
        ('course', '0001_initial'),  # make sure this matches your course app's initial migration
    ]

    operations = [
        migrations.AddField(
            model_name='classperiod',
            name='course',
            field=models.ForeignKey('course.Course', on_delete=django.db.models.deletion.SET_NULL, null=True, related_name='course_period'),
        ),
    ]