from django.db import models

# Create your models here.


class MyBaseModel(models.Model):
    is_active = models.BooleanField(default=False, verbose_name='Is active')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created at')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Updated at')

    class Meta:
        abstract = True
        ordering = ['pk']


class Category(MyBaseModel):
    title = models.CharField(max_length=250, unique=True, null=False, blank=False, verbose_name="title")
    description = models.TextField(null=False, blank=False, verbose_name="description")

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        ordering = ['id']

    def __str__(self):
        return self.title


class Post(MyBaseModel):
    title = models.CharField(max_length=250, null=False, blank=False, verbose_name="title")
    description = models.TextField(null=False, blank=False, verbose_name="description")
    category = models.ForeignKey(Category, related_name="posts", on_delete=models.CASCADE, verbose_name="category")

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"
        ordering = ['id']

    def __str__(self):
        return self.title


class Comment(MyBaseModel):
    post = models.ForeignKey(Post, related_name="comments", on_delete=models, verbose_name="post")
    author = models.CharField(max_length=250, null=False, blank=False, verbose_name="author")
    content = models.TextField(null=False, blank=False, verbose_name="content")
    is_approved = models.BooleanField(default=False, verbose_name="is_approved")

    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"
        ordering = ['id']

    def __str__(self):
        return self.author


class Media(MyBaseModel):
    post = models.ForeignKey(Post, related_name='media', on_delete=models.CASCADE, verbose_name="post")
    # 'image' or 'video'
    media_type = models.CharField(max_length=20, null=False, blank=False, verbose_name="media_type")
    media_file = models.FileField(upload_to='media/blog/')

    class Meta:
        verbose_name = "Media"
        verbose_name_plural = "Media"
        ordering = ['id']

    def __str__(self):
        return self.media_type
