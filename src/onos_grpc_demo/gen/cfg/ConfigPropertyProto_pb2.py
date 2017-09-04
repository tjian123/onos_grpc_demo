# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cfg/ConfigPropertyProto.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from cfg import ConfigPropertyEnumsProto_pb2 as cfg_dot_ConfigPropertyEnumsProto__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='cfg/ConfigPropertyProto.proto',
  package='cfg',
  syntax='proto3',
  serialized_pb=_b('\n\x1d\x63\x66g/ConfigPropertyProto.proto\x12\x03\x63\x66g\x1a\"cfg/ConfigPropertyEnumsProto.proto\"\x9a\x01\n\x13\x43onfigPropertyProto\x12\x0c\n\x04name\x18\x01 \x01(\t\x12*\n\x04type\x18\x02 \x01(\x0e\x32\x1c.cfg.ConfigPropertyTypeProto\x12\r\n\x05value\x18\x03 \x01(\t\x12\x15\n\rdefault_value\x18\x04 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x05 \x01(\t\x12\x0e\n\x06is_set\x18\x06 \x01(\x08\x42!\n\x1forg.onosproject.grpc.cfg.modelsb\x06proto3')
  ,
  dependencies=[cfg_dot_ConfigPropertyEnumsProto__pb2.DESCRIPTOR,])




_CONFIGPROPERTYPROTO = _descriptor.Descriptor(
  name='ConfigPropertyProto',
  full_name='cfg.ConfigPropertyProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='cfg.ConfigPropertyProto.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='type', full_name='cfg.ConfigPropertyProto.type', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='cfg.ConfigPropertyProto.value', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='default_value', full_name='cfg.ConfigPropertyProto.default_value', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='description', full_name='cfg.ConfigPropertyProto.description', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='is_set', full_name='cfg.ConfigPropertyProto.is_set', index=5,
      number=6, type=8, cpp_type=7, label=1,
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
  serialized_start=75,
  serialized_end=229,
)

_CONFIGPROPERTYPROTO.fields_by_name['type'].enum_type = cfg_dot_ConfigPropertyEnumsProto__pb2._CONFIGPROPERTYTYPEPROTO
DESCRIPTOR.message_types_by_name['ConfigPropertyProto'] = _CONFIGPROPERTYPROTO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ConfigPropertyProto = _reflection.GeneratedProtocolMessageType('ConfigPropertyProto', (_message.Message,), dict(
  DESCRIPTOR = _CONFIGPROPERTYPROTO,
  __module__ = 'cfg.ConfigPropertyProto_pb2'
  # @@protoc_insertion_point(class_scope:cfg.ConfigPropertyProto)
  ))
_sym_db.RegisterMessage(ConfigPropertyProto)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\037org.onosproject.grpc.cfg.models'))
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
