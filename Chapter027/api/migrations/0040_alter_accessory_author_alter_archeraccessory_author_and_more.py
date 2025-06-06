# Generated by Django 5.1.1 on 2025-06-05 11:56

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0039_competition_end_date_competition_end_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accessory',
            name='author',
            field=models.ForeignKey(default=1, help_text='format: required, default=1 (superuser)', on_delete=django.db.models.deletion.PROTECT, related_name='accessory_author', to=settings.AUTH_USER_MODEL, verbose_name='author of accessory'),
        ),
        migrations.AlterField(
            model_name='archeraccessory',
            name='author',
            field=models.ForeignKey(default=1, help_text='format: required, default=1 (superuser)', on_delete=django.db.models.deletion.PROTECT, related_name='archeraccessory_author', to=settings.AUTH_USER_MODEL, verbose_name='author of archer accessory'),
        ),
        migrations.AlterField(
            model_name='archeraccessorymembership',
            name='author',
            field=models.ForeignKey(default=1, help_text='format: required, default=1 (superuser)', on_delete=django.db.models.deletion.PROTECT, related_name='archeraccessorymembership_author', to=settings.AUTH_USER_MODEL, verbose_name='author of archer accessory membership'),
        ),
        migrations.AlterField(
            model_name='arrow',
            name='author',
            field=models.ForeignKey(default=1, help_text='format: required, default=1 (superuser)', on_delete=django.db.models.deletion.PROTECT, related_name='arrow_author', to=settings.AUTH_USER_MODEL, verbose_name='author of arrow'),
        ),
        migrations.AlterField(
            model_name='arrowfletching',
            name='author',
            field=models.ForeignKey(default=1, help_text='format: required, default=1 (superuser)', on_delete=django.db.models.deletion.PROTECT, related_name='arrowfletching_author', to=settings.AUTH_USER_MODEL, verbose_name='author of arrow fletching'),
        ),
        migrations.AlterField(
            model_name='arrowtype',
            name='author',
            field=models.ForeignKey(default=1, help_text='format: required, default=1 (superuser)', on_delete=django.db.models.deletion.PROTECT, related_name='arrowtype_author', to=settings.AUTH_USER_MODEL, verbose_name='author of arrow type'),
        ),
        migrations.AlterField(
            model_name='arrowtypemembership',
            name='author',
            field=models.ForeignKey(default=1, help_text='format: required, default=1 (superuser)', on_delete=django.db.models.deletion.PROTECT, related_name='arrowtypemembership_author', to=settings.AUTH_USER_MODEL, verbose_name='author of arrow type membership'),
        ),
        migrations.AlterField(
            model_name='bestofclubmembership',
            name='author',
            field=models.ForeignKey(default=1, help_text='format: required, default=1 (superuser)', on_delete=django.db.models.deletion.PROTECT, related_name='bestofclubmembership_author', to=settings.AUTH_USER_MODEL, verbose_name='author of best of club membership'),
        ),
        migrations.AlterField(
            model_name='bowsight',
            name='author',
            field=models.ForeignKey(default=1, help_text='format: required, default=1 (superuser)', on_delete=django.db.models.deletion.PROTECT, related_name='bowsight_author', to=settings.AUTH_USER_MODEL, verbose_name='author of bow sight'),
        ),
        migrations.AlterField(
            model_name='bowsightarcher',
            name='author',
            field=models.ForeignKey(default=1, help_text='format: required, default=1 (superuser)', on_delete=django.db.models.deletion.PROTECT, related_name='bowsightarcher_author', to=settings.AUTH_USER_MODEL, verbose_name='author of bowsight archer'),
        ),
        migrations.AlterField(
            model_name='clubchampionship',
            name='author',
            field=models.ForeignKey(default=1, help_text='format: required, default=1 (superuser)', on_delete=django.db.models.deletion.PROTECT, related_name='clubchampionship_author', to=settings.AUTH_USER_MODEL, verbose_name='author of club championship'),
        ),
        migrations.AlterField(
            model_name='clubchampionshipmembership',
            name='author',
            field=models.ForeignKey(default=1, help_text='format: required, default=1 (superuser)', on_delete=django.db.models.deletion.PROTECT, related_name='clubchampionshipmembership_author', to=settings.AUTH_USER_MODEL, verbose_name='author of club championship membership'),
        ),
        migrations.AlterField(
            model_name='distance',
            name='author',
            field=models.ForeignKey(default=1, help_text='format: required, default=1 (superuser)', on_delete=django.db.models.deletion.PROTECT, related_name='distance_author', to=settings.AUTH_USER_MODEL, verbose_name='author of distance'),
        ),
        migrations.AlterField(
            model_name='fletching',
            name='author',
            field=models.ForeignKey(default=1, help_text='format: required, default=1 (superuser)', on_delete=django.db.models.deletion.PROTECT, related_name='fletching_author', to=settings.AUTH_USER_MODEL, verbose_name='author of fletching'),
        ),
        migrations.AlterField(
            model_name='range',
            name='author',
            field=models.ForeignKey(default=1, help_text='format: required, default=1 (superuser)', on_delete=django.db.models.deletion.PROTECT, related_name='range_author', to=settings.AUTH_USER_MODEL, verbose_name='author of range'),
        ),
        migrations.AlterField(
            model_name='rangeround',
            name='author',
            field=models.ForeignKey(default=1, help_text='format: required, default=1 (superuser)', on_delete=django.db.models.deletion.PROTECT, related_name='rangeround_author', to=settings.AUTH_USER_MODEL, verbose_name='author of range round'),
        ),
        migrations.AlterField(
            model_name='round',
            name='author',
            field=models.ForeignKey(default=1, help_text='format: required, default=1 (superuser)', on_delete=django.db.models.deletion.PROTECT, related_name='round_author', to=settings.AUTH_USER_MODEL, verbose_name='author of round'),
        ),
        migrations.AlterField(
            model_name='rounddistance',
            name='author',
            field=models.ForeignKey(default=1, help_text='format: required, default=1 (superuser)', on_delete=django.db.models.deletion.PROTECT, related_name='rounddistance_author', to=settings.AUTH_USER_MODEL, verbose_name='author of round distance'),
        ),
        migrations.AlterField(
            model_name='roundmembership',
            name='author',
            field=models.ForeignKey(default=1, help_text='format: required, default=1 (superuser)', on_delete=django.db.models.deletion.PROTECT, related_name='roundmembership_author', to=settings.AUTH_USER_MODEL, verbose_name='author of round membership'),
        ),
        migrations.AlterField(
            model_name='scoremembership',
            name='author',
            field=models.ForeignKey(default=1, help_text='format: required, default=1 (superuser)', on_delete=django.db.models.deletion.PROTECT, related_name='scoremembership_author', to=settings.AUTH_USER_MODEL, verbose_name='author of score membership'),
        ),
    ]
