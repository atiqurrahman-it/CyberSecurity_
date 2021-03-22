from django.db import models

from embed_video.fields import EmbedVideoField
from django.utils.safestring import mark_safe
from colorfield.fields import ColorField
from phonenumber_field.modelfields import PhoneNumberField
from ckeditor_uploader.fields import RichTextUploadingField


class Header_navbar(models.Model):
    logo = models.ImageField()
    color = ColorField(default='#ffffff')
    hover_color = ColorField(default='#ffffff')
    background_color = ColorField(default='#ffffff')
    background_image = models.ImageField()
    sort_title = models.CharField(max_length=150)
    sort_Discriptioin = models.CharField(max_length=240)
    video_link = EmbedVideoField()  # same like models.URLField()
    phone = PhoneNumberField()
    facebook = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    Create = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def image_tag(self):
        from django.utils.html import mark_safe
        return mark_safe('<img src="%s" width="180px" height="55px" />' % (self.logo.url))

    image_tag.short_description = 'Image'

    def __str__(self):
        return self.sort_title


class Header_second_part(models.Model):
    skill_pic = models.ImageField()
    sort_title = models.CharField(max_length=150)
    sort_Discriptioin = models.TextField()
    Create = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def image_tag(self):
        from django.utils.html import mark_safe
        return mark_safe('<img src="%s" width="110px" height="60px" />' % (self.skill_pic.url))

    image_tag.short_description = 'Image'

    def __str__(self):
        return self.sort_title


class Our_Approach_section_backend(models.Model):
    heading = models.CharField(max_length=80, blank=True)
    sort_title = models.CharField(max_length=200)
    background_color = ColorField(default='#ffffff')
    short_description = models.TextField()
    sidebar_image = models.ImageField()
    Create = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def image_tag(self):
        from django.utils.html import mark_safe
        return mark_safe('<img src="%s" width="110px" height="60px" />' % (self.sidebar_image.url))

    image_tag.short_description = 'Image'

    def __str__(self):
        return self.heading


class Our_Approach_section(models.Model):
    sort_title = models.CharField(max_length=150)
    short_description = models.CharField(max_length=300)

    Create = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.sort_title


class Our_Challenges_section_background(models.Model):
    heading = models.CharField(max_length=80, blank=True)
    short_description = models.TextField()
    background_image = models.ImageField()

    Create = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def image_tag(self):
        from django.utils.html import mark_safe
        return mark_safe('<img src="%s" width="110px" height="60px" />' % (self.background_image.url))

    image_tag.short_description = 'Image'

    def __str__(self):
        return self.heading


class Our_Challenges_section(models.Model):
    logo = models.ImageField()
    title = models.CharField(max_length=200)
    short_description = models.TextField()

    Create = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def image_tag(self):
        from django.utils.html import mark_safe
        return mark_safe('<img src="%s" width="110px" height="60px" />' % (self.logo.url))

    image_tag.short_description = 'Image'

    def __str__(self):
        return self.title


class Service_bg_section(models.Model):
    Heading = models.CharField(max_length=100)
    short_description = models.TextField()
    background_color = ColorField(default='#ffffff')
    Create = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.Heading


class Service(models.Model):
    name = models.CharField(max_length=150)
    image = models.ImageField()
    Service_details = RichTextUploadingField()
    Create = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def image_tag(self):
        from django.utils.html import mark_safe
        return mark_safe('<img src="%s" width="110px" height="60px" />' % (self.image.url))

    image_tag.short_description = 'Image'

    def __str__(self):
        return self.name


class CUSTOMERS_review_bg(models.Model):
    heading = models.CharField(max_length=200)
    bg_image = models.ImageField()
    Create = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def image_tag(self):
        from django.utils.html import mark_safe
        return mark_safe('<img src="%s" width="110px" height="60px" />' % (self.bg_image.url))

    image_tag.short_description = 'Image'

    def __str__(self):
        return self.heading


class CUSTOMERS_review(models.Model):
    name = models.CharField(max_length=200)
    position = models.CharField(max_length=100)
    review = models.TextField()
    rating_review = models.IntegerField(default=1)
    Create = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class another_company_project(models.Model):
    company_url = models.URLField(blank=True, null=True)
    logo = models.ImageField()
    Create = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def image_tag(self):
        from django.utils.html import mark_safe
        return mark_safe('<img src="%s" width="110px" height="60px" />' % (self.logo.url))

    image_tag.short_description = 'Image'


class Latest_News_Section(models.Model):
    title = models.CharField(max_length=190)
    details = models.CharField(max_length=800)
    Create = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Latest_News_Category(models.Model):
    name = models.CharField(max_length=200)
    Create = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Latest_News_Post(models.Model):
    title = models.CharField(max_length=200)
    category_news_post = models.ForeignKey(Latest_News_Category, on_delete=models.CASCADE)
    news_details = RichTextUploadingField()
    news_image = models.ImageField()
    Create = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def image_tag(self):
        from django.utils.html import mark_safe
        return mark_safe('<img src="%s" width="110px" height="60px" />' % (self.news_image.url))

    image_tag.short_description = 'Image'

    def __str__(self):
        return self.title


class Our_team(models.Model):
    name = models.CharField(max_length=150)
    image = models.ImageField()
    position = models.CharField(max_length=100)
    facebook = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)

    Create = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def image_tag(self):
        from django.utils.html import mark_safe
        return mark_safe('<img src="%s" width="110px" height="60px" />' % (self.image.url))

    image_tag.short_description = 'Image'

    def __str__(self):
        return self.name


class Why_Choose_Us_background(models.Model):
    title = models.CharField(max_length=200)
    details = models.CharField(max_length=800)
    background_image = models.ImageField()
    Create = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def image_tag(self):
        from django.utils.html import mark_safe
        return mark_safe('<img src="%s" width="110px" height="60px" />' % (self.background_image.url))

    image_tag.short_description = 'Image'

    def __str__(self):
        return self.title


class Why_Choose_Us(models.Model):
    Skills = models.CharField(max_length=100)
    logo = models.ImageField()
    quantity = models.IntegerField()

    Create = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def image_tag(self):
        from django.utils.html import mark_safe
        return mark_safe('<img src="%s" width="110px" height="60px" />' % (self.logo.url))

    image_tag.short_description = 'Image'

    def __str__(self):
        return self.Skills


class Contact_section_bg(models.Model):
    heading = models.CharField(max_length=90)
    short_description = models.TextField()
    bg_image = models.ImageField()
    # Embed_a_map = models.URLField(blank=True, null=True)
    # map = models.CharField(max_length=600)
    Create = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def image_tag(self):
        from django.utils.html import mark_safe
        return mark_safe('<img src="%s" width="110px" height="60px" />' % (self.bg_image.url))

    image_tag.short_description = 'Image'

    def __str__(self):
        return self.heading


class Contact(models.Model):
    Name = models.CharField(max_length=100)
    Email = models.EmailField()
    subject = models.CharField(max_length=150)
    message = models.TextField()
    Create = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.Name


class Footer_First_part(models.Model):
    logo = models.ImageField()
    short_description = models.CharField(max_length=350)
    location = models.CharField(max_length=120)
    email = models.EmailField()
    Create = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def image_tag(self):
        from django.utils.html import mark_safe
        return mark_safe('<img src="%s" width="110px" height="60px" />' % (self.logo.url))

    image_tag.short_description = 'Image'

    def __str__(self):
        return self.location


class Footer_Solution_part(models.Model):
    name = models.CharField(max_length=150)
    link = models.URLField(blank=True, null=True)
    Create = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Footer_Resources_part(models.Model):
    name = models.CharField(max_length=150)
    link = models.URLField(blank=True, null=True)
    Create = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
