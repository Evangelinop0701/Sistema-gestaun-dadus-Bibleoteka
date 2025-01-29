from django.db import models
from mainApp.models import Staff
import uuid
from django.contrib.auth.models import User

# class StaffUser(models.Model):
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     staff = models.OneToOneField(Staff, on_delete=models.CASCADE, related_name='staff_user')
#     user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_staff')

#     def __str__(self):
#         return f"Naran Staff: {self.staff.naran_staff} - Username: {self.user.username}"