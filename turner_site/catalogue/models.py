from datetime import date

from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.fields import StreamField
from wagtail.wagtailcore import blocks
from wagtail.wagtailadmin.edit_handlers import StreamFieldPanel
from wagtail.wagtailimages.blocks import ImageChooserBlock


class TurnerImageBlock(blocks.StructBlock):
    image_title = blocks.CharBlock(required=True)
    thumbnail = ImageChooserBlock()
    full_image = ImageChooserBlock()
    copyright_conditions_of_use = blocks.CharBlock()

    unique_identifying_number = blocks.CharBlock()
    date_of_submission = blocks.DateTimeBlock(default=date.today)

    # person submitting
    person_submitting_images = blocks.CharBlock()
    current_owning_inst_person = blocks.CharBlock()
    inst_personal_unique_impression_accession_no = blocks.CharBlock()
    inst_personal_unique_image_accession_no = blocks.CharBlock()

    # Dimensions
    impression_physical_dimensions = blocks.CharBlock()
    size_of_paper = blocks.CharBlock()
    size_of_plate_impression = blocks.CharBlock()
    size_of_picture = blocks.CharBlock()

    # Physical Attributes
    paper_type = blocks.CharBlock()
    comments_on_impression = blocks.RichTextBlock()
    condition = blocks.CharBlock()
    physical_history = blocks.CharBlock()

    # Digital Image
    digital_image_dimensions = blocks.CharBlock()
    digital_image_capture_mechanism = blocks.CharBlock()
    imaging_device = blocks.CharBlock()
    device_settings = blocks.CharBlock()
    calibration = blocks.CharBlock()
    date_of_capture = blocks.CharBlock()

    # Engraving info
    rawlinson_finerg_number = blocks.CharBlock()
    proposed_version_state = blocks.CharBlock()
    engraver = blocks.CharBlock()
    original_engraving_date = blocks.CharBlock()
    original_publication = blocks.CharBlock()
    actual_publication = blocks.CharBlock()

    # text and info on impression
    printed_text_on_impression = blocks.RichTextBlock()
    written_info_on_impression = blocks.RichTextBlock()
    turner_touching_comments = blocks.RichTextBlock()
    previous_collection_owner = blocks.RichTextBlock()

    links_related_info = blocks.CharBlock()
    histories_or_original_drawing = blocks.CharBlock()


class CatalogueIndexPage(Page):

    body = StreamField([
        ('image', TurnerImageBlock()),
    ])

    content_panels = Page.content_panels + [
        StreamFieldPanel('body'),
    ]





    # caption = rawlinson_finerg_number + title + original_ingraving_date

    # content_panels = Page.content_panels + [
    #     MultiFieldPanel([
    #         FieldPanel('image_title'),
    #         ImageChooserPanel('thumbnail'),
    #         ImageChooserPanel('full_image'),
    #         FieldPanel('copyright_conditions_of_use'),
    #         FieldPanel('unique_identifying_number'),
    #         FieldPanel('date_of_submission'),
    # ], heading="Image"),
    #     MultiFieldPanel([
    #         FieldPanel('person_submitting_images'),
    #         FieldPanel('current_owning_inst_person'),
    #         FieldPanel('inst_personal_unique_impression_accession_no'),
    #         FieldPanel('inst_personal_unique_image_accession_no'),
    #     ], heading="Person Submitting"),
    #     MultiFieldPanel([
    #         FieldPanel('impression_physical_dimensions'),
    #         FieldPanel('size_of_paper'),
    #         FieldPanel('size_of_plate_impression'),
    #         FieldPanel('size_of_picture'),
    #     ], heading="Dimensions"),
    #     MultiFieldPanel([
    #         FieldPanel('paper_type'),
    #         FieldPanel('comments_on_impression'),
    #         FieldPanel('condition'),
    #         FieldPanel('physical_history'),
    #     ], heading="Physical Attributes"),
    #     MultiFieldPanel([
    #         FieldPanel('digital_image_dimensions'),
    #         FieldPanel('digital_image_capture_mechanism'),
    #         FieldPanel('imaging_device'),
    #         FieldPanel('device_settings'),
    #         FieldPanel('calibration'),
    #         FieldPanel('date_of_capture'),
    #     ], heading="Digital Image"),
    #     MultiFieldPanel([
    #         FieldPanel('rawlinson_finerg_number'),
    #         FieldPanel('proposed_version_state'),
    #         FieldPanel('engraver'),
    #         FieldPanel('original_engraving_date'),
    #         FieldPanel('original_publication'),
    #         FieldPanel('actual_publication'),
    #     ], heading="Engraving Info"),
    #     MultiFieldPanel([
    #         FieldPanel('printed_text_on_impression'),
    #         FieldPanel('written_info_on_impression'),
    #         FieldPanel('turner_touching_comments'),
    #         FieldPanel('previous_collection_owner'),
    #         FieldPanel('links_related_info'),
    #         FieldPanel('histories_or_original_drawing'),
    #     ], heading="Text and info on Impression"),
    # ]
    #
    # search_fields = Page.search_fields + [
    #     index.SearchField('image_title'),
    #     index.SearchField('copyright_conditions_of_use'),
    #     index.SearchField('unique_identifying_number'),
    #     index.SearchField('date_of_submission'),
    #     index.SearchField('person_submitting_images'),
    #     index.SearchField('inst_personal_unique_impression_accession_no'),
    #     index.SearchField('inst_personal_unique_image_accession_no'),
    #     index.SearchField('impression_physical_dimensions'),
    #     index.SearchField('size_of_paper'),
    #     index.SearchField('size_of_plate_impression'),
    #     index.SearchField('size_of_picture'),
    #     index.SearchField('paper_type'),
    #     index.SearchField('comments_on_impression'),
    #     index.SearchField('condition'),
    #     index.SearchField('physical_history'),
    #     index.SearchField('digital_image_dimensions'),
    #     index.SearchField('digital_image_capture_mechanism'),
    #     index.SearchField('imaging_device'),
    #     index.SearchField('device_settings'),
    #     index.SearchField('calibration'),
    #     index.SearchField('date_of_capture'),
    #     index.SearchField('rawlinson_finerg_number'),
    #     index.SearchField('proposed_version_state'),
    #     index.SearchField('engraver'),
    #     index.SearchField('original_engraving_date'),
    #     index.SearchField('original_publication'),
    #     index.SearchField('actual_publication'),
    #     index.SearchField('printed_text_on_impression'),
    #     index.SearchField('written_info_on_impression'),
    #     index.SearchField('turner_touching_comments'),
    #     index.SearchField('previous_collection_owner'),
    #     index.SearchField('links_related_info'),
    #     index.SearchField('histories_or_original_drawing'),
    # ]