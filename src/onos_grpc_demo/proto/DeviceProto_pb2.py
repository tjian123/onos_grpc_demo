# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: DeviceProto.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import DeviceEnumsProto_pb2 as DeviceEnumsProto__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='DeviceProto.proto',
  package='net',
  syntax='proto3',
  serialized_pb=_b('\n\x11\x44\x65viceProto.proto\x12\x03net\x1a\x16\x44\x65viceEnumsProto.proto\"\xa0\x02\n\x0b\x44\x65viceProto\x12\x11\n\tdevice_id\x18\x01 \x01(\t\x12)\n\x04type\x18\x02 \x01(\x0e\x32\x1b.net.device.DeviceTypeProto\x12\x14\n\x0cmanufacturer\x18\x03 \x01(\t\x12\x12\n\nhw_version\x18\x04 \x01(\t\x12\x12\n\nsw_version\x18\x05 \x01(\t\x12\x15\n\rserial_number\x18\x06 \x01(\t\x12\x12\n\nchassis_id\x18\x07 \x01(\t\x12\x36\n\x0b\x61nnotations\x18\x08 \x03(\x0b\x32!.net.DeviceProto.AnnotationsEntry\x1a\x32\n\x10\x41nnotationsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x42!\n\x1forg.onosproject.grpc.net.modelsb\x06proto3')
  ,
  dependencies=[DeviceEnumsProto__pb2.DESCRIPTOR,])




_DEVICEPROTO_ANNOTATIONSENTRY = _descriptor.Descriptor(
  name='AnnotationsEntry',
  full_name='net.DeviceProto.AnnotationsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='net.DeviceProto.AnnotationsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='net.DeviceProto.AnnotationsEntry.value', index=1,
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
  serialized_start=289,
  serialized_end=339,
)

_DEVICEPROTO = _descriptor.Descriptor(
  name='DeviceProto',
  full_name='net.DeviceProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='device_id', full_name='net.DeviceProto.device_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='type', full_name='net.DeviceProto.type', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='manufacturer', full_name='net.DeviceProto.manufacturer', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='hw_version', full_name='net.DeviceProto.hw_version', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sw_version', full_name='net.DeviceProto.sw_version', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='serial_number', full_name='net.DeviceProto.serial_number', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='chassis_id', full_name='net.DeviceProto.chassis_id', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='annotations', full_name='net.DeviceProto.annotations', index=7,
      number=8, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_DEVICEPROTO_ANNOTATIONSENTRY, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=51,
  serialized_end=339,
)

_DEVICEPROTO_ANNOTATIONSENTRY.containing_type = _DEVICEPROTO
_DEVICEPROTO.fields_by_name['type'].enum_type = DeviceEnumsProto__pb2._DEVICETYPEPROTO
_DEVICEPROTO.fields_by_name['annotations'].message_type = _DEVICEPROTO_ANNOTATIONSENTRY
DESCRIPTOR.message_types_by_name['DeviceProto'] = _DEVICEPROTO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DeviceProto = _reflection.GeneratedProtocolMessageType('DeviceProto', (_message.Message,), dict(

  AnnotationsEntry = _reflection.GeneratedProtocolMessageType('AnnotationsEntry', (_message.Message,), dict(
    DESCRIPTOR = _DEVICEPROTO_ANNOTATIONSENTRY,
    __module__ = 'DeviceProto_pb2'
    # @@protoc_insertion_point(class_scope:net.DeviceProto.AnnotationsEntry)
    ))
  ,
  DESCRIPTOR = _DEVICEPROTO,
  __module__ = 'DeviceProto_pb2'
  # @@protoc_insertion_point(class_scope:net.DeviceProto)
  ))
_sym_db.RegisterMessage(DeviceProto)
_sym_db.RegisterMessage(DeviceProto.AnnotationsEntry)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\037org.onosproject.grpc.net.models'))
_DEVICEPROTO_ANNOTATIONSENTRY.has_options = True
_DEVICEPROTO_ANNOTATIONSENTRY._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001'))
# @@protoc_insertion_point(module_scope)
