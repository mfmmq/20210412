# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: todo.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2

from google.protobuf.empty_pb2 import *

DESCRIPTOR = _descriptor.FileDescriptor(
  name='todo.proto',
  package='todo',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\ntodo.proto\x12\x04todo\x1a\x1bgoogle/protobuf/empty.proto\"J\n\x08TodoItem\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0e\n\x06\x61\x63tion\x18\x03 \x01(\t\x12\x13\n\x0bis_complete\x18\x04 \x01(\x08\x12\r\n\x05order\x18\x05 \x01(\t\"T\n\x08TodoList\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0f\n\x07\x63reator\x18\x03 \x01(\t\x12\x1d\n\x05items\x18\x04 \x03(\x0b\x32\x0e.todo.TodoItem2\xab\x01\n\x04Todo\x12\x36\n\nCreateItem\x12\x0e.todo.TodoItem\x1a\x16.google.protobuf.Empty\"\x00\x12\x36\n\nUpdateItem\x12\x0e.todo.TodoItem\x1a\x16.google.protobuf.Empty\"\x00\x12\x33\n\x07GetList\x12\x16.google.protobuf.Empty\x1a\x0e.todo.TodoList\"\x00P\x00\x62\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,],
  public_dependencies=[google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,])




_TODOITEM = _descriptor.Descriptor(
  name='TodoItem',
  full_name='todo.TodoItem',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='todo.TodoItem.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='action', full_name='todo.TodoItem.action', index=1,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='is_complete', full_name='todo.TodoItem.is_complete', index=2,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='order', full_name='todo.TodoItem.order', index=3,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=49,
  serialized_end=123,
)


_TODOLIST = _descriptor.Descriptor(
  name='TodoList',
  full_name='todo.TodoList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='todo.TodoList.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='todo.TodoList.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='creator', full_name='todo.TodoList.creator', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='items', full_name='todo.TodoList.items', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=125,
  serialized_end=209,
)

_TODOLIST.fields_by_name['items'].message_type = _TODOITEM
DESCRIPTOR.message_types_by_name['TodoItem'] = _TODOITEM
DESCRIPTOR.message_types_by_name['TodoList'] = _TODOLIST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TodoItem = _reflection.GeneratedProtocolMessageType('TodoItem', (_message.Message,), {
  'DESCRIPTOR' : _TODOITEM,
  '__module__' : 'todo_pb2'
  # @@protoc_insertion_point(class_scope:todo.TodoItem)
  })
_sym_db.RegisterMessage(TodoItem)

TodoList = _reflection.GeneratedProtocolMessageType('TodoList', (_message.Message,), {
  'DESCRIPTOR' : _TODOLIST,
  '__module__' : 'todo_pb2'
  # @@protoc_insertion_point(class_scope:todo.TodoList)
  })
_sym_db.RegisterMessage(TodoList)



_TODO = _descriptor.ServiceDescriptor(
  name='Todo',
  full_name='todo.Todo',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=212,
  serialized_end=383,
  methods=[
  _descriptor.MethodDescriptor(
    name='CreateItem',
    full_name='todo.Todo.CreateItem',
    index=0,
    containing_service=None,
    input_type=_TODOITEM,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='UpdateItem',
    full_name='todo.Todo.UpdateItem',
    index=1,
    containing_service=None,
    input_type=_TODOITEM,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetList',
    full_name='todo.Todo.GetList',
    index=2,
    containing_service=None,
    input_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    output_type=_TODOLIST,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_TODO)

DESCRIPTOR.services_by_name['Todo'] = _TODO

# @@protoc_insertion_point(module_scope)
