# this service node is going to multiply 2 numbers

import rospy
from lab_1_pkg import multiplier, multiplierResponse

def callback(request):
    return multiplierResponse(request.a*request.b)

def multiply():
    rospy.init_node("multiplier_service") #initializing a node and naming it
    service = rospy.service("multiplier, multiplier, callback") # making a service object 
    rospy.spin() # to keep it running until we stop it



if __name__ == '__main__':
    multiply()


# now go to CMakeLists.txt and in this file, go to srv and uncomment all the files and 
# add a file called multiplier.srv

# hit save and then go to catkin_install_python, and inside the bracket add scripts/service_server_node
# save this

# open terminal
    #start roscore
    # open up 2 new terminals
    # catkin_make (to build our project)
    # source devel/setup.bash (in both terminals)

# rosrun lab_1_pkg service_server_node.py

# in other terminal
    # rosservice list (this will list all the services that are running)
    # rosservice call /multilier hit tab
    