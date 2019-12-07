from django.db import models


# Create your models here.
class Student(models.Model):
    student_id = models.CharField(max_length=200, blank=False)
    first_name = models.CharField(max_length=200, blank=False)
    last_name = models.CharField(max_length=200, blank=False)
    choices = (
        ('ยังไม่จ่าย', 'ยังไม่จ่าย'),
        ('จ่ายแล้ว', 'จ่ายแล้ว')
    )
    january = models.CharField(max_length=10, choices=choices, default='ยังไม่จ่าย')
    february = models.CharField(max_length=10, choices=choices, default='ยังไม่จ่าย')
    march = models.CharField(max_length=10, choices=choices, default='ยังไม่จ่าย')
    april = models.CharField(max_length=10, choices=choices, default='ยังไม่จ่าย')
    may = models.CharField(max_length=10, choices=choices, default='ยังไม่จ่าย')
    june = models.CharField(max_length=10, choices=choices, default='ยังไม่จ่าย')
    july = models.CharField(max_length=10, choices=choices, default='ยังไม่จ่าย')
    august = models.CharField(max_length=10, choices=choices, default='ยังไม่จ่าย')
    september = models.CharField(max_length=10, choices=choices, default='ยังไม่จ่าย')
    october = models.CharField(max_length=10, choices=choices, default='ยังไม่จ่าย')
    november = models.CharField(max_length=10, choices=choices, default='ยังไม่จ่าย')
    december = models.CharField(max_length=10, choices=choices, default='ยังไม่จ่าย')
    issues = models.CharField(max_length=50, default="No Issues")

    def __str__(self):
        return 'Student ID: {0} | Full Name: {1} {2}'.format(self.student_id, self.first_name, self.last_name)
