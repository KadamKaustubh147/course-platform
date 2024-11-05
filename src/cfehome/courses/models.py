from django.db import models

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
    EMAIL_REQUIRED = "email_required", "Email required"
    
# This is a model obv
class Course(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(blank=True, null=True) # null=True matlab database mei empty ho sakta hai
    
    # image
    # access choices rakhenge
    access = models.CharField(
        max_length=10,
        choices=AccessRequirement.choices,
        default=AccessRequirement.DRAFT
    )
    status = models.CharField(
        max_length=10,
        choices=PublishStatus.choices,
        default=PublishStatus.DRAFT
        )
    
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

