from __future__ import unicode_literals

from django.db import models
from django.conf import settings


class Profile(models.Model):
	#BOOL_CHOICES = ((True, 'Yes'), (False, 'No'))

	user = models.OneToOneField(settings.AUTH_USER_MODEL)
	tel = models.CharField(max_length=10,blank=True,null=True)
	direccion = models.CharField(max_length=10,blank=True,null=True)
	#is_soporte = models.BooleanField(choices=BOOL_CHOICES)

	def __str__(self):
		return 'Perfil del usuario {}'.format(self.user.username)