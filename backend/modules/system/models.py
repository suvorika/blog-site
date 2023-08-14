from django.db import models
from django.urls import reverse
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.exceptions import ObjectDoesNotExist
from django.utils import timezone
from django.core.cache import cache

# from datetime import date, timedelta
from modules.services.utils import unique_slugify
from django.core.validators import FileExtensionValidator
from django.contrib.auth.models import User
from modules.services.utils import unique_slugify
from django.contrib.auth import get_user_model

User = get_user_model()


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    slug = models.SlugField(verbose_name="URL", max_length=255, blank=True, unique=True)
    following = models.ManyToManyField(
        "self",
        verbose_name="Подписки",
        related_name="followers",
        symmetrical=False,
        blank=True,
    )
    avatar = models.ImageField(
        verbose_name="Аватар",
        upload_to="images/avatars/%Y/%m/%d/",
        default="images/avatars/default1.png",
        blank=True,
        validators=[FileExtensionValidator(allowed_extensions=("png", "jpg", "jpeg"))],
    )
    bio = models.TextField(max_length=500, blank=True, verbose_name="Информация о себе")
    birth_date = models.DateField(null=True, blank=True, verbose_name="Дата рождения")

    class Meta:
        db_table = "app_profiles"
        ordering = ("user",)
        verbose_name = "Профиль"
        verbose_name_plural = "Профили"

    def save(self, *args, **kwargs):
        """
        Сохранение полей модели при их отсутствии заполнения
        """
        if not self.slug:
            self.slug = unique_slugify(self, self.user.username)
        super().save(*args, **kwargs)

    def __str__(self):
        """
        Возвращение строки
        """
        return self.user.username

    def get_absolute_url(self):
        """
        Ссылка на профиль
        """
        return reverse("profile_detail", kwargs={"slug": self.slug})

    def is_online(self):
        last_seen = cache.get(f"last-seen-{self.user.id}")
        if last_seen is not None and timezone.now() < last_seen + timezone.timedelta(
            seconds=300
        ):
            return True
        return False

    @property
    def get_avatar(self):
        if self.avatar:
            return self.avatar.url
        return (
            f"https://ui-avatars.com/api/?size=190&background=random&name={self.slug}"
        )


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        try:
            instance.profile.save()
        except ObjectDoesNotExist:
            Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    try:
        instance.profile.save()
    except ObjectDoesNotExist:
        Profile.objects.create(user=instance)


class Feedback(models.Model):
    """
    Модель обратной связи
    """

    subject = models.CharField(max_length=255, verbose_name="Тема письма")
    email = models.EmailField(max_length=255, verbose_name="Электронный адрес (email)")
    content = models.TextField(verbose_name="Содержимое письма")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Дата отправки")
    ip_address = models.GenericIPAddressField(
        verbose_name="IP отправителя", blank=True, null=True
    )
    user = models.ForeignKey(
        User,
        verbose_name="Пользователь",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = "Обратная связь"
        verbose_name_plural = "Обратная связь"
        ordering = ["-time_create"]
        db_table = "app_feedback"

    def __str__(self):
        return f"Вам письмо от {self.email}"
