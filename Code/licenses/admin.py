from django.contrib import admin
from licenses.models import License
from licenses.models import Section
from licenses.models import Paragraph


admin.site.register(License)
admin.site.register(Section)
admin.site.register(Paragraph)
