
def get_anonymous_user():
    from users.models import User

    anonymous_user, _ = User.objects.get_or_create(
        username="Anonymous", password='1234AnonymousUser',
    )
    return anonymous_user.pk
