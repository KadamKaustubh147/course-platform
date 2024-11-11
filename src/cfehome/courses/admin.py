from cloudinary import CloudinaryImage
from django.contrib import admin
# Register your models here.
from .models import Course
from django.utils.html import format_html

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    # ordering bhi change kar sakte
    list_display = ['title', 'status', 'access', 'display_image']
    list_filter =  ['status', 'access']
    fields = ['title', 'description', 'status', 'image', 'access', 'display_image']
    readonly_fields = ['display_image']
    
    # args and kwargs not used
    def display_image(self, obj, *args,**kwargs):
        url = obj.image_admin_url
        # fir return format_html(f"<img src='{url}'/>)
        cloudinary_id = str(obj.image)
        # cloudinary stores id in the DB
        cloudinary_html = CloudinaryImage(cloudinary_id).image(width=500) # isse actual image change ho rha hai
        return format_html(f"<img src={url} />")
    
    display_image.short_description = "Current Image"
    
'''
Function Definition:

def display_image(self, obj, *args, **kwargs):
display_image is defined as a method within the CourseAdmin class.
self refers to the CourseAdmin instance.
obj is the specific instance of the Course model that’s being displayed in the admin. This parameter allows access to the attributes of the Course object, such as its image field.
*args and **kwargs are optional arguments that can be used if additional parameters are passed to the function. Here, they’re not used, so they don’t affect the function.
Accessing the Image URL:

url = obj.image.url
This line retrieves the URL for the image field of the Course object (obj). In Django, if the image field is a FileField or ImageField, accessing obj.image.url will give the absolute URL of the uploaded image file, assuming that an image has been uploaded for this Course instance.


'''

# chahe register decorator use karo ya fir admin.site.register(Course) dono same hai

# admin.site.register(Course)

