from django.contrib import admin
from .models import Category, Project, Inquiry,Contact

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'description')

class InquiryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'message', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('name', 'email')
    
    
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "phone", "subject", "submitted_at")
    search_fields = ("name", "email", "subject")

admin.site.register(Category, CategoryAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Inquiry, InquiryAdmin)
