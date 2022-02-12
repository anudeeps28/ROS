# creating a new custom message inside of ROS

# make a new folder called msg, and make new files. Some of the examples are:
    # position.msg
    # velocity.msg

# what I need to add here: the variables that I need in the message file

string message
float32 X
float32 y

# go to publisher node, and import this message into that publishe node, also instead of standard, also change the argumen from string to position
# message, call the position function there

# go the the subscriber node
    # see in subscriber thing

# edit the xml file
    # add the build dependency which is called message generation
    # add the executable dependency which is called message runtime

# changes in CMakeLists
    # in the find package function add 
        # message_generatiom
    # also uncomment the function called message_files
    # Message1.msg
    # position.msg - add this

# also remove comments from generate message 

# then do catkin_make in the project folder
# run source devel/setup.bash 
# rosrun lab_1_pkg publishers.oy

# in new terminal, run roscore
# then go to project folder, and then source devel/setup.bash
# rosrun lab_1_pkg subscriber.py
# this will publish our own custom message 
