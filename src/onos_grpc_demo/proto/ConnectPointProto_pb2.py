# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ConnectPointProto.proto

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
  name='ConnectPointProto.proto',
  package='net',
  syntax='proto3',
  serialized_pb=_b('\n\x17\x43onnectPointProto.proto\x12\x03net\"K\n\x11\x43onnectPointProto\x12\x13\n\tdevice_id\x18\x01 \x01(\tH\x00\x12\x13\n\x0bport_number\x18\x02 \x01(\tB\x0c\n\nelement_idB!\n\x1forg.onosproject.grpc.net.modelsb\x06proto3')
)




_CONNECTPOINTPROTO = _descriptor.Descriptor(
  name='ConnectPointProto',
  full_name='net.ConnectPointProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='device_id', full_name='net.ConnectPointProto.device_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='port_number', full_name='net.ConnectPointProto.port_number', index=1,
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
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='element_id', full_name='net.ConnectPointProto.element_id',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=32,
  serialized_end=107,
)

_CONNECTPOINTPROTO.oneofs_by_name['element_id'].fields.append(
  _CONNECTPOINTPROTO.fields_by_name['device_id'])
_CONNECTPOINTPROTO.fields_by_name['device_id'].containing_oneof = _CONNECTPOINTPROTO.oneofs_by_name['element_id']
DESCRIPTOR.message_types_by_name['ConnectPointProto'] = _CONNECTPOINTPROTO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ConnectPointProto = _reflection.GeneratedProtocolMessageType('ConnectPointProto', (_message.Message,), dict(
  DESCRIPTOR = _CONNECTPOINTPROTO,
  __module__ = 'ConnectPointProto_pb2'
  # @@protoc_insertion_point(class_scope:net.ConnectPointProto)
  ))
_sym_db.RegisterMessage(ConnectPointProto)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\037org.onosproject.grpc.net.models'))
# @@protoc_insertion_point(module_scope)
