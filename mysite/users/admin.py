from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.core.mail import send_mail

from users.models import BlockEmailSender, BlockUser


class BlockUserAdmin(UserAdmin):
    list_display = (
        'username',
        'email',
        'is_staff',
        'first_name',
        'last_name',
        'apto_number'

    )
    fieldsets = UserAdmin.fieldsets


def sent_block_email(modeladmin, request, queryset):
    emails_to_sent = queryset.all()
    messages = []
    block_users = BlockUser.objects.all()
    for user in block_users:
        for email in emails_to_sent:
            send_mail(
                email.subject,
                '',
                'from@example.com',
                [user.email],
                fail_silently=False,
                html_message=email.email_html
            )


sent_block_email.short_description = "send email to block recidents"


class BlockEmailSenderAdmin(admin.ModelAdmin):
    list_display = ['subject', 'email_name', 'email_description']
    actions = [sent_block_email]


admin.site.register(BlockEmailSender, BlockEmailSenderAdmin)
