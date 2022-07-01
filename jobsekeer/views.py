
from rest_framework.generics import ListAPIView,RetrieveAPIView
from jobposter.models import Job_Post
from rest_framework.permissions import IsAuthenticated
from jobsekeer.serializer import ListSerializer
from rest_framework.response import Response

class ListAPI(RetrieveAPIView):
    serializer_class = ListSerializer
    queryset = Job_Post
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        obj = Job_Post.objects.all()
        serializer = ListSerializer(obj,many=True)
        return Response({"status":"success","detail":serializer.data})