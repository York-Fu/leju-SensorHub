#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from sys import path
import os
import yaml

import rospy
from sensor_msgs.msg import Imu
from sensor_msgs.msg import ChannelFloat32
from sensor_msgs.msg import RelativeHumidity
from sensor_msgs.msg import Temperature
from sensor_msgs.msg import Illuminance
from sensor_msgs.msg import FluidPressure
from sensor_msgs.msg import Range
from bodyhub.msg import SensorRawData
from SensorHubServiceProcess import SensorHubServiceInit

# sensorNameIDFilePath = "/home/dm/catkin_ws/src/bodyhub/config/sensorNameID.yaml"
sensorNameIDFilePath = os.path.abspath(os.path.join(os.getcwd(),"MyFile/catkin_workspace/src/sensor_hub/config/sensorNameID.yaml"))
sensorDataDict = dict()




class sensor_hub():
    def __init__(self, IDname_dict):

        self.IDname_dict = IDname_dict
        self.orientation = [0,0,0,0,0,0,0,0,0]
        self.angular_velocity = [0,0,0,0,0,0,0,0,0]
        self.linear_acceleration = [0,0,0,0,0,0,0,0,0]

        rospy.Subscriber("MediumSize/BodyHub/SensorRaw", SensorRawData, self.sensor_raw_callback)
        self.mpu6050_pub = rospy.Publisher('MediumSize/SensorHub/Imu', Imu, queue_size=1)
        self.sensor_pub = rospy.Publisher('MediumSize/SensorHub/SensorData', ChannelFloat32, queue_size=1)
        # fftest
        self.mmm=0
        self.sensor_CF1 = rospy.Publisher('MediumSize/SensorHub/sensor_CF1', ChannelFloat32, queue_size=1)
        self.sensor_Humidity = rospy.Publisher('MediumSize/SensorHub/Humidity', RelativeHumidity, queue_size=1)
        self.sensor_Temperature = rospy.Publisher('MediumSize/SensorHub/Temperature', Temperature, queue_size=1)
        self.sensor_Illuminance = rospy.Publisher('MediumSize/SensorHub/Illuminance', Illuminance, queue_size=1)
        self.sensor_Distance = rospy.Publisher('MediumSize/SensorHub/sensor_Distance', Range, queue_size=1)
        


        self.sensor_FootPressure = rospy.Publisher('MediumSize/SensorHub/FootPressure', ChannelFloat32, queue_size=1)
        self.sensor_MAG = rospy.Publisher('MediumSize/SensorHub/sensor_MAG', ChannelFloat32, queue_size=1)
        self.sensor_Fire = rospy.Publisher('MediumSize/SensorHub/sensor_Fire', ChannelFloat32, queue_size=1)
        self.sensor_PIR = rospy.Publisher('MediumSize/SensorHub/sensor_PIR', ChannelFloat32, queue_size=1)
        self.sensor_Touch = rospy.Publisher('MediumSize/SensorHub/sensor_Touch', ChannelFloat32, queue_size=1)
        # fftest end


    def hexTo16int(self, j):
        d = 0x8000
        i = j
        if (j&d == 0):
            ii = i
            iii = ii
            return iii *1
        else:
            ii = i
            iii = ~(ii-1)
            iiii = iii & 0x7fff
            return iiii * -1

    



    def sensor_raw_callback(self,rawdata):

        sensor_count = 0
        sensor_id = ()
        sensor_address = ()
        sensor_length = ()
        sensor_data = ()

        sensor_id = rawdata.sensorReadID
        sensor_count = rawdata.sensorCount
        sensor_address = rawdata.sensorStartAddress
        sensor_length = rawdata.sensorReadLength
        sensor_data = rawdata.sensorData
        sensor_data_length = rawdata.dataLength

        data_index = 0
        sensorDataDict = {}
        for idNum in range(sensor_count):
            sensorDataDict[ord(sensor_id[idNum])] = sensor_data[data_index:(data_index+sensor_length[idNum])]
            data_index = sensor_length[idNum]

        # fftest
        self.mmm += 1
        sensor_id_list = list(sensor_id)
        for i in range(9):
            sensorDataDict[i+i*10] = [i,i,i,i,i]
            sensor_count = sensor_count+1
            sensor_id_list.append(chr(i+i*10))
        # fftest end

        # 打印data字典
        rospy.loginfo("sensorDataDict:")
        for idNum in range(sensor_count):
            print(ord(sensor_id_list[idNum]))
            rospy.loginfo(sensorDataDict[ord(sensor_id_list[idNum])])

            
        #IMU publish
        if 200 in sensorDataDict:
            self.angular_velocity[0] = self.hexTo16int(sensorDataDict[200][0] + sensorDataDict[200][1] * 256)    #Gyro_x
            self.angular_velocity[1] = self.hexTo16int(sensorDataDict[200][2] + sensorDataDict[200][3] * 256)    #Gyro_y
            self.angular_velocity[2] = self.hexTo16int(sensorDataDict[200][4] + sensorDataDict[200][5] * 256)    #Gyro_z
            self.linear_acceleration[0] = self.hexTo16int(sensorDataDict[200][6] + sensorDataDict[200][7] * 256)      #ACC_x
            self.linear_acceleration[1] = self.hexTo16int(sensorDataDict[200][8] + sensorDataDict[200][9] * 256)      #ACC_y
            self.linear_acceleration[2] = self.hexTo16int(sensorDataDict[200][10] + sensorDataDict[200][11] * 256)    #ACC_z
            self.mpu6050_pub.publish(orientation_covariance=self.orientation,angular_velocity_covariance=self.angular_velocity,linear_acceleration_covariance=self.linear_acceleration)
        
        #fftest publish
        if 11 in sensorDataDict:
            print("11111","ChannelFloat32")
            self.sensor_CF1.publish(name="channel111",values=[self.mmm,12,13])
        if 22 in sensorDataDict:
            print("22222","RelativeHumidity")
            self.sensor_Humidity.publish(relative_humidity=86,variance=566)
        if 33 in sensorDataDict:
            print("33333","Temperature")
            self.sensor_Temperature.publish(temperature=27,variance=702)
        if 44 in sensorDataDict:
            print("44444","Illuminance")
            self.sensor_Illuminance.publish(illuminance=52,variance=258)
        if 55 in sensorDataDict:
            print("55555","FootPressure")
            self.sensor_FootPressure.publish(name="sensor_FootPressure_L_R",values=[78,12])
        if 102 in sensorDataDict:
            self.sensor_Illuminance.publish(illuminance=sensorDataDict[102][0],variance=sensorDataDict[102][1])
            
        
        print("11126","sensor_Distance")
        self.sensor_Distance.publish(min_range=2,max_range=0.3,range=1.11)
        print("11127","sensor_Fire")
        self.sensor_Fire.publish(name="sensor_Fire",values=[77,12,13])
        print("11128","sensor_PIR")
        self.sensor_PIR.publish(name="sensor_PIR",values=[78,12,13])
        print("11129","sensor_Touch")
        self.sensor_Touch.publish(name="sensor_Touch",values=[79,12,13])
        #fftest publish end
        
        for i_d in sensor_id:
            sensorNum = ord(i_d)
            if self.IDname_dict.get(sensorNum):
                id_name = self.IDname_dict[sensorNum]
                self.sensor_pub.publish(name=id_name,values=sensorDataDict[sensorNum])




if __name__ == '__main__':

    try:
        
        # 初始化ros节点
        rospy.init_node('SensorHubNode', anonymous=True, log_level=rospy.INFO)# DEBUG INFO ERROR WARN
        print('Starting SensorHubNode node')
        SensorHubServiceInit()

        sensor_nameID_yaml = open(sensorNameIDFilePath)
        sensor_nameID_doc = sensor_nameID_yaml.read()
        sensor_nameID_dict = yaml.load(sensor_nameID_doc)
        rospy.loginfo(sensor_nameID_dict)

        # sensor_IDname_dict
        sensor_IDname_dict = {}
        for sensor_name in sensor_nameID_dict["sensorNameID"]:
            sensor_IDname_dict[sensor_nameID_dict["sensorNameID"][sensor_name]] = sensor_name
        rospy.loginfo(sensor_IDname_dict)

        sensor_hub(sensor_IDname_dict)

        rospy.spin()

    except KeyboardInterrupt:
        rospy.logwarn ("Shutting down SensorHub node.")