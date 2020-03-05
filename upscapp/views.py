from django.shortcuts import render, get_object_or_404
from .models import ServicesData, FeedBackData, Post, Comment
from .forms import FeedbackForm, ContactForm, CommentForm, PostForm
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.core.mail import send_mail
from django.http import HttpResponse
from django.utils import timezone
from django.contrib.contenttypes.models import ContentType


@login_required
def homeview(request):
    return render(request, 'home.html')


# @login_required
# def servicesview(request):
#     services = ServicesData.objects.all()
#     key = request.GET.get("search_key", "")
#     if key:
#         services = ServicesData.objects.filter(subject_name__icontains=key)
#     page = request.GET.get('page', 1)
#     paginator = Paginator(services, 2)
#     try:
#         services = paginator.page(page)
#     except PageNotAnInteger:
#         services = paginator.page(1)
#     except EmptyPage:
#         services = paginator.page(paginator.num_pages)
#     return render(request, 'services.html', {'services': services, 'key': key})


@login_required
def servicesview(request):
    # subject_instructor_name = ServicesData.objects.all().values_list('subject_instructor_name', flat=True)
    subject_instructor_name = ServicesData.objects.order_by(
        'subject_instructor_name').values_list('subject_instructor_name', flat=True).distinct()
    sub = request.GET.get("search_key", "")
    q_objects = Q()
    if sub:
        q_objects.add(Q(subject_name__icontains=sub), Q.AND)
    if q_objects:
        services = ServicesData.objects.filter(q_objects)
    else:
        services = ServicesData.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(services, 2)
    try:
        services = paginator.page(page)
    except PageNotAnInteger:
        services = paginator.page(1)
    except EmptyPage:
        services = paginator.page(paginator.num_pages)
    return render(request, 'services.html',
                  {'services': services, 'sub': sub, 'subject_instructor_name': subject_instructor_name})


@login_required
def contactview(request):
    if request.method == 'POST':
        cform = ContactForm(request.POST)
        if cform.is_valid():
            sender_name = cform.cleaned_data['name']
            sender_email = cform.cleaned_data['email']
            message = "{0} has sent you a new message:\n\n{1}".format(
                sender_name, cform.cleaned_data['message'])
            send_mail('Enquiry', message, sender_email, [
                      'manas@micropyramid.com', 'manasranjanpati94@gmail.com'])
            return HttpResponse('Thanks for contacting us!')
    else:
        cform = ContactForm()

    return render(request, 'contact.html', {'cform': cform})


@login_required
def gallaryview(request):
    return render(request, 'gallary.html')


@login_required
def feedbackview(request):
    if request.method == "POST":
        fform = FeedbackForm(request.POST)
        if fform.is_valid():
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            adress = request.POST.get('adress')
            email = request.POST.get('adress')
            subject = request.POST.get('subject')
            feedback = request.POST.get('feedback')

            data = FeedBackData(
                first_name=first_name,
                last_name=last_name,
                adress=adress,
                email=email,
                subject=subject,
                feedback=feedback

            )

            data.save()
            fform = FeedbackForm
            return render(request, 'feedback.html', {'fform': fform})
    else:
        fform = FeedbackForm()
        return render(request, 'feedback.html', {'fform': fform})


@login_required
def post_list(request):
    post = Post.objects.filter(
        published_date__lte=timezone.now()).order_by('published_date')
    pie = request.GET.get("search_key", "")
    if pie:
        post = Post.objects.filter(title__icontains=pie)
    page = request.GET.get('page', 1)
    paginator = Paginator(post, 2)
    try:
        post = paginator.page(page)
    except PageNotAnInteger:
        post = paginator.page(1)
    except EmptyPage:
        post = paginator.page(paginator.num_pages)
    return render(request, 'post_list.html', {'post': post, 'pie': pie})


@login_required
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    content_type = ContentType.objects.get_for_model(Post)
    obj_id = post.id
    comments = Comment.objects.filter(
        content_type=content_type, object_id=obj_id)
    parent_id = request.POST.get("parent_id")
    csubmit = False
    if parent_id:
        content_type = ContentType.objects.get_for_model(Comment)
        Comment.objects.create(content_type=content_type, object_id=parent_id,
                               parent_id=parent_id,
                               user=request.user,
                               text=request.POST.get("text"))
    if request.method == 'POST':
        form = CommentForm(data=request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.content_type = content_type
            new_comment.user = request.user
            new_comment.save()
            csubmit = True
    else:
        form = CommentForm()

    page = request.GET.get('page', 1)
    paginator = Paginator(comments, 2)
    try:
        comments = paginator.page(page)
    except PageNotAnInteger:
        comments = paginator.page(1)
    except EmptyPage:
        comments = paginator.page(paginator.num_pages)
    return render(request, 'post_detail.html', {'post': post, 'comments': comments, 'csubmit': csubmit, 'form': form})


@login_required
def postcreation_view(request):
    if request.method == "POST":
        pform = PostForm(request.POST)
        if pform.is_valid():
            title = request.POST.get('title'),
            content = request.POST.get('content')
            published_date = request.POST.get('published_date')
            data = Post(
                title=title,
                content=content,
                published_date=published_date
            )
            data.save()
            return render(request, 'post_create.html', {'pform': pform})
    else:
        pform = PostForm(request.POST)
    return render(request, 'post_create.html', {'pform': pform})
