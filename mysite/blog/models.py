from django.db import models

# Create your models here.
from wagtail.models import Page, Orderable
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel, InlinePanel
from modelcluster.fields import ParentalKey
from wagtail.search import index

# class BlogIndexPage(Page):
#     intro = RichTextField(blank=True)

#     content_panels = Page.content_panels + [
#         FieldPanel('intro')
#     ]

#     def get_context(self, request):
#         # Update context to include only published posts, ordered by reverse-chron
#         context = super().get_context(request)
#         blogpages = self.get_children().live().order_by('-first_published_at')
#         context['blogpages'] = blogpages
#         return context

# class BlogPage(Page):
#     date = models.DateField("Post date")
#     intro = models.CharField(max_length=250)
#     body = RichTextField(blank=True)
#     image = models.ForeignKey(
#         'wagtailimages.Image', on_delete=models.SET_NULL, related_name='+', blank=True, null=True
#     )
#     caption = models.CharField(blank=True, max_length=250)

#     content_panels = Page.content_panels + [
#         FieldPanel('intro'),
#         FieldPanel('body'),
#         FieldPanel('date'),
#         FieldPanel('image'),
#         FieldPanel('caption'),
#     ]

class AwardsIndexPage(Page):
    intro = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('intro')
    ]

    def get_context(self, request):
        # Update context to include only published posts, ordered by reverse-chron
        context = super().get_context(request)
        blogpages = self.get_children().live().order_by('-first_published_at')
        context['blogpages'] = blogpages
        return context

class AwardsPage(Page):
    intro = models.CharField(max_length=250)
    year = models.CharField(max_length=10, default="")
    date = models.DateField("Post date")
    body = RichTextField("body")
    image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.SET_NULL, related_name='+', blank=True, null=True
    )
    caption = models.CharField(blank=True, max_length=250)

    content_panels = Page.content_panels + [
        FieldPanel('intro'),
        FieldPanel('year'),
        FieldPanel('date'),
        FieldPanel('body'),
        FieldPanel('image'),
        FieldPanel('caption'),
    ]


class NationalConferenceIndexPage(Page):
    intro = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('intro')
    ]

    def get_context(self, request):
        # Update context to include only published posts, ordered by reverse-chron
        context = super().get_context(request)
        blogpages = self.get_children().live().order_by('-first_published_at')
        context['blogpages'] = blogpages
        return context
    
class NationalConferencePage(Page):
    intro = models.CharField(max_length=250)
    body = RichTextField("body", blank=True)
    year = RichTextField("year", blank=True)
    type = models.CharField(max_length=100, default="")
    date = models.DateField("Date")
    venue = models.CharField(max_length=250)
    
    image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.SET_NULL, related_name='+', blank=True, null=True
    )
    caption = models.CharField(blank=True, max_length=250)

    content_panels = Page.content_panels + [
        FieldPanel('intro'),
        FieldPanel('body'),
        FieldPanel('year'),
        FieldPanel('type'),
        FieldPanel('date'),
        FieldPanel('venue'),
        FieldPanel('image'),
        FieldPanel('caption'),
        
    ]

# International Conference 
class BlogIndexPage(Page):
    intro = RichTextField(blank=True)

    def get_context(self, request):
        # Update context to include only published posts, ordered by reverse-chron
        context = super().get_context(request)
        blogpages = self.get_children().live().order_by('-first_published_at')
        context['blogpages'] = blogpages
        return context

class BlogPage(Page):
    intro = models.CharField(max_length=250)
    body = RichTextField(blank=True)
    year = RichTextField("year", blank=True)
    date = models.DateField("Date")
    venue = models.CharField(max_length=250, default="")
    search_fields = Page.search_fields + [
        index.SearchField('intro'),
        index.SearchField('body'),
    ]

    content_panels = Page.content_panels + [
        FieldPanel('intro'),
        FieldPanel('body'),
        FieldPanel('year'),
        FieldPanel('date'),
        FieldPanel('venue'),
        InlinePanel('gallery_images', label="Gallery images"),
    ]


class BlogPageGalleryImage(Orderable):
    page = ParentalKey(BlogPage, on_delete=models.CASCADE, related_name='gallery_images')
    image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.CASCADE, related_name='+'
    )
    caption = models.CharField(blank=True, max_length=250)

    panels = [
        FieldPanel('image'),
        FieldPanel('caption'),
    ]

# class InternationalConferenceIndexPage(Page):
#     intro = RichTextField(blank=True)

#     content_panels = Page.content_panels + [
#         FieldPanel('intro')
#     ]

#     def get_context(self, request):
#         # Update context to include only published posts, ordered by reverse-chron
#         context = super().get_context(request)
#         blogpages = self.get_children().live().order_by('-first_published_at')
#         context['blogpages'] = blogpages
#         return context
    
# class InternationalConferencePage(Page):
#     intro = models.CharField(max_length=250)
#     body = RichTextField("body", blank=True)
#     year = RichTextField("year", blank=True)
#     type = models.CharField(max_length=100, default="")
#     date = models.DateField("Date")
#     venue = models.CharField(max_length=250)
#     caption = models.CharField(blank=True, max_length=250)
#     image = models.ForeignKey(
#         'wagtailimages.Image', on_delete=models.CASCADE, related_name='+'
#     )

#     def main_image(self):
#         gallery_item = self.gallery_images.first()
#         if gallery_item:
#             return gallery_item.image
#         else:
#             return None

#     content_panels = Page.content_panels + [
#         FieldPanel('intro'),
#         FieldPanel('body'),
#         FieldPanel('year'),
#         FieldPanel('type'),
#         FieldPanel('date'),
#         FieldPanel('venue'),
#         FieldPanel('caption'),
#         InlinePanel('gallery_images', label="Gallery images"),
#     ]

# class InternationalConferencePageGalleryImage(Orderable):
#     page = ParentalKey(BlogPage, on_delete=models.CASCADE, related_name='gallery_images')
#     image = models.ForeignKey(
#         'wagtailimages.Image', on_delete=models.CASCADE, related_name='+'
#     )
#     caption = models.CharField(blank=True, max_length=250)

#     panels = [
#         FieldPanel('image'),
#         FieldPanel('caption'),
#     ]

class WorkshopIndexPage(Page):
    intro = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('intro')
    ]

    def get_context(self, request):
        # Update context to include only published posts, ordered by reverse-chron
        context = super().get_context(request)
        blogpages = self.get_children().live().order_by('-first_published_at')
        context['blogpages'] = blogpages
        return context
    
class WorkshopPage(Page):
    date = models.DateField("Date")
    intro = models.CharField(max_length=250)
    venue = models.CharField(max_length=250)
    year = RichTextField("year", blank=True)
    image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.SET_NULL, related_name='+', blank=True, null=True
    )
    caption = models.CharField(blank=True, max_length=250)

    content_panels = Page.content_panels + [
        FieldPanel('intro'),
        FieldPanel('year'),
        FieldPanel('date'),
        FieldPanel('image'),
        FieldPanel('caption'),
        FieldPanel('venue'),
    ]


class DownloadsIndexPage(Page):
    intro = RichTextField(blank=True)
    
    content_panels = Page.content_panels + [
        FieldPanel('intro'),
    ]

    def get_context(self, request):
        # Update context to include only published posts, ordered by reverse-chron
        context = super().get_context(request)
        blogpages = self.get_children().live().order_by('-first_published_at')
        context['blogpages'] = blogpages
        return context
    
class DownloadsPage(Page):
    intro = RichTextField(blank=True)
    date = models.DateField("Date")
    file = models.ForeignKey(
        'wagtaildocs.Document', on_delete=models.SET_NULL, related_name='+', blank=True, null=True
    )

    content_panels = Page.content_panels + [
        FieldPanel('intro'),
        FieldPanel('date'),
        FieldPanel('file'),
    ]

class GalleryIndexPage(Page):
    intro = RichTextField(blank=True)
    
    content_panels = Page.content_panels + [
        FieldPanel('intro'),
    ]

    def get_context(self, request):
        # Update context to include only published posts, ordered by reverse-chron
        context = super().get_context(request)
        blogpages = self.get_children().live().order_by('-first_published_at')
        context['blogpages'] = blogpages
        return context
    
class GalleryPage(Page):
    label = RichTextField(blank=True)
    content = RichTextField(blank=True)
    image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.SET_NULL, related_name='+', blank=True, null=True
    )

    content_panels = Page.content_panels + [
        FieldPanel('label'),
        FieldPanel('content'),
        FieldPanel('image'),
    ]

class NewsletterIndexPage(Page):
    intro = RichTextField(blank=True)
    
    
    content_panels = Page.content_panels + [
        FieldPanel('intro'),
    ]

    def get_context(self, request):
        # Update context to include only published posts, ordered by reverse-chron
        context = super().get_context(request)
        blogpages = self.get_children().live().order_by('-first_published_at')
        context['blogpages'] = blogpages
        return context
    
class NewsletterPage(Page):
    intro = RichTextField(blank=True)
    year = RichTextField(blank=True)
    volume = RichTextField(blank=True)
    issue = RichTextField(blank=True)
    month = RichTextField(blank=True)
    file = models.ForeignKey(
        'wagtaildocs.Document', on_delete=models.SET_NULL, related_name='+', blank=True, null=True
    )

    content_panels = Page.content_panels + [
        FieldPanel('intro'),
        FieldPanel('year'),
        FieldPanel('volume'),
        FieldPanel('issue'),
        FieldPanel('month'),
        FieldPanel('file'),
    ]
    
class AnnualReportIndexPage(Page):
    intro = RichTextField(blank=True)
    
    
    content_panels = Page.content_panels + [
        FieldPanel('intro'),
    ]

    def get_context(self, request):
        # Update context to include only published posts, ordered by reverse-chron
        context = super().get_context(request)
        blogpages = self.get_children().live().order_by('-first_published_at')
        context['blogpages'] = blogpages
        return context
    
class AnnualReportPage(Page):
    name = RichTextField(blank=True)
    year = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('name'),
        FieldPanel('year'),
    ]
    
