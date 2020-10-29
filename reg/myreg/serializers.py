from rest_framework import serializers
from  myreg.models import Reg
class RegSerializer(serializers.ModelSerializer):
    class Meta:
        model =Reg
        fields = '__all__'
        
class RegSerializer2(serializers.ModelSerializer):
    class Meta:
        model =Reg
        fields = '__all__'        
        



