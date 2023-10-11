from django.db import models

class Tutorial(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True, max_length=200)
    thumbnail = models.ImageField(upload_to="images/",default="images/Projectile Shooter.png")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class TutorialChapter(models.Model):
    tutorial = models.ForeignKey(Tutorial, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.title} in {self.tutorial.title}"

class TutorialChapterContent(models.Model):
    tutorial = models.ForeignKey(Tutorial, on_delete=models.CASCADE)
    chapter = models.ForeignKey(TutorialChapter, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, null=True, blank=True)
    text = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='tutorial_chapter_content/', null=True, blank=True)
    code_file_name = models.CharField(max_length=30, null=True, blank=True)
    code = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.title} in {self.chapter.title} of {self.tutorial.title}"

class TutorialSourceCode(models.Model):
    tutorial = models.ForeignKey(Tutorial, on_delete=models.CASCADE)
    code_file_name = models.CharField(max_length=30, null=True, blank=True)
    code = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.code_file_name} in {self.tutorial.title}"

class Blog(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class BlogContent(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='blog_content/', null=True, blank=True)
    code_file_name = models.CharField(max_length=30, null=True, blank=True)
    code = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.title} in {self.blog.title}"


class News(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=200, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class NewsContent(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='news_content/', null=True, blank=True)

    def __str__(self):
        return f"{self.title} in {self.news.title}"

"""


"""