from django.db import models
from User.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.utils import timezone


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    parent = models.ForeignKey(
        'self', null=True, blank=True, on_delete=models.CASCADE)
    content_type = models.ForeignKey(
        ContentType, related_name="comments", on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    text = models.TextField(null=False, blank=False)

    def __str__(self):
        return self.text[:20]

    def children(self):
        return Comment.objects.filter(object_id=self.id)

    # @property
    # def get_content_type(self):
    #     post = self
    #     content_type = ContentType.objects.get_for_model(post.__class__)
    #     return content_type


class ServicesData(models.Model):
    comments = GenericRelation(Comment)
    subject_code = models.IntegerField(primary_key=True)
    subject_name = models.CharField(max_length=100, unique=True)
    subject_duration = models.CharField(max_length=100)
    subject_startdate = models.DateField(max_length=100)
    subject_starttime = models.TimeField(max_length=100)
    subject_instructor_name = models.CharField(max_length=100)
    subject_instructor_experience = models.CharField(max_length=100)

    def __str__(self):
        return self.subject_name


class FeedBackData(models.Model):
    comments = GenericRelation(Comment)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    adress = models.CharField(max_length=250)
    email = models.EmailField(max_length=100)
    subject = models.CharField(max_length=100)
    feedback = models.CharField(max_length=250)

    def __str__(self):
        return self.first_name


class ContactData(models.Model):

    name = models.CharField(max_length=25)
    GENDER_CHOICE = (
        ('Male', 'Male'),
        ('Female', 'Female')
    )
    gender = models.CharField(max_length=10, choices=GENDER_CHOICE)
    email = models.EmailField(max_length=30)
    mobile = models.BigIntegerField()
    about = models.CharField(max_length=500)


class Post(models.Model):
    post = GenericRelation(Comment)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=120)
    image = models.ImageField(upload_to='blogpic',
                              null=True,
                              blank=True,)
    content = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateField(blank=True, null=True)
    updated = models.DateTimeField(auto_now_add=False)

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title

    def publish(self):
        self.published_date = timezone.now()
        self.save()
