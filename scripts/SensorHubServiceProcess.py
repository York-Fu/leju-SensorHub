
import os
import rospy
import yaml
from sensorhub.srv import SensorHubService, SensorHubServiceResponse

YamlFilePath = os.path.abspath(os.path.join(os.getcwd(),"MyFile/catkin_workspace/src/sensor_hub/config/sensorNameID.yaml"))



def RequestCallback(request):

    File = open(YamlFilePath)
    YamlDoc = yaml.load(File)
    #print("YamlDoc:",YamlDoc)
    File.close()

    SensorNameDict = YamlDoc["sensorNameID"]
    print("SensorNameDict:",SensorNameDict)
    
    if request.SensorName in SensorNameDict:
        SensorId = SensorNameDict[request.SensorName]
        print("Request:",request.SensorName, request.Instruct, request.Paramete) # print info
        if SensorId == 200:
            pass
        elif SensorId == 102:
            pass
        elif ensorId == 103:
            if request.Instruct == 'set':
                pass
        else:
            return SensorHubServiceResponse("error: not found id!")
        return SensorHubServiceResponse("operate successfully")
    else:
        return SensorHubServiceResponse("error: not found name!")
    

def SensorHubServiceInit():
    service = rospy.Service('/SensorHubService', SensorHubService, RequestCallback)
    print('Create service of /SensorHubService')