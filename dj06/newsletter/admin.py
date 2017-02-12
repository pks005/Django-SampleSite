from django.contrib import admin

# Register your models here.
from newsletter.forms import SignUpForm
from newsletter.models import SignUp

class extraInfo(admin.ModelAdmin):
    list_display = ['__str__', 'username', 'timestamp', 'updated']
    model = SignUpForm


admin.site.register(SignUp,extraInfo)