from django import forms
from .models import Post

# we will create a form for our Post model.
# form's name is PostForm, and this form is a Modelform
class PostForm(forms.ModelForm): 

    class Meta:
    # I let Django know which Model should be used to create this form.
        model = Post
        # This fields should end up in our form.
        fields = ('title', 'text')