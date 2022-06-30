import time
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from django.conf import settings

from celery import shared_task

from stories.models import Subscriber, Story
from stories.publisher import Publish




@shared_task
def process_func():
    time.sleep(10)
    return 'Process done'


@shared_task
def send_mail_to_subscribers():
    # select email from Subscriber # (('idris',), ('idris'), ('idris'))
    email_list = Subscriber.objects.filter(is_active=True).values_list('email', flat=True)
    stories = Story.objects.all()
    # mail_text = render_to_string('email-subscribers.html', {
    #     'stories': stories, 
    # })
    mail_text = "salam"
    Publish(data={"body": mail_text, "subject": "News about site", "recipients": list(email_list), "subtype": "html"  }, event_type="send_mail")
    # msg = EmailMultiAlternatives(subject='Stories', body=mail_text, from_email=settings.EMAIL_HOST_USER, to=email_list, )
    # msg.attach_alternative(mail_text, "text/html")
    # msg.send()

# 1. background task
# 2. paralel
# 3. periodic task