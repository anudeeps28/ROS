# we are going to create a client that is going to subscribe to the service that we created 

import rospy
from lab_1_pkg import multiplier, multiplierResponse

def multiplier_client(x,y):
    rospy.init_node("client_node") #initializing
    rospy.wait_for_service("multiplier") #wait for multiplier service
    rate = rospy.rate(1)
    while not rospy.is_shutdown():
        try:
            multiply_two_ints = rospy.ServiceProxy("multiplier", multiplier)
            response = multiply_two_ints(x,y)
            rospy.logingo(response.result)
            rate.sleep()
        except:
            rospy.ServiceException as e:
            print("Service call failed %s", e)






if __name__ == '__main__':
    multiplier_client(7,2)


# also, add this python script to CMakeLists.txt in catkin_install_python thingy

# open up a terminal window
# go into the package, do catkin_make
# source devel.setup.bas
# rosrun lab_1_pkg service_server_node.py

# new ternimal
    # source devel.setup.bas
    # rosrun lab_1_pkg service_client_node
    
