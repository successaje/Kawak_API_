# Generated by Django 3.0.14 on 2022-03-15 09:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='EssayReview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.TextField(max_length=512)),
                ('Topic', models.CharField(choices=[('Art', 'Art'), ('Anatomy', 'Anatomy'), ('Biology', 'Biology'), ('Blockchain', 'Blockchain'), ('Business', 'Business'), ('Comedy', 'Comedy'), ('Communication', 'Communication'), ('Design', 'Design'), ('Education', 'Education'), ('Engineering', 'Engineering'), ('Finance', 'Finance'), ('Health', 'Health'), ('History', 'History'), ('Games', 'Games'), ('Law', 'Law'), ('Linguistics', 'Linguistics'), ('Literature', 'Literature'), ('Politics', 'Politics'), ('Philosophy', 'Philosophy'), ('Religion', 'Religion'), ('Sciences', 'Sciences'), ('Others', 'Others')], max_length=255)),
                ('EssayReviewContent', models.TextField(default=False)),
                ('submitted_at', models.DateTimeField(auto_now=True)),
                ('Reviewer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-submitted_at'],
            },
        ),
    ]