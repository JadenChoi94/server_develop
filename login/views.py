from rest_framework.views import APIView
from rest_framework.response import Response
from .models import LoginUser
from django.contrib.auth.hashers import make_password, check_password


class AppLogin(APIView):
    def post(self, request):
        user_id = request.data.get('user_id', "")
        user_pw = request.data.get('user_pw', "")
        user = LoginUser.objects.filter(user_id=user_id).first()
        if user is None:
            return Response(dict(msg="해당 ID의 사용자가 없습니다."))
        if check_password(user_pw, user.user_pw):
            return Response(dict(msg="로그인 성공"))
        else:
            return Response(dict(msg="로그인 실패. 패스워드 불일치"))

class RegistUser(APIView):
    def post(self, request):
        user_id = request.data.get('user_id', "")
        user_pw = request.data.get('user_pw', "")
        user_pw_crypted = make_password(user_pw)    # 암호화

        if LoginUser.objects.filter(user_id=user_id).exists():
            # DB에 있는 값 출력할 때 어떻게 나오는지 보려고 user 객체에 담음
            user = LoginUser.objects.filter(user_id=user_id).first()
            data = dict(
                msg="이미 존재하는 아이디입니다.",
                user_id=user.user_id,
                user_pw=user.user_pw
            )
            return Response(data)

        LoginUser.objects.create(user_id=user_id, user_pw=user_pw_crypted)

        data = dict(
            user_id=user_id,
            user_pw=user_pw_crypted
        )

        return Response(data=data)