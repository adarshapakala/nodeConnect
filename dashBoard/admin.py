from django.contrib import admin
from .models import Questions
from .models import Platforms
from .models import Catogeries
from .models import QuestionGroup
from .models import UserCurrentQuestion

admin.site.register(Questions)
admin.site.register(Platforms)
admin.site.register(Catogeries)
admin.site.register(QuestionGroup)
admin.site.register(UserCurrentQuestion)


# Register your models here.
