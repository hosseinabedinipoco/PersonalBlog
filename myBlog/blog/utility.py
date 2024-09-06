from users.models import User

def is_user(request):
    user_id = request.session.get('user_id')
    return user_id

def is_admin(request):
    user_id = request.session.get('user_id')
    if not user_id:
        return False
    user = User.objects.get(pk=user_id)
    return user.is_Admin