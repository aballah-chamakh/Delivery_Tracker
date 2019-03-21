from rest_framework import serializers
from .models import Vehicle
from driver.models import Driver

class VehicleSerializer(serializers.ModelSerializer):
    coordinate = serializers.SerializerMethodField('get_vehicle_coodinate',read_only=True)
    driver = serializers.SerializerMethodField('get_current_driver',read_only=True)
    image = serializers.CharField(source='image.url',read_only=True)
    image_file = serializers.ImageField(source='image',write_only=True,required=False)
    driver_id = serializers.CharField(write_only=True,required=False)
    class Meta :
        model = Vehicle
        fields = ['id','delivery_company','name','coordinate','image','image_file','driver','driver_id','tracked']
    def get_vehicle_coodinate(self,vehicle_obj):
        coordinate = {'lat':vehicle_obj.latitude,'long':vehicle_obj.longitude}
        return coordinate
    def get_current_driver(self,vehicle_obj):
        #driver_info = {'driver_username':'no driver','driver_id':'no id'}
        if hasattr(vehicle_obj, 'driver') == True :
            driver_obj  = vehicle_obj.driver
            driver_info = {'driver_username':driver_obj.user.username,'driver_id':driver_obj.id}
            return driver_info
        return None

    def create(self,validated_data):
        image = validated_data.get('image_file')
        vehicle_name = validated_data.get('name')
        driver_id = validated_data.get('driver_id')
        vehicle_obj = self.Meta.model.objects.create(name=vehicle_name)
        print(image)
        if image is not None  :
            print('set image')
            vehicle_obj.image = image
            vehicle_obj.save()
        if driver_id is not None :
            driver_obj = Driver.objects.get(id=driver_id)
            driver_obj.vehicle = vehicle_obj
            driver_obj.save()
        return vehicle_obj
    def update(self, vehicle_obj, validated_data):
        # raise_errors_on_nested_writes('update', self, validated_data)
        print('let us update')
        for attr, value in validated_data.items():
            print(attr)
            # if attr == 'image' and image == None :
            #     print('image id None')
            #     continue

            if attr == 'driver_id' and value is not None :
                new_driver_obj = Driver.objects.get(id=value)
                if hasattr(vehicle_obj,'driver') :
                    old_driver_obj = vehicle_obj.driver
                    old_driver_obj.vehicle = None
                    old_driver_obj.save()
                new_driver_obj.vehicle = vehicle_obj
                new_driver_obj.save()
            else:
                setattr(vehicle_obj, attr, value)
        if validated_data.get('driver_id') is None and hasattr(vehicle_obj,'driver') :
            driver_obj = vehicle_obj.driver
            driver_obj.vehicle = None
            driver_obj.save()
        vehicle_obj.save()

        return vehicle_obj
