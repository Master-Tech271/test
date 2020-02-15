from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from drivingtest.models import *


# Register your models here.
@admin.register(Question)
class QuestionAdmin(ImportExportModelAdmin):
        pass

@admin.register(Option)
class OptionAdmin(ImportExportModelAdmin):
        pass
