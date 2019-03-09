from rest_framework import serializers

class VehicleSerializer(serializers.ModelSerializer):
    coordinate = serializers.SerializerMethod('get_vehicle_coodinate')
    class Meta :
        fields = ['name','coordinate']
    def get_vehicle_coodinate(self,vehicle_obj):
        coordinate = {'lat':vehicle_obj.latitude,'long':vehicle_obj.logitude}
        return coordinate
