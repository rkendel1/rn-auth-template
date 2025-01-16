from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User
from users.serializers import UserSerializer


class RegisterView(APIView):
    def post(self, request):
        data = request.data
        user = User.objects.create_user(
            username=data['username'],
            email=data['email'],
            password=data['password']
        )

        # Generate JWT tokens
        refresh = RefreshToken.for_user(user)
        access_token = str(refresh.access_token)
        refresh_token = str(refresh)

        # Serialize the user data
        serializer = UserSerializer(user)

        return Response({
            'user': serializer.data,
            'access': access_token,
            'refresh': refresh_token,
        })