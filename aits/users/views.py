from rest_framework import viewsets, permissions, generics
from .serializers import StudentSerializer, LecturerSerializer,RegistrarSerializer, UserSerializer
from .models import User

class LecturerListSerializer(UserSerializer):
    class Meta(UserSerializer.Meta):
        fields = ['id', 'email', 'first_name', 'last_name', 'role', 'lecturer_reg_number']

class LecturerViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = LecturerListSerializer
    permission_classes = [permissions.IsAuthenticated]
    
class RegisterStudentView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = StudentSerializer
    permission_classes = [permissions.AllowAny]

class RegisterLecturerView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = LecturerSerializer
    permission_classes = [permissions.AllowAny]

class RegisterRegistrarView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = RegistrarSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        if self.request.user.role == 'registrar':
            return User.objects.filter(role='lecturer')
        return User.objects.none()

    
