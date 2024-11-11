import helpers
from django.db import models
from cloudinary.models import CloudinaryField

helpers.cloudinary_init()

# Create your models here.

"""
- Courses:
	- Title
	- Description
	- Thumbnail/Image
	- Access:
		- Anyone
		- Email required
        - Purchase required
		- User required (n/a)
	- Status: 
		- Published
		- Coming Soon
		- Draft
	- Lessons
		- Title
		- Description
		- Video
		- Status: Published, Coming Soon, Draft
"""

# classes are useful for choices if multiple jaga choice field ko use karna hai

class PublishStatus(models.TextChoices):
    PUBLISHED = "pub", "Published"
    COMING_SOON = "soon", "Coming Soon"
    DRAFT = "draft", "Draft"

# pub is stored in the DB and Published is showed for the user
class AccessRequirement(models.TextChoices):
    ANYONE = "any", "Anyone"
    EMAIL_REQUIRED = "email", "Email required"
    
def handle_upload(instance, filename):
    return f"{filename}"


# This is a model obv
class Course(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(blank=True, null=True) # null=True matlab database mei empty ho sakta hai
    
    # image = models.ImageField(upload_to=handle_upload, blank=True, null=True)
    image = CloudinaryField("image")
    # access choices rakhenge
    access = models.CharField(
        max_length=5,
        choices=AccessRequirement.choices,
        default=AccessRequirement.EMAIL_REQUIRED
    )
    status = models.CharField(
        max_length=10,
        choices=PublishStatus.choices,
        default=PublishStatus.DRAFT
        )
    # image = models.ImageField()
    
    '''
        The @property decorator allows you to define a method as if it were an attribute. This means that instead of calling it like a method (object.is_published()), you can access it like an attribute (object.is_published).

        This code defines a method called `is_published()` that checks whether an object's `status` attribute is set to `PublishStatus.PUBLISHED`.

Here's a breakdown:

1. **Method Definition**: `is_published(self)` is likely defined inside a class (e.g., a post, article, or similar content class).
  
2. **Purpose**: The method returns a Boolean (`True` or `False`) depending on the condition.
  
3. **Condition**: `self.status == PublishStatus.PUBLISHED` compares the object's `status` with `PublishStatus.PUBLISHED`.

   - `self.status` likely holds the current status of the object.
   - `PublishStatus.PUBLISHED` is probably a constant or enumeration value indicating the "published" status.

4. **Return**: If `self.status` matches `PublishStatus.PUBLISHED`, it returns `True`; otherwise, it returns `False`.

In short, `is_published()` will check if the object's `status` indicates that it’s published and return `True` if it is, `False` otherwise.

        
        
        '''
    @property
    def is_published(self):
        return self.status == PublishStatus.PUBLISHED
    
    @property
    def image_admin_url(self):
        if not self.image:
            return ""
        image_options = {
            "width": 200,
        }
        url = self.image.build_url(**image_options)
        return url

# Ye aur bakchodi karne ke liye hai
    def get_image_detail(self, as_html=False, width=750):
        if not self.image:
            return ""
        image_options = {
            "width": width,
        }
        if as_html:
            # This below thing is equivalent to CloudinaryImage(str(self.image)).image(**image_options)
            return self.image.image(**image_options)
        # CloudinaryImage(cloudinary_id).build_url(**image_options)
        url = self.image.build_url(**image_options)
        return url

    def get_image_thumbnail(self, as_html=False, width=500):
        if not self.image:
            return ""
        image_options = {
            "width": width, # defined in the function ka input
        }
        if as_html:
            # This below thing is equivalent to CloudinaryImage(str(self.image)).image(**image_options)
            return self.image.image(**image_options)
        # CloudinaryImage(cloudinary_id).build_url(**image_options)
        url = self.image.build_url(**image_options)
        return url


'''
	- Lessons
		- Title
		- Description
		- Video
		- Status: Published, Coming Soon, Draft
'''

# Django Query language

# Lesson.objects.all()
# Lesson.objects.first() one of them
# course_obj = Course.objects.first()
# Lessons.objects.filter(my_related_obj__id=course_obj.id)


class Lesson(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(blank=True, null=True)