from django.db import models
from django.conf import settings
# from allauth.account.models import EmailAddress


def _path_to_avatar(instance, filename):
    return '{user_id}/{dirname}/{filename}'.format(
                        user_id=instance.user.id,
                        dirname='avatar',
                        filename=filename)

# Create model here

class UserProfile(models.Model):
    """
    User's profile adding more information for Django Auth User
    """
    user = models.OneToOneField(settings.AUTH_USER_MODEL, primary_key=True, related_name='user_profile')
    avatar = models.ImageField(upload_to=_path_to_avatar, blank=True, default='', max_length=257)

    # def account_verified(self):
    #     verified = False
    #     if self.user.is_authenticated:
    #         verified = EmailAddress.objects.filter(
    #                                     email=self.user.email).exists()
    #     return verified


class Document(models.Model):
    docfile = models.FileField(upload_to='documents/%Y/%m/%d')

