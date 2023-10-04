# from django.core.mail import EmailMessage, BadHeaderError
# from templated_mail.mail import BaseEmailMessage
from django.shortcuts import render
from .tasks import notify_customers


def say_hello(request):
    notify_customers.delay("Hello")

    # try:
    #     message = BaseEmailMessage(
    #         template_name="emails/hello.html", context={"name": "mosh"}
    #     )
    #     message.send(["user@uuu.com"])
    # except BadHeaderError:
    #     pass
    return render(request, "hello.html", {"name": "Mosh"})
