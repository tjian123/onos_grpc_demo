# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: net/HostLocationProto.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from net import ConnectPointProto_pb2 as net_dot_ConnectPointProto__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='net/HostLocationProto.proto',
  package='net',
  syntax='proto3',
  serialized_pb=_b('\n\x1bnet/HostLocationProto.proto\x12\x03net\x1a\x1bnet/ConnectPointProto.proto\"P\n\x11HostLocationProto\x12-\n\rconnect_point\x18\x01 \x01(\x0b\x32\x16.net.ConnectPointProto\x12\x0c\n\x04time\x18\x02 \x01(\x04\x42!\n\x1forg.onosproject.grpc.net.modelsb\x06proto3')
  ,
  dependencies=[net_dot_ConnectPointProto__pb2.DESCRIPTOR,])




_HOSTLOCATIONPROTO = _descriptor.Descriptor(
  name='HostLocationProto',
  full_name='net.HostLocationProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='connect_point', full_name='net.HostLocationProto.connect_point', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='time', full_name='net.HostLocationProto.time', index=1,
      number=2, type=4, cpp_type=4, label=1,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=65,
  serialized_end=145,
)

_HOSTLOCATIONPROTO.fields_by_name['connect_point'].message_type = net_dot_ConnectPointProto__pb2._CONNECTPOINTPROTO
DESCRIPTOR.message_types_by_name['HostLocationProto'] = _HOSTLOCATIONPROTO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

HostLocationProto = _reflection.GeneratedProtocolMessageType('HostLocationProto', (_message.Message,), dict(
  DESCRIPTOR = _HOSTLOCATIONPROTO,
  __module__ = 'net.HostLocationProto_pb2'
  # @@protoc_insertion_point(class_scope:net.HostLocationProto)
  ))
_sym_db.RegisterMessage(HostLocationProto)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\037org.onosproject.grpc.net.models'))
try:
  # THESE ELEMENTS WILL BE DEPRECATED.
  # Please use the generated *_pb2_grpc.py files instead.
  import grpc
  from grpc.beta import implementations as beta_implementations
  from grpc.beta import interfaces as beta_interfaces
  from grpc.framework.common import cardinality
  from grpc.framework.interfaces.face import utilities as face_utilities
except ImportError:
  pass
# @@protoc_insertion_point(module_scope)
