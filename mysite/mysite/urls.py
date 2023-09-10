from django.conf import settings
from django.urls import include, path
from django.contrib import admin

from wagtail.admin import urls as wagtailadmin_urls
from wagtail import urls as wagtail_urls
from wagtail.documents import urls as wagtaildocs_urls

from search import views as search_views

urlpatterns = [
    path("django-admin/", admin.site.urls),
    path("admin/", include(wagtailadmin_urls)),
    path("a-login/", search_views.alogin, name="alogin"),
    path("a-logout/", search_views.alogout, name="alogout"),
    path("admin-login/", search_views.adminlogin, name="adminlogin"),
    path("admin-home/", search_views.adminhome, name="adminhome"),
    path("pending-details/", search_views.pendingdetails, name="pendingdetails"),
    path("verify/<int:id>", search_views.verify, name="verify"),
    path("remove/<int:id>", search_views.remove, name="remove"),
    path("documents/", include(wagtaildocs_urls)),
    path("search/", search_views.search, name="search"),
    path("", search_views.homepage, name='home'),
    path("index/", search_views.index, name='home'),
    path("index1/", search_views.index1, name='home1'),
    path("index2/", search_views.index2, name='home2'),
    # path("gallery/", search_views.gallery, name='gallery'),
    path("membership/", search_views.membership, name='membership'),
    path("membership1/", search_views.membership1, name='membership1'),
    path("membership2/", search_views.membership2, name='membership2'),
    path("directory/", search_views.directory, name='directory'),
    path("workshopt/", search_views.workshopt, name='workshopt'),
    path("workshop1/", search_views.workshop1, name='workshop1'),
    path("workshop2/", search_views.workshop2, name='workshop2'),
    path("registration01/", search_views.registration01, name='registration01'),
    path("registration02/", search_views.registration02, name='registration02'),#new
    path("registration11/", search_views.registration11, name='registration11'),
    path("registration12/", search_views.registration12, name='registration12'),
    path("awardst/", search_views.awardst, name='awards'),
    path("awards1/", search_views.awards1, name='awards1'),
    path("awards2/", search_views.awards2, name='awards2'),
    path("downloadst/", search_views.downloadst, name='downloadst'),
    path("downloads1/", search_views.downloads1, name='downloads1'),
    path("downloads2/", search_views.downloads2, name='downloads2'),
    path("conferencet/", search_views.conferencest, name='conferences'),
    path("conferences1/", search_views.conferences1, name='conferences1'),
    path("conferences2/", search_views.conferences2, name='conferences2'),
    path("logout/", search_views.logout, name="logout"),
    path("insertmemberinfo1/", search_views.insertmemberinfo1, name="insertmemberinfo1"),
    # path("django-admin/", admin.site.urls),
    # path("admin/", include(wagtailadmin_urls)),
    # path("documents/", include(wagtaildocs_urls)),
    # path("/search/", search_views.search, name="search"),
    path('welcome/', search_views.welcome, name="index"),
    path('insert/', search_views.InsertValue, name='insert'),
    path('login/', search_views.login, name='login'),
    path('register/', search_views.register, name='register'),
    path('result/', search_views.ShowValues, name='result'),
    path('index/', search_views.index, name='index'),
    path("society/", search_views.society, name='society'),
    path("society1/", search_views.society1, name='society1'),
    path("society2/", search_views.society2, name='society2'),
    path("council/", search_views.council, name='council'),
    path("council1/", search_views.council1, name='council1'),
    path("council2/", search_views.council2, name='council2'),
    path("legendary/", search_views.legendary, name='legendary'),
    path("legendary1/", search_views.legendary1, name='legendary1'),
    path("legendary2/", search_views.legendary2, name='legendary2'),
    path("journals/", search_views.journals, name='journals'),
    path("journals1/", search_views.journals1, name='journals1'),
    path("journals2/", search_views.journals2, name='journals2'),
    path("editorial/", search_views.editorial, name='editorial'),
    path("editorial1/", search_views.editorial1, name='editorial1'),
    path("editorial2/", search_views.editorial2, name='editorial2'),
    path("books/", search_views.books, name='books'),
    path("books1/", search_views.books1, name='books1'),
    path("books2/", search_views.books2, name='books2'),
    path("newslettert/", search_views.newslettert, name='newsletter'),
    path("newsletter1/", search_views.newsletter1, name='newsletter1'),
    path("newsletter2/", search_views.newsletter2, name='newsletter2'),
    path("nomination/", search_views.nomination, name='nomination'),
    path("nomination1/", search_views.nomination1, name='nomination1'),
    path("nomination2/", search_views.nomination2, name='nomination2'),
    path("annualreportt/", search_views.annualreportt, name='annualrepoortt'),
    path("annualreport1/", search_views.annualreport1, name='annualreport1'),
    path("annualreport2/", search_views.annualreport2, name='annualreport2'),
    path("election/", search_views.election, name='election'),
    path("election1/", search_views.election1, name='election1'),
    path("election2/", search_views.election2, name='election2'),

    path('getmembership/', search_views.getmembership, name='getmembership'),



]


if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    # Serve static and media files from development server
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns = urlpatterns + [
    # For anything not caught by a more specific rule above, hand over to
    # Wagtail's page serving mechanism. This should be the last pattern in
    # the list:
    path("", include(wagtail_urls)),
    # Alternatively, if you want Wagtail pages to be served from a subpath
    # of your site, rather than the site root:
    #    path("pages/", include(wagtail_urls)),
]
