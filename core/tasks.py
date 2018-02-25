from Metaproject.celery import app
from .utils import send_activation_email
from .models import Profile


@app.task
def send_activation_email_task(profile_pk, host):
    profile = Profile.objects.get(pk=profile_pk)
    send_activation_email(profile, host)