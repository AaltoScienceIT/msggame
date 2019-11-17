# Generated by Django 2.2.7 on 2019-11-17 22:29

from django.db import migrations, models
import django.db.models.deletion
import msggame.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('round', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('round', models.IntegerField(default=msggame.models.current_round)),
                ('status', models.TextField(choices=[('ACTIVE', 'Active'), ('COMPLETED', 'Completed'), ('STALLED', 'Stalled')], default='Active')),
                ('ts_create', models.DateTimeField(auto_now_add=True, null=True)),
                ('ts_last', models.DateTimeField(auto_now=True, null=True)),
                ('ts_received', models.DateTimeField(blank=True, null=True)),
                ('relays', models.IntegerField(default=0)),
                ('path_ids', models.TextField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(blank=True, max_length=50, null=True)),
                ('secret_pin', models.IntegerField(blank=True, null=True)),
                ('pin', models.IntegerField(blank=True, null=True)),
                ('centrality', models.FloatField(default=0)),
                ('score', models.FloatField(default=0)),
                ('consent_research', models.BooleanField(default=False)),
                ('consent_research_withname', models.BooleanField(default=False)),
                ('consent_research_open', models.BooleanField(default=False)),
                ('ts_lastactive', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Round',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('round', models.IntegerField(unique=True)),
                ('send_messages', models.BooleanField(default=True)),
                ('max_links', models.IntegerField(default=10)),
                ('allow_new_links', models.BooleanField(default=True)),
                ('disallow_existing_links', models.BooleanField(default=False)),
                ('require_links', models.BooleanField(default=False)),
                ('links_from_relays', models.BooleanField(default=True)),
                ('auto_create_messages', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Relay',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('round', models.IntegerField(default=msggame.models.current_round)),
                ('ts', models.DateTimeField(auto_now_add=True)),
                ('destination', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='relay_destination', to='msggame.Person')),
                ('message', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='msggame.Message')),
                ('source', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='relay_source', to='msggame.Person')),
            ],
        ),
        migrations.AddField(
            model_name='message',
            name='current_holder',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='current_messages', to='msggame.Person'),
        ),
        migrations.AddField(
            model_name='message',
            name='origin',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='message_origins', to='msggame.Person'),
        ),
        migrations.AddField(
            model_name='message',
            name='target',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='message_targets', to='msggame.Person'),
        ),
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('round', models.IntegerField(default=msggame.models.current_round)),
                ('ts_create', models.DateTimeField(auto_now_add=True)),
                ('ts_used', models.DateTimeField(auto_now=True)),
                ('nuses', models.IntegerField(default=0)),
                ('destination', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='link_destinations', to='msggame.Person')),
                ('source', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='link_sources', to='msggame.Person')),
            ],
        ),
    ]