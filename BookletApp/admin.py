from django.contrib import admin

#from .models import User
from .models import Comment
from .models import File


class CommentAdminInline(admin.TabularInline):
	model= Comment
	fields= ['text', ]
	extra= 0


class FileAdmin(admin.ModelAdmin):
	list_display= ['id', 'name', 'uploaded_date']
	inlines= [CommentAdminInline, ]

class CategoryAdmin(admin.ModelAdmin):
	list_display= ['id', 'name']


#admin.site.register(User)	

admin.site.register(File, FileAdmin)

from .models import Category
admin.site.register(Category, CategoryAdmin)
from .models import Download
admin.site.register(Download)
from .models import Upload
admin.site.register(Upload)
