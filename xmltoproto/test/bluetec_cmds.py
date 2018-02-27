import bluetec_pb2
import bluetec_tools

def BT_GEN_POWER_ON_REQ(sock ,local_addr):
	obj = bluetec_pb2.BT_GEN_POWER_ON_REQ_C()
	obj.opcode = 0x1
	obj.local_addr = local_addr.getStr()
	bluetec_tools.send_data(sock, obj.SerializeToString())
def BT_GEN_POWER_OFF_REQ(sock):
	obj = bluetec_pb2.BT_GEN_POWER_OFF_REQ_C()
	obj.opcode = 0x2
	bluetec_tools.send_data(sock, obj.SerializeToString())
def BT_GEN_GET_LOCAL_STATUS_REQ(sock ,sid):
	obj = bluetec_pb2.BT_GEN_GET_LOCAL_STATUS_REQ_C()
	obj.opcode = 0x3
	obj.sid = sid
	bluetec_tools.send_data(sock, obj.SerializeToString())
def BT_GEN_SET_LOCAL_CONFIG_REQ(sock ,cid ,size ,data):
	obj = bluetec_pb2.BT_GEN_SET_LOCAL_CONFIG_REQ_C()
	obj.opcode = 0x4
	obj.cid = cid
	obj.size = size
	obj.data = data
	bluetec_tools.send_data(sock, obj.SerializeToString())
def BT_GEN_READ_LOCAL_CONFIG_REQ(sock ,cid):
	obj = bluetec_pb2.BT_GEN_READ_LOCAL_CONFIG_REQ_C()
	obj.opcode = 0x5
	obj.cid = cid
	bluetec_tools.send_data(sock, obj.SerializeToString())
def BT_GEN_SSP_DEBUG_MODE_REQ(sock ,enable):
	obj = bluetec_pb2.BT_GEN_SSP_DEBUG_MODE_REQ_C()
	obj.opcode = 0x6
	obj.enable = enable
	bluetec_tools.send_data(sock, obj.SerializeToString())
def BT_GEN_SEARCH_REMOTE_DEV_REQ(sock ,count ,timer):
	obj = bluetec_pb2.BT_GEN_SEARCH_REMOTE_DEV_REQ_C()
	obj.opcode = 0x7
	obj.count = count
	obj.timer = timer
	bluetec_tools.send_data(sock, obj.SerializeToString())
def BT_GEN_SEARCH_REMOTE_DEV_CANCEL_REQ(sock):
	obj = bluetec_pb2.BT_GEN_SEARCH_REMOTE_DEV_CANCEL_REQ_C()
	obj.opcode = 0xA
	bluetec_tools.send_data(sock, obj.SerializeToString())
def BT_GEN_SET_LOCAL_NAME_REQ(sock ,length ,name):
	obj = bluetec_pb2.BT_GEN_SET_LOCAL_NAME_REQ_C()
	obj.opcode = 0xB
	obj.length = length
	obj.name = name
	bluetec_tools.send_data(sock, obj.SerializeToString())
def BT_GEN_READ_REMOTE_NAME_REQ(sock ,addr):
	obj = bluetec_pb2.BT_GEN_READ_REMOTE_NAME_REQ_C()
	obj.opcode = 0xC
	obj.addr = addr.getStr()
	bluetec_tools.send_data(sock, obj.SerializeToString())
def BT_GEN_READ_REMOTE_NAME_CANCEL_REQ(sock ,addr):
	obj = bluetec_pb2.BT_GEN_READ_REMOTE_NAME_CANCEL_REQ_C()
	obj.opcode = 0xE
	obj.addr = addr.getStr()
	bluetec_tools.send_data(sock, obj.SerializeToString())
def BT_GEN_GET_LINK_QUALITY_REQ(sock ,addr):
	obj = bluetec_pb2.BT_GEN_GET_LINK_QUALITY_REQ_C()
	obj.opcode = 0x66
	obj.addr = addr.getStr()
	bluetec_tools.send_data(sock, obj.SerializeToString())
def BT_GEN_SET_LOCAL_MODE_REQ(sock ,discovery ,bonded ,connectable):
	obj = bluetec_pb2.BT_GEN_SET_LOCAL_MODE_REQ_C()
	obj.opcode = 0xF
	obj.discovery = discovery
	obj.bonded = bonded
	obj.connectable = connectable
	bluetec_tools.send_data(sock, obj.SerializeToString())
def BT_GEN_SERVICE_SEARCH_REQ(sock ,addr ,timeout):
	obj = bluetec_pb2.BT_GEN_SERVICE_SEARCH_REQ_C()
	obj.opcode = 0x10
	obj.addr = addr.getStr()
	obj.timeout = timeout
	bluetec_tools.send_data(sock, obj.SerializeToString())
def BT_GEN_SDP_SEARCH_CANCEL_REQ(sock ,addr):
	obj = bluetec_pb2.BT_GEN_SDP_SEARCH_CANCEL_REQ_C()
	obj.opcode = 0x13
	obj.addr = addr.getStr()
	bluetec_tools.send_data(sock, obj.SerializeToString())
def BT_GEN_ENTER_TEST_MODE_REQ(sock):
	obj = bluetec_pb2.BT_GEN_ENTER_TEST_MODE_REQ_C()
	obj.opcode = 0x14
	bluetec_tools.send_data(sock, obj.SerializeToString())
def BT_GEN_DISABLE_TEST_MODE_REQ(sock):
	obj = bluetec_pb2.BT_GEN_DISABLE_TEST_MODE_REQ_C()
	obj.opcode = 0x15
	bluetec_tools.send_data(sock, obj.SerializeToString())
def BT_GEN_SERVICE_SEARCH_EXT_REQ(sock ,addr ,uuid):
	obj = bluetec_pb2.BT_GEN_SERVICE_SEARCH_EXT_REQ_C()
	obj.opcode = 0x1A
	obj.addr = addr.getStr()
	obj.uuid = uuid
	bluetec_tools.send_data(sock, obj.SerializeToString())
def BT_GEN_GET_LOCAL_OOB_DATA_REQ(sock):
	obj = bluetec_pb2.BT_GEN_GET_LOCAL_OOB_DATA_REQ_C()
	obj.opcode = 0x1D
	bluetec_tools.send_data(sock, obj.SerializeToString())
def BT_GEN_SET_REMOTE_OOB_DATA_REQ(sock ,addr ,oobHashC ,oobRandR):
	obj = bluetec_pb2.BT_GEN_SET_REMOTE_OOB_DATA_REQ_C()
	obj.opcode = 0x1E
	obj.addr = addr.getStr()
	obj.oobHashC = oobHashC
	obj.oobRandR = oobRandR
	bluetec_tools.send_data(sock, obj.SerializeToString())
def BT_GEN_SEARCH_DEVICE_INFO_REQ(sock ,remote ,timeout):
	obj = bluetec_pb2.BT_GEN_SEARCH_DEVICE_INFO_REQ_C()
	obj.opcode = 0x61
	obj.remote = remote.getStr()
	obj.timeout = timeout
	bluetec_tools.send_data(sock, obj.SerializeToString())
def BT_GEN_REGISTER_DEVICE_INFO_REQ(sock ,vendorID ,productID ,version ,sourceID):
	obj = bluetec_pb2.BT_GEN_REGISTER_DEVICE_INFO_REQ_C()
	obj.opcode = 0x60
	obj.vendorID = vendorID
	obj.productID = productID
	obj.version = version
	obj.sourceID = sourceID
	bluetec_tools.send_data(sock, obj.SerializeToString())
def BT_GEN_UNREGISTER_DEVICE_INFO_REQ(sock):
	obj = bluetec_pb2.BT_GEN_UNREGISTER_DEVICE_INFO_REQ_C()
	obj.opcode = 0x65
	bluetec_tools.send_data(sock, obj.SerializeToString())
def BT_GEN_CANCEL_SEARCH_DEVICE_INFO_REQ(sock):
	obj = bluetec_pb2.BT_GEN_CANCEL_SEARCH_DEVICE_INFO_REQ_C()
	obj.opcode = 0x64
	bluetec_tools.send_data(sock, obj.SerializeToString())
def BT_CM_PAIRING_REMOTE_DEV_REQ(sock ,addr):
	obj = bluetec_pb2.BT_CM_PAIRING_REMOTE_DEV_REQ_C()
	obj.opcode = 0x20
	obj.addr = addr.getStr()
	bluetec_tools.send_data(sock, obj.SerializeToString())
def BT_CM_PAIRING_CANCEL_DEV_REQ(sock ,addr):
	obj = bluetec_pb2.BT_CM_PAIRING_CANCEL_DEV_REQ_C()
	obj.opcode = 0x21
	obj.addr = addr.getStr()
	bluetec_tools.send_data(sock, obj.SerializeToString())
def BT_CM_PIN_CODE_RES(sock ,remote ,len ,pin_code):
	obj = bluetec_pb2.BT_CM_PIN_CODE_RES_C()
	obj.opcode = 0x23
	obj.remote = remote.getStr()
	obj.len = len
	obj.pin_code = pin_code
	bluetec_tools.send_data(sock, obj.SerializeToString())
def BT_CM_NUMERIC_CONFIRM_RES(sock ,remote ,accept):
	obj = bluetec_pb2.BT_CM_NUMERIC_CONFIRM_RES_C()
	obj.opcode = 0x25
	obj.remote = remote.getStr()
	obj.accept = accept
	bluetec_tools.send_data(sock, obj.SerializeToString())
def BT_CM_CON_AUTHORIZE_RES(sock ,remote ,accept):
	obj = bluetec_pb2.BT_CM_CON_AUTHORIZE_RES_C()
	obj.opcode = 0x30
	obj.remote = remote.getStr()
	obj.accept = accept
	bluetec_tools.send_data(sock, obj.SerializeToString())
def BT_CM_SERVICE_CON_REQ(sock ,addr ,service):
	obj = bluetec_pb2.BT_CM_SERVICE_CON_REQ_C()
	obj.opcode = 0x31
	obj.addr = addr.getStr()
	obj.service = service
	bluetec_tools.send_data(sock, obj.SerializeToString())
def BT_CM_SERVICE_CON_CANCEL_REQ(sock ,addr):
	obj = bluetec_pb2.BT_CM_SERVICE_CON_CANCEL_REQ_C()
	obj.opcode = 0x34
	obj.addr = addr.getStr()
	bluetec_tools.send_data(sock, obj.SerializeToString())
def BT_CM_SERVICE_DISCON_REQ(sock ,addr ,service):
	obj = bluetec_pb2.BT_CM_SERVICE_DISCON_REQ_C()
	obj.opcode = 0x35
	obj.addr = addr.getStr()
	obj.service = service
	bluetec_tools.send_data(sock, obj.SerializeToString())
def BT_HFP_DIAL_OUT_REQ(sock ,did ,size ,num):
	obj = bluetec_pb2.BT_HFP_DIAL_OUT_REQ_C()
	obj.opcode = 0x205
	obj.did = did
	obj.size = size
	obj.num = num
	bluetec_tools.send_data(sock, obj.SerializeToString())
def BT_HFP_LAST_DIAL_REQ(sock ,did):
	obj = bluetec_pb2.BT_HFP_LAST_DIAL_REQ_C()
	obj.opcode = 0x206
	obj.did = did
	bluetec_tools.send_data(sock, obj.SerializeToString())
def BT_HFP_MEM_DIAL_REQ(sock ,did ,index):
	obj = bluetec_pb2.BT_HFP_MEM_DIAL_REQ_C()
	obj.opcode = 0x207
	obj.did = did
	obj.index = index
	bluetec_tools.send_data(sock, obj.SerializeToString())
def BT_HFP_CALL_ANSWER_REQ(sock ,did):
	obj = bluetec_pb2.BT_HFP_CALL_ANSWER_REQ_C()
	obj.opcode = 0x208
	obj.did = did
	bluetec_tools.send_data(sock, obj.SerializeToString())
def BT_HFP_CALL_REJECT_REQ(sock ,did):
	obj = bluetec_pb2.BT_HFP_CALL_REJECT_REQ_C()
	obj.opcode = 0x209
	obj.did = did
	bluetec_tools.send_data(sock, obj.SerializeToString())
def BT_HFP_TERMINATE_CALL_REQ(sock ,did):
	obj = bluetec_pb2.BT_HFP_TERMINATE_CALL_REQ_C()
	obj.opcode = 0x20A
	obj.did = did
	bluetec_tools.send_data(sock, obj.SerializeToString())
def BT_HFP_CLIP_ENABLE_REQ(sock ,did ,enable):
	obj = bluetec_pb2.BT_HFP_CLIP_ENABLE_REQ_C()
	obj.opcode = 0x210
	obj.did = did
	obj.enable = enable
	bluetec_tools.send_data(sock, obj.SerializeToString())
def BT_HFP_CCWA_ENABLE_REQ(sock ,did ,enable):
	obj = bluetec_pb2.BT_HFP_CCWA_ENABLE_REQ_C()
	obj.opcode = 0x212
	obj.did = did
	obj.enable = enable
	bluetec_tools.send_data(sock, obj.SerializeToString())
def BT_HFP_AUDIO_TRANSFER_REQ(sock ,did ,side):
	obj = bluetec_pb2.BT_HFP_AUDIO_TRANSFER_REQ_C()
	obj.opcode = 0x20D
	obj.did = did
	obj.side = side
	bluetec_tools.send_data(sock, obj.SerializeToString())
def BT_HFP_SEND_DTMF_REQ(sock ,did ,code):
	obj = bluetec_pb2.BT_HFP_SEND_DTMF_REQ_C()
	obj.opcode = 0x214
	obj.did = did
	obj.code = code
	bluetec_tools.send_data(sock, obj.SerializeToString())
def BT_HFP_PESPONSE_AND_HOLD_REQ(sock ,did ,action):
	obj = bluetec_pb2.BT_HFP_PESPONSE_AND_HOLD_REQ_C()
	obj.opcode = 0x220
	obj.did = did
	obj.action = action
	bluetec_tools.send_data(sock, obj.SerializeToString())
def BT_HFP_CALL_HOLD_REQ(sock ,did ,action ,index):
	obj = bluetec_pb2.BT_HFP_CALL_HOLD_REQ_C()
	obj.opcode = 0x221
	obj.did = did
	obj.action = action
	obj.index = index
	bluetec_tools.send_data(sock, obj.SerializeToString())
def BT_HFP_ANSWER_SECOND_CALL_REQ(sock ,did ,hold):
	obj = bluetec_pb2.BT_HFP_ANSWER_SECOND_CALL_REQ_C()
	obj.opcode = 0x233
	obj.did = did
	obj.hold = hold
	bluetec_tools.send_data(sock, obj.SerializeToString())
def BT_HFP_TERMINATE_CALL_BY_INDEX_REQ(sock ,did ,index):
	obj = bluetec_pb2.BT_HFP_TERMINATE_CALL_BY_INDEX_REQ_C()
	obj.opcode = 0x234
	obj.did = did
	obj.index = index
	bluetec_tools.send_data(sock, obj.SerializeToString())
def BT_HFP_SWITCH_CALL_REQ(sock ,did):
	obj = bluetec_pb2.BT_HFP_SWITCH_CALL_REQ_C()
	obj.opcode = 0x235
	obj.did = did
	bluetec_tools.send_data(sock, obj.SerializeToString())
def BT_HFP_JOIN_CALL_REQ(sock ,did):
	obj = bluetec_pb2.BT_HFP_JOIN_CALL_REQ_C()
	obj.opcode = 0x236
	obj.did = did
	bluetec_tools.send_data(sock, obj.SerializeToString())
def BT_HFP_GET_SUBSCRIBER_NUM_REQ(sock ,did):
	obj = bluetec_pb2.BT_HFP_GET_SUBSCRIBER_NUM_REQ_C()
	obj.opcode = 0x216
	obj.did = did
	bluetec_tools.send_data(sock, obj.SerializeToString())
def BT_HFP_GET_OPERATOR_NAME_REQ(sock ,did):
	obj = bluetec_pb2.BT_HFP_GET_OPERATOR_NAME_REQ_C()
	obj.opcode = 0x215
	obj.did = did
	bluetec_tools.send_data(sock, obj.SerializeToString())
def BT_HFP_GET_CURRENT_CALL_LIST_REQ(sock ,did):
	obj = bluetec_pb2.BT_HFP_GET_CURRENT_CALL_LIST_REQ_C()
	obj.opcode = 0x217
	obj.did = did
	bluetec_tools.send_data(sock, obj.SerializeToString())
def BT_SPP_DATA_SEND_REQ(sock ,spp_id ,length ,data):
	obj = bluetec_pb2.BT_SPP_DATA_SEND_REQ_C()
	obj.opcode = 0x101
	obj.spp_id = spp_id
	obj.length = length
	obj.data = data.getStr()
	bluetec_tools.send_data(sock, obj.SerializeToString())
def BT_SPP_ACTIVE_SERVER_REQ(sock ,uuid ,length ,name):
	obj = bluetec_pb2.BT_SPP_ACTIVE_SERVER_REQ_C()
	obj.opcode = 0x103
	obj.uuid = uuid.getStr()
	obj.length = length
	obj.name = name
	bluetec_tools.send_data(sock, obj.SerializeToString())
def BT_SPP_DEACTIVE_SERVER_REQ(sock ,sppId):
	obj = bluetec_pb2.BT_SPP_DEACTIVE_SERVER_REQ_C()
	obj.opcode = 0x104
	obj.sppId = sppId
	bluetec_tools.send_data(sock, obj.SerializeToString())
def BT_AV_MEDIA_START_REQ(sock ,did):
	obj = bluetec_pb2.BT_AV_MEDIA_START_REQ_C()
	obj.opcode = 0x301
	obj.did = did
	bluetec_tools.send_data(sock, obj.SerializeToString())
def BT_AV_MEDIA_STOP_REQ(sock ,did):
	obj = bluetec_pb2.BT_AV_MEDIA_STOP_REQ_C()
	obj.opcode = 0x302
	obj.did = did
	bluetec_tools.send_data(sock, obj.SerializeToString())
def BT_AV_MEDIA_PASS_THROUGH_REQ(sock ,did ,opid ,state):
	obj = bluetec_pb2.BT_AV_MEDIA_PASS_THROUGH_REQ_C()
	obj.opcode = 0x304
	obj.did = did
	obj.opid = opid
	obj.state = state
	bluetec_tools.send_data(sock, obj.SerializeToString())
def BT_AV_GET_CAPBILITY_REQ(sock ,device_id ,caps):
	obj = bluetec_pb2.BT_AV_GET_CAPBILITY_REQ_C()
	obj.opcode = 0x305
	obj.device_id = device_id
	obj.caps = caps
	bluetec_tools.send_data(sock, obj.SerializeToString())
def BT_AV_GET_PLAY_STATUS_REQ(sock ,did):
	obj = bluetec_pb2.BT_AV_GET_PLAY_STATUS_REQ_C()
	obj.opcode = 0x306
	obj.did = did
	bluetec_tools.send_data(sock, obj.SerializeToString())
def BT_AV_NOTI_REGISTER_REQ(sock ,did ,Notimask ,PlaybackInterval ,configMask):
	obj = bluetec_pb2.BT_AV_NOTI_REGISTER_REQ_C()
	obj.opcode = 0x307
	obj.did = did
	obj.Notimask = Notimask
	obj.PlaybackInterval = PlaybackInterval
	obj.configMask = configMask
	bluetec_tools.send_data(sock, obj.SerializeToString())
def BT_AV_LIST_APP_ATT_ID_REQ(sock ,did):
	obj = bluetec_pb2.BT_AV_LIST_APP_ATT_ID_REQ_C()
	obj.opcode = 0x308
	obj.did = did
	bluetec_tools.send_data(sock, obj.SerializeToString())
def BT_AV_LIST_APP_VALUE_ID_REQ(sock ,did ,attributeid):
	obj = bluetec_pb2.BT_AV_LIST_APP_VALUE_ID_REQ_C()
	obj.opcode = 0x309
	obj.did = did
	obj.attributeid = attributeid
	bluetec_tools.send_data(sock, obj.SerializeToString())
def BT_AV_GET_APP_VALUE_REQ(sock ,did ,attributes):
	obj = bluetec_pb2.BT_AV_GET_APP_VALUE_REQ_C()
	obj.opcode = 0x30A
	obj.did = did
	obj.attributes = attributes
	bluetec_tools.send_data(sock, obj.SerializeToString())
def BT_AV_SET_APP_VALUE_REQ(sock ,did ,attvalPairCount ,attIdLen ,attId ,valIdLen ,valId):
	obj = bluetec_pb2.BT_AV_SET_APP_VALUE_REQ_C()
	obj.opcode = 0x30B
	obj.did = did
	obj.attvalPairCount = attvalPairCount
	obj.attIdLen = attIdLen
	obj.attId = attId.getStr()
	obj.valIdLen = valIdLen
	obj.valId = valId.getStr()
	bluetec_tools.send_data(sock, obj.SerializeToString())
def BT_AV_GET_APP_ATT_TXT_REQ(sock ,did ,attributes):
	obj = bluetec_pb2.BT_AV_GET_APP_ATT_TXT_REQ_C()
	obj.opcode = 0x30C
	obj.did = did
	obj.attributes = attributes
	bluetec_tools.send_data(sock, obj.SerializeToString())
def BT_AV_GET_APP_VALUE_TXT_REQ(sock ,did ,attribute_id ,valIdCount ,values):
	obj = bluetec_pb2.BT_AV_GET_APP_VALUE_TXT_REQ_C()
	obj.opcode = 0x30D
	obj.did = did
	obj.attribute_id = attribute_id
	obj.valIdCount = valIdCount
	obj.values = values.getStr()
	bluetec_tools.send_data(sock, obj.SerializeToString())
def BT_AV_ELEMENT_ATTRIBUTES_REQ(sock ,did ,attributes):
	obj = bluetec_pb2.BT_AV_ELEMENT_ATTRIBUTES_REQ_C()
	obj.opcode = 0x30E
	obj.did = did
	obj.attributes = attributes
	bluetec_tools.send_data(sock, obj.SerializeToString())
def BT_AV_INFORM_BATTERY_STATUS_REQ(sock ,did ,battery_status):
	obj = bluetec_pb2.BT_AV_INFORM_BATTERY_STATUS_REQ_C()
	obj.opcode = 0x30F
	obj.did = did
	obj.battery_status = battery_status
	bluetec_tools.send_data(sock, obj.SerializeToString())
def BT_AV_INFORM_CHARSET_REQ(sock ,did ,charsets):
	obj = bluetec_pb2.BT_AV_INFORM_CHARSET_REQ_C()
	obj.opcode = 0x310
	obj.did = did
	obj.charsets = charsets
	bluetec_tools.send_data(sock, obj.SerializeToString())
def BT_AV_SET_ABSOLUTE_VOL_REQ(sock ,did ,volume):
	obj = bluetec_pb2.BT_AV_SET_ABSOLUTE_VOL_REQ_C()
	obj.opcode = 0x311
	obj.did = did
	obj.volume = volume
	bluetec_tools.send_data(sock, obj.SerializeToString())
def BT_AV_SET_ADDR_PLAYER_REQ(sock ,did ,pid):
	obj = bluetec_pb2.BT_AV_SET_ADDR_PLAYER_REQ_C()
	obj.opcode = 0x312
	obj.did = did
	obj.pid = pid
	bluetec_tools.send_data(sock, obj.SerializeToString())
def BT_AV_PLAY_ITEM_REQ(sock ,did ,scope ,uidHigh ,uidLow ,uid_counter):
	obj = bluetec_pb2.BT_AV_PLAY_ITEM_REQ_C()
	obj.opcode = 0x313
	obj.did = did
	obj.scope = scope
	obj.uidHigh = uidHigh
	obj.uidLow = uidLow
	obj.uid_counter = uid_counter
	bluetec_tools.send_data(sock, obj.SerializeToString())
def BT_AV_ADD_NOW_PLAYING_REQ(sock ,did ,scope ,uidHigh ,uidLow ,uid_counter):
	obj = bluetec_pb2.BT_AV_ADD_NOW_PLAYING_REQ_C()
	obj.opcode = 0x314
	obj.did = did
	obj.scope = scope
	obj.uidHigh = uidHigh
	obj.uidLow = uidLow
	obj.uid_counter = uid_counter
	bluetec_tools.send_data(sock, obj.SerializeToString())
def BT_AV_SET_BROWSED_PLAYER_REQ(sock ,did ,pid):
	obj = bluetec_pb2.BT_AV_SET_BROWSED_PLAYER_REQ_C()
	obj.opcode = 0x315
	obj.did = did
	obj.pid = pid
	bluetec_tools.send_data(sock, obj.SerializeToString())
def BT_AV_CHANGE_PATH_REQ(sock ,did ,direction ,uidHigh ,folder_uid_low ,uid_counter):
	obj = bluetec_pb2.BT_AV_CHANGE_PATH_REQ_C()
	obj.opcode = 0x316
	obj.did = did
	obj.direction = direction
	obj.uidHigh = uidHigh
	obj.folder_uid_low = folder_uid_low
	obj.uid_counter = uid_counter
	bluetec_tools.send_data(sock, obj.SerializeToString())
def BT_AV_GET_ITEM_ATT_REQ(sock ,did ,scope ,uidHigh ,uidLow ,uid_counter ,attributes):
	obj = bluetec_pb2.BT_AV_GET_ITEM_ATT_REQ_C()
	obj.opcode = 0x317
	obj.did = did
	obj.scope = scope
	obj.uidHigh = uidHigh
	obj.uidLow = uidLow
	obj.uid_counter = uid_counter
	obj.attributes = attributes
	bluetec_tools.send_data(sock, obj.SerializeToString())
def BT_AV_GET_FOLDER_ITEM_REQ(sock ,did ,scope ,start ,end ,attributeMask):
	obj = bluetec_pb2.BT_AV_GET_FOLDER_ITEM_REQ_C()
	obj.opcode = 0x318
	obj.did = did
	obj.scope = scope
	obj.start = start
	obj.end = end
	obj.attributeMask = attributeMask
	bluetec_tools.send_data(sock, obj.SerializeToString())
def BT_AV_SEARCH_REQ(sock ,did ,size ,str):
	obj = bluetec_pb2.BT_AV_SEARCH_REQ_C()
	obj.opcode = 0x319
	obj.did = did
	obj.size = size
	obj.str = str.getStr()
	bluetec_tools.send_data(sock, obj.SerializeToString())
def BT_AV_GET_BROWSE_XML_STREAM_REQ(sock ,did):
	obj = bluetec_pb2.BT_AV_GET_BROWSE_XML_STREAM_REQ_C()
	obj.opcode = 0x319
	obj.did = did
	bluetec_tools.send_data(sock, obj.SerializeToString())
def BT_PBDL_ATCMD_START_SERVICE_REQ(sock ,deviceid ,serviceid):
	obj = bluetec_pb2.BT_PBDL_ATCMD_START_SERVICE_REQ_C()
	obj.opcode = 0x401
	obj.deviceid = deviceid
	obj.serviceid = serviceid
	bluetec_tools.send_data(sock, obj.SerializeToString())
def BT_PBDL_ATCMD_GET_STORAGE_REQ(sock ,did):
	obj = bluetec_pb2.BT_PBDL_ATCMD_GET_STORAGE_REQ_C()
	obj.opcode = 0x402
	obj.did = did
	bluetec_tools.send_data(sock, obj.SerializeToString())
def BT_PBDL_ATCMD_GET_CURRENT_STORAGE_REQ(sock ,did):
	obj = bluetec_pb2.BT_PBDL_ATCMD_GET_CURRENT_STORAGE_REQ_C()
	obj.opcode = 0x403
	obj.did = did
	bluetec_tools.send_data(sock, obj.SerializeToString())
def BT_PBDL_ATCMD_SET_STORAGE_REQ(sock ,did ,Storage):
	obj = bluetec_pb2.BT_PBDL_ATCMD_SET_STORAGE_REQ_C()
	obj.opcode = 0x404
	obj.did = did
	obj.Storage = Storage
	bluetec_tools.send_data(sock, obj.SerializeToString())
def BT_PBDL_ATCMD_READ_PB_ENTRY_REQ(sock ,did ,Start_index ,End_index):
	obj = bluetec_pb2.BT_PBDL_ATCMD_READ_PB_ENTRY_REQ_C()
	obj.opcode = 0x405
	obj.did = did
	obj.Start_index = Start_index
	obj.End_index = End_index
	bluetec_tools.send_data(sock, obj.SerializeToString())
def BT_PBDL_ATCMD_FIND_PB_ENTRY_REQ(sock ,did ,textLen ,text):
	obj = bluetec_pb2.BT_PBDL_ATCMD_FIND_PB_ENTRY_REQ_C()
	obj.opcode = 0x406
	obj.did = did
	obj.textLen = textLen
	obj.text = text
	bluetec_tools.send_data(sock, obj.SerializeToString())
def BT_PBDL_ATCMD_ENTRY_DATA_ABORT_REQ(sock ,did):
	obj = bluetec_pb2.BT_PBDL_ATCMD_ENTRY_DATA_ABORT_REQ_C()
	obj.opcode = 0x407
	obj.did = did
	bluetec_tools.send_data(sock, obj.SerializeToString())
def BT_PBDL_PBAP_SET_FOLDER_REQ(sock ,repository ,phonebook):
	obj = bluetec_pb2.BT_PBDL_PBAP_SET_FOLDER_REQ_C()
	obj.opcode = 0x410
	obj.repository = repository
	obj.phonebook = phonebook
	bluetec_tools.send_data(sock, obj.SerializeToString())
def BT_PBDL_PBAP_GET_PBSIZE_REQ(sock ,repository ,phonebook):
	obj = bluetec_pb2.BT_PBDL_PBAP_GET_PBSIZE_REQ_C()
	obj.opcode = 0x411
	obj.repository = repository
	obj.phonebook = phonebook
	bluetec_tools.send_data(sock, obj.SerializeToString())
def BT_PBDL_PBAP_PULL_PB_REQ(sock ,repository ,phonebook ,ver ,filter_lo ,filter_hi ,start_list ,max_list):
	obj = bluetec_pb2.BT_PBDL_PBAP_PULL_PB_REQ_C()
	obj.opcode = 0x412
	obj.repository = repository
	obj.phonebook = phonebook
	obj.ver = ver
	obj.filter_lo = filter_lo
	obj.filter_hi = filter_hi
	obj.start_list = start_list
	obj.max_list = max_list
	bluetec_tools.send_data(sock, obj.SerializeToString())
def BT_PBDL_PBAP_PULL_VCARD_LIST_REQ(sock ,order ,srchAttr ,srchValLen ,SearchValue ,start_list ,max_list):
	obj = bluetec_pb2.BT_PBDL_PBAP_PULL_VCARD_LIST_REQ_C()
	obj.opcode = 0x413
	obj.order = order
	obj.srchAttr = srchAttr
	obj.srchValLen = srchValLen
	obj.SearchValue = SearchValue.getStr()
	obj.start_list = start_list
	obj.max_list = max_list
	bluetec_tools.send_data(sock, obj.SerializeToString())
def BT_PBDL_PBAP_PULL_VCARD_ENTRY_REQ(sock ,entry ,filter_lo ,filter_hi ,ver):
	obj = bluetec_pb2.BT_PBDL_PBAP_PULL_VCARD_ENTRY_REQ_C()
	obj.opcode = 0x414
	obj.entry = entry
	obj.filter_lo = filter_lo
	obj.filter_hi = filter_hi
	obj.ver = ver
	bluetec_tools.send_data(sock, obj.SerializeToString())
def BT_PBDL_PBAP_PULL_ABORT_REQ(sock):
	obj = bluetec_pb2.BT_PBDL_PBAP_PULL_ABORT_REQ_C()
	obj.opcode = 0x41B
	bluetec_tools.send_data(sock, obj.SerializeToString())
def BT_PBDL_OPPS_PUT_ABORT_REQ(sock):
	obj = bluetec_pb2.BT_PBDL_OPPS_PUT_ABORT_REQ_C()
	obj.opcode = 0x420
	bluetec_tools.send_data(sock, obj.SerializeToString())
def BT_PBDL_PULL_PB_REQ(sock):
	obj = bluetec_pb2.BT_PBDL_PULL_PB_REQ_C()
	obj.opcode = 0x430
	bluetec_tools.send_data(sock, obj.SerializeToString())
def BT_MAP_GET_DEVICE_LIST_REQ(sock):
	obj = bluetec_pb2.BT_MAP_GET_DEVICE_LIST_REQ_C()
	obj.opcode = 0x501
	bluetec_tools.send_data(sock, obj.SerializeToString())
def BT_MAP_GET_SDP_RECORD_REQ(sock ,addr):
	obj = bluetec_pb2.BT_MAP_GET_SDP_RECORD_REQ_C()
	obj.opcode = 0x502
	obj.addr = addr.getStr()
	bluetec_tools.send_data(sock, obj.SerializeToString())
def BT_MAP_ESTABLIST_CONNECTION_REQ(sock ,addr ,masInstId):
	obj = bluetec_pb2.BT_MAP_ESTABLIST_CONNECTION_REQ_C()
	obj.opcode = 0x503
	obj.addr = addr.getStr()
	obj.masInstId = masInstId
	bluetec_tools.send_data(sock, obj.SerializeToString())
def BT_MAP_DESTROY_CONNECTION_REQ(sock ,mapcInst):
	obj = bluetec_pb2.BT_MAP_DESTROY_CONNECTION_REQ_C()
	obj.opcode = 0x504
	obj.mapcInst = mapcInst
	bluetec_tools.send_data(sock, obj.SerializeToString())
def BT_MAP_SET_FLODER_REQ(sock ,mapcInst ,length ,name):
	obj = bluetec_pb2.BT_MAP_SET_FLODER_REQ_C()
	obj.opcode = 0x505
	obj.mapcInst = mapcInst
	obj.length = length
	obj.name = name
	bluetec_tools.send_data(sock, obj.SerializeToString())
def BT_MAP_SET_FLODER_BACK_REQ(sock ,mapcInst):
	obj = bluetec_pb2.BT_MAP_SET_FLODER_BACK_REQ_C()
	obj.opcode = 0x506
	obj.mapcInst = mapcInst
	bluetec_tools.send_data(sock, obj.SerializeToString())
def BT_MAP_SET_FLODER_ROOT_REQ(sock ,mapcInst):
	obj = bluetec_pb2.BT_MAP_SET_FLODER_ROOT_REQ_C()
	obj.opcode = 0x507
	obj.mapcInst = mapcInst
	bluetec_tools.send_data(sock, obj.SerializeToString())
def BT_MAP_GET_FLODERLIST_REQ(sock ,InstanceId ,maxcount ,offset):
	obj = bluetec_pb2.BT_MAP_GET_FLODERLIST_REQ_C()
	obj.opcode = 0x508
	obj.InstanceId = InstanceId
	obj.maxcount = maxcount
	obj.offset = offset
	bluetec_tools.send_data(sock, obj.SerializeToString())
def BT_MAP_GET_MESSAGELIST_REQ(sock ,mapcInst ,maxcount ,offset ,subjectLen ,folderNameLen ,folderName ,paramterMask ,filterMessageType ,filterPeriodBegin ,filterPeriodEnd ,filterReadStatus ,recipientLen ,filterRecipient ,originatorLen ,filterOriginator ,filterPriority):
	obj = bluetec_pb2.BT_MAP_GET_MESSAGELIST_REQ_C()
	obj.opcode = 0x509
	obj.mapcInst = mapcInst
	obj.maxcount = maxcount
	obj.offset = offset
	obj.subjectLen = subjectLen
	obj.folderNameLen = folderNameLen
	obj.folderName = folderName
	obj.paramterMask = paramterMask
	obj.filterMessageType = filterMessageType
	obj.filterPeriodBegin = filterPeriodBegin
	obj.filterPeriodEnd = filterPeriodEnd
	obj.filterReadStatus = filterReadStatus
	obj.recipientLen = recipientLen
	obj.filterRecipient = filterRecipient
	obj.originatorLen = originatorLen
	obj.filterOriginator = filterOriginator
	obj.filterPriority = filterPriority
	bluetec_tools.send_data(sock, obj.SerializeToString())
def BT_MAP_GET_MESSAGE_REQ(sock ,instanceId ,handlerLen ,handle ,attachment ,charset ,fractionRequest):
	obj = bluetec_pb2.BT_MAP_GET_MESSAGE_REQ_C()
	obj.opcode = 0x50A
	obj.instanceId = instanceId
	obj.handlerLen = handlerLen
	obj.handle = handle
	obj.attachment = attachment
	obj.charset = charset
	obj.fractionRequest = fractionRequest
	bluetec_tools.send_data(sock, obj.SerializeToString())
def BT_MAP_SET_MESSAGE_STATUS_REQ(sock ,mapcInst ,value ,handlerLen ,handle):
	obj = bluetec_pb2.BT_MAP_SET_MESSAGE_STATUS_REQ_C()
	obj.opcode = 0x50B
	obj.mapcInst = mapcInst
	obj.value = value
	obj.handlerLen = handlerLen
	obj.handle = handle
	bluetec_tools.send_data(sock, obj.SerializeToString())
def BT_MAP_PUT_MESSAGE_REQ(sock ,mapcInst ,length ,content ,transparent ,retry ,charset):
	obj = bluetec_pb2.BT_MAP_PUT_MESSAGE_REQ_C()
	obj.opcode = 0x50D
	obj.mapcInst = mapcInst
	obj.length = length
	obj.content = content.getStr()
	obj.transparent = transparent
	obj.retry = retry
	obj.charset = charset
	bluetec_tools.send_data(sock, obj.SerializeToString())
def BT_MAP_UPDATE_INBOX_REQ(sock ,mapcInst):
	obj = bluetec_pb2.BT_MAP_UPDATE_INBOX_REQ_C()
	obj.opcode = 0x50C
	obj.mapcInst = mapcInst
	bluetec_tools.send_data(sock, obj.SerializeToString())
def BT_MAP_REGISTER_NOTIFICATION_REQ(sock ,mapcInst ,status):
	obj = bluetec_pb2.BT_MAP_REGISTER_NOTIFICATION_REQ_C()
	obj.opcode = 0x50E
	obj.mapcInst = mapcInst
	obj.status = status
	bluetec_tools.send_data(sock, obj.SerializeToString())
def BT_MSG_SUPPORT_SMS_FORMAT_REQ(sock ,did):
	obj = bluetec_pb2.BT_MSG_SUPPORT_SMS_FORMAT_REQ_C()
	obj.opcode = 0x529
	obj.did = did
	bluetec_tools.send_data(sock, obj.SerializeToString())
def BT_MSG_CURRENT_SMS_FORMAT_REQ(sock ,did):
	obj = bluetec_pb2.BT_MSG_CURRENT_SMS_FORMAT_REQ_C()
	obj.opcode = 0x52A
	obj.did = did
	bluetec_tools.send_data(sock, obj.SerializeToString())
def BT_MSG_SET_SMS_FORMAT_REQ(sock ,did ,format):
	obj = bluetec_pb2.BT_MSG_SET_SMS_FORMAT_REQ_C()
	obj.opcode = 0x520
	obj.did = did
	obj.format = format
	bluetec_tools.send_data(sock, obj.SerializeToString())
def BT_MSG_GET_SUPPORT_SMS_STORAGE_REQ(sock ,did):
	obj = bluetec_pb2.BT_MSG_GET_SUPPORT_SMS_STORAGE_REQ_C()
	obj.opcode = 0x52B
	obj.did = did
	bluetec_tools.send_data(sock, obj.SerializeToString())
def BT_MSG_GET_CURRENT_SMS_STORAGE_REQ(sock ,did):
	obj = bluetec_pb2.BT_MSG_GET_CURRENT_SMS_STORAGE_REQ_C()
	obj.opcode = 0x52C
	obj.did = did
	bluetec_tools.send_data(sock, obj.SerializeToString())
def BT_MSG_SELECT_SMS_STORAGE_REQ(sock ,did ,mem1 ,mem2 ,mem3):
	obj = bluetec_pb2.BT_MSG_SELECT_SMS_STORAGE_REQ_C()
	obj.opcode = 0x521
	obj.did = did
	obj.mem1 = mem1
	obj.mem2 = mem2
	obj.mem3 = mem3
	bluetec_tools.send_data(sock, obj.SerializeToString())
def BT_MSG_GET_SUPPORT_LIST_SMS_REQ(sock ,did):
	obj = bluetec_pb2.BT_MSG_GET_SUPPORT_LIST_SMS_REQ_C()
	obj.opcode = 0x52D
	obj.did = did
	bluetec_tools.send_data(sock, obj.SerializeToString())
def BT_MSG_LIST_SMS_REQ(sock ,did ,stat):
	obj = bluetec_pb2.BT_MSG_LIST_SMS_REQ_C()
	obj.opcode = 0x522
	obj.did = did
	obj.stat = stat
	bluetec_tools.send_data(sock, obj.SerializeToString())
def BT_MSG_READ_SMS_REQ(sock ,did ,index):
	obj = bluetec_pb2.BT_MSG_READ_SMS_REQ_C()
	obj.opcode = 0x523
	obj.did = did
	obj.index = index
	bluetec_tools.send_data(sock, obj.SerializeToString())
def BT_MSG_DELETE_SMS_REQ(sock ,did ,index):
	obj = bluetec_pb2.BT_MSG_DELETE_SMS_REQ_C()
	obj.opcode = 0x527
	obj.did = did
	obj.index = index
	bluetec_tools.send_data(sock, obj.SerializeToString())
def BT_MSG_SET_SMS_NOTIFICATION_REQ(sock ,did ,state):
	obj = bluetec_pb2.BT_MSG_SET_SMS_NOTIFICATION_REQ_C()
	obj.opcode = 0x528
	obj.did = did
	obj.state = state
	bluetec_tools.send_data(sock, obj.SerializeToString())
def BT_MSG_SEND_SMS_REQ(sock ,did ,addrLen ,address ,dataLen ,data):
	obj = bluetec_pb2.BT_MSG_SEND_SMS_REQ_C()
	obj.opcode = 0x524
	obj.did = did
	obj.addrLen = addrLen
	obj.address = address
	obj.dataLen = dataLen
	obj.data = data
	bluetec_tools.send_data(sock, obj.SerializeToString())
def BT_HID_CONNECT_REQ(sock ,addr):
	obj = bluetec_pb2.BT_HID_CONNECT_REQ_C()
	obj.opcode = 0x701
	obj.addr = addr.getStr()
	bluetec_tools.send_data(sock, obj.SerializeToString())
def BT_HID_DISCONNECT_REQ(sock):
	obj = bluetec_pb2.BT_HID_DISCONNECT_REQ_C()
	obj.opcode = 0x702
	bluetec_tools.send_data(sock, obj.SerializeToString())
def BT_HID_DATA_REQ(sock ,key ,xRef ,yRef ,wheelRef):
	obj = bluetec_pb2.BT_HID_DATA_REQ_C()
	obj.opcode = 0x703
	obj.key = key
	obj.xRef = xRef
	obj.yRef = yRef
	obj.wheelRef = wheelRef
	bluetec_tools.send_data(sock, obj.SerializeToString())
