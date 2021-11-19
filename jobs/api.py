from .models import Jobs,Aplay
from .serializers import JobSerilizer ,AplaySerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics , mixins


@api_view(['GET'])
def jobsapi(request):
    all_jobs = Jobs.objects.all()
    data = JobSerilizer(all_jobs , many=True).data
    return Response({'data':data})
    
@api_view(['GET'])
def jobdetail(request,id):
    job_detail=Jobs.objects.get(id=id)
    data = JobSerilizer(job_detail).data
    return Response({'data':data})
    
#get only 
class Jobs_Class_Api(generics.ListAPIView):
    model=Jobs
    queryset=Jobs.objects.all()
    serializer_class=JobSerilizer
 #get only using id   
class Job_Detail_Api(generics.RetrieveUpdateDestroyAPIView):
    queryset=Jobs.objects.all()
    serializer_class=JobSerilizer
    lookup_field='id'
    
#post only
class mixins_list(mixins.RetrieveModelMixin,generics.GenericAPIView):
    queryset=Jobs.objects.all()
    serializer_class=JobSerilizer
    #def get(self , request):
        #return self.list(request)
    def post(self ,request):
        return self.create(request)
class mixins_up_des(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
    queryset=Jobs.objects.all()
    serializer_class=JobSerilizer
    def get(self , request,pk):
        return self.retrieve(request)
    def put(self ,request,pk):
        return self.update(request)
    def delet(self ,request,pk):
        return self.destroy(request)
        
@api_view(['GET'])
def aplay_api(request):
    aply_list = Aplay.objects.all()
    data = AplaySerializer(aply_list , many=True).data
    return Response({'data':data})
    