from applications.serializers import PQualifiedCvSerializers, PUnQualifiedCvSerializers
from applications.models import QualifiedCv, UnQualifiedCv
from rest_framework.views import APIView
from rest_framework.response import Response
'from django.contrib.auth import get_user_model'
User = get_user_model()

# Create your views here.


class CustomerView(APIView):
    def get(self, request, format=None):
        try:
            user = self.request.user
            useremail = user.email
            username = user.name
            userid = user.id
            applications_list = []
            qualified = QualifiedCv.objects.filter(user=userid)
            unqualified = UnQualifiedCv.objects.filter(user=userid)

            for i in qualified:
                applications_list.append(PQualifiedCvSerializers(i).data)
            for i in unqualified:
                applications_list.append(PUnQualifiedCvSerializers(i).data)

            user = User.objects.get(id=user.id)
            return Response({'useremail': useremail, 'username': username, 'apps': applications_list})
        except:
            return Response({'error': 'something went wrong while getting User data'})
