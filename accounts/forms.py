from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User

# 회원가입
class CustomUserCreationForm(UserCreationForm):
    class Meta():
        model = User
        fields = ('username', 'profile_image', )

# 로그인
class CustomAuthenticationForm(AuthenticationForm):
    pass