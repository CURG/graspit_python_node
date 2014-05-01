import socket
import gen_proto
import gen_proto.GraspitMessage_pb2
import struct
import rospy

class GraspitProtobufSocket(object):
    def __init__(self, host='localhost', port=4766):
        self.host = host
        self.port = port
        self.socket = socket.socket()


    def reconnect(self):
        self.socket = socket.socket()
        self.socket.connect((self.host, self.port))

    def send(self, msg, retry_limit = 1):
        try:
            self.socket.sendall(msg)
            return True
        except Exception as e:
            rospy.logerr("error: " + e.message + str(e))
            if retry_limit:
                self.reconnect()
                return self.send(msg, retry_limit - 1)
            else:
                return False

    def send_proto(self, proto_msg):
        """
        :param proto_msg : a protobuf message to send
        :type proto_msg :gen_proto.GraspitMessage_pb2.GraspitProtobufMessage
        """

        assert isinstance(proto_msg, gen_proto.GraspitMessage_pb2.GraspitProtobufMessage)
        s = proto_msg.SerializeToString()
        message_struct = struct.pack("<I", len(s)) + s
        rospy.loginfo("proto_msg.ByteSize(): " + str(len(s)))
        return self.send(message_struct)