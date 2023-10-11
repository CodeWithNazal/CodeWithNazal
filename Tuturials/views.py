from django.shortcuts import render, get_object_or_404, redirect

from .models import Tutorial, TutorialChapter, TutorialChapterContent
from .models import Blog, BlogContent
from .models import News, NewsContent

def home(request):
    tutorials = Tutorial.objects.order_by('-created_at')[:3]
    blogs = Blog.objects.order_by('-created_at')[:3]
    news = News.objects.order_by('-created_at')[:5]

    return render(request, 'home.html',{ 'tutorials':tutorials, 'blogs':blogs, 'news':news})

def tutorials(request):
    is_superuser = request.user.is_superuser

    tutorials = Tutorial.objects.all().order_by("-created_at")
    return render(request, 'tutorials.html', {"tutorials":tutorials, "is_superuser":is_superuser})

def tutorial(request, tutorial_title):
    is_superuser = request.user.is_superuser

    tutorial = get_object_or_404(Tutorial, title=tutorial_title)
    chapters = tutorial.tutorialchapter_set.all()

    return render(request, 'tutorial.html', {'tutorial':tutorial, 'chapters':chapters, "is_superuser":is_superuser})

def chapter(request, tutorial_title, chapter_title):
    is_superuser = request.user.is_superuser
    
    tutorial = get_object_or_404(Tutorial, title=tutorial_title)
    chapters = tutorial.tutorialchapter_set.all()

    chapter_instance = get_object_or_404(TutorialChapter, tutorial=tutorial, title=chapter_title)

    chapter_content = chapter_instance.tutorialchaptercontent_set.all()

    return render(request, 'chapter.html', {'tutorial': tutorial, 'chapter': chapter_instance, 'chapter_content': chapter_content, 'is_superuser':is_superuser, 'chapters':chapters})


def source_code(request, tutorial_title):
    is_superuser = request.user.is_superuser

    tutorial = get_object_or_404(Tutorial, title=tutorial_title)
    source_codes = tutorial.tutorialsourcecode_set.all()

    return render(request, 'source_code.html', {'tutorial': tutorial, 'is_superuser':is_superuser, 'source_codes': source_codes})


def create_tutorial(request):
    if request.method == 'POST':
        title = request.POST.get('tutorial-content-title', '')
        description = request.POST.get('tutorial-content-description', '')
        filename = request.POST.get('tutorial-content-code-filename', '')
        code = request.POST.get('tutorial-content-code', '')
        image = request.FILES.get('tutorial-content-image', None)  # Include it if it exists

        tutorial_title = request.POST.get('tutorial-title', '')
        chapter_title = request.POST.get('chapter-title', '')

        tutorial = Tutorial.objects.get(title=tutorial_title)
        chapter = TutorialChapter.objects.get(tutorial=tutorial, title=chapter_title)

        # Create the model object with the provided data
        new_model = TutorialChapterContent(
            tutorial=tutorial,
            chapter=chapter,
            title=title,
            text=description,
            code_file_name=filename,
            code=code,
            image=image  # Include it even if it's None
        )
        new_model.save()

        # Redirect to a success page or wherever you want
        return redirect('chapter', tutorial_title=tutorial_title, chapter_title=chapter_title)

    return redirect('home')

def create_chapter(request):
    if request.method == 'POST':
        title = request.POST.get('tutorial-chapter-title', '')

        tutorial_title = request.POST.get('tutorial-title', '')

        tutorial = Tutorial.objects.get(title=tutorial_title)

        # Create the model object with the provided data
        new_model = TutorialChapter(
            tutorial=tutorial,
            title=title,
        )
        new_model.save()

        # Redirect to a success page or wherever you want
        return redirect('tutorial', tutorial_title=tutorial_title)

    return redirect('home')

def blogs(request):
    blogs = Blog.objects.all()
    return render(request, "blogs.html", {'blogs':blogs})

def blog(request, blog_title):
    is_superuser = request.user.is_superuser

    blog = get_object_or_404(Blog, title=blog_title)

    blog_contents = blog.blogcontent_set.all()

    return render(request, 'blog.html', {'blog':blog, 'blog_contents':blog_contents, 'is_superuser':is_superuser})

def create_blogcontent(request):
    if request.method == 'POST':
        title = request.POST.get('blog-content-title', '')
        description = request.POST.get('blog-content-description', '')
        filename = request.POST.get('blog-content-code-filename', '')
        code = request.POST.get('blog-content-code', '')
        image = request.FILES.get('blog-content-image', None)  # Include it if it exists

        blog_title = request.POST.get('blog-title', '')

        blog = Blog.objects.get(title=blog_title)

        new_model = BlogContent(
            blog=blog,
            title=title,
            description=description,
            code_file_name=filename,
            code=code,
            image=image  # Include it even if it's None
        )
        new_model.save()

        # Redirect to a success page or wherever you want
        return redirect('blog', blog_title=blog_title)

    return redirect('home')

def news_all(request):
    all_news = News.objects.all()
    return render(request, "news_all.html", {'all_news':all_news})

def news_instance(request, news_title):
    is_superuser = request.user.is_superuser

    single_news = get_object_or_404(News, title=news_title)
    news_contents = single_news.newscontent_set.all()

    return render(request, 'news_instance.html', {'single_news':single_news, 'news_contents': news_contents, 'is_superuser':is_superuser})

def create_news(request):
    if request.method == 'POST':
        title = request.POST.get('news-content-title', '')
        description = request.POST.get('news-content-description', '')
        image = request.FILES.get('news-content-image', None)  # Include it if it exists

        news_title = request.POST.get('news-title', '')

        news = News.objects.get(title=news_title)

        new_model = NewsContent(
            news=news,
            title=title,
            description=description,
            image=image  
        )
        new_model.save()

        # Redirect to a success page or wherever you want
        return redirect('news_instance', news_title=news_title)

    return redirect('home')    

def searched(request):
    if request.method == "POST":
        searchedval = request.POST['search']
        tutorials = Tutorial.objects.filter(title__contains=searchedval)
        blogs = Blog.objects.filter(title__contains=searchedval)
        news = News.objects.filter(title__contains=searchedval)

        return render(request, 'searched.html', {"searchedval":searchedval, "tutorials":tutorials, "blogs":blogs, "news":news})

    else:
        return redirect("home")