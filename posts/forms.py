from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'description', 'image', 'category', 'tags']

    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get("title")
        description = cleaned_data.get("description")

        if title and description and title.lower() == description.lower():
            raise forms.ValidationError("Title and description must be different")
        return cleaned_data

    def clean_title(self):
        title = self.cleaned_data["title"]
        if "python" in title.lower():
            raise forms.ValidationError("Title must not contain python")
        return title

    def clean_description(self):
        description = self.cleaned_data["description"]
        if len(description) < 3:
            raise forms.ValidationError("Too short text")
        return description