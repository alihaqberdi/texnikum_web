# Generated by Django 4.1.7 on 2023-03-03 07:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_alter_doctor_patsient_alter_nurse_patsient'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admin',
            name='doctor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.doctor'),
        ),
        migrations.AlterField(
            model_name='admin',
            name='nurse',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.nurse'),
        ),
        migrations.AlterField(
            model_name='admin',
            name='senior_doctor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.seniordoctor'),
        ),
        migrations.AlterField(
            model_name='seniordoctor',
            name='doctor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.doctor'),
        ),
        migrations.AlterField(
            model_name='seniordoctor',
            name='nurse',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.nurse'),
        ),
        migrations.AlterField(
            model_name='seniordoctor',
            name='patsient',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.patsient'),
        ),
    ]
