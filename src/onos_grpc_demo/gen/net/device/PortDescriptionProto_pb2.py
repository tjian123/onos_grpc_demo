# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: net/device/PortDescriptionProto.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from net.device import PortEnumsProto_pb2 as net_dot_device_dot_PortEnumsProto__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='net/device/PortDescriptionProto.proto',
  package='net.device',
  syntax='proto3',
  serialized_pb=_b('\n%net/device/PortDescriptionProto.proto\x12\nnet.device\x1a\x1fnet/device/PortEnumsProto.proto\"\xf8\x01\n\x14PortDescriptionProto\x12\x13\n\x0bport_number\x18\x01 \x01(\t\x12\x12\n\nis_enabled\x18\x02 \x01(\x08\x12\'\n\x04type\x18\x03 \x01(\x0e\x32\x19.net.device.PortTypeProto\x12\x12\n\nport_speed\x18\x04 \x01(\x03\x12\x46\n\x0b\x61nnotations\x18\x08 \x03(\x0b\x32\x31.net.device.PortDescriptionProto.AnnotationsEntry\x1a\x32\n\x10\x41nnotationsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x42(\n&org.onosproject.grpc.net.device.modelsb\x06proto3')
  ,
  dependencies=[net_dot_device_dot_PortEnumsProto__pb2.DESCRIPTOR,])




_PORTDESCRIPTIONPROTO_ANNOTATIONSENTRY = _descriptor.Descriptor(
  name='AnnotationsEntry',
  full_name='net.device.PortDescriptionProto.AnnotationsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='net.device.PortDescriptionProto.AnnotationsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='net.device.PortDescriptionProto.AnnotationsEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001')),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=285,
  serialized_end=335,
)

_PORTDESCRIPTIONPROTO = _descriptor.Descriptor(
  name='PortDescriptionProto',
  full_name='net.device.PortDescriptionProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='port_number', full_name='net.device.PortDescriptionProto.port_number', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='is_enabled', full_name='net.device.PortDescriptionProto.is_enabled', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='type', full_name='net.device.PortDescriptionProto.type', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='port_speed', full_name='net.device.PortDescriptionProto.port_speed', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='annotations', full_name='net.device.PortDescriptionProto.annotations', index=4,
      number=8, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_PORTDESCRIPTIONPROTO_ANNOTATIONSENTRY, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=87,
  serialized_end=335,
)

_PORTDESCRIPTIONPROTO_ANNOTATIONSENTRY.containing_type = _PORTDESCRIPTIONPROTO
_PORTDESCRIPTIONPROTO.fields_by_name['type'].enum_type = net_dot_device_dot_PortEnumsProto__pb2._PORTTYPEPROTO
_PORTDESCRIPTIONPROTO.fields_by_name['annotations'].message_type = _PORTDESCRIPTIONPROTO_ANNOTATIONSENTRY
DESCRIPTOR.message_types_by_name['PortDescriptionProto'] = _PORTDESCRIPTIONPROTO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PortDescriptionProto = _reflection.GeneratedProtocolMessageType('PortDescriptionProto', (_message.Message,), dict(

  AnnotationsEntry = _reflection.GeneratedProtocolMessageType('AnnotationsEntry', (_message.Message,), dict(
    DESCRIPTOR = _PORTDESCRIPTIONPROTO_ANNOTATIONSENTRY,
    __module__ = 'net.device.PortDescriptionProto_pb2'
    # @@protoc_insertion_point(class_scope:net.device.PortDescriptionProto.AnnotationsEntry)
    ))
  ,
  DESCRIPTOR = _PORTDESCRIPTIONPROTO,
  __module__ = 'net.device.PortDescriptionProto_pb2'
  # @@protoc_insertion_point(class_scope:net.device.PortDescriptionProto)
  ))
_sym_db.RegisterMessage(PortDescriptionProto)
_sym_db.RegisterMessage(PortDescriptionProto.AnnotationsEntry)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n&org.onosproject.grpc.net.device.models'))
_PORTDESCRIPTIONPROTO_ANNOTATIONSENTRY.has_options = True
_PORTDESCRIPTIONPROTO_ANNOTATIONSENTRY._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001'))
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
