# Generated by Django 4.0.6 on 2024-11-26 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0003_alter_business_profile_pic_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='business',
            name='type',
            field=models.CharField(choices=[('startup', 'Startup'), ('enterprise', 'Enterprise'), ('freelancer', 'Freelancer')], default='startup', max_length=50),
        ),
        migrations.AddField(
            model_name='freelancer',
            name='email',
            field=models.EmailField(blank=True, max_length=254),
        ),
    ]
