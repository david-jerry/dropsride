from django import forms
from django.forms import ModelForm

from .models import News

class NewsForm(ModelForm):
    class Meta:
        model = News
        fields = ["image", "title", "summary", "keywords", "draft", "content", "audio", "tags"]

    def clean_image(self):
        data = self.cleaned_data["image"]
        if data == None or data == "":
            raise forms.ValidationError("News post requires a cover image")
        return data

    def clean_title(self):
        data = self.cleaned_data["title"]
        if data == "":
            raise forms.ValidationError("News title is required.")
        return data

    def clean_summary(self):
        data = self.cleaned_data["summary"]
        if data == "":
            raise forms.ValidationError("Summary is required for SEO.")
        elif len(data) < 50:
            raise forms.ValidationError("News Summary must be at least 50 characters long.")
        return data

    def clean_keywords(self):
        data = self.cleaned_data["keywords"]
        if data == "":
            raise forms.ValidationError("Keywords is required for SEO.")
        elif " , " not in data:
            raise forms.ValidationError("This field must contain a comma. This is a list of keywords to be used for SEO.")
        return data

    # def save(self, request):
    #     news = super().save(request)
    #     news.image = self.cleaned_data['image']
    #     news.title = self.cleaned_data['title']
    #     news.summary = self.cleaned_data['summary']
    #     news.keywords = self.cleaned_data['keywords']
    #     news.draft = self.cleaned_data['draft']
    #     news.content = self.cleaned_data['content']
    #     news.audio = self.cleaned_data['audio']
    #     news.tags = self.cleaned_data['tags']
    #     news.draft = True
    #     news.author = request.user
    #     news.save()
    #     return news


