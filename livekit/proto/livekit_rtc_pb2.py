# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: livekit_rtc.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import livekit_models_pb2 as livekit__models__pb2

DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\x11livekit_rtc.proto\x12\x07livekit\x1a\x14livekit_models.proto"\xe3\x04\n\rSignalRequest\x12,\n\x05offer\x18\x01 \x01(\x0b\x32\x1b.livekit.SessionDescriptionH\x00\x12-\n\x06\x61nswer\x18\x02 \x01(\x0b\x32\x1b.livekit.SessionDescriptionH\x00\x12*\n\x07trickle\x18\x03 \x01(\x0b\x32\x17.livekit.TrickleRequestH\x00\x12-\n\tadd_track\x18\x04 \x01(\x0b\x32\x18.livekit.AddTrackRequestH\x00\x12)\n\x04mute\x18\x05 \x01(\x0b\x32\x19.livekit.MuteTrackRequestH\x00\x12\x33\n\x0csubscription\x18\x06 \x01(\x0b\x32\x1b.livekit.UpdateSubscriptionH\x00\x12\x35\n\rtrack_setting\x18\x07 \x01(\x0b\x32\x1c.livekit.UpdateTrackSettingsH\x00\x12&\n\x05leave\x18\x08 \x01(\x0b\x32\x15.livekit.LeaveRequestH\x00\x12\x33\n\rupdate_layers\x18\n \x01(\x0b\x32\x1a.livekit.UpdateVideoLayersH\x00\x12\x42\n\x17subscription_permission\x18\x0b \x01(\x0b\x32\x1f.livekit.SubscriptionPermissionH\x00\x12(\n\nsync_state\x18\x0c \x01(\x0b\x32\x12.livekit.SyncStateH\x00\x12-\n\x08simulate\x18\r \x01(\x0b\x32\x19.livekit.SimulateScenarioH\x00\x42\t\n\x07message"\xd6\x06\n\x0eSignalResponse\x12%\n\x04join\x18\x01 \x01(\x0b\x32\x15.livekit.JoinResponseH\x00\x12-\n\x06\x61nswer\x18\x02 \x01(\x0b\x32\x1b.livekit.SessionDescriptionH\x00\x12,\n\x05offer\x18\x03 \x01(\x0b\x32\x1b.livekit.SessionDescriptionH\x00\x12*\n\x07trickle\x18\x04 \x01(\x0b\x32\x17.livekit.TrickleRequestH\x00\x12,\n\x06update\x18\x05 \x01(\x0b\x32\x1a.livekit.ParticipantUpdateH\x00\x12:\n\x0ftrack_published\x18\x06 \x01(\x0b\x32\x1f.livekit.TrackPublishedResponseH\x00\x12&\n\x05leave\x18\x08 \x01(\x0b\x32\x15.livekit.LeaveRequestH\x00\x12)\n\x04mute\x18\t \x01(\x0b\x32\x19.livekit.MuteTrackRequestH\x00\x12\x34\n\x10speakers_changed\x18\n \x01(\x0b\x32\x18.livekit.SpeakersChangedH\x00\x12*\n\x0broom_update\x18\x0b \x01(\x0b\x32\x13.livekit.RoomUpdateH\x00\x12>\n\x12\x63onnection_quality\x18\x0c \x01(\x0b\x32 .livekit.ConnectionQualityUpdateH\x00\x12\x39\n\x13stream_state_update\x18\r \x01(\x0b\x32\x1a.livekit.StreamStateUpdateH\x00\x12\x45\n\x19subscribed_quality_update\x18\x0e \x01(\x0b\x32 .livekit.SubscribedQualityUpdateH\x00\x12O\n\x1esubscription_permission_update\x18\x0f \x01(\x0b\x32%.livekit.SubscriptionPermissionUpdateH\x00\x12\x17\n\rrefresh_token\x18\x10 \x01(\tH\x00\x12>\n\x11track_unpublished\x18\x11 \x01(\x0b\x32!.livekit.TrackUnpublishedResponseH\x00\x42\t\n\x07message"\xdc\x01\n\x0f\x41\x64\x64TrackRequest\x12\x0b\n\x03\x63id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12 \n\x04type\x18\x03 \x01(\x0e\x32\x12.livekit.TrackType\x12\r\n\x05width\x18\x04 \x01(\r\x12\x0e\n\x06height\x18\x05 \x01(\r\x12\r\n\x05muted\x18\x06 \x01(\x08\x12\x13\n\x0b\x64isable_dtx\x18\x07 \x01(\x08\x12$\n\x06source\x18\x08 \x01(\x0e\x32\x14.livekit.TrackSource\x12#\n\x06layers\x18\t \x03(\x0b\x32\x13.livekit.VideoLayer"N\n\x0eTrickleRequest\x12\x15\n\rcandidateInit\x18\x01 \x01(\t\x12%\n\x06target\x18\x02 \x01(\x0e\x32\x15.livekit.SignalTarget".\n\x10MuteTrackRequest\x12\x0b\n\x03sid\x18\x01 \x01(\t\x12\r\n\x05muted\x18\x02 \x01(\x08"\xd9\x02\n\x0cJoinResponse\x12\x1b\n\x04room\x18\x01 \x01(\x0b\x32\r.livekit.Room\x12-\n\x0bparticipant\x18\x02 \x01(\x0b\x32\x18.livekit.ParticipantInfo\x12\x34\n\x12other_participants\x18\x03 \x03(\x0b\x32\x18.livekit.ParticipantInfo\x12\x16\n\x0eserver_version\x18\x04 \x01(\t\x12\'\n\x0bice_servers\x18\x05 \x03(\x0b\x32\x12.livekit.ICEServer\x12\x1a\n\x12subscriber_primary\x18\x06 \x01(\x08\x12\x17\n\x0f\x61lternative_url\x18\x07 \x01(\t\x12:\n\x14\x63lient_configuration\x18\x08 \x01(\x0b\x32\x1c.livekit.ClientConfiguration\x12\x15\n\rserver_region\x18\t \x01(\t"H\n\x16TrackPublishedResponse\x12\x0b\n\x03\x63id\x18\x01 \x01(\t\x12!\n\x05track\x18\x02 \x01(\x0b\x32\x12.livekit.TrackInfo"-\n\x18TrackUnpublishedResponse\x12\x11\n\ttrack_sid\x18\x01 \x01(\t"/\n\x12SessionDescription\x12\x0c\n\x04type\x18\x01 \x01(\t\x12\x0b\n\x03sdp\x18\x02 \x01(\t"C\n\x11ParticipantUpdate\x12.\n\x0cparticipants\x18\x01 \x03(\x0b\x32\x18.livekit.ParticipantInfo"s\n\x12UpdateSubscription\x12\x12\n\ntrack_sids\x18\x01 \x03(\t\x12\x11\n\tsubscribe\x18\x02 \x01(\x08\x12\x36\n\x12participant_tracks\x18\x03 \x03(\x0b\x32\x1a.livekit.ParticipantTracks"\x82\x01\n\x13UpdateTrackSettings\x12\x12\n\ntrack_sids\x18\x01 \x03(\t\x12\x10\n\x08\x64isabled\x18\x03 \x01(\x08\x12&\n\x07quality\x18\x04 \x01(\x0e\x32\x15.livekit.VideoQuality\x12\r\n\x05width\x18\x05 \x01(\r\x12\x0e\n\x06height\x18\x06 \x01(\r"%\n\x0cLeaveRequest\x12\x15\n\rcan_reconnect\x18\x01 \x01(\x08"K\n\x11UpdateVideoLayers\x12\x11\n\ttrack_sid\x18\x01 \x01(\t\x12#\n\x06layers\x18\x02 \x03(\x0b\x32\x13.livekit.VideoLayer"?\n\tICEServer\x12\x0c\n\x04urls\x18\x01 \x03(\t\x12\x10\n\x08username\x18\x02 \x01(\t\x12\x12\n\ncredential\x18\x03 \x01(\t"9\n\x0fSpeakersChanged\x12&\n\x08speakers\x18\x01 \x03(\x0b\x32\x14.livekit.SpeakerInfo")\n\nRoomUpdate\x12\x1b\n\x04room\x18\x01 \x01(\x0b\x32\r.livekit.Room"l\n\x15\x43onnectionQualityInfo\x12\x17\n\x0fparticipant_sid\x18\x01 \x01(\t\x12+\n\x07quality\x18\x02 \x01(\x0e\x32\x1a.livekit.ConnectionQuality\x12\r\n\x05score\x18\x03 \x01(\x02"J\n\x17\x43onnectionQualityUpdate\x12/\n\x07updates\x18\x01 \x03(\x0b\x32\x1e.livekit.ConnectionQualityInfo"b\n\x0fStreamStateInfo\x12\x17\n\x0fparticipant_sid\x18\x01 \x01(\t\x12\x11\n\ttrack_sid\x18\x02 \x01(\t\x12#\n\x05state\x18\x03 \x01(\x0e\x32\x14.livekit.StreamState"D\n\x11StreamStateUpdate\x12/\n\rstream_states\x18\x01 \x03(\x0b\x32\x18.livekit.StreamStateInfo"L\n\x11SubscribedQuality\x12&\n\x07quality\x18\x01 \x01(\x0e\x32\x15.livekit.VideoQuality\x12\x0f\n\x07\x65nabled\x18\x02 \x01(\x08"f\n\x17SubscribedQualityUpdate\x12\x11\n\ttrack_sid\x18\x01 \x01(\t\x12\x38\n\x14subscribed_qualities\x18\x02 \x03(\x0b\x32\x1a.livekit.SubscribedQuality"p\n\x0fTrackPermission\x12\x17\n\x0fparticipant_sid\x18\x01 \x01(\t\x12\x12\n\nall_tracks\x18\x02 \x01(\x08\x12\x12\n\ntrack_sids\x18\x03 \x03(\t\x12\x1c\n\x14participant_identity\x18\x04 \x01(\t"g\n\x16SubscriptionPermission\x12\x18\n\x10\x61ll_participants\x18\x01 \x01(\x08\x12\x33\n\x11track_permissions\x18\x02 \x03(\x0b\x32\x18.livekit.TrackPermission"[\n\x1cSubscriptionPermissionUpdate\x12\x17\n\x0fparticipant_sid\x18\x01 \x01(\t\x12\x11\n\ttrack_sid\x18\x02 \x01(\t\x12\x0f\n\x07\x61llowed\x18\x03 \x01(\x08"\xd5\x01\n\tSyncState\x12+\n\x06\x61nswer\x18\x01 \x01(\x0b\x32\x1b.livekit.SessionDescription\x12\x31\n\x0csubscription\x18\x02 \x01(\x0b\x32\x1b.livekit.UpdateSubscription\x12\x37\n\x0epublish_tracks\x18\x03 \x03(\x0b\x32\x1f.livekit.TrackPublishedResponse\x12/\n\rdata_channels\x18\x04 \x03(\x0b\x32\x18.livekit.DataChannelInfo"S\n\x0f\x44\x61taChannelInfo\x12\r\n\x05label\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\r\x12%\n\x06target\x18\x03 \x01(\x0e\x32\x15.livekit.SignalTarget"}\n\x10SimulateScenario\x12\x18\n\x0espeaker_update\x18\x01 \x01(\x05H\x00\x12\x16\n\x0cnode_failure\x18\x02 \x01(\x08H\x00\x12\x13\n\tmigration\x18\x03 \x01(\x08H\x00\x12\x16\n\x0cserver_leave\x18\x04 \x01(\x08H\x00\x42\n\n\x08scenario*-\n\x0cSignalTarget\x12\r\n\tPUBLISHER\x10\x00\x12\x0e\n\nSUBSCRIBER\x10\x01*%\n\x0bStreamState\x12\n\n\x06\x41\x43TIVE\x10\x00\x12\n\n\x06PAUSED\x10\x01\x42\x46Z#github.com/livekit/protocol/livekit\xaa\x02\rLiveKit.Proto\xea\x02\x0eLiveKit::Protob\x06proto3'
)

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, "livekit_rtc_pb2", globals())
if _descriptor._USE_C_DESCRIPTORS == False:

    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b"Z#github.com/livekit/protocol/livekit\252\002\rLiveKit.Proto\352\002\016LiveKit::Proto"
    _SIGNALTARGET._serialized_start = 4272
    _SIGNALTARGET._serialized_end = 4317
    _STREAMSTATE._serialized_start = 4319
    _STREAMSTATE._serialized_end = 4356
    _SIGNALREQUEST._serialized_start = 53
    _SIGNALREQUEST._serialized_end = 664
    _SIGNALRESPONSE._serialized_start = 667
    _SIGNALRESPONSE._serialized_end = 1521
    _ADDTRACKREQUEST._serialized_start = 1524
    _ADDTRACKREQUEST._serialized_end = 1744
    _TRICKLEREQUEST._serialized_start = 1746
    _TRICKLEREQUEST._serialized_end = 1824
    _MUTETRACKREQUEST._serialized_start = 1826
    _MUTETRACKREQUEST._serialized_end = 1872
    _JOINRESPONSE._serialized_start = 1875
    _JOINRESPONSE._serialized_end = 2220
    _TRACKPUBLISHEDRESPONSE._serialized_start = 2222
    _TRACKPUBLISHEDRESPONSE._serialized_end = 2294
    _TRACKUNPUBLISHEDRESPONSE._serialized_start = 2296
    _TRACKUNPUBLISHEDRESPONSE._serialized_end = 2341
    _SESSIONDESCRIPTION._serialized_start = 2343
    _SESSIONDESCRIPTION._serialized_end = 2390
    _PARTICIPANTUPDATE._serialized_start = 2392
    _PARTICIPANTUPDATE._serialized_end = 2459
    _UPDATESUBSCRIPTION._serialized_start = 2461
    _UPDATESUBSCRIPTION._serialized_end = 2576
    _UPDATETRACKSETTINGS._serialized_start = 2579
    _UPDATETRACKSETTINGS._serialized_end = 2709
    _LEAVEREQUEST._serialized_start = 2711
    _LEAVEREQUEST._serialized_end = 2748
    _UPDATEVIDEOLAYERS._serialized_start = 2750
    _UPDATEVIDEOLAYERS._serialized_end = 2825
    _ICESERVER._serialized_start = 2827
    _ICESERVER._serialized_end = 2890
    _SPEAKERSCHANGED._serialized_start = 2892
    _SPEAKERSCHANGED._serialized_end = 2949
    _ROOMUPDATE._serialized_start = 2951
    _ROOMUPDATE._serialized_end = 2992
    _CONNECTIONQUALITYINFO._serialized_start = 2994
    _CONNECTIONQUALITYINFO._serialized_end = 3102
    _CONNECTIONQUALITYUPDATE._serialized_start = 3104
    _CONNECTIONQUALITYUPDATE._serialized_end = 3178
    _STREAMSTATEINFO._serialized_start = 3180
    _STREAMSTATEINFO._serialized_end = 3278
    _STREAMSTATEUPDATE._serialized_start = 3280
    _STREAMSTATEUPDATE._serialized_end = 3348
    _SUBSCRIBEDQUALITY._serialized_start = 3350
    _SUBSCRIBEDQUALITY._serialized_end = 3426
    _SUBSCRIBEDQUALITYUPDATE._serialized_start = 3428
    _SUBSCRIBEDQUALITYUPDATE._serialized_end = 3530
    _TRACKPERMISSION._serialized_start = 3532
    _TRACKPERMISSION._serialized_end = 3644
    _SUBSCRIPTIONPERMISSION._serialized_start = 3646
    _SUBSCRIPTIONPERMISSION._serialized_end = 3749
    _SUBSCRIPTIONPERMISSIONUPDATE._serialized_start = 3751
    _SUBSCRIPTIONPERMISSIONUPDATE._serialized_end = 3842
    _SYNCSTATE._serialized_start = 3845
    _SYNCSTATE._serialized_end = 4058
    _DATACHANNELINFO._serialized_start = 4060
    _DATACHANNELINFO._serialized_end = 4143
    _SIMULATESCENARIO._serialized_start = 4145
    _SIMULATESCENARIO._serialized_end = 4270
# @@protoc_insertion_point(module_scope)
