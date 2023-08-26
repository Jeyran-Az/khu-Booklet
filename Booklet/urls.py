
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from BookletApp import views

from BookletApp.views import index, files_list, categories_list, new_category, new_file, about, contact, \
    randomprocesses, fuzzy, graph, stat_methods, probability1, math_softwares, ad_programming, ranalysis, \
    coding, lopt, comfunc, numth, general, defa, help


urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', index, name= 'index'),
    path('files_list/', files_list, name= 'files_list'),
    path('categories_list/', categories_list, name= 'categories_list'),
    path('index/file_create.html/', views.file_create_form),
    path('users/', include('users.urls')),
    path('new_category.html/', new_category, name='new_category'),
    path('new_file/', new_file, name= 'new_file'),
    path('about/', about, name= 'about'),
    path('contact/', contact, name= 'contact'),
    path('categories_list/randomprocesses', randomprocesses, name= 'randomprocesses'),
    path('categories_list/fuzzy', fuzzy, name= 'fuzzy'),
    path('categories_list/graph', graph, name= 'graph'),
    path('categories_list/stat_methods', stat_methods, name= 'stat_methods'),
    path('categories_list/probability1', probability1, name= 'probability1'),
    path('categories_list/math_softwares', math_softwares, name= 'math_softwares'),
    path('categories_list/ad_programming', ad_programming, name= 'ad_programming'),
    path('categories_list/coding', coding, name= 'coding'),
    path('categories_list/lopt', lopt, name= 'lopt'),
    path('categories_list/ranalysis', ranalysis, name= 'ranalysis'),
    path('categories_list/comfunc', comfunc, name= 'comfunc'),
    path('categories_list/numth', numth, name= 'numth'),
    path('general/', general, name= 'general'),
    path('general/defa', defa, name= 'defa'),
    path('help', help, name= 'help'),
    #path('test', test, name= 'test'),
                #path('categories_list/ranalysis', ranalysis, name= 'ranalysis'),
                    #path('categories_list/ranalysis', ranalysis, name= 'ranalysis'),



]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
