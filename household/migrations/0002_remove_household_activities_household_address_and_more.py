# Generated by Django 5.1.4 on 2025-01-01 15:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('household', '0001_initial'),
        ('organizations', '0001_initial'),
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='household',
            name='activities',
        ),
        migrations.AddField(
            model_name='household',
            name='address',
            field=models.TextField(default='Nairobi'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='household',
            name='organization',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='households', to='organizations.organization'),
        ),
        migrations.AlterField(
            model_name='household',
            name='project',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='households', to='projects.project'),
        ),
        migrations.CreateModel(
            name='HouseholdMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('age', models.PositiveIntegerField()),
                ('gender', models.CharField(max_length=50)),
                ('relationship_to_head', models.CharField(max_length=255)),
                ('household', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='members', to='household.household')),
            ],
        ),
    ]
