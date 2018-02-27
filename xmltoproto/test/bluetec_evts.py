import bluetec_pb2
def parseEvent(opcode, data):
	if opcode == 0x8001:
		return BT_GEN_POWER_ON_CFM(opcode, data)
	if opcode == 0x8002:
		return BT_GEN_POWER_OFF_CFM(opcode, data)
	if opcode == 0x8003:
		return BT_GEN_GET_LOCAL_STATUS_CFM(opcode, data)
	if opcode == 0x8004:
		return BT_GEN_SET_LOCAL_CONFIG_CFM(opcode, data)
	if opcode == 0x8005:
		return BT_GEN_READ_LOCAL_CONFIG_CFM(opcode, data)
	if opcode == 0x8006:
		return BT_GEN_SSP_DEBUG_MODE_CFM(opcode, data)
	if opcode == 0x8007:
		return BT_GEN_SEARCH_REMOTE_DEV_CFM(opcode, data)
	if opcode == 0x8008:
		return BT_GEN_SEARCH_REMOTE_DEV_IND(opcode, data)
	if opcode == 0x8009:
		return BT_GEN_SEARCH_REMOTE_DEV_COMP_IND(opcode, data)
	if opcode == 0x800A:
		return BT_GEN_SEARCH_REMOTE_DEV_CANCEL_CFM(opcode, data)
	if opcode == 0x800B:
		return BT_GEN_SET_LOCAL_NAME_CFM(opcode, data)
	if opcode == 0x800C:
		return BT_GEN_READ_REMOTE_NAME_CFM(opcode, data)
	if opcode == 0x800E:
		return BT_GEN_READ_REMOTE_NAME_CANCEL_CFM(opcode, data)
	if opcode == 0x8066:
		return BT_GEN_GET_LINK_QUALITY_CFM(opcode, data)
	if opcode == 0x800F:
		return BT_GEN_SET_LOCAL_MODE_CFM(opcode, data)
	if opcode == 0x8010:
		return BT_GEN_SERVICE_SEARCH_CFM(opcode, data)
	if opcode == 0x8011:
		return BT_GEN_SERVICE_SEARCH_IND(opcode, data)
	if opcode == 0x8012:
		return BT_GEN_SERVICE_SEARCH_COMP_IND(opcode, data)
	if opcode == 0x8013:
		return BT_GEN_SERVICE_SEARCH_CANCEL_CFM(opcode, data)
	if opcode == 0x801A:
		return BT_GEN_SERVICE_SEARCH_EXT_CFM(opcode, data)
	if opcode == 0x801B:
		return BT_GEN_SERVICE_SEARCH_EXT_IND(opcode, data)
	if opcode == 0x801C:
		return BT_GEN_SERVICE_SEARCH_EXT_COMPLETE_IND(opcode, data)
	if opcode == 0x801D:
		return BT_GEN_GET_LOCAL_OOB_DATA_CFM(opcode, data)
	if opcode == 0x801E:
		return BT_GEN_SET_REMOTE_OOB_DATA_CFM(opcode, data)
	if opcode == 0x8061:
		return BT_GEN_FID_SEARCH_DEV_INFO_CFM(opcode, data)
	if opcode == 0xC062:
		return BT_GEN_FID_SEARCH_DEV_INFO_IND(opcode, data)
	if opcode == 0xC063:
		return BT_GEN_FID_SEARCH_DEV_INFO_COMPLETE_IND(opcode, data)
	if opcode == 0x8060:
		return BT_GEN_FID_REGISTER_DEVICE_INFO_CFM(opcode, data)
	if opcode == 0x8065:
		return BT_GEN_UNREGISTER_DEVICE_INFO_CFM(opcode, data)
	if opcode == 0x8064:
		return BT_GEN_CANCEL_SEARCH_DEVICE_INFO_CFM(opcode, data)
	if opcode == 0x8020:
		return BT_CM_PAIRING_REMOTE_DEV_CFM(opcode, data)
	if opcode == 0x8021:
		return BT_CM_PAIRING_CANCEL_DEV_CFM(opcode, data)
	if opcode == 0x8023:
		return BT_CM_PIN_CODE_IND(opcode, data)
	if opcode == 0x8024:
		return BT_CM_PASSKEY_NOTIFICATION_IND(opcode, data)
	if opcode == 0x8025:
		return BT_CM_NUMERIC_CONFIRM_IND(opcode, data)
	if opcode == 0xC026:
		return BT_CM_NUM_DISPLAY_IND(opcode, data)
	if opcode == 0x8027:
		return BT_CM_PASSKEY_REQ_IND(opcode, data)
	if opcode == 0xC027:
		return BT_GEN_FID_PAIR_COMPLETE_IND(opcode, data)
	if opcode == 0x8030:
		return BT_CM_CON_AUTHORIZE_IND(opcode, data)
	if opcode == 0x8031:
		return BT_CM_SERVICE_CON_CFM(opcode, data)
	if opcode == 0x8032:
		return BT_CM_SERVICE_CON_IND(opcode, data)
	if opcode == 0x8033:
		return BT_CM_SERVICE_CON_COMP_IND(opcode, data)
	if opcode == 0x8034:
		return BT_CM_SERVICE_CON_CANCEL_CFM(opcode, data)
	if opcode == 0x8035:
		return BT_CM_SERVICE_DISCON_CFM(opcode, data)
	if opcode == 0x8036:
		return BT_CM_SERVICE_DISCON_IND(opcode, data)
	if opcode == 0x8037:
		return BT_CM_SERVICE_DISCON_COMP_IND(opcode, data)
	if opcode == 0x8201:
		return BT_HFP_SERVICE_IND(opcode, data)
	if opcode == 0x8202:
		return BT_HFP_SIGNAL_IND(opcode, data)
	if opcode == 0x8203:
		return BT_HFP_ROAM_IND(opcode, data)
	if opcode == 0x8204:
		return BT_HFP_BATTCHG_IND(opcode, data)
	if opcode == 0x820C:
		return BT_HFP_CALL_RING_IND(opcode, data)
	if opcode == 0x8205:
		return BT_HFP_FID_DIAL_CFM(opcode, data)
	if opcode == 0x820B:
		return BT_HFP_CALL_STATE_IND(opcode, data)
	if opcode == 0x8206:
		return BT_HFP_LAST_DIAL_CFM(opcode, data)
	if opcode == 0x8207:
		return BT_HFP_MEM_DIAL_CFM(opcode, data)
	if opcode == 0x8208:
		return BT_HFP_CALL_ANSWER_CFM(opcode, data)
	if opcode == 0x8209:
		return BT_HFP_CALL_REJECT_CFM(opcode, data)
	if opcode == 0x820A:
		return BT_HFP_TERMINATE_CALL_CFM(opcode, data)
	if opcode == 0x8210:
		return BT_HFP_CLIP_ENABLE_CFM(opcode, data)
	if opcode == 0x8212:
		return BT_HFP_CCWA_ENABLE_CFM(opcode, data)
	if opcode == 0x8211:
		return BT_HFP_INCOMING_CALL_IND(opcode, data)
	if opcode == 0x8213:
		return BT_HFP_SECOND_INCOMING_CALL_IND(opcode, data)
	if opcode == 0x820D:
		return BT_HFP_AUDIO_TRANSFER_CFM(opcode, data)
	if opcode == 0x820E:
		return BT_HFP_SCO_IND(opcode, data)
	if opcode == 0x8214:
		return BT_HFP_SEND_DTMF_CFM(opcode, data)
	if opcode == 0x8220:
		return BT_HFP_PESPONSE_AND_HOLD_CFM(opcode, data)
	if opcode == 0x8221:
		return BT_HFP_CALL_HOLD_CFM(opcode, data)
	if opcode == 0x8233:
		return BT_HFP_ANSWER_SECOND_CALL_CFM(opcode, data)
	if opcode == 0x8234:
		return BT_HFP_TERMINATE_CALL_BY_INDEX_CFM(opcode, data)
	if opcode == 0x8235:
		return BT_HFP_SWITCH_CALL_CFM(opcode, data)
	if opcode == 0x8236:
		return BT_HFP_JOIN_CALL_CFM(opcode, data)
	if opcode == 0x8216:
		return BT_HFP_GET_SUBSCRIBER_NUM_CFM(opcode, data)
	if opcode == 0x8215:
		return BT_HFP_GET_OPERATOR_NAME_CFM(opcode, data)
	if opcode == 0x8217:
		return BT_HFP_GET_CURRENT_CALL_LIST_CFM(opcode, data)
	if opcode == 0x8218:
		return BT_HFP_GET_CURRENT_CALL_LIST_IND(opcode, data)
	if opcode == 0x8219:
		return BT_HFP_GET_CURRENT_CALL_LIST_COMPLETE_IND(opcode, data)
	if opcode == 0x8101:
		return BT_SPP_DATA_SEND_CFM(opcode, data)
	if opcode == 0x8102:
		return BT_SPP_DATA_RECEIVE_IND(opcode, data)
	if opcode == 0x8103:
		return BT_SPP_ACTIVE_SERVER_CFM(opcode, data)
	if opcode == 0x8104:
		return BT_SPP_DEACTIVE_SERVER_CFM(opcode, data)
	if opcode == 0x8335:
		return BT_AV_AVRCP_CONNECT_IND(opcode, data)
	if opcode == 0x8336:
		return BT_AV_AVRCP_DISCONNECT_IND(opcode, data)
	if opcode == 0x8301:
		return BT_AV_MEDIA_START_CFM(opcode, data)
	if opcode == 0x8302:
		return BT_AV_MEDIA_STOP_CFM(opcode, data)
	if opcode == 0x8304:
		return BT_AV_MEDIA_PASS_THROUGH_CFM(opcode, data)
	if opcode == 0x8305:
		return BT_AV_GET_CAPBILITY_CFM(opcode, data)
	if opcode == 0x8306:
		return BT_AV_GET_PLAY_STATUS_CFM(opcode, data)
	if opcode == 0x8307:
		return BT_AV_NOTI_REGISTER_CFM(opcode, data)
	if opcode == 0x8308:
		return BT_AV_LIST_APP_ATT_ID_CFM(opcode, data)
	if opcode == 0x8309:
		return BT_AV_LIST_APP_VALUE_ID_CFM(opcode, data)
	if opcode == 0x830A:
		return BT_AV_GET_APP_VALUE_CFM(opcode, data)
	if opcode == 0x830B:
		return BT_AV_SET_APP_VALUE_CFM(opcode, data)
	if opcode == 0x830C:
		return BT_AV_GET_APP_ATT_TXT_CFM(opcode, data)
	if opcode == 0x831A:
		return BT_AV_APP_ATT_TXT_DATA_IND(opcode, data)
	if opcode == 0x831B:
		return BT_AV_APP_ATT_TXT_DATA_COMP_IND(opcode, data)
	if opcode == 0x830D:
		return BT_AV_GET_APP_VALUE_TXT_CFM(opcode, data)
	if opcode == 0x831C:
		return BT_AV_APP_VAL_TXT_DATA_IND(opcode, data)
	if opcode == 0x831D:
		return BT_AV_APP_VAL_TXT_DATA_COMP_IND(opcode, data)
	if opcode == 0x830E:
		return BT_AV_ELEMENT_ATTRIBUTES_CFM(opcode, data)
	if opcode == 0x8333:
		return BT_AV_ELEMENT_ATTRIBUTES_DATA_IND(opcode, data)
	if opcode == 0x8334:
		return BT_AV_ELEMENT_ATTRIBUTES_DATA_COMP_IND(opcode, data)
	if opcode == 0x830F:
		return BT_AV_INFORM_BATTERY_STATUS_CFM(opcode, data)
	if opcode == 0x8310:
		return BT_AV_INFORM_CHARSET_CFM(opcode, data)
	if opcode == 0x8311:
		return BT_AV_SET_ABSOLUTE_VOL_CFM(opcode, data)
	if opcode == 0x8312:
		return BT_AV_SET_ADDR_PLAYER_CFM(opcode, data)
	if opcode == 0x8313:
		return BT_AV_PLAY_ITEM_CFM(opcode, data)
	if opcode == 0x8314:
		return BT_AV_ADD_NOW_PLAYING_CFM(opcode, data)
	if opcode == 0x8315:
		return BT_AV_SET_BROWSED_PLAYER_CFM(opcode, data)
	if opcode == 0x8316:
		return BT_AV_CHANGE_PATH_CFM(opcode, data)
	if opcode == 0x8317:
		return BT_AV_GET_ITEM_ATT_CFM(opcode, data)
	if opcode == 0x8331:
		return BT_AV_BROWSE_ITEM_ATTRIBUTES_DATA_IND(opcode, data)
	if opcode == 0x8332:
		return BT_AV_BROWSE_ITEM_ATTRIBUTES_DATA_COMP_IND(opcode, data)
	if opcode == 0x8318:
		return BT_AV_GET_FOLDER_ITEM_CFM(opcode, data)
	if opcode == 0x832F:
		return BT_AV_BROWSE_PLAYER_ITEM_DATA_IND(opcode, data)
	if opcode == 0x832D:
		return BT_AV_BROWSE_FOLDER_ITEM_DATA_IND(opcode, data)
	if opcode == 0x832E:
		return BT_AV_BROWSE_MEDIA_ITEM_DATA_IND(opcode, data)
	if opcode == 0x8330:
		return BT_AV_BROWSE_ITEM_DATA_COMP_IND(opcode, data)
	if opcode == 0x8319:
		return BT_AV_SEARCH_CFM(opcode, data)
	if opcode == 0x8319:
		return BT_AV_GET_BROWSE_XML_STREAM_CFM(opcode, data)
	if opcode == 0x8320:
		return BT_AV_PLAYER_STATUS_CHANGE_NOTI_IND(opcode, data)
	if opcode == 0x8321:
		return BT_AV_TRACK_CHANGE_NOTI_IND(opcode, data)
	if opcode == 0x8322:
		return BT_AV_REACHED_END_NOTI_IND(opcode, data)
	if opcode == 0x8323:
		return BT_AV_REACHED_START_NOTI_IND(opcode, data)
	if opcode == 0x8324:
		return BT_AV_PLAYBACK_POSITION_CHANGE_NOTI_IND(opcode, data)
	if opcode == 0x8325:
		return BT_AV_BATTERY_STATUS_CHANGE_NOTI_IND(opcode, data)
	if opcode == 0x8326:
		return BT_AV_SYSTEM_STATUS_CHANGE_NOTI_IND(opcode, data)
	if opcode == 0x8328:
		return BT_AV_PLAYING_CONTENT_CHANGE_NOTI_IND(opcode, data)
	if opcode == 0x832C:
		return BT_AV_AVAILABLE_PLAYER_CHANGE_NOTI_IND(opcode, data)
	if opcode == 0x8329:
		return BT_AV_ADDRESSED_PLAYER_CHANGE_NOTI_IND(opcode, data)
	if opcode == 0x832A:
		return BT_AV_UID_CHANGE_NOTI_IND(opcode, data)
	if opcode == 0x832B:
		return BT_AV_VOLUME_CHANGE_NOTI_IND(opcode, data)
	if opcode == 0x8327:
		return BT_AVP_FID_EVT_PLAYER_APP_SETTING_CHANGED_IND(opcode, data)
	if opcode == 0x8338:
		return BT_AV_A2DP_CONFIGURATION_IND(opcode, data)
	if opcode == 0x8339:
		return BT_AV_A2DP_STREAM_DATA_IND(opcode, data)
	if opcode == 0x8401:
		return BT_PBDL_ATCMD_START_SERVICE_CFM(opcode, data)
	if opcode == 0x8402:
		return BT_PBDL_ATCMD_GET_STORAGE_CFM(opcode, data)
	if opcode == 0x8403:
		return BT_PBDL_ATCMD_GET_CURRENT_STORAGE_CFM(opcode, data)
	if opcode == 0x8404:
		return BT_PBDL_ATCMD_SET_STORAGE_CFM(opcode, data)
	if opcode == 0x8405:
		return BT_PBDL_ATCMD_READ_PB_ENTRY_CFM(opcode, data)
	if opcode == 0x8406:
		return BT_PBDL_ATCMD_FIND_PB_ENTRY_CFM(opcode, data)
	if opcode == 0x8407:
		return BT_PBDL_ATCMD_ENTRY_DATA_ABORT_CFM(opcode, data)
	if opcode == 0x8408:
		return BT_PBDL_ATCMD_PB_ENTRY_DATA_IND(opcode, data)
	if opcode == 0x8409:
		return BT_PBDL_ATCMD_PB_ENTRY_DATA_COMPLETE_IND(opcode, data)
	if opcode == 0x840A:
		return BT_PBDL_ATCMD_CONNECTION_IND(opcode, data)
	if opcode == 0x840B:
		return BT_PBDL_ATCMD_DISCONNECTION_IND(opcode, data)
	if opcode == 0x8410:
		return BT_PBDL_PBAP_SET_FOLDER_CFM(opcode, data)
	if opcode == 0x8411:
		return BT_PBDL_PBAP_GET_PBSIZE_CFM(opcode, data)
	if opcode == 0x8412:
		return BT_PBDL_PBAP_PULL_PB_CFM(opcode, data)
	if opcode == 0x8413:
		return BT_PBDL_PBAP_PULL_VCARD_LIST_CFM(opcode, data)
	if opcode == 0x8414:
		return BT_PBDL_PBAP_PULL_VCARD_ENTRY_CFM(opcode, data)
	if opcode == 0x8415:
		return BT_PBDL_PBAP_PB_ENTRY_DATA_IND(opcode, data)
	if opcode == 0x8416:
		return BT_PBDL_PBAP_PB_ENTRY_DATA_COMPLETE_IND(opcode, data)
	if opcode == 0x8417:
		return BT_PBDL_PBAP_VCARD_LIST_DATA_IND(opcode, data)
	if opcode == 0x8418:
		return BT_PBDL_PBAP_VCARD_LIST_DATA_COMPLETE_IND(opcode, data)
	if opcode == 0x8419:
		return BT_PBDL_PBAP_VCARD_ENTRY_DATA_IND(opcode, data)
	if opcode == 0x841A:
		return BT_PBDL_PBAP_VCARD_ENTRY_DATA_COMPLETE_IND(opcode, data)
	if opcode == 0x841B:
		return BT_PBDL_PBAP_PULL_ABORT_CFM(opcode, data)
	if opcode == 0x841C:
		return BT_PBDL_OPPS_PUT_FILE_IND(opcode, data)
	if opcode == 0x841D:
		return BT_PBDL_OPPS_PUT_BODY_IND(opcode, data)
	if opcode == 0x841E:
		return BT_PBDL_OPPS_PUT_COMPLETE_IND(opcode, data)
	if opcode == 0x841F:
		return BT_PBDL_OPPS_PUT_ABORT_IND(opcode, data)
	if opcode == 0x8420:
		return BT_PBDL_OPPS_PUT_ABORT_CFM(opcode, data)
	if opcode == 0x8430:
		return BT_PBDL_PULL_PB_CFM(opcode, data)
	if opcode == 0x8432:
		return BT_PBDL_PULL_PB_CMP_IND(opcode, data)
	if opcode == 0x8501:
		return BT_MAP_GET_DEVICE_LIST_CFM(opcode, data)
	if opcode == 0x8502:
		return BT_MAP_GET_SDP_RECORD_CFM(opcode, data)
	if opcode == 0x8510:
		return BT_MAP_GET_SDP_RECORD_IND(opcode, data)
	if opcode == 0x8511:
		return BT_MAP_SDP_RECORD_COMPLETE_IND(opcode, data)
	if opcode == 0x8503:
		return BT_MAP_ESTABLIST_CONNECTION_CFM(opcode, data)
	if opcode == 0x8504:
		return BT_MAP_DESTROY_CONNECTION_CFM(opcode, data)
	if opcode == 0x8505:
		return BT_MAP_SET_FLODER_CFM(opcode, data)
	if opcode == 0x8506:
		return BT_MAP_SET_FLODER_BACK_CFM(opcode, data)
	if opcode == 0x8507:
		return BT_MAP_SET_FLODER_ROOT_CFM(opcode, data)
	if opcode == 0x8508:
		return BT_MAP_GET_FLODERLIST_CFM(opcode, data)
	if opcode == 0x8514:
		return BT_MAP_GET_FLODERLIST_IND(opcode, data)
	if opcode == 0x8515:
		return BT_MAP_FLODERLIST_COMPLETE_IND(opcode, data)
	if opcode == 0x8509:
		return BT_MAP_GET_MESSAGELIST_CFM(opcode, data)
	if opcode == 0x8516:
		return BT_MAP_GET_MESSAGELIST_IND(opcode, data)
	if opcode == 0x8517:
		return BT_MAP_GET_MESSAGELIST_COMPLETE_IND(opcode, data)
	if opcode == 0x850A:
		return BT_MAP_GET_MESSAGE_CFM(opcode, data)
	if opcode == 0x8518:
		return BT_MAP_GET_MESSAGE_IND(opcode, data)
	if opcode == 0x8519:
		return BT_MAP_FID_MESSAGE_COMPLETE_IND(opcode, data)
	if opcode == 0x850B:
		return BT_MAP_SET_MESSAGE_STATUS_CFM(opcode, data)
	if opcode == 0x850D:
		return BT_MAP_PUT_MESSAGE_CFM(opcode, data)
	if opcode == 0x850C:
		return BT_MAP_UPDATE_INBOX_CFM(opcode, data)
	if opcode == 0x850E:
		return BT_MAP_REGISTER_NOTIFICATION_CFM(opcode, data)
	if opcode == 0x851C:
		return BT_MAP_MESSAGE_NOTIFICATION_OFF_IND(opcode, data)
	if opcode == 0x851B:
		return BT_MAP_MESSAGE_NOTIFICATION_IND(opcode, data)
	if opcode == 0x8533:
		return BT_AT_SMS_CONNECTION_IND(opcode, data)
	if opcode == 0x8534:
		return BT_AT_SMS_DISCONNECTION_IND(opcode, data)
	if opcode == 0x8529:
		return BT_MSG_SUPPORT_SMS_FORMAT_CFM(opcode, data)
	if opcode == 0x852A:
		return BT_MSG_CURRENT_SMS_FORMAT_CFM(opcode, data)
	if opcode == 0x8520:
		return BT_MSG_SET_SMS_FORMAT_CFM(opcode, data)
	if opcode == 0x852B:
		return BT_MSG_GET_SUPPORT_SMS_STORAGE_CFM(opcode, data)
	if opcode == 0x852C:
		return BT_MSG_GET_CURRENT_SMS_STORAGE_CFM(opcode, data)
	if opcode == 0x8521:
		return BT_MSG_SELECT_SMS_STORAGE_CFM(opcode, data)
	if opcode == 0x852D:
		return BT_MSG_GET_SUPPORT_LIST_SMS_CFM(opcode, data)
	if opcode == 0x8522:
		return BT_MSG_LIST_SMS_CFM(opcode, data)
	if opcode == 0x8530:
		return BT_MSG_GET_CONTENT_IND(opcode, data)
	if opcode == 0x8531:
		return BT_MSG_GET_CONTENT_COMPLETED_IND(opcode, data)
	if opcode == 0x8523:
		return BT_MSG_READ_SMS_CFM(opcode, data)
	if opcode == 0x8527:
		return BT_MSG_DELETE_SMS_CFM(opcode, data)
	if opcode == 0x8528:
		return BT_MSG_SET_SMS_NOTIFICATION_CFM(opcode, data)
	if opcode == 0x8524:
		return BT_MSG_SEND_SMS_CFM(opcode, data)
	if opcode == 0x8701:
		return BT_HID_CONNECT_CFM(opcode, data)
	if opcode == 0x8702:
		return BT_HID_DISCONNECT_CFM(opcode, data)
	if opcode == 0x8703:
		return BT_HID_DATA_CFM(opcode, data)
	if opcode == 0x8710:
		return BT_HID_STATUS_IND(opcode, data)
def BT_GEN_POWER_ON_CFM(opcode, data):
	obj = bluetec_pb2.BT_GEN_POWER_ON_CFM_C()
	obj.ParseFromString(data)
	return obj
def BT_GEN_POWER_OFF_CFM(opcode, data):
	obj = bluetec_pb2.BT_GEN_POWER_OFF_CFM_C()
	obj.ParseFromString(data)
	return obj
def BT_GEN_GET_LOCAL_STATUS_CFM(opcode, data):
	obj = bluetec_pb2.BT_GEN_GET_LOCAL_STATUS_CFM_C()
	obj.ParseFromString(data)
	return obj
def BT_GEN_SET_LOCAL_CONFIG_CFM(opcode, data):
	obj = bluetec_pb2.BT_GEN_SET_LOCAL_CONFIG_CFM_C()
	obj.ParseFromString(data)
	return obj
def BT_GEN_READ_LOCAL_CONFIG_CFM(opcode, data):
	obj = bluetec_pb2.BT_GEN_READ_LOCAL_CONFIG_CFM_C()
	obj.ParseFromString(data)
	return obj
def BT_GEN_SSP_DEBUG_MODE_CFM(opcode, data):
	obj = bluetec_pb2.BT_GEN_SSP_DEBUG_MODE_CFM_C()
	obj.ParseFromString(data)
	return obj
def BT_GEN_SEARCH_REMOTE_DEV_CFM(opcode, data):
	obj = bluetec_pb2.BT_GEN_SEARCH_REMOTE_DEV_CFM_C()
	obj.ParseFromString(data)
	return obj
def BT_GEN_SEARCH_REMOTE_DEV_IND(opcode, data):
	obj = bluetec_pb2.BT_GEN_SEARCH_REMOTE_DEV_IND_C()
	obj.ParseFromString(data)
	return obj
def BT_GEN_SEARCH_REMOTE_DEV_COMP_IND(opcode, data):
	obj = bluetec_pb2.BT_GEN_SEARCH_REMOTE_DEV_COMP_IND_C()
	obj.ParseFromString(data)
	return obj
def BT_GEN_SEARCH_REMOTE_DEV_CANCEL_CFM(opcode, data):
	obj = bluetec_pb2.BT_GEN_SEARCH_REMOTE_DEV_CANCEL_CFM_C()
	obj.ParseFromString(data)
	return obj
def BT_GEN_SET_LOCAL_NAME_CFM(opcode, data):
	obj = bluetec_pb2.BT_GEN_SET_LOCAL_NAME_CFM_C()
	obj.ParseFromString(data)
	return obj
def BT_GEN_READ_REMOTE_NAME_CFM(opcode, data):
	obj = bluetec_pb2.BT_GEN_READ_REMOTE_NAME_CFM_C()
	obj.ParseFromString(data)
	return obj
def BT_GEN_READ_REMOTE_NAME_CANCEL_CFM(opcode, data):
	obj = bluetec_pb2.BT_GEN_READ_REMOTE_NAME_CANCEL_CFM_C()
	obj.ParseFromString(data)
	return obj
def BT_GEN_GET_LINK_QUALITY_CFM(opcode, data):
	obj = bluetec_pb2.BT_GEN_GET_LINK_QUALITY_CFM_C()
	obj.ParseFromString(data)
	return obj
def BT_GEN_SET_LOCAL_MODE_CFM(opcode, data):
	obj = bluetec_pb2.BT_GEN_SET_LOCAL_MODE_CFM_C()
	obj.ParseFromString(data)
	return obj
def BT_GEN_SERVICE_SEARCH_CFM(opcode, data):
	obj = bluetec_pb2.BT_GEN_SERVICE_SEARCH_CFM_C()
	obj.ParseFromString(data)
	return obj
def BT_GEN_SERVICE_SEARCH_IND(opcode, data):
	obj = bluetec_pb2.BT_GEN_SERVICE_SEARCH_IND_C()
	obj.ParseFromString(data)
	return obj
def BT_GEN_SERVICE_SEARCH_COMP_IND(opcode, data):
	obj = bluetec_pb2.BT_GEN_SERVICE_SEARCH_COMP_IND_C()
	obj.ParseFromString(data)
	return obj
def BT_GEN_SERVICE_SEARCH_CANCEL_CFM(opcode, data):
	obj = bluetec_pb2.BT_GEN_SERVICE_SEARCH_CANCEL_CFM_C()
	obj.ParseFromString(data)
	return obj
def BT_GEN_SERVICE_SEARCH_EXT_CFM(opcode, data):
	obj = bluetec_pb2.BT_GEN_SERVICE_SEARCH_EXT_CFM_C()
	obj.ParseFromString(data)
	return obj
def BT_GEN_SERVICE_SEARCH_EXT_IND(opcode, data):
	obj = bluetec_pb2.BT_GEN_SERVICE_SEARCH_EXT_IND_C()
	obj.ParseFromString(data)
	return obj
def BT_GEN_SERVICE_SEARCH_EXT_COMPLETE_IND(opcode, data):
	obj = bluetec_pb2.BT_GEN_SERVICE_SEARCH_EXT_COMPLETE_IND_C()
	obj.ParseFromString(data)
	return obj
def BT_GEN_GET_LOCAL_OOB_DATA_CFM(opcode, data):
	obj = bluetec_pb2.BT_GEN_GET_LOCAL_OOB_DATA_CFM_C()
	obj.ParseFromString(data)
	return obj
def BT_GEN_SET_REMOTE_OOB_DATA_CFM(opcode, data):
	obj = bluetec_pb2.BT_GEN_SET_REMOTE_OOB_DATA_CFM_C()
	obj.ParseFromString(data)
	return obj
def BT_GEN_FID_SEARCH_DEV_INFO_CFM(opcode, data):
	obj = bluetec_pb2.BT_GEN_FID_SEARCH_DEV_INFO_CFM_C()
	obj.ParseFromString(data)
	return obj
def BT_GEN_FID_SEARCH_DEV_INFO_IND(opcode, data):
	obj = bluetec_pb2.BT_GEN_FID_SEARCH_DEV_INFO_IND_C()
	obj.ParseFromString(data)
	return obj
def BT_GEN_FID_SEARCH_DEV_INFO_COMPLETE_IND(opcode, data):
	obj = bluetec_pb2.BT_GEN_FID_SEARCH_DEV_INFO_COMPLETE_IND_C()
	obj.ParseFromString(data)
	return obj
def BT_GEN_FID_REGISTER_DEVICE_INFO_CFM(opcode, data):
	obj = bluetec_pb2.BT_GEN_FID_REGISTER_DEVICE_INFO_CFM_C()
	obj.ParseFromString(data)
	return obj
def BT_GEN_UNREGISTER_DEVICE_INFO_CFM(opcode, data):
	obj = bluetec_pb2.BT_GEN_UNREGISTER_DEVICE_INFO_CFM_C()
	obj.ParseFromString(data)
	return obj
def BT_GEN_CANCEL_SEARCH_DEVICE_INFO_CFM(opcode, data):
	obj = bluetec_pb2.BT_GEN_CANCEL_SEARCH_DEVICE_INFO_CFM_C()
	obj.ParseFromString(data)
	return obj
def BT_CM_PAIRING_REMOTE_DEV_CFM(opcode, data):
	obj = bluetec_pb2.BT_CM_PAIRING_REMOTE_DEV_CFM_C()
	obj.ParseFromString(data)
	return obj
def BT_CM_PAIRING_CANCEL_DEV_CFM(opcode, data):
	obj = bluetec_pb2.BT_CM_PAIRING_CANCEL_DEV_CFM_C()
	obj.ParseFromString(data)
	return obj
def BT_CM_PIN_CODE_IND(opcode, data):
	obj = bluetec_pb2.BT_CM_PIN_CODE_IND_C()
	obj.ParseFromString(data)
	return obj
def BT_CM_PASSKEY_NOTIFICATION_IND(opcode, data):
	obj = bluetec_pb2.BT_CM_PASSKEY_NOTIFICATION_IND_C()
	obj.ParseFromString(data)
	return obj
def BT_CM_NUMERIC_CONFIRM_IND(opcode, data):
	obj = bluetec_pb2.BT_CM_NUMERIC_CONFIRM_IND_C()
	obj.ParseFromString(data)
	return obj
def BT_CM_NUM_DISPLAY_IND(opcode, data):
	obj = bluetec_pb2.BT_CM_NUM_DISPLAY_IND_C()
	obj.ParseFromString(data)
	return obj
def BT_CM_PASSKEY_REQ_IND(opcode, data):
	obj = bluetec_pb2.BT_CM_PASSKEY_REQ_IND_C()
	obj.ParseFromString(data)
	return obj
def BT_GEN_FID_PAIR_COMPLETE_IND(opcode, data):
	obj = bluetec_pb2.BT_GEN_FID_PAIR_COMPLETE_IND_C()
	obj.ParseFromString(data)
	return obj
def BT_CM_CON_AUTHORIZE_IND(opcode, data):
	obj = bluetec_pb2.BT_CM_CON_AUTHORIZE_IND_C()
	obj.ParseFromString(data)
	return obj
def BT_CM_SERVICE_CON_CFM(opcode, data):
	obj = bluetec_pb2.BT_CM_SERVICE_CON_CFM_C()
	obj.ParseFromString(data)
	return obj
def BT_CM_SERVICE_CON_IND(opcode, data):
	obj = bluetec_pb2.BT_CM_SERVICE_CON_IND_C()
	obj.ParseFromString(data)
	return obj
def BT_CM_SERVICE_CON_COMP_IND(opcode, data):
	obj = bluetec_pb2.BT_CM_SERVICE_CON_COMP_IND_C()
	obj.ParseFromString(data)
	return obj
def BT_CM_SERVICE_CON_CANCEL_CFM(opcode, data):
	obj = bluetec_pb2.BT_CM_SERVICE_CON_CANCEL_CFM_C()
	obj.ParseFromString(data)
	return obj
def BT_CM_SERVICE_DISCON_CFM(opcode, data):
	obj = bluetec_pb2.BT_CM_SERVICE_DISCON_CFM_C()
	obj.ParseFromString(data)
	return obj
def BT_CM_SERVICE_DISCON_IND(opcode, data):
	obj = bluetec_pb2.BT_CM_SERVICE_DISCON_IND_C()
	obj.ParseFromString(data)
	return obj
def BT_CM_SERVICE_DISCON_COMP_IND(opcode, data):
	obj = bluetec_pb2.BT_CM_SERVICE_DISCON_COMP_IND_C()
	obj.ParseFromString(data)
	return obj
def BT_HFP_SERVICE_IND(opcode, data):
	obj = bluetec_pb2.BT_HFP_SERVICE_IND_C()
	obj.ParseFromString(data)
	return obj
def BT_HFP_SIGNAL_IND(opcode, data):
	obj = bluetec_pb2.BT_HFP_SIGNAL_IND_C()
	obj.ParseFromString(data)
	return obj
def BT_HFP_ROAM_IND(opcode, data):
	obj = bluetec_pb2.BT_HFP_ROAM_IND_C()
	obj.ParseFromString(data)
	return obj
def BT_HFP_BATTCHG_IND(opcode, data):
	obj = bluetec_pb2.BT_HFP_BATTCHG_IND_C()
	obj.ParseFromString(data)
	return obj
def BT_HFP_CALL_RING_IND(opcode, data):
	obj = bluetec_pb2.BT_HFP_CALL_RING_IND_C()
	obj.ParseFromString(data)
	return obj
def BT_HFP_FID_DIAL_CFM(opcode, data):
	obj = bluetec_pb2.BT_HFP_FID_DIAL_CFM_C()
	obj.ParseFromString(data)
	return obj
def BT_HFP_CALL_STATE_IND(opcode, data):
	obj = bluetec_pb2.BT_HFP_CALL_STATE_IND_C()
	obj.ParseFromString(data)
	return obj
def BT_HFP_LAST_DIAL_CFM(opcode, data):
	obj = bluetec_pb2.BT_HFP_LAST_DIAL_CFM_C()
	obj.ParseFromString(data)
	return obj
def BT_HFP_MEM_DIAL_CFM(opcode, data):
	obj = bluetec_pb2.BT_HFP_MEM_DIAL_CFM_C()
	obj.ParseFromString(data)
	return obj
def BT_HFP_CALL_ANSWER_CFM(opcode, data):
	obj = bluetec_pb2.BT_HFP_CALL_ANSWER_CFM_C()
	obj.ParseFromString(data)
	return obj
def BT_HFP_CALL_REJECT_CFM(opcode, data):
	obj = bluetec_pb2.BT_HFP_CALL_REJECT_CFM_C()
	obj.ParseFromString(data)
	return obj
def BT_HFP_TERMINATE_CALL_CFM(opcode, data):
	obj = bluetec_pb2.BT_HFP_TERMINATE_CALL_CFM_C()
	obj.ParseFromString(data)
	return obj
def BT_HFP_CLIP_ENABLE_CFM(opcode, data):
	obj = bluetec_pb2.BT_HFP_CLIP_ENABLE_CFM_C()
	obj.ParseFromString(data)
	return obj
def BT_HFP_CCWA_ENABLE_CFM(opcode, data):
	obj = bluetec_pb2.BT_HFP_CCWA_ENABLE_CFM_C()
	obj.ParseFromString(data)
	return obj
def BT_HFP_INCOMING_CALL_IND(opcode, data):
	obj = bluetec_pb2.BT_HFP_INCOMING_CALL_IND_C()
	obj.ParseFromString(data)
	return obj
def BT_HFP_SECOND_INCOMING_CALL_IND(opcode, data):
	obj = bluetec_pb2.BT_HFP_SECOND_INCOMING_CALL_IND_C()
	obj.ParseFromString(data)
	return obj
def BT_HFP_AUDIO_TRANSFER_CFM(opcode, data):
	obj = bluetec_pb2.BT_HFP_AUDIO_TRANSFER_CFM_C()
	obj.ParseFromString(data)
	return obj
def BT_HFP_SCO_IND(opcode, data):
	obj = bluetec_pb2.BT_HFP_SCO_IND_C()
	obj.ParseFromString(data)
	return obj
def BT_HFP_SEND_DTMF_CFM(opcode, data):
	obj = bluetec_pb2.BT_HFP_SEND_DTMF_CFM_C()
	obj.ParseFromString(data)
	return obj
def BT_HFP_PESPONSE_AND_HOLD_CFM(opcode, data):
	obj = bluetec_pb2.BT_HFP_PESPONSE_AND_HOLD_CFM_C()
	obj.ParseFromString(data)
	return obj
def BT_HFP_CALL_HOLD_CFM(opcode, data):
	obj = bluetec_pb2.BT_HFP_CALL_HOLD_CFM_C()
	obj.ParseFromString(data)
	return obj
def BT_HFP_ANSWER_SECOND_CALL_CFM(opcode, data):
	obj = bluetec_pb2.BT_HFP_ANSWER_SECOND_CALL_CFM_C()
	obj.ParseFromString(data)
	return obj
def BT_HFP_TERMINATE_CALL_BY_INDEX_CFM(opcode, data):
	obj = bluetec_pb2.BT_HFP_TERMINATE_CALL_BY_INDEX_CFM_C()
	obj.ParseFromString(data)
	return obj
def BT_HFP_SWITCH_CALL_CFM(opcode, data):
	obj = bluetec_pb2.BT_HFP_SWITCH_CALL_CFM_C()
	obj.ParseFromString(data)
	return obj
def BT_HFP_JOIN_CALL_CFM(opcode, data):
	obj = bluetec_pb2.BT_HFP_JOIN_CALL_CFM_C()
	obj.ParseFromString(data)
	return obj
def BT_HFP_GET_SUBSCRIBER_NUM_CFM(opcode, data):
	obj = bluetec_pb2.BT_HFP_GET_SUBSCRIBER_NUM_CFM_C()
	obj.ParseFromString(data)
	return obj
def BT_HFP_GET_OPERATOR_NAME_CFM(opcode, data):
	obj = bluetec_pb2.BT_HFP_GET_OPERATOR_NAME_CFM_C()
	obj.ParseFromString(data)
	return obj
def BT_HFP_GET_CURRENT_CALL_LIST_CFM(opcode, data):
	obj = bluetec_pb2.BT_HFP_GET_CURRENT_CALL_LIST_CFM_C()
	obj.ParseFromString(data)
	return obj
def BT_HFP_GET_CURRENT_CALL_LIST_IND(opcode, data):
	obj = bluetec_pb2.BT_HFP_GET_CURRENT_CALL_LIST_IND_C()
	obj.ParseFromString(data)
	return obj
def BT_HFP_GET_CURRENT_CALL_LIST_COMPLETE_IND(opcode, data):
	obj = bluetec_pb2.BT_HFP_GET_CURRENT_CALL_LIST_COMPLETE_IND_C()
	obj.ParseFromString(data)
	return obj
def BT_SPP_DATA_SEND_CFM(opcode, data):
	obj = bluetec_pb2.BT_SPP_DATA_SEND_CFM_C()
	obj.ParseFromString(data)
	return obj
def BT_SPP_DATA_RECEIVE_IND(opcode, data):
	obj = bluetec_pb2.BT_SPP_DATA_RECEIVE_IND_C()
	obj.ParseFromString(data)
	return obj
def BT_SPP_ACTIVE_SERVER_CFM(opcode, data):
	obj = bluetec_pb2.BT_SPP_ACTIVE_SERVER_CFM_C()
	obj.ParseFromString(data)
	return obj
def BT_SPP_DEACTIVE_SERVER_CFM(opcode, data):
	obj = bluetec_pb2.BT_SPP_DEACTIVE_SERVER_CFM_C()
	obj.ParseFromString(data)
	return obj
def BT_AV_AVRCP_CONNECT_IND(opcode, data):
	obj = bluetec_pb2.BT_AV_AVRCP_CONNECT_IND_C()
	obj.ParseFromString(data)
	return obj
def BT_AV_AVRCP_DISCONNECT_IND(opcode, data):
	obj = bluetec_pb2.BT_AV_AVRCP_DISCONNECT_IND_C()
	obj.ParseFromString(data)
	return obj
def BT_AV_MEDIA_START_CFM(opcode, data):
	obj = bluetec_pb2.BT_AV_MEDIA_START_CFM_C()
	obj.ParseFromString(data)
	return obj
def BT_AV_MEDIA_STOP_CFM(opcode, data):
	obj = bluetec_pb2.BT_AV_MEDIA_STOP_CFM_C()
	obj.ParseFromString(data)
	return obj
def BT_AV_MEDIA_PASS_THROUGH_CFM(opcode, data):
	obj = bluetec_pb2.BT_AV_MEDIA_PASS_THROUGH_CFM_C()
	obj.ParseFromString(data)
	return obj
def BT_AV_GET_CAPBILITY_CFM(opcode, data):
	obj = bluetec_pb2.BT_AV_GET_CAPBILITY_CFM_C()
	obj.ParseFromString(data)
	return obj
def BT_AV_GET_PLAY_STATUS_CFM(opcode, data):
	obj = bluetec_pb2.BT_AV_GET_PLAY_STATUS_CFM_C()
	obj.ParseFromString(data)
	return obj
def BT_AV_NOTI_REGISTER_CFM(opcode, data):
	obj = bluetec_pb2.BT_AV_NOTI_REGISTER_CFM_C()
	obj.ParseFromString(data)
	return obj
def BT_AV_LIST_APP_ATT_ID_CFM(opcode, data):
	obj = bluetec_pb2.BT_AV_LIST_APP_ATT_ID_CFM_C()
	obj.ParseFromString(data)
	return obj
def BT_AV_LIST_APP_VALUE_ID_CFM(opcode, data):
	obj = bluetec_pb2.BT_AV_LIST_APP_VALUE_ID_CFM_C()
	obj.ParseFromString(data)
	return obj
def BT_AV_GET_APP_VALUE_CFM(opcode, data):
	obj = bluetec_pb2.BT_AV_GET_APP_VALUE_CFM_C()
	obj.ParseFromString(data)
	return obj
def BT_AV_SET_APP_VALUE_CFM(opcode, data):
	obj = bluetec_pb2.BT_AV_SET_APP_VALUE_CFM_C()
	obj.ParseFromString(data)
	return obj
def BT_AV_GET_APP_ATT_TXT_CFM(opcode, data):
	obj = bluetec_pb2.BT_AV_GET_APP_ATT_TXT_CFM_C()
	obj.ParseFromString(data)
	return obj
def BT_AV_APP_ATT_TXT_DATA_IND(opcode, data):
	obj = bluetec_pb2.BT_AV_APP_ATT_TXT_DATA_IND_C()
	obj.ParseFromString(data)
	return obj
def BT_AV_APP_ATT_TXT_DATA_COMP_IND(opcode, data):
	obj = bluetec_pb2.BT_AV_APP_ATT_TXT_DATA_COMP_IND_C()
	obj.ParseFromString(data)
	return obj
def BT_AV_GET_APP_VALUE_TXT_CFM(opcode, data):
	obj = bluetec_pb2.BT_AV_GET_APP_VALUE_TXT_CFM_C()
	obj.ParseFromString(data)
	return obj
def BT_AV_APP_VAL_TXT_DATA_IND(opcode, data):
	obj = bluetec_pb2.BT_AV_APP_VAL_TXT_DATA_IND_C()
	obj.ParseFromString(data)
	return obj
def BT_AV_APP_VAL_TXT_DATA_COMP_IND(opcode, data):
	obj = bluetec_pb2.BT_AV_APP_VAL_TXT_DATA_COMP_IND_C()
	obj.ParseFromString(data)
	return obj
def BT_AV_ELEMENT_ATTRIBUTES_CFM(opcode, data):
	obj = bluetec_pb2.BT_AV_ELEMENT_ATTRIBUTES_CFM_C()
	obj.ParseFromString(data)
	return obj
def BT_AV_ELEMENT_ATTRIBUTES_DATA_IND(opcode, data):
	obj = bluetec_pb2.BT_AV_ELEMENT_ATTRIBUTES_DATA_IND_C()
	obj.ParseFromString(data)
	return obj
def BT_AV_ELEMENT_ATTRIBUTES_DATA_COMP_IND(opcode, data):
	obj = bluetec_pb2.BT_AV_ELEMENT_ATTRIBUTES_DATA_COMP_IND_C()
	obj.ParseFromString(data)
	return obj
def BT_AV_INFORM_BATTERY_STATUS_CFM(opcode, data):
	obj = bluetec_pb2.BT_AV_INFORM_BATTERY_STATUS_CFM_C()
	obj.ParseFromString(data)
	return obj
def BT_AV_INFORM_CHARSET_CFM(opcode, data):
	obj = bluetec_pb2.BT_AV_INFORM_CHARSET_CFM_C()
	obj.ParseFromString(data)
	return obj
def BT_AV_SET_ABSOLUTE_VOL_CFM(opcode, data):
	obj = bluetec_pb2.BT_AV_SET_ABSOLUTE_VOL_CFM_C()
	obj.ParseFromString(data)
	return obj
def BT_AV_SET_ADDR_PLAYER_CFM(opcode, data):
	obj = bluetec_pb2.BT_AV_SET_ADDR_PLAYER_CFM_C()
	obj.ParseFromString(data)
	return obj
def BT_AV_PLAY_ITEM_CFM(opcode, data):
	obj = bluetec_pb2.BT_AV_PLAY_ITEM_CFM_C()
	obj.ParseFromString(data)
	return obj
def BT_AV_ADD_NOW_PLAYING_CFM(opcode, data):
	obj = bluetec_pb2.BT_AV_ADD_NOW_PLAYING_CFM_C()
	obj.ParseFromString(data)
	return obj
def BT_AV_SET_BROWSED_PLAYER_CFM(opcode, data):
	obj = bluetec_pb2.BT_AV_SET_BROWSED_PLAYER_CFM_C()
	obj.ParseFromString(data)
	return obj
def BT_AV_CHANGE_PATH_CFM(opcode, data):
	obj = bluetec_pb2.BT_AV_CHANGE_PATH_CFM_C()
	obj.ParseFromString(data)
	return obj
def BT_AV_GET_ITEM_ATT_CFM(opcode, data):
	obj = bluetec_pb2.BT_AV_GET_ITEM_ATT_CFM_C()
	obj.ParseFromString(data)
	return obj
def BT_AV_BROWSE_ITEM_ATTRIBUTES_DATA_IND(opcode, data):
	obj = bluetec_pb2.BT_AV_BROWSE_ITEM_ATTRIBUTES_DATA_IND_C()
	obj.ParseFromString(data)
	return obj
def BT_AV_BROWSE_ITEM_ATTRIBUTES_DATA_COMP_IND(opcode, data):
	obj = bluetec_pb2.BT_AV_BROWSE_ITEM_ATTRIBUTES_DATA_COMP_IND_C()
	obj.ParseFromString(data)
	return obj
def BT_AV_GET_FOLDER_ITEM_CFM(opcode, data):
	obj = bluetec_pb2.BT_AV_GET_FOLDER_ITEM_CFM_C()
	obj.ParseFromString(data)
	return obj
def BT_AV_BROWSE_PLAYER_ITEM_DATA_IND(opcode, data):
	obj = bluetec_pb2.BT_AV_BROWSE_PLAYER_ITEM_DATA_IND_C()
	obj.ParseFromString(data)
	return obj
def BT_AV_BROWSE_FOLDER_ITEM_DATA_IND(opcode, data):
	obj = bluetec_pb2.BT_AV_BROWSE_FOLDER_ITEM_DATA_IND_C()
	obj.ParseFromString(data)
	return obj
def BT_AV_BROWSE_MEDIA_ITEM_DATA_IND(opcode, data):
	obj = bluetec_pb2.BT_AV_BROWSE_MEDIA_ITEM_DATA_IND_C()
	obj.ParseFromString(data)
	return obj
def BT_AV_BROWSE_ITEM_DATA_COMP_IND(opcode, data):
	obj = bluetec_pb2.BT_AV_BROWSE_ITEM_DATA_COMP_IND_C()
	obj.ParseFromString(data)
	return obj
def BT_AV_SEARCH_CFM(opcode, data):
	obj = bluetec_pb2.BT_AV_SEARCH_CFM_C()
	obj.ParseFromString(data)
	return obj
def BT_AV_GET_BROWSE_XML_STREAM_CFM(opcode, data):
	obj = bluetec_pb2.BT_AV_GET_BROWSE_XML_STREAM_CFM_C()
	obj.ParseFromString(data)
	return obj
def BT_AV_PLAYER_STATUS_CHANGE_NOTI_IND(opcode, data):
	obj = bluetec_pb2.BT_AV_PLAYER_STATUS_CHANGE_NOTI_IND_C()
	obj.ParseFromString(data)
	return obj
def BT_AV_TRACK_CHANGE_NOTI_IND(opcode, data):
	obj = bluetec_pb2.BT_AV_TRACK_CHANGE_NOTI_IND_C()
	obj.ParseFromString(data)
	return obj
def BT_AV_REACHED_END_NOTI_IND(opcode, data):
	obj = bluetec_pb2.BT_AV_REACHED_END_NOTI_IND_C()
	obj.ParseFromString(data)
	return obj
def BT_AV_REACHED_START_NOTI_IND(opcode, data):
	obj = bluetec_pb2.BT_AV_REACHED_START_NOTI_IND_C()
	obj.ParseFromString(data)
	return obj
def BT_AV_PLAYBACK_POSITION_CHANGE_NOTI_IND(opcode, data):
	obj = bluetec_pb2.BT_AV_PLAYBACK_POSITION_CHANGE_NOTI_IND_C()
	obj.ParseFromString(data)
	return obj
def BT_AV_BATTERY_STATUS_CHANGE_NOTI_IND(opcode, data):
	obj = bluetec_pb2.BT_AV_BATTERY_STATUS_CHANGE_NOTI_IND_C()
	obj.ParseFromString(data)
	return obj
def BT_AV_SYSTEM_STATUS_CHANGE_NOTI_IND(opcode, data):
	obj = bluetec_pb2.BT_AV_SYSTEM_STATUS_CHANGE_NOTI_IND_C()
	obj.ParseFromString(data)
	return obj
def BT_AV_PLAYING_CONTENT_CHANGE_NOTI_IND(opcode, data):
	obj = bluetec_pb2.BT_AV_PLAYING_CONTENT_CHANGE_NOTI_IND_C()
	obj.ParseFromString(data)
	return obj
def BT_AV_AVAILABLE_PLAYER_CHANGE_NOTI_IND(opcode, data):
	obj = bluetec_pb2.BT_AV_AVAILABLE_PLAYER_CHANGE_NOTI_IND_C()
	obj.ParseFromString(data)
	return obj
def BT_AV_ADDRESSED_PLAYER_CHANGE_NOTI_IND(opcode, data):
	obj = bluetec_pb2.BT_AV_ADDRESSED_PLAYER_CHANGE_NOTI_IND_C()
	obj.ParseFromString(data)
	return obj
def BT_AV_UID_CHANGE_NOTI_IND(opcode, data):
	obj = bluetec_pb2.BT_AV_UID_CHANGE_NOTI_IND_C()
	obj.ParseFromString(data)
	return obj
def BT_AV_VOLUME_CHANGE_NOTI_IND(opcode, data):
	obj = bluetec_pb2.BT_AV_VOLUME_CHANGE_NOTI_IND_C()
	obj.ParseFromString(data)
	return obj
def BT_AVP_FID_EVT_PLAYER_APP_SETTING_CHANGED_IND(opcode, data):
	obj = bluetec_pb2.BT_AVP_FID_EVT_PLAYER_APP_SETTING_CHANGED_IND_C()
	obj.ParseFromString(data)
	return obj
def BT_AV_A2DP_CONFIGURATION_IND(opcode, data):
	obj = bluetec_pb2.BT_AV_A2DP_CONFIGURATION_IND_C()
	obj.ParseFromString(data)
	return obj
def BT_AV_A2DP_STREAM_DATA_IND(opcode, data):
	obj = bluetec_pb2.BT_AV_A2DP_STREAM_DATA_IND_C()
	obj.ParseFromString(data)
	return obj
def BT_PBDL_ATCMD_START_SERVICE_CFM(opcode, data):
	obj = bluetec_pb2.BT_PBDL_ATCMD_START_SERVICE_CFM_C()
	obj.ParseFromString(data)
	return obj
def BT_PBDL_ATCMD_GET_STORAGE_CFM(opcode, data):
	obj = bluetec_pb2.BT_PBDL_ATCMD_GET_STORAGE_CFM_C()
	obj.ParseFromString(data)
	return obj
def BT_PBDL_ATCMD_GET_CURRENT_STORAGE_CFM(opcode, data):
	obj = bluetec_pb2.BT_PBDL_ATCMD_GET_CURRENT_STORAGE_CFM_C()
	obj.ParseFromString(data)
	return obj
def BT_PBDL_ATCMD_SET_STORAGE_CFM(opcode, data):
	obj = bluetec_pb2.BT_PBDL_ATCMD_SET_STORAGE_CFM_C()
	obj.ParseFromString(data)
	return obj
def BT_PBDL_ATCMD_READ_PB_ENTRY_CFM(opcode, data):
	obj = bluetec_pb2.BT_PBDL_ATCMD_READ_PB_ENTRY_CFM_C()
	obj.ParseFromString(data)
	return obj
def BT_PBDL_ATCMD_FIND_PB_ENTRY_CFM(opcode, data):
	obj = bluetec_pb2.BT_PBDL_ATCMD_FIND_PB_ENTRY_CFM_C()
	obj.ParseFromString(data)
	return obj
def BT_PBDL_ATCMD_ENTRY_DATA_ABORT_CFM(opcode, data):
	obj = bluetec_pb2.BT_PBDL_ATCMD_ENTRY_DATA_ABORT_CFM_C()
	obj.ParseFromString(data)
	return obj
def BT_PBDL_ATCMD_PB_ENTRY_DATA_IND(opcode, data):
	obj = bluetec_pb2.BT_PBDL_ATCMD_PB_ENTRY_DATA_IND_C()
	obj.ParseFromString(data)
	return obj
def BT_PBDL_ATCMD_PB_ENTRY_DATA_COMPLETE_IND(opcode, data):
	obj = bluetec_pb2.BT_PBDL_ATCMD_PB_ENTRY_DATA_COMPLETE_IND_C()
	obj.ParseFromString(data)
	return obj
def BT_PBDL_ATCMD_CONNECTION_IND(opcode, data):
	obj = bluetec_pb2.BT_PBDL_ATCMD_CONNECTION_IND_C()
	obj.ParseFromString(data)
	return obj
def BT_PBDL_ATCMD_DISCONNECTION_IND(opcode, data):
	obj = bluetec_pb2.BT_PBDL_ATCMD_DISCONNECTION_IND_C()
	obj.ParseFromString(data)
	return obj
def BT_PBDL_PBAP_SET_FOLDER_CFM(opcode, data):
	obj = bluetec_pb2.BT_PBDL_PBAP_SET_FOLDER_CFM_C()
	obj.ParseFromString(data)
	return obj
def BT_PBDL_PBAP_GET_PBSIZE_CFM(opcode, data):
	obj = bluetec_pb2.BT_PBDL_PBAP_GET_PBSIZE_CFM_C()
	obj.ParseFromString(data)
	return obj
def BT_PBDL_PBAP_PULL_PB_CFM(opcode, data):
	obj = bluetec_pb2.BT_PBDL_PBAP_PULL_PB_CFM_C()
	obj.ParseFromString(data)
	return obj
def BT_PBDL_PBAP_PULL_VCARD_LIST_CFM(opcode, data):
	obj = bluetec_pb2.BT_PBDL_PBAP_PULL_VCARD_LIST_CFM_C()
	obj.ParseFromString(data)
	return obj
def BT_PBDL_PBAP_PULL_VCARD_ENTRY_CFM(opcode, data):
	obj = bluetec_pb2.BT_PBDL_PBAP_PULL_VCARD_ENTRY_CFM_C()
	obj.ParseFromString(data)
	return obj
def BT_PBDL_PBAP_PB_ENTRY_DATA_IND(opcode, data):
	obj = bluetec_pb2.BT_PBDL_PBAP_PB_ENTRY_DATA_IND_C()
	obj.ParseFromString(data)
	return obj
def BT_PBDL_PBAP_PB_ENTRY_DATA_COMPLETE_IND(opcode, data):
	obj = bluetec_pb2.BT_PBDL_PBAP_PB_ENTRY_DATA_COMPLETE_IND_C()
	obj.ParseFromString(data)
	return obj
def BT_PBDL_PBAP_VCARD_LIST_DATA_IND(opcode, data):
	obj = bluetec_pb2.BT_PBDL_PBAP_VCARD_LIST_DATA_IND_C()
	obj.ParseFromString(data)
	return obj
def BT_PBDL_PBAP_VCARD_LIST_DATA_COMPLETE_IND(opcode, data):
	obj = bluetec_pb2.BT_PBDL_PBAP_VCARD_LIST_DATA_COMPLETE_IND_C()
	obj.ParseFromString(data)
	return obj
def BT_PBDL_PBAP_VCARD_ENTRY_DATA_IND(opcode, data):
	obj = bluetec_pb2.BT_PBDL_PBAP_VCARD_ENTRY_DATA_IND_C()
	obj.ParseFromString(data)
	return obj
def BT_PBDL_PBAP_VCARD_ENTRY_DATA_COMPLETE_IND(opcode, data):
	obj = bluetec_pb2.BT_PBDL_PBAP_VCARD_ENTRY_DATA_COMPLETE_IND_C()
	obj.ParseFromString(data)
	return obj
def BT_PBDL_PBAP_PULL_ABORT_CFM(opcode, data):
	obj = bluetec_pb2.BT_PBDL_PBAP_PULL_ABORT_CFM_C()
	obj.ParseFromString(data)
	return obj
def BT_PBDL_OPPS_PUT_FILE_IND(opcode, data):
	obj = bluetec_pb2.BT_PBDL_OPPS_PUT_FILE_IND_C()
	obj.ParseFromString(data)
	return obj
def BT_PBDL_OPPS_PUT_BODY_IND(opcode, data):
	obj = bluetec_pb2.BT_PBDL_OPPS_PUT_BODY_IND_C()
	obj.ParseFromString(data)
	return obj
def BT_PBDL_OPPS_PUT_COMPLETE_IND(opcode, data):
	obj = bluetec_pb2.BT_PBDL_OPPS_PUT_COMPLETE_IND_C()
	obj.ParseFromString(data)
	return obj
def BT_PBDL_OPPS_PUT_ABORT_IND(opcode, data):
	obj = bluetec_pb2.BT_PBDL_OPPS_PUT_ABORT_IND_C()
	obj.ParseFromString(data)
	return obj
def BT_PBDL_OPPS_PUT_ABORT_CFM(opcode, data):
	obj = bluetec_pb2.BT_PBDL_OPPS_PUT_ABORT_CFM_C()
	obj.ParseFromString(data)
	return obj
def BT_PBDL_PULL_PB_CFM(opcode, data):
	obj = bluetec_pb2.BT_PBDL_PULL_PB_CFM_C()
	obj.ParseFromString(data)
	return obj
def BT_PBDL_PULL_PB_CMP_IND(opcode, data):
	obj = bluetec_pb2.BT_PBDL_PULL_PB_CMP_IND_C()
	obj.ParseFromString(data)
	return obj
def BT_MAP_GET_DEVICE_LIST_CFM(opcode, data):
	obj = bluetec_pb2.BT_MAP_GET_DEVICE_LIST_CFM_C()
	obj.ParseFromString(data)
	return obj
def BT_MAP_GET_SDP_RECORD_CFM(opcode, data):
	obj = bluetec_pb2.BT_MAP_GET_SDP_RECORD_CFM_C()
	obj.ParseFromString(data)
	return obj
def BT_MAP_GET_SDP_RECORD_IND(opcode, data):
	obj = bluetec_pb2.BT_MAP_GET_SDP_RECORD_IND_C()
	obj.ParseFromString(data)
	return obj
def BT_MAP_SDP_RECORD_COMPLETE_IND(opcode, data):
	obj = bluetec_pb2.BT_MAP_SDP_RECORD_COMPLETE_IND_C()
	obj.ParseFromString(data)
	return obj
def BT_MAP_ESTABLIST_CONNECTION_CFM(opcode, data):
	obj = bluetec_pb2.BT_MAP_ESTABLIST_CONNECTION_CFM_C()
	obj.ParseFromString(data)
	return obj
def BT_MAP_DESTROY_CONNECTION_CFM(opcode, data):
	obj = bluetec_pb2.BT_MAP_DESTROY_CONNECTION_CFM_C()
	obj.ParseFromString(data)
	return obj
def BT_MAP_SET_FLODER_CFM(opcode, data):
	obj = bluetec_pb2.BT_MAP_SET_FLODER_CFM_C()
	obj.ParseFromString(data)
	return obj
def BT_MAP_SET_FLODER_BACK_CFM(opcode, data):
	obj = bluetec_pb2.BT_MAP_SET_FLODER_BACK_CFM_C()
	obj.ParseFromString(data)
	return obj
def BT_MAP_SET_FLODER_ROOT_CFM(opcode, data):
	obj = bluetec_pb2.BT_MAP_SET_FLODER_ROOT_CFM_C()
	obj.ParseFromString(data)
	return obj
def BT_MAP_GET_FLODERLIST_CFM(opcode, data):
	obj = bluetec_pb2.BT_MAP_GET_FLODERLIST_CFM_C()
	obj.ParseFromString(data)
	return obj
def BT_MAP_GET_FLODERLIST_IND(opcode, data):
	obj = bluetec_pb2.BT_MAP_GET_FLODERLIST_IND_C()
	obj.ParseFromString(data)
	return obj
def BT_MAP_FLODERLIST_COMPLETE_IND(opcode, data):
	obj = bluetec_pb2.BT_MAP_FLODERLIST_COMPLETE_IND_C()
	obj.ParseFromString(data)
	return obj
def BT_MAP_GET_MESSAGELIST_CFM(opcode, data):
	obj = bluetec_pb2.BT_MAP_GET_MESSAGELIST_CFM_C()
	obj.ParseFromString(data)
	return obj
def BT_MAP_GET_MESSAGELIST_IND(opcode, data):
	obj = bluetec_pb2.BT_MAP_GET_MESSAGELIST_IND_C()
	obj.ParseFromString(data)
	return obj
def BT_MAP_GET_MESSAGELIST_COMPLETE_IND(opcode, data):
	obj = bluetec_pb2.BT_MAP_GET_MESSAGELIST_COMPLETE_IND_C()
	obj.ParseFromString(data)
	return obj
def BT_MAP_GET_MESSAGE_CFM(opcode, data):
	obj = bluetec_pb2.BT_MAP_GET_MESSAGE_CFM_C()
	obj.ParseFromString(data)
	return obj
def BT_MAP_GET_MESSAGE_IND(opcode, data):
	obj = bluetec_pb2.BT_MAP_GET_MESSAGE_IND_C()
	obj.ParseFromString(data)
	return obj
def BT_MAP_FID_MESSAGE_COMPLETE_IND(opcode, data):
	obj = bluetec_pb2.BT_MAP_FID_MESSAGE_COMPLETE_IND_C()
	obj.ParseFromString(data)
	return obj
def BT_MAP_SET_MESSAGE_STATUS_CFM(opcode, data):
	obj = bluetec_pb2.BT_MAP_SET_MESSAGE_STATUS_CFM_C()
	obj.ParseFromString(data)
	return obj
def BT_MAP_PUT_MESSAGE_CFM(opcode, data):
	obj = bluetec_pb2.BT_MAP_PUT_MESSAGE_CFM_C()
	obj.ParseFromString(data)
	return obj
def BT_MAP_UPDATE_INBOX_CFM(opcode, data):
	obj = bluetec_pb2.BT_MAP_UPDATE_INBOX_CFM_C()
	obj.ParseFromString(data)
	return obj
def BT_MAP_REGISTER_NOTIFICATION_CFM(opcode, data):
	obj = bluetec_pb2.BT_MAP_REGISTER_NOTIFICATION_CFM_C()
	obj.ParseFromString(data)
	return obj
def BT_MAP_MESSAGE_NOTIFICATION_OFF_IND(opcode, data):
	obj = bluetec_pb2.BT_MAP_MESSAGE_NOTIFICATION_OFF_IND_C()
	obj.ParseFromString(data)
	return obj
def BT_MAP_MESSAGE_NOTIFICATION_IND(opcode, data):
	obj = bluetec_pb2.BT_MAP_MESSAGE_NOTIFICATION_IND_C()
	obj.ParseFromString(data)
	return obj
def BT_AT_SMS_CONNECTION_IND(opcode, data):
	obj = bluetec_pb2.BT_AT_SMS_CONNECTION_IND_C()
	obj.ParseFromString(data)
	return obj
def BT_AT_SMS_DISCONNECTION_IND(opcode, data):
	obj = bluetec_pb2.BT_AT_SMS_DISCONNECTION_IND_C()
	obj.ParseFromString(data)
	return obj
def BT_MSG_SUPPORT_SMS_FORMAT_CFM(opcode, data):
	obj = bluetec_pb2.BT_MSG_SUPPORT_SMS_FORMAT_CFM_C()
	obj.ParseFromString(data)
	return obj
def BT_MSG_CURRENT_SMS_FORMAT_CFM(opcode, data):
	obj = bluetec_pb2.BT_MSG_CURRENT_SMS_FORMAT_CFM_C()
	obj.ParseFromString(data)
	return obj
def BT_MSG_SET_SMS_FORMAT_CFM(opcode, data):
	obj = bluetec_pb2.BT_MSG_SET_SMS_FORMAT_CFM_C()
	obj.ParseFromString(data)
	return obj
def BT_MSG_GET_SUPPORT_SMS_STORAGE_CFM(opcode, data):
	obj = bluetec_pb2.BT_MSG_GET_SUPPORT_SMS_STORAGE_CFM_C()
	obj.ParseFromString(data)
	return obj
def BT_MSG_GET_CURRENT_SMS_STORAGE_CFM(opcode, data):
	obj = bluetec_pb2.BT_MSG_GET_CURRENT_SMS_STORAGE_CFM_C()
	obj.ParseFromString(data)
	return obj
def BT_MSG_SELECT_SMS_STORAGE_CFM(opcode, data):
	obj = bluetec_pb2.BT_MSG_SELECT_SMS_STORAGE_CFM_C()
	obj.ParseFromString(data)
	return obj
def BT_MSG_GET_SUPPORT_LIST_SMS_CFM(opcode, data):
	obj = bluetec_pb2.BT_MSG_GET_SUPPORT_LIST_SMS_CFM_C()
	obj.ParseFromString(data)
	return obj
def BT_MSG_LIST_SMS_CFM(opcode, data):
	obj = bluetec_pb2.BT_MSG_LIST_SMS_CFM_C()
	obj.ParseFromString(data)
	return obj
def BT_MSG_GET_CONTENT_IND(opcode, data):
	obj = bluetec_pb2.BT_MSG_GET_CONTENT_IND_C()
	obj.ParseFromString(data)
	return obj
def BT_MSG_GET_CONTENT_COMPLETED_IND(opcode, data):
	obj = bluetec_pb2.BT_MSG_GET_CONTENT_COMPLETED_IND_C()
	obj.ParseFromString(data)
	return obj
def BT_MSG_READ_SMS_CFM(opcode, data):
	obj = bluetec_pb2.BT_MSG_READ_SMS_CFM_C()
	obj.ParseFromString(data)
	return obj
def BT_MSG_DELETE_SMS_CFM(opcode, data):
	obj = bluetec_pb2.BT_MSG_DELETE_SMS_CFM_C()
	obj.ParseFromString(data)
	return obj
def BT_MSG_SET_SMS_NOTIFICATION_CFM(opcode, data):
	obj = bluetec_pb2.BT_MSG_SET_SMS_NOTIFICATION_CFM_C()
	obj.ParseFromString(data)
	return obj
def BT_MSG_SEND_SMS_CFM(opcode, data):
	obj = bluetec_pb2.BT_MSG_SEND_SMS_CFM_C()
	obj.ParseFromString(data)
	return obj
def BT_HID_CONNECT_CFM(opcode, data):
	obj = bluetec_pb2.BT_HID_CONNECT_CFM_C()
	obj.ParseFromString(data)
	return obj
def BT_HID_DISCONNECT_CFM(opcode, data):
	obj = bluetec_pb2.BT_HID_DISCONNECT_CFM_C()
	obj.ParseFromString(data)
	return obj
def BT_HID_DATA_CFM(opcode, data):
	obj = bluetec_pb2.BT_HID_DATA_CFM_C()
	obj.ParseFromString(data)
	return obj
def BT_HID_STATUS_IND(opcode, data):
	obj = bluetec_pb2.BT_HID_STATUS_IND_C()
	obj.ParseFromString(data)
	return obj
