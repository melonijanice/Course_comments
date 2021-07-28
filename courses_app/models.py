from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.
class CourseManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['course_name']) < 5:
            errors["course_name"] = "Course name should be at least 5 characters"
        if len(postData['course_description']) < 15:
            errors["course_description"] = "Course description should be at least 15 characters"
        return errors
class Course(models.Model):
    course_name = models.CharField(max_length=50,unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    objects=CourseManager()

class Description(models.Model):
    course_description = models.TextField()
    course=models.OneToOneField(Course, related_name='courses',on_delete=CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

class Comment(models.Model):
    course_comment=models.TextField()
    course=models.ForeignKey(Course,related_name="Comments",on_delete=CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)



