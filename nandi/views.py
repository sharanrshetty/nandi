from django.shortcuts import render

def home(request):
    return render(request, template_name='webpages/home.html')


def course_detail(request):
    return render(request, template_name='webpages/course-detail.html')