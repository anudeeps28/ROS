# creating a publisher in ROS using python

# go inside the package that you want to work on,
# then make a new folder called scripts
# and inside these make a new file subscriber, publisher etc.

#!/user/bin/env

from imaplib import _CommandResults
import rospy
from std_msgs.msg import String
from package_name import Position

# defining the function that we use in main
def talk_to_me(): 
    pub = rospy.Publisher('talking_topic', String , queue_size = 10) #  name of the topic which we are going to publish; talking_topic = name of the topic published, String is the type, queue size = no. which will be kept in line before deletingt
    # in place of string, write position if you are calling messages from position
    # initialize the node
    rospy.init_node('publisher_node') # publisher_node = name of the node
    rate = rospy.Rate(1) #tells ros how long function will sleep before it wakes up again, value is in hertz (the freqency with which ros will send signals); 1\ 
            # if you already have a message file, just use this
            # msg = Position()
            # msg.message = "My Position is:"
            # msg.x = 2.0
            # msg.y = 1.5
        pub.publish(msg) # publishing message from the message file
            # can so this also pub.publish('Hey!') 
        rate.sleep() # sleep function called
        rospy.loginfo # logging the message 

# writing the main function
if __name__ == '__main__':
    try:
        talk_to_me()
    except rospy.ROSInterruptException:
        pass

# then go in CmakeLists and add a function catkin_install_python (PROGRAMS scripts/publisher_node.py
# DESTINATION $(CATKIN_PACKAGE_BIN_DESTINATION)
# ) and save this
# then do catkin_make 
# then do source devel bash/setup.bash
# run roscore
# then do rosrun name_of_package publisher_node.py
    # this will start the publishing node


# in a new terminal: rostopic list
    # to see the list of all the topics that are published until now
    # our newly created talking_topic will also be present there
# rostopic echo /talking_topic: you will get the message published every second

# if the file is not executable, then you need to do chmod +x catkin_ws/src/node.py   

# What is roscore
    makes the ros system ready to accept commands and give commands
    debug when says "Unable to connect with the master"