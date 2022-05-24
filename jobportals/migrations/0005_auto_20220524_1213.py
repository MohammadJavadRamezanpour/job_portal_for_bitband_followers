# Generated by Django 3.2.10 on 2022-05-24 07:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jobportals', '0004_alter_jobdetail_the_amount_of_work_experience'),
    ]

    operations = [
        migrations.RenameField(
            model_name='jobseeker',
            old_name='Preferred_job_category',
            new_name='preferred_job_category',
        ),
        migrations.AlterField(
            model_name='educationalbackground',
            name='jobseeker',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='jobseeker_educationalbackground', to='jobportals.jobseeker'),
        ),
    ]