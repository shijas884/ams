from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=225)

    def __str__(self):
        return self.name

class Visitors(models.Model):
    name = models.CharField(max_length=225)

    def __str__(self):
        return self.name

    
class Schedule(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    purpose_title = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.company.name} - {self.purpose_title}"


class Slot(models.Model):
    STATUS_CHOICES = (
        ('booked', 'Booked'),
        ('open', 'Open'),
    )
    slot = models.ForeignKey('Schedule', on_delete=models.CASCADE, null=True)
    start_slot = models.TimeField()
    end_slot = models.TimeField()
    date = models.DateField()
    user = models.ForeignKey(Visitors, on_delete=models.CASCADE, null=True)
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='open',
        blank=True
    )

    def __str__(self):
        return f"{self.date} | {self.start_slot} - {self.end_slot} | {self.status}"
