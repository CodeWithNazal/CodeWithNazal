# Generated by Django 4.1.4 on 2023-10-08 05:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Tuturials', '0010_tutorial_source_code'),
    ]

    operations = [
        migrations.CreateModel(
            name='TutorialChapter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='TutorialChapterContent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
                ('text', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='tutorial_chapter_content/')),
                ('chapter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Tuturials.tutorialchapter')),
            ],
        ),
        migrations.DeleteModel(
            name='Blog',
        ),
        migrations.RemoveField(
            model_name='chapter',
            name='tutorial',
        ),
        migrations.DeleteModel(
            name='News',
        ),
        migrations.RemoveField(
            model_name='tutorial',
            name='source_code',
        ),
        migrations.DeleteModel(
            name='Chapter',
        ),
        migrations.AddField(
            model_name='tutorialchaptercontent',
            name='tutorial',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Tuturials.tutorial'),
        ),
        migrations.AddField(
            model_name='tutorialchapter',
            name='tutorial',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Tuturials.tutorial'),
        ),
    ]
