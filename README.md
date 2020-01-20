# sensorhub Package

## 1.概述
用于将bodyhub包发布的传感器原始数据，转换为ROS标准数据格式。
## 2.如何运行
```
rosrun sensorhub SensorHubNode.py
```
## 3.节点API
### 3.1.话题
#### 3.1.1.Subscribed Topics
|名称|类型|说明|
|:-:|:-:|:-:|
|/MediumSize/BodyHub/SensorRaw|SensorRawData|bodyhub节点发布的传感器原始数据|
- /MediumSize/BodyHub/SensorRaw  
  详情可参考bodyhub节点话题部分的说明。
#### 3.1.2.Published Topics
|名称|类型|说明|
|:-:|:-:|:-:|
|MediumSize/SensorHub/Imu|[Imu][sensor_msgs/Imu]|imu传感器姿态数据|
|MediumSize/SensorHub/MagneticField|[MagneticField][sensor_msgs/MagneticField]|磁场传感器测得的磁场强度在三个方向的分量|
|MediumSize/SensorHub/BatteryState|[BatteryState][sensor_msgs/BatteryState]|机器人电源状态|
|MediumSize/SensorHub/Range|[Range][sensor_msgs/Range]|测距传感器测量值|
|MediumSize/SensorHub/sensor_CF1|[ChannelFloat32][sensor_msgs/ChannelFloat32]|带通道标识的32位浮点型数据|
|MediumSize/SensorHub/Illuminance|[Illuminance][sensor_msgs/Illuminance]|光照度传感器测量值|
|MediumSize/SensorHub/Temperature|[Temperature][sensor_msgs/Temperature]|温度传感器测量值|
|MediumSize/SensorHub/Humidity|[RelativeHumidity][sensor_msgs/RelativeHumidity]|湿度传感器测量值|
- MediumSize/SensorHub/Imu  
  imu传感器姿态数据，包含三轴角速度、三轴加速度物理值，单位参考类型链接。
- MediumSize/SensorHub/MagneticField  
  磁场传感器测得的磁场强度的物理值，包含在xyz三个方向的分量，单位参考类型链接。
- MediumSize/SensorHub/BatteryState  
  机器人电源状态，详细参考[sensor_msgs/BatteryState][sensor_msgs/BatteryState]。
- MediumSize/SensorHub/Range  
  测距传感器测量的物理数值，单位参考类型链接。
- MediumSize/SensorHub/sensor_CF1  
  带通道标识的32位浮点型数据，用来表示部分传感器测量的状态，详细参考代码，单位参考类型链接。
- MediumSize/SensorHub/Illuminance  
  光照度传感器测量的环境光强的物理数值，单位参考类型链接。
- MediumSize/SensorHub/Temperature  
  温度传感器测量的环境温度的物理数值，单位参考类型链接。
- MediumSize/SensorHub/RelativeHumidity  
  湿度传感器测量的环境湿度的百分比，单位参考类型链接。
### 3.2.服务
无
### 3.3.参数
无
## 附录
[sensor_msgs/Imu]: http://docs.ros.org/api/sensor_msgs/html/msg/Imu.html
[sensor_msgs/MagneticField]: http://docs.ros.org/api/sensor_msgs/html/msg/MagneticField.html
[sensor_msgs/BatteryState]: http://docs.ros.org/api/sensor_msgs/html/msg/BatteryState.html
[sensor_msgs/Range]: http://docs.ros.org/api/sensor_msgs/html/msg/Range.html
[sensor_msgs/ChannelFloat32]: http://docs.ros.org/api/sensor_msgs/html/msg/ChannelFloat32.html
[sensor_msgs/Illuminance]: http://docs.ros.org/api/sensor_msgs/html/msg/Illuminance.html
[sensor_msgs/Temperature]: http://docs.ros.org/api/sensor_msgs/html/msg/Temperature.html
[sensor_msgs/RelativeHumidity]: http://docs.ros.org/api/sensor_msgs/html/msg/RelativeHumidity.html