from django.core.validators import MinLengthValidator
from django.db import models
from django.db.models import Model, ForeignKey, ManyToManyField
from django.db.models.fields import DateField, SlugField, TextField, EmailField, CharField
from django.utils.functional import empty
from django.utils.text import slugify


# Create your models here.
class Post(Model):
    def __str__(self):
        return self.title + " " + self.excerpt

    def save(
        self,
        *args,
        **kwargs,
    ):
        self.slug = slugify(self.title)

        super().save(*args, **kwargs)

    title = CharField(max_length=150, null=False, blank=False, default=' ')
    excerpt = CharField(max_length=300, null=True, blank=True, default=' ')
    image_name = CharField(max_length=300)
    created_at = DateField(auto_now_add=True)
    updated_at = DateField(auto_now=True)
    slug = SlugField(unique=True, db_index=True, editable=False, default='')
    content = TextField(validators=[MinLengthValidator(10)])
    author = ForeignKey('Author', on_delete=models.SET_NULL, related_name='posts', null=True)
    tags = ManyToManyField('Tag', blank=True)


class Author(Model):
    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.email})"

    first_name = CharField(max_length=150, null=False, blank=False, default=' ')
    last_name = CharField(max_length=150, null=False, blank=False, default=' ')
    email = EmailField(max_length=150)
    created_at = DateField(auto_now_add=True)
    updated_at = DateField(auto_now=True)


class Tag(Model):
    def __str__(self):
        return self.caption

    caption = CharField(max_length=20, null=False, blank=False, default=' ')
    created_at = DateField(auto_now_add=True)
    updated_at = DateField(auto_now=True)