from django.db import models


class Employee(models.Model):
    emp_id = models.AutoField(primary_key=True, editable=False)
    name = models.CharField(max_length=100,)
    manager = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        # return f"Employee:{self.name} => Manager:{self.manager}"
        return f"{self.name}"

    class Meta:
        ordering = ["emp_id"]
