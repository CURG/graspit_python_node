# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)



DESCRIPTOR = descriptor.FileDescriptor(
  name='Renderable.proto',
  package='',
  serialized_pb='\n\x10Renderable.proto\"\x86\x06\n\nRenderable\x12\x30\n\npointCloud\x18\x01 \x01(\x0b\x32\x1c.Renderable.PointCloudXYZRGB\x12\x17\n\x0frenderableFrame\x18\x02 \x01(\t\x12,\n\x0bpointCloud2\x18\x03 \x01(\x0b\x32\x17.Renderable.PointCloud2\x12 \n\x05\x66rame\x18\x04 \x01(\x0b\x32\x11.Renderable.Frame\x1a+\n\x08PointXYZ\x12\t\n\x01x\x18\x01 \x02(\x02\x12\t\n\x01y\x18\x02 \x02(\x02\x12\t\n\x01z\x18\x03 \x02(\x02\x1a\x34\n\x08\x43olorRGB\x12\x0b\n\x03red\x18\x01 \x02(\x02\x12\r\n\x05green\x18\x02 \x02(\x02\x12\x0c\n\x04\x62lue\x18\x03 \x02(\x02\x1aW\n\x0bPointXYZRGB\x12#\n\x05point\x18\x01 \x02(\x0b\x32\x14.Renderable.PointXYZ\x12#\n\x05\x63olor\x18\x02 \x02(\x0b\x32\x14.Renderable.ColorRGB\x1aJ\n\x10PointCloudXYZRGB\x12\'\n\x06points\x18\x01 \x03(\x0b\x32\x17.Renderable.PointXYZRGB\x12\r\n\x05units\x18\x02 \x01(\x02\x1a\x8d\x01\n\x0bPointCloud2\x12\n\n\x02id\x18\x01 \x02(\x05\x12\x0e\n\x06\x66ields\x18\x02 \x03(\t\x12\x0c\n\x04\x64\x61ta\x18\x03 \x02(\x0c\x12\x0e\n\x06height\x18\x04 \x02(\r\x12\r\n\x05width\x18\x05 \x02(\r\x12\x14\n\x0cis_bigendian\x18\x06 \x02(\x08\x12\x10\n\x08is_dense\x18\x07 \x02(\x08\x12\r\n\x05units\x18\x08 \x01(\x02\x1a\x38\n\nQuaternion\x12\t\n\x01w\x18\x01 \x02(\x02\x12\t\n\x01x\x18\x02 \x02(\x02\x12\t\n\x01y\x18\x03 \x02(\x02\x12\t\n\x01z\x18\x04 \x02(\x02\x1a\x80\x01\n\x05\x46rame\x12)\n\x0btranslation\x18\x01 \x02(\x0b\x32\x14.Renderable.PointXYZ\x12+\n\x0borientation\x18\x02 \x02(\x0b\x32\x16.Renderable.Quaternion\x12\x10\n\x08\x66rame_id\x18\x03 \x02(\t\x12\r\n\x05units\x18\x04 \x01(\x02*\x08\x08\x64\x10\x80\x80\x80\x80\x02')




_RENDERABLE_POINTXYZ = descriptor.Descriptor(
  name='PointXYZ',
  full_name='Renderable.PointXYZ',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='x', full_name='Renderable.PointXYZ.x', index=0,
      number=1, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='y', full_name='Renderable.PointXYZ.y', index=1,
      number=2, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='z', full_name='Renderable.PointXYZ.z', index=2,
      number=3, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=190,
  serialized_end=233,
)

_RENDERABLE_COLORRGB = descriptor.Descriptor(
  name='ColorRGB',
  full_name='Renderable.ColorRGB',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='red', full_name='Renderable.ColorRGB.red', index=0,
      number=1, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='green', full_name='Renderable.ColorRGB.green', index=1,
      number=2, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='blue', full_name='Renderable.ColorRGB.blue', index=2,
      number=3, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=235,
  serialized_end=287,
)

_RENDERABLE_POINTXYZRGB = descriptor.Descriptor(
  name='PointXYZRGB',
  full_name='Renderable.PointXYZRGB',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='point', full_name='Renderable.PointXYZRGB.point', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='color', full_name='Renderable.PointXYZRGB.color', index=1,
      number=2, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=289,
  serialized_end=376,
)

_RENDERABLE_POINTCLOUDXYZRGB = descriptor.Descriptor(
  name='PointCloudXYZRGB',
  full_name='Renderable.PointCloudXYZRGB',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='points', full_name='Renderable.PointCloudXYZRGB.points', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='units', full_name='Renderable.PointCloudXYZRGB.units', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=378,
  serialized_end=452,
)

_RENDERABLE_POINTCLOUD2 = descriptor.Descriptor(
  name='PointCloud2',
  full_name='Renderable.PointCloud2',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='id', full_name='Renderable.PointCloud2.id', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='fields', full_name='Renderable.PointCloud2.fields', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='data', full_name='Renderable.PointCloud2.data', index=2,
      number=3, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='height', full_name='Renderable.PointCloud2.height', index=3,
      number=4, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='width', full_name='Renderable.PointCloud2.width', index=4,
      number=5, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='is_bigendian', full_name='Renderable.PointCloud2.is_bigendian', index=5,
      number=6, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='is_dense', full_name='Renderable.PointCloud2.is_dense', index=6,
      number=7, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='units', full_name='Renderable.PointCloud2.units', index=7,
      number=8, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=455,
  serialized_end=596,
)

_RENDERABLE_QUATERNION = descriptor.Descriptor(
  name='Quaternion',
  full_name='Renderable.Quaternion',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='w', full_name='Renderable.Quaternion.w', index=0,
      number=1, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='x', full_name='Renderable.Quaternion.x', index=1,
      number=2, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='y', full_name='Renderable.Quaternion.y', index=2,
      number=3, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='z', full_name='Renderable.Quaternion.z', index=3,
      number=4, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=598,
  serialized_end=654,
)

_RENDERABLE_FRAME = descriptor.Descriptor(
  name='Frame',
  full_name='Renderable.Frame',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='translation', full_name='Renderable.Frame.translation', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='orientation', full_name='Renderable.Frame.orientation', index=1,
      number=2, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='frame_id', full_name='Renderable.Frame.frame_id', index=2,
      number=3, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='units', full_name='Renderable.Frame.units', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=657,
  serialized_end=785,
)

_RENDERABLE = descriptor.Descriptor(
  name='Renderable',
  full_name='Renderable',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='pointCloud', full_name='Renderable.pointCloud', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='renderableFrame', full_name='Renderable.renderableFrame', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='pointCloud2', full_name='Renderable.pointCloud2', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='frame', full_name='Renderable.frame', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_RENDERABLE_POINTXYZ, _RENDERABLE_COLORRGB, _RENDERABLE_POINTXYZRGB, _RENDERABLE_POINTCLOUDXYZRGB, _RENDERABLE_POINTCLOUD2, _RENDERABLE_QUATERNION, _RENDERABLE_FRAME, ],
  enum_types=[
  ],
  options=None,
  is_extendable=True,
  extension_ranges=[(100, 536870912), ],
  serialized_start=21,
  serialized_end=795,
)

_RENDERABLE_POINTXYZ.containing_type = _RENDERABLE;
_RENDERABLE_COLORRGB.containing_type = _RENDERABLE;
_RENDERABLE_POINTXYZRGB.fields_by_name['point'].message_type = _RENDERABLE_POINTXYZ
_RENDERABLE_POINTXYZRGB.fields_by_name['color'].message_type = _RENDERABLE_COLORRGB
_RENDERABLE_POINTXYZRGB.containing_type = _RENDERABLE;
_RENDERABLE_POINTCLOUDXYZRGB.fields_by_name['points'].message_type = _RENDERABLE_POINTXYZRGB
_RENDERABLE_POINTCLOUDXYZRGB.containing_type = _RENDERABLE;
_RENDERABLE_POINTCLOUD2.containing_type = _RENDERABLE;
_RENDERABLE_QUATERNION.containing_type = _RENDERABLE;
_RENDERABLE_FRAME.fields_by_name['translation'].message_type = _RENDERABLE_POINTXYZ
_RENDERABLE_FRAME.fields_by_name['orientation'].message_type = _RENDERABLE_QUATERNION
_RENDERABLE_FRAME.containing_type = _RENDERABLE;
_RENDERABLE.fields_by_name['pointCloud'].message_type = _RENDERABLE_POINTCLOUDXYZRGB
_RENDERABLE.fields_by_name['pointCloud2'].message_type = _RENDERABLE_POINTCLOUD2
_RENDERABLE.fields_by_name['frame'].message_type = _RENDERABLE_FRAME
DESCRIPTOR.message_types_by_name['Renderable'] = _RENDERABLE

class Renderable(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  
  class PointXYZ(message.Message):
    __metaclass__ = reflection.GeneratedProtocolMessageType
    DESCRIPTOR = _RENDERABLE_POINTXYZ
    
    # @@protoc_insertion_point(class_scope:Renderable.PointXYZ)
  
  class ColorRGB(message.Message):
    __metaclass__ = reflection.GeneratedProtocolMessageType
    DESCRIPTOR = _RENDERABLE_COLORRGB
    
    # @@protoc_insertion_point(class_scope:Renderable.ColorRGB)
  
  class PointXYZRGB(message.Message):
    __metaclass__ = reflection.GeneratedProtocolMessageType
    DESCRIPTOR = _RENDERABLE_POINTXYZRGB
    
    # @@protoc_insertion_point(class_scope:Renderable.PointXYZRGB)
  
  class PointCloudXYZRGB(message.Message):
    __metaclass__ = reflection.GeneratedProtocolMessageType
    DESCRIPTOR = _RENDERABLE_POINTCLOUDXYZRGB
    
    # @@protoc_insertion_point(class_scope:Renderable.PointCloudXYZRGB)
  
  class PointCloud2(message.Message):
    __metaclass__ = reflection.GeneratedProtocolMessageType
    DESCRIPTOR = _RENDERABLE_POINTCLOUD2
    
    # @@protoc_insertion_point(class_scope:Renderable.PointCloud2)
  
  class Quaternion(message.Message):
    __metaclass__ = reflection.GeneratedProtocolMessageType
    DESCRIPTOR = _RENDERABLE_QUATERNION
    
    # @@protoc_insertion_point(class_scope:Renderable.Quaternion)
  
  class Frame(message.Message):
    __metaclass__ = reflection.GeneratedProtocolMessageType
    DESCRIPTOR = _RENDERABLE_FRAME
    
    # @@protoc_insertion_point(class_scope:Renderable.Frame)
  DESCRIPTOR = _RENDERABLE
  
  # @@protoc_insertion_point(class_scope:Renderable)

# @@protoc_insertion_point(module_scope)
