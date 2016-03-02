# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import json
import wagtail.wagtaildocs.blocks
import wagtail.wagtailimages.blocks
import wagtail.wagtailcore.fields
import wagtail.wagtailcore.blocks
import wagtail.wagtailembeds.blocks
import project_tier.protocol.models

def convert_to_streamfield(apps, schema_editor):
    ComponentPage = apps.get_model("protocol", "ComponentPage")
    for page in ComponentPage.objects.all():
        page.body = json.dumps([{ 'type': 'rich_text', 'value': page.description }])
        page.save()


def convert_to_richtext(apps, schema_editor):
    ComponentPage = apps.get_model("protocol", "ComponentPage")
    for page in ComponentPage.objects.all():
        if page.body.raw_text is None:
            raw_text = ''.join([
                child.value.source for child in page.body
                if child.block_type == 'rich_text'
            ])
            page.description = raw_text
            page.save()

class Migration(migrations.Migration):

    dependencies = [
        ('protocol', '0015_auto_20160224_1244'),
    ]

    operations = [
        migrations.AddField(
            model_name='componentpage',
            name='body',
            field=wagtail.wagtailcore.fields.StreamField([(b'h2', wagtail.wagtailcore.blocks.CharBlock(classname='title', label='Section Title', icon='title')), (b'paragraph', wagtail.wagtailcore.blocks.RichTextBlock(icon='pilcrow')), (b'rich_text', wagtail.wagtailcore.blocks.RichTextBlock(icon='pilcrow')), (b'embed', wagtail.wagtailembeds.blocks.EmbedBlock(icon='media')), (b'aligned_image', wagtail.wagtailcore.blocks.StructBlock([(b'image', wagtail.wagtailimages.blocks.ImageChooserBlock()), (b'caption', wagtail.wagtailcore.blocks.RichTextBlock()), (b'alignment', project_tier.protocol.models.ImageFormatChoiceBlock())], icon='image', label='Aligned image')), (b'tip', wagtail.wagtailcore.blocks.StructBlock([(b'title', wagtail.wagtailcore.blocks.CharBlock(label='Tip Heading')), (b'details', wagtail.wagtailcore.blocks.RichTextBlock())], icon='help', label='Tip')), (b'extended_info', wagtail.wagtailcore.blocks.StructBlock([(b'heading', wagtail.wagtailcore.blocks.CharBlock(help_text='The heading of an extended info setting', label='Heading')), (b'details', wagtail.wagtailcore.blocks.RichTextBlock())], icon='plus-inverse', label='Extended Info')), (b'document', wagtail.wagtaildocs.blocks.DocumentChooserBlock(icon='doc-full-inverse'))], default=''),
            preserve_default=False,
        ),
        migrations.RunPython(
            convert_to_streamfield,
            convert_to_richtext,
        ),
    ]
