#!/usr/bin/python
import subprocess
import sys
import rospy



if __name__=="__main__":
    rospy.init_node('graspit_remote')
    graspit_ssh_url = rospy.get_param('~graspit_ssh_url', 'srihari@192.168.11.47')
    graspit_display = rospy.get_param('~graspit_display',':1.0')
    graspit_world_name = rospy.get_param('~graspit_world','3objectbarrett')
    graspit_remote_bin = rospy.get_param('~graspit_remote_bin', '~/graspit_bci/bin/graspit')
    spargs = ['ssh',graspit_ssh_url, '-t', "pkill graspit;export DISPLAY=%s; export GRASPIT_REMOTE_SERVER_URL=tcp://192.168.11.200:5561; bash -ic '%s %s'"%(graspit_display, graspit_remote_bin, graspit_world_name)]
    p = subprocess.Popen(spargs)
    rospy.spin()
    p.kill()

        
