from django.forms import ModelForm
from book_app.models import Book


class BookForm(ModelForm):
    class Meta:
        fields = ["title", "pages"]
        model = Book