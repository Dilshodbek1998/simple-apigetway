# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: book.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='book.proto',
  package='book',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n\nbook.proto\x12\x04\x62ook\x1a\x1bgoogle/protobuf/empty.proto\"L\n\x06\x41uthor\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x12\n\nfirst_name\x18\x02 \x01(\t\x12\x11\n\tlast_name\x18\x03 \x01(\t\x12\x0f\n\x07\x63ountry\x18\x04 \x01(\t\"A\n\x04\x42ook\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x11\n\tauthor_id\x18\x03 \x01(\x05\x12\x0c\n\x04year\x18\x04 \x01(\x05\"\x1f\n\x11\x42ookDetailRequest\x12\n\n\x02id\x18\x01 \x01(\x05\"\x1f\n\x11\x42ookDeleteRequest\x12\n\n\x02id\x18\x01 \x01(\x05\"N\n\x11\x42ookUpdateRequest\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x11\n\tauthor_id\x18\x03 \x01(\x05\x12\x0c\n\x04year\x18\x04 \x01(\x05\"-\n\x10\x42ookListResponse\x12\x19\n\x05\x62ooks\x18\x01 \x03(\x0b\x32\n.book.Book\"\x11\n\x0f\x42ookListRequest2\x9d\x02\n\x0b\x42ookService\x12&\n\nBookCreate\x12\n.book.Book\x1a\n.book.Book\"\x00\x12\x33\n\nBookDetail\x12\x17.book.BookDetailRequest\x1a\n.book.Book\"\x00\x12?\n\nBookDelete\x12\x17.book.BookDeleteRequest\x1a\x16.google.protobuf.Empty\"\x00\x12\x33\n\nBookUpdate\x12\x17.book.BookUpdateRequest\x1a\n.book.Book\"\x00\x12;\n\x08\x42ookList\x12\x15.book.BookListRequest\x1a\x16.book.BookListResponse\"\x00\x62\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,])




_AUTHOR = _descriptor.Descriptor(
  name='Author',
  full_name='book.Author',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='book.Author.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='first_name', full_name='book.Author.first_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='last_name', full_name='book.Author.last_name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='country', full_name='book.Author.country', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_end=125,
)


_BOOK = _descriptor.Descriptor(
  name='Book',
  full_name='book.Book',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='book.Book.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='book.Book.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='author_id', full_name='book.Book.author_id', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='year', full_name='book.Book.year', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=127,
  serialized_end=192,
)


_BOOKDETAILREQUEST = _descriptor.Descriptor(
  name='BookDetailRequest',
  full_name='book.BookDetailRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='book.BookDetailRequest.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=194,
  serialized_end=225,
)


_BOOKDELETEREQUEST = _descriptor.Descriptor(
  name='BookDeleteRequest',
  full_name='book.BookDeleteRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='book.BookDeleteRequest.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=227,
  serialized_end=258,
)


_BOOKUPDATEREQUEST = _descriptor.Descriptor(
  name='BookUpdateRequest',
  full_name='book.BookUpdateRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='book.BookUpdateRequest.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='book.BookUpdateRequest.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='author_id', full_name='book.BookUpdateRequest.author_id', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='year', full_name='book.BookUpdateRequest.year', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=260,
  serialized_end=338,
)


_BOOKLISTRESPONSE = _descriptor.Descriptor(
  name='BookListResponse',
  full_name='book.BookListResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='books', full_name='book.BookListResponse.books', index=0,
      number=1, type=11, cpp_type=10, label=3,
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
  serialized_start=340,
  serialized_end=385,
)


_BOOKLISTREQUEST = _descriptor.Descriptor(
  name='BookListRequest',
  full_name='book.BookListRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=387,
  serialized_end=404,
)

_BOOKLISTRESPONSE.fields_by_name['books'].message_type = _BOOK
DESCRIPTOR.message_types_by_name['Author'] = _AUTHOR
DESCRIPTOR.message_types_by_name['Book'] = _BOOK
DESCRIPTOR.message_types_by_name['BookDetailRequest'] = _BOOKDETAILREQUEST
DESCRIPTOR.message_types_by_name['BookDeleteRequest'] = _BOOKDELETEREQUEST
DESCRIPTOR.message_types_by_name['BookUpdateRequest'] = _BOOKUPDATEREQUEST
DESCRIPTOR.message_types_by_name['BookListResponse'] = _BOOKLISTRESPONSE
DESCRIPTOR.message_types_by_name['BookListRequest'] = _BOOKLISTREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Author = _reflection.GeneratedProtocolMessageType('Author', (_message.Message,), {
  'DESCRIPTOR' : _AUTHOR,
  '__module__' : 'book_pb2'
  # @@protoc_insertion_point(class_scope:book.Author)
  })
_sym_db.RegisterMessage(Author)

Book = _reflection.GeneratedProtocolMessageType('Book', (_message.Message,), {
  'DESCRIPTOR' : _BOOK,
  '__module__' : 'book_pb2'
  # @@protoc_insertion_point(class_scope:book.Book)
  })
_sym_db.RegisterMessage(Book)

BookDetailRequest = _reflection.GeneratedProtocolMessageType('BookDetailRequest', (_message.Message,), {
  'DESCRIPTOR' : _BOOKDETAILREQUEST,
  '__module__' : 'book_pb2'
  # @@protoc_insertion_point(class_scope:book.BookDetailRequest)
  })
_sym_db.RegisterMessage(BookDetailRequest)

BookDeleteRequest = _reflection.GeneratedProtocolMessageType('BookDeleteRequest', (_message.Message,), {
  'DESCRIPTOR' : _BOOKDELETEREQUEST,
  '__module__' : 'book_pb2'
  # @@protoc_insertion_point(class_scope:book.BookDeleteRequest)
  })
_sym_db.RegisterMessage(BookDeleteRequest)

BookUpdateRequest = _reflection.GeneratedProtocolMessageType('BookUpdateRequest', (_message.Message,), {
  'DESCRIPTOR' : _BOOKUPDATEREQUEST,
  '__module__' : 'book_pb2'
  # @@protoc_insertion_point(class_scope:book.BookUpdateRequest)
  })
_sym_db.RegisterMessage(BookUpdateRequest)

BookListResponse = _reflection.GeneratedProtocolMessageType('BookListResponse', (_message.Message,), {
  'DESCRIPTOR' : _BOOKLISTRESPONSE,
  '__module__' : 'book_pb2'
  # @@protoc_insertion_point(class_scope:book.BookListResponse)
  })
_sym_db.RegisterMessage(BookListResponse)

BookListRequest = _reflection.GeneratedProtocolMessageType('BookListRequest', (_message.Message,), {
  'DESCRIPTOR' : _BOOKLISTREQUEST,
  '__module__' : 'book_pb2'
  # @@protoc_insertion_point(class_scope:book.BookListRequest)
  })
_sym_db.RegisterMessage(BookListRequest)



_BOOKSERVICE = _descriptor.ServiceDescriptor(
  name='BookService',
  full_name='book.BookService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=407,
  serialized_end=692,
  methods=[
  _descriptor.MethodDescriptor(
    name='BookCreate',
    full_name='book.BookService.BookCreate',
    index=0,
    containing_service=None,
    input_type=_BOOK,
    output_type=_BOOK,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='BookDetail',
    full_name='book.BookService.BookDetail',
    index=1,
    containing_service=None,
    input_type=_BOOKDETAILREQUEST,
    output_type=_BOOK,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='BookDelete',
    full_name='book.BookService.BookDelete',
    index=2,
    containing_service=None,
    input_type=_BOOKDELETEREQUEST,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='BookUpdate',
    full_name='book.BookService.BookUpdate',
    index=3,
    containing_service=None,
    input_type=_BOOKUPDATEREQUEST,
    output_type=_BOOK,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='BookList',
    full_name='book.BookService.BookList',
    index=4,
    containing_service=None,
    input_type=_BOOKLISTREQUEST,
    output_type=_BOOKLISTRESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_BOOKSERVICE)

DESCRIPTOR.services_by_name['BookService'] = _BOOKSERVICE

# @@protoc_insertion_point(module_scope)