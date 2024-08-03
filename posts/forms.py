from django import forms

class PostForm(forms.Form):
    title = forms.CharField(max_length=100)
    content = forms.CharField()
    image = forms.ImageField()


    def clean_title(self):
        title = self.cleaned_data.get('title')
        if title == "python":
            raise forms.ValidationError("Название не может быть ")
        return title


    def clean(self):
        title = self.cleaned_data.get('title')
        content = self.cleaned_data.get('content')
        if title.lower() == content.lower():
            raise forms.ValidationError("Заголовок и контент не могут совпадать ")
        return self.cleaned_data