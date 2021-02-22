from django import forms
from .models import Article, Comment


class ArticleForm(forms.ModelForm):
    title = forms.CharField(
        label='제목',
        widget=forms.TextInput(attrs={
            'class': 'my-title form-control',
            'placeholder': 'Enter the title',
            'maxlength': 10,
        })
    )
    content = forms.CharField(
        label='내용',
        widget=forms.Textarea(attrs={
            'class': 'my-content form-control',
            'rows': 5,
            'cols': 50,
        }),
        error_messages={
            'required': '내용 넣어라...'
        }
    )

    class Meta:
        model = Article
        fields = ['title', 'content',]

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        exclude = ['article', 'user',]   

        
# class ArticleForm(forms.Form):
#     REGION_A = 'seoul'
#     REGION_B = 'daejeon'
#     REGIONS = [
#         (REGION_A, '서울'),
#         (REGION_B, '대전'),
#     ]

#     title = forms.CharField(max_length=10)
#     content = forms.CharField(widget=forms.Textarea)
#     region = forms.ChoiceField(choices=REGIONS, widget=forms.RadioSelect)