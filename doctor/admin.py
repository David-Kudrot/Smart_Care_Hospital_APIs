from django.contrib import admin
from doctor.models import AvailableTime, Designation, Doctor, Review, Specialization

# Register your models here.
class SpecializationAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {"slug" : ("name",)}
    
admin.site.register(Specialization, SpecializationAdmin)

class DesignationAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {"slug" : ("name",)}

admin.site.register(Designation, DesignationAdmin)

admin.site.register(AvailableTime)

admin.site.register(Doctor)
admin.site.register(Review)