# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: net/device/PortStatisticsProto.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='net/device/PortStatisticsProto.proto',
  package='net.device',
  syntax='proto3',
  serialized_pb=_b('\n$net/device/PortStatisticsProto.proto\x12\nnet.device\"\xab\x02\n\x13PortStatisticsProto\x12\x0c\n\x04port\x18\x01 \x01(\x05\x12\x18\n\x10packets_received\x18\x02 \x01(\x03\x12\x14\n\x0cpackets_sent\x18\x03 \x01(\x03\x12\x16\n\x0e\x62ytes_received\x18\x04 \x01(\x03\x12\x12\n\nbytes_sent\x18\x05 \x01(\x03\x12\x1a\n\x12packets_rx_dropped\x18\x06 \x01(\x03\x12\x1a\n\x12packets_tx_dropped\x18\x07 \x01(\x03\x12\x19\n\x11packets_rx_errors\x18\x08 \x01(\x03\x12\x19\n\x11packets_tx_errors\x18\t \x01(\x03\x12\x14\n\x0c\x64uration_sec\x18\n \x01(\x03\x12\x15\n\rduration_nano\x18\x0b \x01(\x03\x12\x0f\n\x07is_zero\x18\x0c \x01(\x08\x42(\n&org.onosproject.grpc.net.device.modelsb\x06proto3')
)




_PORTSTATISTICSPROTO = _descriptor.Descriptor(
  name='PortStatisticsProto',
  full_name='net.device.PortStatisticsProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='port', full_name='net.device.PortStatisticsProto.port', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='packets_received', full_name='net.device.PortStatisticsProto.packets_received', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='packets_sent', full_name='net.device.PortStatisticsProto.packets_sent', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='bytes_received', full_name='net.device.PortStatisticsProto.bytes_received', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='bytes_sent', full_name='net.device.PortStatisticsProto.bytes_sent', index=4,
      number=5, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='packets_rx_dropped', full_name='net.device.PortStatisticsProto.packets_rx_dropped', index=5,
      number=6, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='packets_tx_dropped', full_name='net.device.PortStatisticsProto.packets_tx_dropped', index=6,
      number=7, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='packets_rx_errors', full_name='net.device.PortStatisticsProto.packets_rx_errors', index=7,
      number=8, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='packets_tx_errors', full_name='net.device.PortStatisticsProto.packets_tx_errors', index=8,
      number=9, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='duration_sec', full_name='net.device.PortStatisticsProto.duration_sec', index=9,
      number=10, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='duration_nano', full_name='net.device.PortStatisticsProto.duration_nano', index=10,
      number=11, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='is_zero', full_name='net.device.PortStatisticsProto.is_zero', index=11,
      number=12, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=53,
  serialized_end=352,
)

DESCRIPTOR.message_types_by_name['PortStatisticsProto'] = _PORTSTATISTICSPROTO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PortStatisticsProto = _reflection.GeneratedProtocolMessageType('PortStatisticsProto', (_message.Message,), dict(
  DESCRIPTOR = _PORTSTATISTICSPROTO,
  __module__ = 'net.device.PortStatisticsProto_pb2'
  # @@protoc_insertion_point(class_scope:net.device.PortStatisticsProto)
  ))
_sym_db.RegisterMessage(PortStatisticsProto)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n&org.onosproject.grpc.net.device.models'))
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
