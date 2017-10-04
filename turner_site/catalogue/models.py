from django import forms
from datetime import date

from django.db import models

from modelcluster.tags import ClusterTaggableManager

from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.fields import StreamField, RichTextField
from wagtail.wagtailcore import blocks
from wagtail.wagtailadmin.edit_handlers import FieldPanel, StreamFieldPanel, MultiFieldPanel, InlinePanel, FieldRowPanel
from wagtail.wagtailimages.blocks import ImageChooserBlock
from wagtail.wagtailsearch import index

from wagtail.contrib.table_block.blocks import TableBlock
from wagtail.wagtailimages.models import Image
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel


class TurnerCatalogue(Page):
    intro_catalogue = models.CharField(max_length=500, blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('intro_catalogue'),

    ]


class TurnerImage(Page):
    # Image
    image_title = models.CharField(max_length=255)
    thumbnail = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    full_image =models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    copyright_conditions_of_use = models.CharField(max_length=255) # dropdown?

    unique_identifying_number = models.CharField(max_length=255)
    date_of_submission = models.DateField(('Date'), default=date.today)


    # person submitting
    person_submitting_images = models.CharField(max_length=255)
    current_owning_inst_person = models.CharField(max_length=255)
    inst_personal_unique_impression_accession_no = models.CharField(max_length=255)
    inst_personal_unique_image_accession_no = models.CharField(max_length=255)

    # Dimensions
    impression_physical_dimensions = models.CharField(max_length=255)
    size_of_paper = models.CharField(max_length=255)
    size_of_plate_impression = models.CharField(max_length=255)
    size_of_picture = models.CharField(max_length=255)

    # Physical Attributes
    paper_type = models.CharField(max_length=255)
    condition = models.CharField(max_length=255)  # dropdown?
    physical_history = models.CharField(max_length=255)
    comments_on_impression = RichTextField()


    # Digital Image
    digital_image_dimensions = models.CharField(max_length=255)
    digital_image_capture_mechanism = models.CharField(max_length=255)
    imaging_device = models.CharField(max_length=255)
    device_settings = models.CharField(max_length=255)
    calibration = models.CharField(max_length=255)
    date_of_capture = models.CharField(max_length=255)

    # Engraving info
    rawlinson_finberg_number = models.CharField(max_length=255)
    proposed_version_state = models.CharField(max_length=255)
    engraver = models.CharField(max_length=255)
    original_engraving_date = models.CharField(max_length=255)
    original_publication = models.CharField(max_length=255)
    actual_publication = models.CharField(max_length=255)

    # text and info on impression
    printed_text_on_impression = RichTextField()
    written_info_on_impression = RichTextField()
    turner_touching_comments = RichTextField()
    previous_collection_owner = models.CharField(max_length=255)

    links_related_info = models.CharField(max_length=255)
    histories_or_original_drawing = models.CharField(max_length=255)

    # caption = rawlinson_finerg_number + title + original_ingraving_date

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('image_title'),
            ImageChooserPanel('thumbnail'),
            ImageChooserPanel('full_image'),
            FieldPanel('copyright_conditions_of_use'),
            FieldPanel('unique_identifying_number'),
            FieldPanel('date_of_submission'),
    ], heading="Image"),
        MultiFieldPanel([
            FieldPanel('person_submitting_images'),
            FieldPanel('current_owning_inst_person'),
            FieldPanel('inst_personal_unique_impression_accession_no'),
            FieldPanel('inst_personal_unique_image_accession_no'),
        ], heading="Person Submitting"),
        MultiFieldPanel([
            FieldPanel('impression_physical_dimensions'),
            FieldPanel('size_of_paper'),
            FieldPanel('size_of_plate_impression'),
            FieldPanel('size_of_picture'),
        ], heading="Dimensions"),
        MultiFieldPanel([
            FieldPanel('paper_type'),
            FieldPanel('comments_on_impression'),
            FieldPanel('condition'),
            FieldPanel('physical_history'),
        ], heading="Physical Attributes"),
        MultiFieldPanel([
            FieldPanel('digital_image_dimensions'),
            FieldPanel('digital_image_capture_mechanism'),
            FieldPanel('imaging_device'),
            FieldPanel('device_settings'),
            FieldPanel('calibration'),
            FieldPanel('date_of_capture'),
        ], heading="Digital Image"),
        MultiFieldPanel([
            FieldPanel('rawlinson_finberg_number'),
            FieldPanel('proposed_version_state'),
            FieldPanel('engraver'),
            FieldPanel('original_engraving_date'),
            FieldPanel('original_publication'),
            FieldPanel('actual_publication'),
        ], heading="Engraving Info"),
        MultiFieldPanel([
            FieldPanel('printed_text_on_impression'),
            FieldPanel('written_info_on_impression'),
            FieldPanel('turner_touching_comments'),
            FieldPanel('previous_collection_owner'),
            FieldPanel('links_related_info'),
            FieldPanel('histories_or_original_drawing'),
        ], heading="Text and info on Impression"),
    ]

    search_fields = Page.search_fields + [
        index.SearchField('image_title'),
        index.SearchField('copyright_conditions_of_use'),
        index.SearchField('unique_identifying_number'),
        index.SearchField('date_of_submission'),
        index.SearchField('person_submitting_images'),
        index.SearchField('inst_personal_unique_impression_accession_no'),
        index.SearchField('inst_personal_unique_image_accession_no'),
        index.SearchField('impression_physical_dimensions'),
        index.SearchField('size_of_paper'),
        index.SearchField('size_of_plate_impression'),
        index.SearchField('size_of_picture'),
        index.SearchField('paper_type'),
        index.SearchField('comments_on_impression'),
        index.SearchField('condition'),
        index.SearchField('physical_history'),
        index.SearchField('digital_image_dimensions'),
        index.SearchField('digital_image_capture_mechanism'),
        index.SearchField('imaging_device'),
        index.SearchField('device_settings'),
        index.SearchField('calibration'),
        index.SearchField('date_of_capture'),
        index.SearchField('rawlinson_finberg_number'),
        index.SearchField('proposed_version_state'),
        index.SearchField('engraver'),
        index.SearchField('original_engraving_date'),
        index.SearchField('original_publication'),
        index.SearchField('actual_publication'),
        index.SearchField('printed_text_on_impression'),
        index.SearchField('written_info_on_impression'),
        index.SearchField('turner_touching_comments'),
        index.SearchField('previous_collection_owner'),
        index.SearchField('links_related_info'),
        index.SearchField('histories_or_original_drawing'),
    ]
