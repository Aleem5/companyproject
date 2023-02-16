from django.contrib import admin

from department.models import Employee

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('emp_id',  'name', 'manager')
    list_filter = ( 'manager', )
    list_per_page = 5

admin.site.register(Employee , EmployeeAdmin)

admin.site.site_header = 'Employee Admin'
admin.site.site_title = 'Employee Admin Portal'
admin.site.index_title = 'Welcome to Employee Portal'