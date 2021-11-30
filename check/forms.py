from django.forms import ModelForm
from .models import Todo_safe, Todo_unsafe, user

class Todosafeform(ModelForm):

    class Meta:
        model = Todo_safe
        fields = '__all__'

class Todounsafeform(ModelForm):

    class Meta:
        model = Todo_unsafe
        fields = '__all__'

class userform(ModelForm):

    class Meta:
        model = user
        fields = '__all__'

