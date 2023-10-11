from django.contrib import admin

from .models import Tutorial, TutorialChapter, TutorialChapterContent, TutorialSourceCode
from .models import Blog, BlogContent
from .models import News, NewsContent

admin.site.register(Tutorial)
admin.site.register(TutorialChapter)
admin.site.register(TutorialChapterContent)
admin.site.register(TutorialSourceCode)

admin.site.register(Blog)
admin.site.register(BlogContent)

admin.site.register(News)
admin.site.register(NewsContent)


