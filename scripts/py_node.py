#!/usr/bin/env python

import rospy

if __name__ == '__main__':
    rospy.init_node('py_node')

    rospy.loginfo('Start')
    rospy.sleep(1)
    
    rate = rospy.Rate(10)

    while not rospy.is_shutdown():
        rospy.loginfo('while node')
        rate.sleep()
