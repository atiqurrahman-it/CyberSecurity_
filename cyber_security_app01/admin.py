from django.contrib import admin

from .models import Contact, Service, Latest_News_Section, Latest_News_Category, Latest_News_Post, Our_team, \
    Why_Choose_Us, Why_Choose_Us_background, Header_navbar, Header_second_part, Our_Approach_section_backend, \
    Our_Approach_section, Our_Challenges_section_background, Our_Challenges_section, Footer_First_part, \
    Contact_section_bg, another_company_project, CUSTOMERS_review, CUSTOMERS_review_bg, Footer_Solution_part, \
    Footer_Resources_part, Service_bg_section

from embed_video.admin import AdminVideoMixin


# Register your models here.


class MyModelAdmin(AdminVideoMixin, admin.ModelAdmin):
    list_display = ('sort_title', 'image_tag', 'Create', 'updated')


admin.site.register(Header_navbar, MyModelAdmin)


class Header_second_part_admin(admin.ModelAdmin):
    list_display = ['__str__', 'image_tag', 'sort_title', 'Create', 'updated']
    search_fields = ["sort_title"]
    list_filter = ['Create']

    # ordering = ['date_created']
    # list_per_page = 10

    class Meta:
        Model = Header_second_part


admin.site.register(Header_second_part, Header_second_part_admin)


class Our_Approach_section_backend_admin(admin.ModelAdmin):
    list_display = ['__str__', 'heading', 'background_color', 'image_tag', 'Create', 'updated']

    class Meta:
        Model = Our_Approach_section_backend


admin.site.register(Our_Approach_section_backend, Our_Approach_section_backend_admin)


class Our_Approach_section_admin(admin.ModelAdmin):
    list_display = ['__str__', 'sort_title', 'Create', 'updated']
    search_fields = ["sort_title"]
    list_filter = ['Create']

    class Meta:
        Model = Our_Approach_section


admin.site.register(Our_Approach_section, Our_Approach_section_admin)


class Our_Challenges_section_background_admin(admin.ModelAdmin):
    list_display = ['__str__', 'heading', 'image_tag', 'Create', 'updated']

    class Meta:
        Model = Our_Challenges_section_background


admin.site.register(Our_Challenges_section_background, Our_Challenges_section_background_admin)


class Our_Challenges_section_admin(admin.ModelAdmin):
    list_display = ['__str__', 'title', 'image_tag', 'Create', 'updated']

    class Meta:
        Model = Our_Challenges_section


admin.site.register(Our_Challenges_section, Our_Challenges_section_admin)


class Service_bg_section_admin(admin.ModelAdmin):
    list_display = ['Heading', 'background_color', 'Create', 'updated']

    class Meta:
        Model = Service_bg_section


admin.site.register(Service_bg_section, Service_bg_section_admin)


class Service_admin(admin.ModelAdmin):
    list_display = ['name', 'image_tag', 'Create', 'updated']
    search_fields = ["__str__"]
    list_filter = ['Create', "name"]

    class Meta:
        Model = Service


admin.site.register(Service, Service_admin)


class CUSTOMERS_review_bg_admin(admin.ModelAdmin):
    list_display = ['heading', 'image_tag', 'Create', 'updated']

    class Meta:
        Model = CUSTOMERS_review_bg


admin.site.register(CUSTOMERS_review_bg, CUSTOMERS_review_bg_admin)


class CUSTOMERS_review_admin(admin.ModelAdmin):
    list_display = ['name', 'position', 'Create', 'updated']
    search_fields = ["name", "position"]
    list_filter = ["Create", "name"]

    class Meta:
        Model = CUSTOMERS_review


admin.site.register(CUSTOMERS_review, CUSTOMERS_review_admin)


class another_company_project_admin(admin.ModelAdmin):
    list_display = ['image_tag', 'Create', 'updated']
    search_fields = ["company_url"]
    list_filter = ['Create']
    list_per_page = 10

    class Meta:
        Model = another_company_project


admin.site.register(another_company_project, another_company_project_admin)


class Latest_News_Section_admin(admin.ModelAdmin):
    list_display = ['title', 'Create', 'updated']

    class Meta:
        Model = Latest_News_Section


admin.site.register(Latest_News_Section, Latest_News_Section_admin)


class Latest_News_Category_admin(admin.ModelAdmin):
    list_display = ['name', 'Create', 'updated']
    search_fields = ["name", "Create"]
    list_filter = ["Create", "name"]

    class Meta:
        Model = Latest_News_Category


admin.site.register(Latest_News_Category, Latest_News_Category_admin)


class Latest_News_Post_admin(admin.ModelAdmin):
    list_display = ['title', 'category_news_post', 'image_tag', 'Create', 'updated']
    search_fields = ["title", "category_news_post"]
    list_filter = ["Create", "category_news_post"]

    class Meta:
        Model = Latest_News_Post


admin.site.register(Latest_News_Post, Latest_News_Post_admin)


class Our_team_admin(admin.ModelAdmin):
    list_display = ['name', 'position', 'image_tag', 'Create', 'updated']
    search_fields = ["name", "position"]
    list_filter = ['Create', "name"]

    class Meta:
        Model = Our_team


admin.site.register(Our_team, Our_team_admin)


class Why_Choose_Us_section_admin(admin.ModelAdmin):
    list_display = ['title', 'image_tag', 'Create', 'updated']

    class Meta:
        Model = Why_Choose_Us_background


admin.site.register(Why_Choose_Us_background, Why_Choose_Us_section_admin)


class Why_Choose_Us_admin(admin.ModelAdmin):
    list_display = ['Skills', 'quantity', 'image_tag', 'Create', 'updated']
    search_fields = ["Skills", "quantity"]
    list_filter = ["Create", "Skills"]

    class Meta:
        Model = Why_Choose_Us


admin.site.register(Why_Choose_Us, Why_Choose_Us_admin)


class Contact_section_bg_admin(admin.ModelAdmin):
    list_display = ['heading', 'image_tag', 'Create', 'updated']

    class Meta:
        Model = Contact_section_bg


admin.site.register(Contact_section_bg, Contact_section_bg_admin)


class Contact_admin(admin.ModelAdmin):
    list_display = ['Name', 'Email', 'Create']
    search_fields = ["Name", "Email", "Create"]
    list_filter = ["Create", "Name"]

    class Meta:
        Model = Contact


admin.site.register(Contact, Contact_admin)


class Footer_First_part_admin(admin.ModelAdmin):
    list_display = ['email', 'image_tag', 'Create']
    search_fields = ["Name", "Email", "Create"]
    list_filter = ["Create"]

    class Meta:
        Model = Footer_First_part


admin.site.register(Footer_First_part, Footer_First_part_admin)


class Footer_Solution_part_admin(admin.ModelAdmin):
    list_display = ['name', 'Create']
    search_fields = ["name", "Create"]
    list_filter = ["Create", "name"]

    class Meta:
        Model = Footer_Solution_part


admin.site.register(Footer_Solution_part, Footer_Solution_part_admin)


class Footer_Resources_part_admin(admin.ModelAdmin):
    list_display = ['name', 'Create']
    search_fields = ["name", "Create"]
    list_filter = ["Create", "name"]

    class Meta:
        Model = Footer_Resources_part


admin.site.register(Footer_Resources_part, Footer_Resources_part_admin)
