from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError('Email field should not be empty')
        if not username:
            raise ValueError('Username field should not be empty')
        user = self.model(email=self.normalize_email(email), username=username)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):
        if not email:
            raise ValueError('Email field should not be empty')
        if not username:
            raise ValueError('Username field should not be empty')
        user = self.model(
            email=self.normalize_email(email),
            username=username,
            is_staff=True,
            is_superuser=True
        )
        user.is_admin = True
        user.set_password(password)
        user.save(using=self._db)
        return user
