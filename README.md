# Drone-surveillance
This repo contains all the files used in creating a drone simulation for aerial surveillance and monitoring.

Simulation is run using ros noetic, Rviz and Gazebo on Ubuntu 20.04 VM

The simulation has an integrated camera that captures the surrounding and provides visual information to the user for surveillance.

Lidar can be enabled on the drone through rviz which can create a 3d mapping for the area and objects present within it.

Darknet_ros has been integrated into the simulation to help with object detection using yolov5 (currently testing).

2 seperate darknet nodes have been created using python scripts( Darknet_bridge and image_saver). These nodes save the camera feed of the drone as images and detect objects within these images (currently testing).

## References-
The skeletal framework for basic drone simulation has been built upon the hector quadrotor repo by RAFALAMAO: (https://github.com/RAFALAMAO/hector-quadrotor-noetic)

Darknet_ros has been cloned form the repo : (https://github.com/leggedrobotics/darknet_ros.git)
