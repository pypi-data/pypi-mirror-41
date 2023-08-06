# -*- coding: utf-8 -*-
import json
from django.conf import settings
from django.template import loader
from django.core.mail import EmailMultiAlternatives
from django.core.mail.backends.base import BaseEmailBackend

DEBUG_EMAIL_FILE_PATH = '/tmp/{}.json'.format(settings.PROJECT_NAME)


class EmailBackend(BaseEmailBackend):

    def send_messages(self, email_messages):
        messagens = []
        for message in email_messages:
            messagens.append(dict(from_email=message.from_email, to=', '.join(message.to), message=message.body))
        open(DEBUG_EMAIL_FILE_PATH, 'w').write(json.dumps(messagens))
        return len(messagens)


def _as_html(subject, message, actions=()):
    from djangoplus.admin.models import Settings
    url = 'http://{}'.format(settings.HOST_NAME or 'localhost:8000')
    app_settings = Settings.default()
    context = dict()
    context['subject'] = subject
    context['project_url'] = url
    context['project_name'] = app_settings.initials
    context['project_description'] = app_settings.name
    context['project_logo'] = app_settings.logo and '{}/media/{}'.format(url, app_settings.logo) or \
        '{}/static/images/mail.png'.format(url)
    context['actions'] = actions
    context['message'] = message.replace('\n', '<br>').replace('\t', '&nbsp;'*4)
    html = loader.render_to_string('mail.html', context)
    return html


def send_mail(subject, message, to, reply_to=None, actions=()):
    html = _as_html(subject, message, actions)
    if settings.SENDGRID_KEY:
        import sendgrid
        from sendgrid.helpers.mail import Email, Content, Mail
        sg = sendgrid.SendGridAPIClient(apikey=settings.SENDGRID_KEY)
        from_email = Email(settings.DEFAULT_FROM_EMAIL)
        to_email = Email(to)
        content = Content("text/html", html)
        mail = Mail(from_email, subject, to_email, content)
        if reply_to:
            mail.reply_to = Email(reply_to)
        response = sg.client.mail.send.post(request_body=mail.get())
        return response.status_code
    else:
        reply_to = reply_to and [reply_to] or None
        from_email = 'Não-Responder <{}>'.format(settings.DEFAULT_FROM_EMAIL)
        email = EmailMultiAlternatives(subject, 'Mensagem em anexo.', from_email, [to], reply_to=reply_to)
        email.attach_alternative(html, "text/html")
        return email.send()
