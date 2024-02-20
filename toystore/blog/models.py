from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.


class MyBaseModel(models.Model):
    is_active = models.BooleanField(default=False, verbose_name='Is active')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created at')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Updated at')

    class Meta:
        abstract = True
        ordering = ['pk']


class BlogCategory(MyBaseModel):
    title = models.CharField(max_length=250, unique=True, null=False, blank=False, verbose_name="title")
    description = models.TextField(null=False, blank=False, verbose_name="description")

    class Meta:
        verbose_name = "BlogCategory"
        verbose_name_plural = "BlogCategories"
        ordering = ['id']

    def __str__(self):
        return self.title


class Post(MyBaseModel):
    title = models.CharField(max_length=250, null=False, blank=False, verbose_name="title")
    description = models.TextField(null=False, blank=False, verbose_name="description")
    category = models.ForeignKey(BlogCategory, related_name="posts", on_delete=models.CASCADE, verbose_name="category")

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"
        ordering = ['id']

    def __str__(self):
        return self.title


class BlogComment(MyBaseModel):
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE, verbose_name="post")
    author = models.ForeignKey(User, null=False, blank=False, verbose_name="author", on_delete=models.CASCADE)
    content = models.TextField(null=False, blank=False, verbose_name="content")

    class Meta:
        verbose_name = "BlogComment"
        verbose_name_plural = "BlogComments"
        ordering = ['id']

    def __str__(self):
        return self.author


class BlogMedia(MyBaseModel):
    MEDIA_TYPES = [('image', 'image'), ('video', 'video'), ('audio', 'audio')]
    post = models.ForeignKey(Post, related_name='media', on_delete=models.CASCADE, verbose_name="post")
    media_type = models.CharField(max_length=20, choices=MEDIA_TYPES, null=False, blank=False,
                                  verbose_name="media_type")
    media_file = models.FileField(upload_to='media/blog/')

    class Meta:
        verbose_name = "Media"
        verbose_name_plural = "Media"
        ordering = ['id']

    def __str__(self):
        return self.media_type

    @property
    def get_images(self):
        """
        Get images related to the given post.
        """
        return BlogMedia.objects.filter(post=self.post, media_type='image')

    @property
    def get_videos(self):
        """
        Get videos related to the given post.
        """
        return BlogMedia.objects.filter(post=self.post, media_type='video')

    @property
    def get_audios(self):
        """
        Get videos related to the given post.
        """
        return BlogMedia.objects.filter(post=self.post, media_type='audio')
