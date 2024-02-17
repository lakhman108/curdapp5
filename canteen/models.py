from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from django.utils.translation import gettext_lazy as _



class CustomUser(AbstractUser):
    # Add any custom fields here
    groups = models.ManyToManyField(
        Group,
        verbose_name=_('groups'),
        blank=True,
        related_name='customuser_set',  # Change 'customuser_set' to a unique name
        related_query_name='customuser',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=_('user permissions'),
        blank=True,
        related_name='customuser_set',  # Change 'customuser_set' to a unique name
        related_query_name='customuser',
        help_text=_('Specific permissions for this user.'),
    )

    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'
        verbose_name = _('user')
        verbose_name_plural = _('users')


class Service(models.Model):
    service_icon = models.CharField(max_length=100, blank=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
