# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: easyfl/pb/server_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from easyfl.pb import common_pb2 as easyfl_dot_pb_dot_common__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1e\x65\x61syfl/pb/server_service.proto\x12\teasyfl.pb\x1a\x16\x65\x61syfl/pb/common.proto\"p\n\rUploadRequest\x12\x0f\n\x07task_id\x18\x01 \x01(\t\x12\x10\n\x08round_id\x18\x02 \x01(\x05\x12\x11\n\tclient_id\x18\x03 \x01(\t\x12)\n\x07\x63ontent\x18\x04 \x01(\x0b\x32\x18.easyfl.pb.UploadContent\"\x8b\x01\n\rUploadContent\x12\x0c\n\x04\x64\x61ta\x18\x01 \x01(\x0c\x12!\n\x04type\x18\x02 \x01(\x0e\x32\x13.easyfl.pb.DataType\x12\x11\n\tdata_size\x18\x03 \x01(\x03\x12\'\n\x06metric\x18\x04 \x01(\x0b\x32\x17.easyfl.pb.ClientMetric\x12\r\n\x05\x65xtra\x18\x63 \x01(\x0c\"-\n\x0bPerformance\x12\x10\n\x08\x61\x63\x63uracy\x18\x01 \x01(\x02\x12\x0c\n\x04loss\x18\x02 \x01(\x02\"3\n\x0eUploadResponse\x12!\n\x06status\x18\x01 \x01(\x0b\x32\x11.easyfl.pb.Status\"W\n\nRunRequest\x12\r\n\x05model\x18\x01 \x01(\x0c\x12\"\n\x07\x63lients\x18\x02 \x03(\x0b\x32\x11.easyfl.pb.Client\x12\x16\n\x0e\x65tcd_addresses\x18\x03 \x01(\t\"0\n\x0bRunResponse\x12!\n\x06status\x18\x01 \x01(\x0b\x32\x11.easyfl.pb.Status\"\r\n\x0bStopRequest\"1\n\x0cStopResponse\x12!\n\x06status\x18\x01 \x01(\x0b\x32\x11.easyfl.pb.Status\";\n\x06\x43lient\x12\x11\n\tclient_id\x18\x01 \x01(\t\x12\x0f\n\x07\x61\x64\x64ress\x18\x02 \x01(\t\x12\r\n\x05index\x18\x03 \x01(\x05\x32\xc3\x01\n\rServerService\x12?\n\x06Upload\x12\x18.easyfl.pb.UploadRequest\x1a\x19.easyfl.pb.UploadResponse\"\x00\x12\x36\n\x03Run\x12\x15.easyfl.pb.RunRequest\x1a\x16.easyfl.pb.RunResponse\"\x00\x12\x39\n\x04Stop\x12\x16.easyfl.pb.StopRequest\x1a\x17.easyfl.pb.StopResponse\"\x00\x62\x06proto3')



_UPLOADREQUEST = DESCRIPTOR.message_types_by_name['UploadRequest']
_UPLOADCONTENT = DESCRIPTOR.message_types_by_name['UploadContent']
_PERFORMANCE = DESCRIPTOR.message_types_by_name['Performance']
_UPLOADRESPONSE = DESCRIPTOR.message_types_by_name['UploadResponse']
_RUNREQUEST = DESCRIPTOR.message_types_by_name['RunRequest']
_RUNRESPONSE = DESCRIPTOR.message_types_by_name['RunResponse']
_STOPREQUEST = DESCRIPTOR.message_types_by_name['StopRequest']
_STOPRESPONSE = DESCRIPTOR.message_types_by_name['StopResponse']
_CLIENT = DESCRIPTOR.message_types_by_name['Client']
UploadRequest = _reflection.GeneratedProtocolMessageType('UploadRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPLOADREQUEST,
  '__module__' : 'easyfl.pb.server_service_pb2'
  # @@protoc_insertion_point(class_scope:easyfl.pb.UploadRequest)
  })
_sym_db.RegisterMessage(UploadRequest)

UploadContent = _reflection.GeneratedProtocolMessageType('UploadContent', (_message.Message,), {
  'DESCRIPTOR' : _UPLOADCONTENT,
  '__module__' : 'easyfl.pb.server_service_pb2'
  # @@protoc_insertion_point(class_scope:easyfl.pb.UploadContent)
  })
_sym_db.RegisterMessage(UploadContent)

Performance = _reflection.GeneratedProtocolMessageType('Performance', (_message.Message,), {
  'DESCRIPTOR' : _PERFORMANCE,
  '__module__' : 'easyfl.pb.server_service_pb2'
  # @@protoc_insertion_point(class_scope:easyfl.pb.Performance)
  })
_sym_db.RegisterMessage(Performance)

UploadResponse = _reflection.GeneratedProtocolMessageType('UploadResponse', (_message.Message,), {
  'DESCRIPTOR' : _UPLOADRESPONSE,
  '__module__' : 'easyfl.pb.server_service_pb2'
  # @@protoc_insertion_point(class_scope:easyfl.pb.UploadResponse)
  })
_sym_db.RegisterMessage(UploadResponse)

RunRequest = _reflection.GeneratedProtocolMessageType('RunRequest', (_message.Message,), {
  'DESCRIPTOR' : _RUNREQUEST,
  '__module__' : 'easyfl.pb.server_service_pb2'
  # @@protoc_insertion_point(class_scope:easyfl.pb.RunRequest)
  })
_sym_db.RegisterMessage(RunRequest)

RunResponse = _reflection.GeneratedProtocolMessageType('RunResponse', (_message.Message,), {
  'DESCRIPTOR' : _RUNRESPONSE,
  '__module__' : 'easyfl.pb.server_service_pb2'
  # @@protoc_insertion_point(class_scope:easyfl.pb.RunResponse)
  })
_sym_db.RegisterMessage(RunResponse)

StopRequest = _reflection.GeneratedProtocolMessageType('StopRequest', (_message.Message,), {
  'DESCRIPTOR' : _STOPREQUEST,
  '__module__' : 'easyfl.pb.server_service_pb2'
  # @@protoc_insertion_point(class_scope:easyfl.pb.StopRequest)
  })
_sym_db.RegisterMessage(StopRequest)

StopResponse = _reflection.GeneratedProtocolMessageType('StopResponse', (_message.Message,), {
  'DESCRIPTOR' : _STOPRESPONSE,
  '__module__' : 'easyfl.pb.server_service_pb2'
  # @@protoc_insertion_point(class_scope:easyfl.pb.StopResponse)
  })
_sym_db.RegisterMessage(StopResponse)

Client = _reflection.GeneratedProtocolMessageType('Client', (_message.Message,), {
  'DESCRIPTOR' : _CLIENT,
  '__module__' : 'easyfl.pb.server_service_pb2'
  # @@protoc_insertion_point(class_scope:easyfl.pb.Client)
  })
_sym_db.RegisterMessage(Client)

_SERVERSERVICE = DESCRIPTOR.services_by_name['ServerService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _UPLOADREQUEST._serialized_start=69
  _UPLOADREQUEST._serialized_end=181
  _UPLOADCONTENT._serialized_start=184
  _UPLOADCONTENT._serialized_end=323
  _PERFORMANCE._serialized_start=325
  _PERFORMANCE._serialized_end=370
  _UPLOADRESPONSE._serialized_start=372
  _UPLOADRESPONSE._serialized_end=423
  _RUNREQUEST._serialized_start=425
  _RUNREQUEST._serialized_end=512
  _RUNRESPONSE._serialized_start=514
  _RUNRESPONSE._serialized_end=562
  _STOPREQUEST._serialized_start=564
  _STOPREQUEST._serialized_end=577
  _STOPRESPONSE._serialized_start=579
  _STOPRESPONSE._serialized_end=628
  _CLIENT._serialized_start=630
  _CLIENT._serialized_end=689
  _SERVERSERVICE._serialized_start=692
  _SERVERSERVICE._serialized_end=887
# @@protoc_insertion_point(module_scope)