from django.contrib import admin
from .models import Post
# Register your models here.

class PostAdmin(admin.ModelAdmin):
	list_display = ["title","content","publish_date"]
	list_display_links = ["title","content","publish_date"]
	list_filter = ["title","content","publish_date"]
	search_fields = ["title","content","publish_date"]
	class Meta:
		model = Post

admin.site.register(Post,PostAdmin)