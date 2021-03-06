from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'wcdb.views.index'),
    url(r'^import/(?P<kind>(.*))$', 'wcdb.views.importView'),
    url(r'^crisis/(?P<crisis_id>CRI_[A-Z]{6})$', 'wcdb.views.crisisView'),
    url(r'^orgs/(?P<orgs_id>ORG_[A-Z]{6})$', 'wcdb.views.orgsView'),
    url(r'^people/(?P<people_id>PER_[A-Z]{6})$', 'wcdb.views.peopleView'),
    url(r'^export/$', 'wcdb.views.exportView'),
    url(r'^unittests/$', 'wcdb.views.unittestsView'),
    url(r'^download/$', 'wcdb.views.downloadView'),
    url(r'^search/$', 'wcdb.views.searchView'),
    url(r'^queries/(?P<query_num>(.*))$', 'wcdb.views.queriesView'),
    url(r'^crisespage/(?P<kind>(.*))$', 'wcdb.views.crisesPage'),
    url(r'^orgpage/(?P<kind>(.*))$', 'wcdb.views.orgPage'),
    url(r'^pplpage/(?P<kind>(.*))$', 'wcdb.views.pplPage'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),	
)
