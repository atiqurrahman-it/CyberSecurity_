from django.shortcuts import render, redirect, HttpResponse, get_object_or_404, Http404
from .models import Contact, Service, Our_team, Latest_News_Section, Latest_News_Post, Latest_News_Category, \
    Header_navbar, Header_second_part, Our_Approach_section_backend, Our_Approach_section, \
    Our_Challenges_section_background, Our_Challenges_section, Why_Choose_Us_background, Why_Choose_Us, \
    Contact_section_bg, \
    another_company_project, CUSTOMERS_review, Footer_First_part, CUSTOMERS_review_bg, Service_bg_section, \
    Footer_Resources_part, Footer_Solution_part

from django.conf import settings
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.

def Homepage(request):
    header_nav = Header_navbar.objects.latest('id')  # get_object_or_404()
    header_2nd_part = Header_second_part.objects.all().order_by('-id')[:3]
    Our_Approach_bg = Our_Approach_section_backend.objects.latest('id')  # get_object_or_404()
    Our_Approach = Our_Approach_section.objects.all().order_by('-id')[:4]
    Our_Challenges_bg = Our_Challenges_section_background.objects.latest('id')  # get_object_or_404()
    Our_Challenges = Our_Challenges_section.objects.all().order_by('-id')[:4]
    service_bg = Service_bg_section.objects.latest('id')  # get_object_or_404()
    total_service = Service.objects.all().order_by('-id')[:4]
    custom_review_bg = CUSTOMERS_review_bg.objects.latest('id')  # get_object_or_404()
    Customers_review = CUSTOMERS_review.objects.all().order_by('-id')
    company_project = another_company_project.objects.all().order_by('-id')
    news_section = Latest_News_Section.objects.latest('id')  # get_object_or_404()
    total_news = Latest_News_Post.objects.all().order_by('-id')[:3]
    total_team = Our_team.objects.all().order_by('-id')[:3]
    Why_Choose_bg = Why_Choose_Us_background.objects.latest('id')  # get_object_or_404()
    Why_Choose = Why_Choose_Us.objects.all().order_by('-id')[:4]
    contact_bg = Contact_section_bg.objects.latest('id')  # get_object_or_404()
    footer_fist_par = Footer_First_part.objects.latest('id')  # get_object_or_404()
    footer_resources = Footer_Resources_part.objects.all().order_by('-id')[:6]
    footer_solution = Footer_Solution_part.objects.all().order_by('-id')[:6]

    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        x = Contact(Name=name, Email=email, subject=subject, message=message)
        x.save()
        subject = request.POST['subject']
        from_email = request.POST['email']
        message = request.POST['message']
        to_email = settings.EMAIL_HOST_USER
        # mail_to = [to_email]
        if subject and message and from_email and to_email:
            try:
                send_mail(subject, message, from_email, [to_email])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')

            return redirect("contact")
        else:
            return HttpResponse('Make sure all fields are entered and valid.')

    data = {
        "total_service": total_service,
        "total_team": total_team,
        "news_section": news_section,
        "total_news": total_news,
        "header_nav": header_nav,
        "header_2nd_part": header_2nd_part,
        "footer_fist_par": footer_fist_par,
        "footer_resources": footer_resources,
        "footer_solution": footer_solution,
        "Our_Approach_bg": Our_Approach_bg,
        "Our_Approach": Our_Approach,
        "Our_Challenges_bg": Our_Challenges_bg,
        "Our_Challenges": Our_Challenges,
        "Why_Choose_bg": Why_Choose_bg,
        "Why_Choose": Why_Choose,
        "contact_bg": contact_bg,
        "company_project": company_project,
        "custom_review_bg": custom_review_bg,
        "Customers_review": Customers_review,
        "service_bg": service_bg,
    }
    return render(request, 'index.html', data)


def Contact_view(request):
    contact_bg = Contact_section_bg.objects.latest('id')  # get_object_or_404()
    header_nav = Header_navbar.objects.latest('id')  # get_object_or_404()
    footer_fist_par = Footer_First_part.objects.latest('id')  # get_object_or_404()
    footer_resources = Footer_Resources_part.objects.all().order_by('-id')[:6]
    footer_solution = Footer_Solution_part.objects.all().order_by('-id')[:6]
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        x = Contact(Name=name, Email=email, subject=subject, message=message)
        x.save()
        subject = request.POST['subject']
        from_email = request.POST['email']
        message = request.POST['message']
        to_email = settings.EMAIL_HOST_USER
        # mail_to = [to_email]
        if subject and message and from_email and to_email:
            try:
                send_mail(subject, message, from_email, [to_email])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')

            return redirect("contact")
        else:
            return HttpResponse('Make sure all fields are entered and valid.')
    data = {
        "contact_bg": contact_bg,

        "header_nav": header_nav,
        "footer_fist_par": footer_fist_par,
        "footer_resources": footer_resources,
        "footer_solution": footer_solution,
    }
    return render(request, 'Contact.html', data)


def Our_tem(request):
    total_team = Our_team.objects.all().order_by('-id')

    header_nav = Header_navbar.objects.latest('id')  # get_object_or_404()
    footer_fist_par = Footer_First_part.objects.latest('id')  # get_object_or_404()
    footer_resources = Footer_Resources_part.objects.all().order_by('-id')[:6]
    footer_solution = Footer_Solution_part.objects.all().order_by('-id')[:6]

    page = request.GET.get('page', 1)
    paginator = Paginator(total_team, 6)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)
    data = {
        "total_team": users,  # total_team

        "header_nav": header_nav,
        "footer_fist_par": footer_fist_par,
        "footer_resources": footer_resources,
        "footer_solution": footer_solution,
    }
    return render(request, 'our_team.html', data)


def Our_Services(request):
    total_service = Service.objects.all().order_by('-id')

    header_nav = Header_navbar.objects.latest('id')  # get_object_or_404()
    footer_fist_par = Footer_First_part.objects.latest('id')  # get_object_or_404()
    footer_resources = Footer_Resources_part.objects.all().order_by('-id')[:6]
    footer_solution = Footer_Solution_part.objects.all().order_by('-id')[:6]

    page = request.GET.get('page', 1)
    paginator = Paginator(total_service, 8)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)
    data = {
        "total_service": users,  # total_service

        "header_nav": header_nav,
        "footer_fist_par": footer_fist_par,
        "footer_resources": footer_resources,
        "footer_solution": footer_solution,
    }
    return render(request, 'Our_Services.html', data)


def service_single_page(request, id):
    single_service_details = get_object_or_404(Service, id=id)

    header_nav = Header_navbar.objects.latest('id')  # get_object_or_404()
    footer_fist_par = Footer_First_part.objects.latest('id')  # get_object_or_404()
    footer_resources = Footer_Resources_part.objects.all().order_by('-id')[:6]
    footer_solution = Footer_Solution_part.objects.all().order_by('-id')[:6]

    data = {
        "single_service_details": single_service_details,

        "header_nav": header_nav,
        "footer_fist_par": footer_fist_par,
        "footer_resources": footer_resources,
        "footer_solution": footer_solution,
    }
    return render(request, 'service_single_page.html', data)


def Latest_News(request):
    news_section = Latest_News_Section.objects.latest('id')  # get_object_or_404()
    total_news_all = Latest_News_Post.objects.all().order_by('-id')

    header_nav = Header_navbar.objects.latest('id')  # get_object_or_404()
    footer_fist_par = Footer_First_part.objects.latest('id')  # get_object_or_404()
    footer_resources = Footer_Resources_part.objects.all().order_by('-id')[:6]
    footer_solution = Footer_Solution_part.objects.all().order_by('-id')[:6]

    page = request.GET.get('page', 1)
    paginator = Paginator(total_news_all, 6)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)
    data = {
        "news_section": news_section,
        "total_news": users,

        "header_nav": header_nav,
        "footer_fist_par": footer_fist_par,
        "footer_resources": footer_resources,
        "footer_solution": footer_solution,
    }
    return render(request, 'Latest_News.html', data)


def Latest_News_details(request, id):
    news_details = get_object_or_404(Latest_News_Post, id=id)
    Recent_Post = Latest_News_Post.objects.all().order_by('-id')[:3]
    category = Latest_News_Category.objects.all().order_by('-id')[:6]

    header_nav = Header_navbar.objects.latest('id')  # get_object_or_404()
    footer_fist_par = Footer_First_part.objects.latest('id')  # get_object_or_404()
    footer_resources = Footer_Resources_part.objects.all().order_by('-id')[:6]
    footer_solution = Footer_Solution_part.objects.all().order_by('-id')[:6]

    data = {
        "news_details": news_details,
        "Recent_Post": Recent_Post,
        "category": category,

        "header_nav": header_nav,
        "footer_fist_par": footer_fist_par,
        "footer_resources": footer_resources,
        "footer_solution": footer_solution,
    }
    return render(request, 'Latest_News_details.html', data)


def Latest_News_category(request, id):  # category show
    cat = get_object_or_404(Latest_News_Category, id=id)  # name import Category model
    Related_category = Latest_News_Post.objects.filter(category_news_post=cat.id)  # category import Article

    header_nav = Header_navbar.objects.latest('id')  # get_object_or_404()
    footer_fist_par = Footer_First_part.objects.latest('id')  # get_object_or_404()
    footer_resources = Footer_Resources_part.objects.all().order_by('-id')[:6]
    footer_solution = Footer_Solution_part.objects.all().order_by('-id')[:6]

    data = {
        "category_name": cat,
        "Related_category_show": Related_category,

        "header_nav": header_nav,
        "footer_fist_par": footer_fist_par,
        "footer_resources": footer_resources,
        "footer_solution": footer_solution,
    }
    return render(request, 'individual_news_category_show.html', data)


def search(request):
    header_nav = Header_navbar.objects.latest('id')  # get_object_or_404()
    footer_fist_par = Footer_First_part.objects.latest('id')  # get_object_or_404()
    footer_resources = Footer_Resources_part.objects.all().order_by('-id')[:6]
    footer_solution = Footer_Solution_part.objects.all().order_by('-id')[:6]

    try:
        q = request.POST.get('search')

    except:
        q = None
    if q:
        search_pro = Latest_News_Post.objects.filter(title__icontains=q)

        # search_pro = Article.objects.filter(Q(name__icontains='Boston') | Q(state__icontains='NY')

        data = {
            "Latest_News_Post": search_pro,
            "header_nav": header_nav,
            "footer_fist_par": footer_fist_par,
            "footer_resources": footer_resources,
            "footer_solution": footer_solution,

        }
        if search_pro.exists():
            return render(request, 'search.html', data)

        else:
            return render(request, 'Search_not_found.html', data)

    else:
        data = {
            "header_nav": header_nav,
            "footer_fist_par": footer_fist_par,
            "footer_resources": footer_resources,
            "footer_solution": footer_solution,

        }
        return render(request, 'Error_440.html', data)
