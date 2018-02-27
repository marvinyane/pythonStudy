import sys
import bluetec_pb2
def DUMP_MESSAGE(obj):
	if obj.opcode == 0x1:
		DUMP_BT_GEN_POWER_ON_REQ(obj)
	if obj.opcode == 0x8001:
		DUMP_BT_GEN_POWER_ON_CFM(obj)
	if obj.opcode == 0x2:
		DUMP_BT_GEN_POWER_OFF_REQ(obj)
	if obj.opcode == 0x8002:
		DUMP_BT_GEN_POWER_OFF_CFM(obj)
	if obj.opcode == 0x3:
		DUMP_BT_GEN_GET_LOCAL_STATUS_REQ(obj)
	if obj.opcode == 0x8003:
		DUMP_BT_GEN_GET_LOCAL_STATUS_CFM(obj)
	if obj.opcode == 0x4:
		DUMP_BT_GEN_SET_LOCAL_CONFIG_REQ(obj)
	if obj.opcode == 0x8004:
		DUMP_BT_GEN_SET_LOCAL_CONFIG_CFM(obj)
	if obj.opcode == 0x5:
		DUMP_BT_GEN_READ_LOCAL_CONFIG_REQ(obj)
	if obj.opcode == 0x8005:
		DUMP_BT_GEN_READ_LOCAL_CONFIG_CFM(obj)
	if obj.opcode == 0x6:
		DUMP_BT_GEN_SSP_DEBUG_MODE_REQ(obj)
	if obj.opcode == 0x8006:
		DUMP_BT_GEN_SSP_DEBUG_MODE_CFM(obj)
	if obj.opcode == 0x7:
		DUMP_BT_GEN_SEARCH_REMOTE_DEV_REQ(obj)
	if obj.opcode == 0x8007:
		DUMP_BT_GEN_SEARCH_REMOTE_DEV_CFM(obj)
	if obj.opcode == 0x8008:
		DUMP_BT_GEN_SEARCH_REMOTE_DEV_IND(obj)
	if obj.opcode == 0x8009:
		DUMP_BT_GEN_SEARCH_REMOTE_DEV_COMP_IND(obj)
	if obj.opcode == 0xA:
		DUMP_BT_GEN_SEARCH_REMOTE_DEV_CANCEL_REQ(obj)
	if obj.opcode == 0x800A:
		DUMP_BT_GEN_SEARCH_REMOTE_DEV_CANCEL_CFM(obj)
	if obj.opcode == 0xB:
		DUMP_BT_GEN_SET_LOCAL_NAME_REQ(obj)
	if obj.opcode == 0x800B:
		DUMP_BT_GEN_SET_LOCAL_NAME_CFM(obj)
	if obj.opcode == 0xC:
		DUMP_BT_GEN_READ_REMOTE_NAME_REQ(obj)
	if obj.opcode == 0x800C:
		DUMP_BT_GEN_READ_REMOTE_NAME_CFM(obj)
	if obj.opcode == 0xE:
		DUMP_BT_GEN_READ_REMOTE_NAME_CANCEL_REQ(obj)
	if obj.opcode == 0x800E:
		DUMP_BT_GEN_READ_REMOTE_NAME_CANCEL_CFM(obj)
	if obj.opcode == 0x66:
		DUMP_BT_GEN_GET_LINK_QUALITY_REQ(obj)
	if obj.opcode == 0x8066:
		DUMP_BT_GEN_GET_LINK_QUALITY_CFM(obj)
	if obj.opcode == 0xF:
		DUMP_BT_GEN_SET_LOCAL_MODE_REQ(obj)
	if obj.opcode == 0x800F:
		DUMP_BT_GEN_SET_LOCAL_MODE_CFM(obj)
	if obj.opcode == 0x10:
		DUMP_BT_GEN_SERVICE_SEARCH_REQ(obj)
	if obj.opcode == 0x8010:
		DUMP_BT_GEN_SERVICE_SEARCH_CFM(obj)
	if obj.opcode == 0x8011:
		DUMP_BT_GEN_SERVICE_SEARCH_IND(obj)
	if obj.opcode == 0x8012:
		DUMP_BT_GEN_SERVICE_SEARCH_COMP_IND(obj)
	if obj.opcode == 0x13:
		DUMP_BT_GEN_SDP_SEARCH_CANCEL_REQ(obj)
	if obj.opcode == 0x8013:
		DUMP_BT_GEN_SERVICE_SEARCH_CANCEL_CFM(obj)
	if obj.opcode == 0x14:
		DUMP_BT_GEN_ENTER_TEST_MODE_REQ(obj)
	if obj.opcode == 0x15:
		DUMP_BT_GEN_DISABLE_TEST_MODE_REQ(obj)
	if obj.opcode == 0x1A:
		DUMP_BT_GEN_SERVICE_SEARCH_EXT_REQ(obj)
	if obj.opcode == 0x801A:
		DUMP_BT_GEN_SERVICE_SEARCH_EXT_CFM(obj)
	if obj.opcode == 0x801B:
		DUMP_BT_GEN_SERVICE_SEARCH_EXT_IND(obj)
	if obj.opcode == 0x801C:
		DUMP_BT_GEN_SERVICE_SEARCH_EXT_COMPLETE_IND(obj)
	if obj.opcode == 0x1D:
		DUMP_BT_GEN_GET_LOCAL_OOB_DATA_REQ(obj)
	if obj.opcode == 0x801D:
		DUMP_BT_GEN_GET_LOCAL_OOB_DATA_CFM(obj)
	if obj.opcode == 0x1E:
		DUMP_BT_GEN_SET_REMOTE_OOB_DATA_REQ(obj)
	if obj.opcode == 0x801E:
		DUMP_BT_GEN_SET_REMOTE_OOB_DATA_CFM(obj)
	if obj.opcode == 0x61:
		DUMP_BT_GEN_SEARCH_DEVICE_INFO_REQ(obj)
	if obj.opcode == 0x8061:
		DUMP_BT_GEN_FID_SEARCH_DEV_INFO_CFM(obj)
	if obj.opcode == 0xC062:
		DUMP_BT_GEN_FID_SEARCH_DEV_INFO_IND(obj)
	if obj.opcode == 0xC063:
		DUMP_BT_GEN_FID_SEARCH_DEV_INFO_COMPLETE_IND(obj)
	if obj.opcode == 0x60:
		DUMP_BT_GEN_REGISTER_DEVICE_INFO_REQ(obj)
	if obj.opcode == 0x8060:
		DUMP_BT_GEN_FID_REGISTER_DEVICE_INFO_CFM(obj)
	if obj.opcode == 0x65:
		DUMP_BT_GEN_UNREGISTER_DEVICE_INFO_REQ(obj)
	if obj.opcode == 0x8065:
		DUMP_BT_GEN_UNREGISTER_DEVICE_INFO_CFM(obj)
	if obj.opcode == 0x64:
		DUMP_BT_GEN_CANCEL_SEARCH_DEVICE_INFO_REQ(obj)
	if obj.opcode == 0x8064:
		DUMP_BT_GEN_CANCEL_SEARCH_DEVICE_INFO_CFM(obj)
	if obj.opcode == 0x20:
		DUMP_BT_CM_PAIRING_REMOTE_DEV_REQ(obj)
	if obj.opcode == 0x8020:
		DUMP_BT_CM_PAIRING_REMOTE_DEV_CFM(obj)
	if obj.opcode == 0x21:
		DUMP_BT_CM_PAIRING_CANCEL_DEV_REQ(obj)
	if obj.opcode == 0x8021:
		DUMP_BT_CM_PAIRING_CANCEL_DEV_CFM(obj)
	if obj.opcode == 0x8023:
		DUMP_BT_CM_PIN_CODE_IND(obj)
	if obj.opcode == 0x23:
		DUMP_BT_CM_PIN_CODE_RES(obj)
	if obj.opcode == 0x8024:
		DUMP_BT_CM_PASSKEY_NOTIFICATION_IND(obj)
	if obj.opcode == 0x8025:
		DUMP_BT_CM_NUMERIC_CONFIRM_IND(obj)
	if obj.opcode == 0xC026:
		DUMP_BT_CM_NUM_DISPLAY_IND(obj)
	if obj.opcode == 0x8027:
		DUMP_BT_CM_PASSKEY_REQ_IND(obj)
	if obj.opcode == 0x25:
		DUMP_BT_CM_NUMERIC_CONFIRM_RES(obj)
	if obj.opcode == 0xC027:
		DUMP_BT_GEN_FID_PAIR_COMPLETE_IND(obj)
	if obj.opcode == 0x8030:
		DUMP_BT_CM_CON_AUTHORIZE_IND(obj)
	if obj.opcode == 0x30:
		DUMP_BT_CM_CON_AUTHORIZE_RES(obj)
	if obj.opcode == 0x31:
		DUMP_BT_CM_SERVICE_CON_REQ(obj)
	if obj.opcode == 0x8031:
		DUMP_BT_CM_SERVICE_CON_CFM(obj)
	if obj.opcode == 0x8032:
		DUMP_BT_CM_SERVICE_CON_IND(obj)
	if obj.opcode == 0x8033:
		DUMP_BT_CM_SERVICE_CON_COMP_IND(obj)
	if obj.opcode == 0x34:
		DUMP_BT_CM_SERVICE_CON_CANCEL_REQ(obj)
	if obj.opcode == 0x8034:
		DUMP_BT_CM_SERVICE_CON_CANCEL_CFM(obj)
	if obj.opcode == 0x35:
		DUMP_BT_CM_SERVICE_DISCON_REQ(obj)
	if obj.opcode == 0x8035:
		DUMP_BT_CM_SERVICE_DISCON_CFM(obj)
	if obj.opcode == 0x8036:
		DUMP_BT_CM_SERVICE_DISCON_IND(obj)
	if obj.opcode == 0x8037:
		DUMP_BT_CM_SERVICE_DISCON_COMP_IND(obj)
	if obj.opcode == 0x8201:
		DUMP_BT_HFP_SERVICE_IND(obj)
	if obj.opcode == 0x8202:
		DUMP_BT_HFP_SIGNAL_IND(obj)
	if obj.opcode == 0x8203:
		DUMP_BT_HFP_ROAM_IND(obj)
	if obj.opcode == 0x8204:
		DUMP_BT_HFP_BATTCHG_IND(obj)
	if obj.opcode == 0x820C:
		DUMP_BT_HFP_CALL_RING_IND(obj)
	if obj.opcode == 0x205:
		DUMP_BT_HFP_DIAL_OUT_REQ(obj)
	if obj.opcode == 0x8205:
		DUMP_BT_HFP_FID_DIAL_CFM(obj)
	if obj.opcode == 0x820B:
		DUMP_BT_HFP_CALL_STATE_IND(obj)
	if obj.opcode == 0x206:
		DUMP_BT_HFP_LAST_DIAL_REQ(obj)
	if obj.opcode == 0x8206:
		DUMP_BT_HFP_LAST_DIAL_CFM(obj)
	if obj.opcode == 0x207:
		DUMP_BT_HFP_MEM_DIAL_REQ(obj)
	if obj.opcode == 0x8207:
		DUMP_BT_HFP_MEM_DIAL_CFM(obj)
	if obj.opcode == 0x208:
		DUMP_BT_HFP_CALL_ANSWER_REQ(obj)
	if obj.opcode == 0x8208:
		DUMP_BT_HFP_CALL_ANSWER_CFM(obj)
	if obj.opcode == 0x209:
		DUMP_BT_HFP_CALL_REJECT_REQ(obj)
	if obj.opcode == 0x8209:
		DUMP_BT_HFP_CALL_REJECT_CFM(obj)
	if obj.opcode == 0x20A:
		DUMP_BT_HFP_TERMINATE_CALL_REQ(obj)
	if obj.opcode == 0x820A:
		DUMP_BT_HFP_TERMINATE_CALL_CFM(obj)
	if obj.opcode == 0x210:
		DUMP_BT_HFP_CLIP_ENABLE_REQ(obj)
	if obj.opcode == 0x8210:
		DUMP_BT_HFP_CLIP_ENABLE_CFM(obj)
	if obj.opcode == 0x212:
		DUMP_BT_HFP_CCWA_ENABLE_REQ(obj)
	if obj.opcode == 0x8212:
		DUMP_BT_HFP_CCWA_ENABLE_CFM(obj)
	if obj.opcode == 0x8211:
		DUMP_BT_HFP_INCOMING_CALL_IND(obj)
	if obj.opcode == 0x8213:
		DUMP_BT_HFP_SECOND_INCOMING_CALL_IND(obj)
	if obj.opcode == 0x20D:
		DUMP_BT_HFP_AUDIO_TRANSFER_REQ(obj)
	if obj.opcode == 0x820D:
		DUMP_BT_HFP_AUDIO_TRANSFER_CFM(obj)
	if obj.opcode == 0x820E:
		DUMP_BT_HFP_SCO_IND(obj)
	if obj.opcode == 0x214:
		DUMP_BT_HFP_SEND_DTMF_REQ(obj)
	if obj.opcode == 0x8214:
		DUMP_BT_HFP_SEND_DTMF_CFM(obj)
	if obj.opcode == 0x220:
		DUMP_BT_HFP_PESPONSE_AND_HOLD_REQ(obj)
	if obj.opcode == 0x8220:
		DUMP_BT_HFP_PESPONSE_AND_HOLD_CFM(obj)
	if obj.opcode == 0x221:
		DUMP_BT_HFP_CALL_HOLD_REQ(obj)
	if obj.opcode == 0x8221:
		DUMP_BT_HFP_CALL_HOLD_CFM(obj)
	if obj.opcode == 0x233:
		DUMP_BT_HFP_ANSWER_SECOND_CALL_REQ(obj)
	if obj.opcode == 0x8233:
		DUMP_BT_HFP_ANSWER_SECOND_CALL_CFM(obj)
	if obj.opcode == 0x234:
		DUMP_BT_HFP_TERMINATE_CALL_BY_INDEX_REQ(obj)
	if obj.opcode == 0x8234:
		DUMP_BT_HFP_TERMINATE_CALL_BY_INDEX_CFM(obj)
	if obj.opcode == 0x235:
		DUMP_BT_HFP_SWITCH_CALL_REQ(obj)
	if obj.opcode == 0x8235:
		DUMP_BT_HFP_SWITCH_CALL_CFM(obj)
	if obj.opcode == 0x236:
		DUMP_BT_HFP_JOIN_CALL_REQ(obj)
	if obj.opcode == 0x8236:
		DUMP_BT_HFP_JOIN_CALL_CFM(obj)
	if obj.opcode == 0x216:
		DUMP_BT_HFP_GET_SUBSCRIBER_NUM_REQ(obj)
	if obj.opcode == 0x8216:
		DUMP_BT_HFP_GET_SUBSCRIBER_NUM_CFM(obj)
	if obj.opcode == 0x215:
		DUMP_BT_HFP_GET_OPERATOR_NAME_REQ(obj)
	if obj.opcode == 0x8215:
		DUMP_BT_HFP_GET_OPERATOR_NAME_CFM(obj)
	if obj.opcode == 0x217:
		DUMP_BT_HFP_GET_CURRENT_CALL_LIST_REQ(obj)
	if obj.opcode == 0x8217:
		DUMP_BT_HFP_GET_CURRENT_CALL_LIST_CFM(obj)
	if obj.opcode == 0x8218:
		DUMP_BT_HFP_GET_CURRENT_CALL_LIST_IND(obj)
	if obj.opcode == 0x8219:
		DUMP_BT_HFP_GET_CURRENT_CALL_LIST_COMPLETE_IND(obj)
	if obj.opcode == 0x101:
		DUMP_BT_SPP_DATA_SEND_REQ(obj)
	if obj.opcode == 0x8101:
		DUMP_BT_SPP_DATA_SEND_CFM(obj)
	if obj.opcode == 0x8102:
		DUMP_BT_SPP_DATA_RECEIVE_IND(obj)
	if obj.opcode == 0x103:
		DUMP_BT_SPP_ACTIVE_SERVER_REQ(obj)
	if obj.opcode == 0x8103:
		DUMP_BT_SPP_ACTIVE_SERVER_CFM(obj)
	if obj.opcode == 0x104:
		DUMP_BT_SPP_DEACTIVE_SERVER_REQ(obj)
	if obj.opcode == 0x8104:
		DUMP_BT_SPP_DEACTIVE_SERVER_CFM(obj)
	if obj.opcode == 0x8335:
		DUMP_BT_AV_AVRCP_CONNECT_IND(obj)
	if obj.opcode == 0x8336:
		DUMP_BT_AV_AVRCP_DISCONNECT_IND(obj)
	if obj.opcode == 0x301:
		DUMP_BT_AV_MEDIA_START_REQ(obj)
	if obj.opcode == 0x8301:
		DUMP_BT_AV_MEDIA_START_CFM(obj)
	if obj.opcode == 0x302:
		DUMP_BT_AV_MEDIA_STOP_REQ(obj)
	if obj.opcode == 0x8302:
		DUMP_BT_AV_MEDIA_STOP_CFM(obj)
	if obj.opcode == 0x304:
		DUMP_BT_AV_MEDIA_PASS_THROUGH_REQ(obj)
	if obj.opcode == 0x8304:
		DUMP_BT_AV_MEDIA_PASS_THROUGH_CFM(obj)
	if obj.opcode == 0x305:
		DUMP_BT_AV_GET_CAPBILITY_REQ(obj)
	if obj.opcode == 0x8305:
		DUMP_BT_AV_GET_CAPBILITY_CFM(obj)
	if obj.opcode == 0x306:
		DUMP_BT_AV_GET_PLAY_STATUS_REQ(obj)
	if obj.opcode == 0x8306:
		DUMP_BT_AV_GET_PLAY_STATUS_CFM(obj)
	if obj.opcode == 0x307:
		DUMP_BT_AV_NOTI_REGISTER_REQ(obj)
	if obj.opcode == 0x8307:
		DUMP_BT_AV_NOTI_REGISTER_CFM(obj)
	if obj.opcode == 0x308:
		DUMP_BT_AV_LIST_APP_ATT_ID_REQ(obj)
	if obj.opcode == 0x8308:
		DUMP_BT_AV_LIST_APP_ATT_ID_CFM(obj)
	if obj.opcode == 0x309:
		DUMP_BT_AV_LIST_APP_VALUE_ID_REQ(obj)
	if obj.opcode == 0x8309:
		DUMP_BT_AV_LIST_APP_VALUE_ID_CFM(obj)
	if obj.opcode == 0x30A:
		DUMP_BT_AV_GET_APP_VALUE_REQ(obj)
	if obj.opcode == 0x830A:
		DUMP_BT_AV_GET_APP_VALUE_CFM(obj)
	if obj.opcode == 0x30B:
		DUMP_BT_AV_SET_APP_VALUE_REQ(obj)
	if obj.opcode == 0x830B:
		DUMP_BT_AV_SET_APP_VALUE_CFM(obj)
	if obj.opcode == 0x30C:
		DUMP_BT_AV_GET_APP_ATT_TXT_REQ(obj)
	if obj.opcode == 0x830C:
		DUMP_BT_AV_GET_APP_ATT_TXT_CFM(obj)
	if obj.opcode == 0x831A:
		DUMP_BT_AV_APP_ATT_TXT_DATA_IND(obj)
	if obj.opcode == 0x831B:
		DUMP_BT_AV_APP_ATT_TXT_DATA_COMP_IND(obj)
	if obj.opcode == 0x30D:
		DUMP_BT_AV_GET_APP_VALUE_TXT_REQ(obj)
	if obj.opcode == 0x830D:
		DUMP_BT_AV_GET_APP_VALUE_TXT_CFM(obj)
	if obj.opcode == 0x831C:
		DUMP_BT_AV_APP_VAL_TXT_DATA_IND(obj)
	if obj.opcode == 0x831D:
		DUMP_BT_AV_APP_VAL_TXT_DATA_COMP_IND(obj)
	if obj.opcode == 0x30E:
		DUMP_BT_AV_ELEMENT_ATTRIBUTES_REQ(obj)
	if obj.opcode == 0x830E:
		DUMP_BT_AV_ELEMENT_ATTRIBUTES_CFM(obj)
	if obj.opcode == 0x8333:
		DUMP_BT_AV_ELEMENT_ATTRIBUTES_DATA_IND(obj)
	if obj.opcode == 0x8334:
		DUMP_BT_AV_ELEMENT_ATTRIBUTES_DATA_COMP_IND(obj)
	if obj.opcode == 0x30F:
		DUMP_BT_AV_INFORM_BATTERY_STATUS_REQ(obj)
	if obj.opcode == 0x830F:
		DUMP_BT_AV_INFORM_BATTERY_STATUS_CFM(obj)
	if obj.opcode == 0x310:
		DUMP_BT_AV_INFORM_CHARSET_REQ(obj)
	if obj.opcode == 0x8310:
		DUMP_BT_AV_INFORM_CHARSET_CFM(obj)
	if obj.opcode == 0x311:
		DUMP_BT_AV_SET_ABSOLUTE_VOL_REQ(obj)
	if obj.opcode == 0x8311:
		DUMP_BT_AV_SET_ABSOLUTE_VOL_CFM(obj)
	if obj.opcode == 0x312:
		DUMP_BT_AV_SET_ADDR_PLAYER_REQ(obj)
	if obj.opcode == 0x8312:
		DUMP_BT_AV_SET_ADDR_PLAYER_CFM(obj)
	if obj.opcode == 0x313:
		DUMP_BT_AV_PLAY_ITEM_REQ(obj)
	if obj.opcode == 0x8313:
		DUMP_BT_AV_PLAY_ITEM_CFM(obj)
	if obj.opcode == 0x314:
		DUMP_BT_AV_ADD_NOW_PLAYING_REQ(obj)
	if obj.opcode == 0x8314:
		DUMP_BT_AV_ADD_NOW_PLAYING_CFM(obj)
	if obj.opcode == 0x315:
		DUMP_BT_AV_SET_BROWSED_PLAYER_REQ(obj)
	if obj.opcode == 0x8315:
		DUMP_BT_AV_SET_BROWSED_PLAYER_CFM(obj)
	if obj.opcode == 0x316:
		DUMP_BT_AV_CHANGE_PATH_REQ(obj)
	if obj.opcode == 0x8316:
		DUMP_BT_AV_CHANGE_PATH_CFM(obj)
	if obj.opcode == 0x317:
		DUMP_BT_AV_GET_ITEM_ATT_REQ(obj)
	if obj.opcode == 0x8317:
		DUMP_BT_AV_GET_ITEM_ATT_CFM(obj)
	if obj.opcode == 0x8331:
		DUMP_BT_AV_BROWSE_ITEM_ATTRIBUTES_DATA_IND(obj)
	if obj.opcode == 0x8332:
		DUMP_BT_AV_BROWSE_ITEM_ATTRIBUTES_DATA_COMP_IND(obj)
	if obj.opcode == 0x318:
		DUMP_BT_AV_GET_FOLDER_ITEM_REQ(obj)
	if obj.opcode == 0x8318:
		DUMP_BT_AV_GET_FOLDER_ITEM_CFM(obj)
	if obj.opcode == 0x832F:
		DUMP_BT_AV_BROWSE_PLAYER_ITEM_DATA_IND(obj)
	if obj.opcode == 0x832D:
		DUMP_BT_AV_BROWSE_FOLDER_ITEM_DATA_IND(obj)
	if obj.opcode == 0x832E:
		DUMP_BT_AV_BROWSE_MEDIA_ITEM_DATA_IND(obj)
	if obj.opcode == 0x8330:
		DUMP_BT_AV_BROWSE_ITEM_DATA_COMP_IND(obj)
	if obj.opcode == 0x319:
		DUMP_BT_AV_SEARCH_REQ(obj)
	if obj.opcode == 0x8319:
		DUMP_BT_AV_SEARCH_CFM(obj)
	if obj.opcode == 0x319:
		DUMP_BT_AV_GET_BROWSE_XML_STREAM_REQ(obj)
	if obj.opcode == 0x8319:
		DUMP_BT_AV_GET_BROWSE_XML_STREAM_CFM(obj)
	if obj.opcode == 0x8320:
		DUMP_BT_AV_PLAYER_STATUS_CHANGE_NOTI_IND(obj)
	if obj.opcode == 0x8321:
		DUMP_BT_AV_TRACK_CHANGE_NOTI_IND(obj)
	if obj.opcode == 0x8322:
		DUMP_BT_AV_REACHED_END_NOTI_IND(obj)
	if obj.opcode == 0x8323:
		DUMP_BT_AV_REACHED_START_NOTI_IND(obj)
	if obj.opcode == 0x8324:
		DUMP_BT_AV_PLAYBACK_POSITION_CHANGE_NOTI_IND(obj)
	if obj.opcode == 0x8325:
		DUMP_BT_AV_BATTERY_STATUS_CHANGE_NOTI_IND(obj)
	if obj.opcode == 0x8326:
		DUMP_BT_AV_SYSTEM_STATUS_CHANGE_NOTI_IND(obj)
	if obj.opcode == 0x8328:
		DUMP_BT_AV_PLAYING_CONTENT_CHANGE_NOTI_IND(obj)
	if obj.opcode == 0x832C:
		DUMP_BT_AV_AVAILABLE_PLAYER_CHANGE_NOTI_IND(obj)
	if obj.opcode == 0x8329:
		DUMP_BT_AV_ADDRESSED_PLAYER_CHANGE_NOTI_IND(obj)
	if obj.opcode == 0x832A:
		DUMP_BT_AV_UID_CHANGE_NOTI_IND(obj)
	if obj.opcode == 0x832B:
		DUMP_BT_AV_VOLUME_CHANGE_NOTI_IND(obj)
	if obj.opcode == 0x8327:
		DUMP_BT_AVP_FID_EVT_PLAYER_APP_SETTING_CHANGED_IND(obj)
	if obj.opcode == 0x8338:
		DUMP_BT_AV_A2DP_CONFIGURATION_IND(obj)
	if obj.opcode == 0x8339:
		DUMP_BT_AV_A2DP_STREAM_DATA_IND(obj)
	if obj.opcode == 0x401:
		DUMP_BT_PBDL_ATCMD_START_SERVICE_REQ(obj)
	if obj.opcode == 0x8401:
		DUMP_BT_PBDL_ATCMD_START_SERVICE_CFM(obj)
	if obj.opcode == 0x402:
		DUMP_BT_PBDL_ATCMD_GET_STORAGE_REQ(obj)
	if obj.opcode == 0x8402:
		DUMP_BT_PBDL_ATCMD_GET_STORAGE_CFM(obj)
	if obj.opcode == 0x403:
		DUMP_BT_PBDL_ATCMD_GET_CURRENT_STORAGE_REQ(obj)
	if obj.opcode == 0x8403:
		DUMP_BT_PBDL_ATCMD_GET_CURRENT_STORAGE_CFM(obj)
	if obj.opcode == 0x404:
		DUMP_BT_PBDL_ATCMD_SET_STORAGE_REQ(obj)
	if obj.opcode == 0x8404:
		DUMP_BT_PBDL_ATCMD_SET_STORAGE_CFM(obj)
	if obj.opcode == 0x405:
		DUMP_BT_PBDL_ATCMD_READ_PB_ENTRY_REQ(obj)
	if obj.opcode == 0x8405:
		DUMP_BT_PBDL_ATCMD_READ_PB_ENTRY_CFM(obj)
	if obj.opcode == 0x406:
		DUMP_BT_PBDL_ATCMD_FIND_PB_ENTRY_REQ(obj)
	if obj.opcode == 0x8406:
		DUMP_BT_PBDL_ATCMD_FIND_PB_ENTRY_CFM(obj)
	if obj.opcode == 0x407:
		DUMP_BT_PBDL_ATCMD_ENTRY_DATA_ABORT_REQ(obj)
	if obj.opcode == 0x8407:
		DUMP_BT_PBDL_ATCMD_ENTRY_DATA_ABORT_CFM(obj)
	if obj.opcode == 0x8408:
		DUMP_BT_PBDL_ATCMD_PB_ENTRY_DATA_IND(obj)
	if obj.opcode == 0x8409:
		DUMP_BT_PBDL_ATCMD_PB_ENTRY_DATA_COMPLETE_IND(obj)
	if obj.opcode == 0x840A:
		DUMP_BT_PBDL_ATCMD_CONNECTION_IND(obj)
	if obj.opcode == 0x840B:
		DUMP_BT_PBDL_ATCMD_DISCONNECTION_IND(obj)
	if obj.opcode == 0x410:
		DUMP_BT_PBDL_PBAP_SET_FOLDER_REQ(obj)
	if obj.opcode == 0x8410:
		DUMP_BT_PBDL_PBAP_SET_FOLDER_CFM(obj)
	if obj.opcode == 0x411:
		DUMP_BT_PBDL_PBAP_GET_PBSIZE_REQ(obj)
	if obj.opcode == 0x8411:
		DUMP_BT_PBDL_PBAP_GET_PBSIZE_CFM(obj)
	if obj.opcode == 0x412:
		DUMP_BT_PBDL_PBAP_PULL_PB_REQ(obj)
	if obj.opcode == 0x8412:
		DUMP_BT_PBDL_PBAP_PULL_PB_CFM(obj)
	if obj.opcode == 0x413:
		DUMP_BT_PBDL_PBAP_PULL_VCARD_LIST_REQ(obj)
	if obj.opcode == 0x8413:
		DUMP_BT_PBDL_PBAP_PULL_VCARD_LIST_CFM(obj)
	if obj.opcode == 0x414:
		DUMP_BT_PBDL_PBAP_PULL_VCARD_ENTRY_REQ(obj)
	if obj.opcode == 0x8414:
		DUMP_BT_PBDL_PBAP_PULL_VCARD_ENTRY_CFM(obj)
	if obj.opcode == 0x8415:
		DUMP_BT_PBDL_PBAP_PB_ENTRY_DATA_IND(obj)
	if obj.opcode == 0x8416:
		DUMP_BT_PBDL_PBAP_PB_ENTRY_DATA_COMPLETE_IND(obj)
	if obj.opcode == 0x8417:
		DUMP_BT_PBDL_PBAP_VCARD_LIST_DATA_IND(obj)
	if obj.opcode == 0x8418:
		DUMP_BT_PBDL_PBAP_VCARD_LIST_DATA_COMPLETE_IND(obj)
	if obj.opcode == 0x8419:
		DUMP_BT_PBDL_PBAP_VCARD_ENTRY_DATA_IND(obj)
	if obj.opcode == 0x841A:
		DUMP_BT_PBDL_PBAP_VCARD_ENTRY_DATA_COMPLETE_IND(obj)
	if obj.opcode == 0x41B:
		DUMP_BT_PBDL_PBAP_PULL_ABORT_REQ(obj)
	if obj.opcode == 0x841B:
		DUMP_BT_PBDL_PBAP_PULL_ABORT_CFM(obj)
	if obj.opcode == 0x841C:
		DUMP_BT_PBDL_OPPS_PUT_FILE_IND(obj)
	if obj.opcode == 0x841D:
		DUMP_BT_PBDL_OPPS_PUT_BODY_IND(obj)
	if obj.opcode == 0x841E:
		DUMP_BT_PBDL_OPPS_PUT_COMPLETE_IND(obj)
	if obj.opcode == 0x841F:
		DUMP_BT_PBDL_OPPS_PUT_ABORT_IND(obj)
	if obj.opcode == 0x420:
		DUMP_BT_PBDL_OPPS_PUT_ABORT_REQ(obj)
	if obj.opcode == 0x8420:
		DUMP_BT_PBDL_OPPS_PUT_ABORT_CFM(obj)
	if obj.opcode == 0x430:
		DUMP_BT_PBDL_PULL_PB_REQ(obj)
	if obj.opcode == 0x8430:
		DUMP_BT_PBDL_PULL_PB_CFM(obj)
	if obj.opcode == 0x8432:
		DUMP_BT_PBDL_PULL_PB_CMP_IND(obj)
	if obj.opcode == 0x501:
		DUMP_BT_MAP_GET_DEVICE_LIST_REQ(obj)
	if obj.opcode == 0x8501:
		DUMP_BT_MAP_GET_DEVICE_LIST_CFM(obj)
	if obj.opcode == 0x502:
		DUMP_BT_MAP_GET_SDP_RECORD_REQ(obj)
	if obj.opcode == 0x8502:
		DUMP_BT_MAP_GET_SDP_RECORD_CFM(obj)
	if obj.opcode == 0x8510:
		DUMP_BT_MAP_GET_SDP_RECORD_IND(obj)
	if obj.opcode == 0x8511:
		DUMP_BT_MAP_SDP_RECORD_COMPLETE_IND(obj)
	if obj.opcode == 0x503:
		DUMP_BT_MAP_ESTABLIST_CONNECTION_REQ(obj)
	if obj.opcode == 0x8503:
		DUMP_BT_MAP_ESTABLIST_CONNECTION_CFM(obj)
	if obj.opcode == 0x504:
		DUMP_BT_MAP_DESTROY_CONNECTION_REQ(obj)
	if obj.opcode == 0x8504:
		DUMP_BT_MAP_DESTROY_CONNECTION_CFM(obj)
	if obj.opcode == 0x505:
		DUMP_BT_MAP_SET_FLODER_REQ(obj)
	if obj.opcode == 0x506:
		DUMP_BT_MAP_SET_FLODER_BACK_REQ(obj)
	if obj.opcode == 0x507:
		DUMP_BT_MAP_SET_FLODER_ROOT_REQ(obj)
	if obj.opcode == 0x8505:
		DUMP_BT_MAP_SET_FLODER_CFM(obj)
	if obj.opcode == 0x8506:
		DUMP_BT_MAP_SET_FLODER_BACK_CFM(obj)
	if obj.opcode == 0x8507:
		DUMP_BT_MAP_SET_FLODER_ROOT_CFM(obj)
	if obj.opcode == 0x508:
		DUMP_BT_MAP_GET_FLODERLIST_REQ(obj)
	if obj.opcode == 0x8508:
		DUMP_BT_MAP_GET_FLODERLIST_CFM(obj)
	if obj.opcode == 0x8514:
		DUMP_BT_MAP_GET_FLODERLIST_IND(obj)
	if obj.opcode == 0x8515:
		DUMP_BT_MAP_FLODERLIST_COMPLETE_IND(obj)
	if obj.opcode == 0x509:
		DUMP_BT_MAP_GET_MESSAGELIST_REQ(obj)
	if obj.opcode == 0x8509:
		DUMP_BT_MAP_GET_MESSAGELIST_CFM(obj)
	if obj.opcode == 0x8516:
		DUMP_BT_MAP_GET_MESSAGELIST_IND(obj)
	if obj.opcode == 0x8517:
		DUMP_BT_MAP_GET_MESSAGELIST_COMPLETE_IND(obj)
	if obj.opcode == 0x50A:
		DUMP_BT_MAP_GET_MESSAGE_REQ(obj)
	if obj.opcode == 0x850A:
		DUMP_BT_MAP_GET_MESSAGE_CFM(obj)
	if obj.opcode == 0x8518:
		DUMP_BT_MAP_GET_MESSAGE_IND(obj)
	if obj.opcode == 0x8519:
		DUMP_BT_MAP_FID_MESSAGE_COMPLETE_IND(obj)
	if obj.opcode == 0x50B:
		DUMP_BT_MAP_SET_MESSAGE_STATUS_REQ(obj)
	if obj.opcode == 0x850B:
		DUMP_BT_MAP_SET_MESSAGE_STATUS_CFM(obj)
	if obj.opcode == 0x50D:
		DUMP_BT_MAP_PUT_MESSAGE_REQ(obj)
	if obj.opcode == 0x850D:
		DUMP_BT_MAP_PUT_MESSAGE_CFM(obj)
	if obj.opcode == 0x50C:
		DUMP_BT_MAP_UPDATE_INBOX_REQ(obj)
	if obj.opcode == 0x850C:
		DUMP_BT_MAP_UPDATE_INBOX_CFM(obj)
	if obj.opcode == 0x50E:
		DUMP_BT_MAP_REGISTER_NOTIFICATION_REQ(obj)
	if obj.opcode == 0x850E:
		DUMP_BT_MAP_REGISTER_NOTIFICATION_CFM(obj)
	if obj.opcode == 0x851C:
		DUMP_BT_MAP_MESSAGE_NOTIFICATION_OFF_IND(obj)
	if obj.opcode == 0x851B:
		DUMP_BT_MAP_MESSAGE_NOTIFICATION_IND(obj)
	if obj.opcode == 0x8533:
		DUMP_BT_AT_SMS_CONNECTION_IND(obj)
	if obj.opcode == 0x8534:
		DUMP_BT_AT_SMS_DISCONNECTION_IND(obj)
	if obj.opcode == 0x529:
		DUMP_BT_MSG_SUPPORT_SMS_FORMAT_REQ(obj)
	if obj.opcode == 0x8529:
		DUMP_BT_MSG_SUPPORT_SMS_FORMAT_CFM(obj)
	if obj.opcode == 0x52A:
		DUMP_BT_MSG_CURRENT_SMS_FORMAT_REQ(obj)
	if obj.opcode == 0x852A:
		DUMP_BT_MSG_CURRENT_SMS_FORMAT_CFM(obj)
	if obj.opcode == 0x520:
		DUMP_BT_MSG_SET_SMS_FORMAT_REQ(obj)
	if obj.opcode == 0x8520:
		DUMP_BT_MSG_SET_SMS_FORMAT_CFM(obj)
	if obj.opcode == 0x52B:
		DUMP_BT_MSG_GET_SUPPORT_SMS_STORAGE_REQ(obj)
	if obj.opcode == 0x852B:
		DUMP_BT_MSG_GET_SUPPORT_SMS_STORAGE_CFM(obj)
	if obj.opcode == 0x52C:
		DUMP_BT_MSG_GET_CURRENT_SMS_STORAGE_REQ(obj)
	if obj.opcode == 0x852C:
		DUMP_BT_MSG_GET_CURRENT_SMS_STORAGE_CFM(obj)
	if obj.opcode == 0x521:
		DUMP_BT_MSG_SELECT_SMS_STORAGE_REQ(obj)
	if obj.opcode == 0x8521:
		DUMP_BT_MSG_SELECT_SMS_STORAGE_CFM(obj)
	if obj.opcode == 0x52D:
		DUMP_BT_MSG_GET_SUPPORT_LIST_SMS_REQ(obj)
	if obj.opcode == 0x852D:
		DUMP_BT_MSG_GET_SUPPORT_LIST_SMS_CFM(obj)
	if obj.opcode == 0x522:
		DUMP_BT_MSG_LIST_SMS_REQ(obj)
	if obj.opcode == 0x8522:
		DUMP_BT_MSG_LIST_SMS_CFM(obj)
	if obj.opcode == 0x8530:
		DUMP_BT_MSG_GET_CONTENT_IND(obj)
	if obj.opcode == 0x8531:
		DUMP_BT_MSG_GET_CONTENT_COMPLETED_IND(obj)
	if obj.opcode == 0x523:
		DUMP_BT_MSG_READ_SMS_REQ(obj)
	if obj.opcode == 0x8523:
		DUMP_BT_MSG_READ_SMS_CFM(obj)
	if obj.opcode == 0x527:
		DUMP_BT_MSG_DELETE_SMS_REQ(obj)
	if obj.opcode == 0x8527:
		DUMP_BT_MSG_DELETE_SMS_CFM(obj)
	if obj.opcode == 0x528:
		DUMP_BT_MSG_SET_SMS_NOTIFICATION_REQ(obj)
	if obj.opcode == 0x8528:
		DUMP_BT_MSG_SET_SMS_NOTIFICATION_CFM(obj)
	if obj.opcode == 0x524:
		DUMP_BT_MSG_SEND_SMS_REQ(obj)
	if obj.opcode == 0x8524:
		DUMP_BT_MSG_SEND_SMS_CFM(obj)
	if obj.opcode == 0x701:
		DUMP_BT_HID_CONNECT_REQ(obj)
	if obj.opcode == 0x8701:
		DUMP_BT_HID_CONNECT_CFM(obj)
	if obj.opcode == 0x702:
		DUMP_BT_HID_DISCONNECT_REQ(obj)
	if obj.opcode == 0x8702:
		DUMP_BT_HID_DISCONNECT_CFM(obj)
	if obj.opcode == 0x703:
		DUMP_BT_HID_DATA_REQ(obj)
	if obj.opcode == 0x8703:
		DUMP_BT_HID_DATA_CFM(obj)
	if obj.opcode == 0x8710:
		DUMP_BT_HID_STATUS_IND(obj)
def DUMP_BT_GEN_POWER_ON_REQ(obj):
	sys.stdout.write('BT_GEN_POWER_ON_REQ')
	sys.stdout.write(' local_addr=%s' % obj.local_addr)
	sys.stdout.write('\n')
def DUMP_BT_GEN_POWER_ON_CFM(obj):
	sys.stdout.write('BT_GEN_POWER_ON_CFM')
	sys.stdout.write(' status=%d' % obj.status)
	sys.stdout.write(' version=%d' % obj.version)
	sys.stdout.write(' supportservice=%d' % obj.supportservice)
	sys.stdout.write('\n')
def DUMP_BT_GEN_POWER_OFF_REQ(obj):
	sys.stdout.write('BT_GEN_POWER_OFF_REQ')
	sys.stdout.write('\n')
def DUMP_BT_GEN_POWER_OFF_CFM(obj):
	sys.stdout.write('BT_GEN_POWER_OFF_CFM')
	sys.stdout.write(' status=%d' % obj.status)
	sys.stdout.write('\n')
def DUMP_BT_GEN_GET_LOCAL_STATUS_REQ(obj):
	sys.stdout.write('BT_GEN_GET_LOCAL_STATUS_REQ')
	sys.stdout.write(' sid=%d' % obj.sid)
	sys.stdout.write('\n')
def DUMP_BT_GEN_GET_LOCAL_STATUS_CFM(obj):
	sys.stdout.write('BT_GEN_GET_LOCAL_STATUS_CFM')
	sys.stdout.write(' sid=%d' % obj.sid)
	sys.stdout.write(' data=%s' % obj.data)
	sys.stdout.write('\n')
def DUMP_BT_GEN_SET_LOCAL_CONFIG_REQ(obj):
	sys.stdout.write('BT_GEN_SET_LOCAL_CONFIG_REQ')
	sys.stdout.write(' cid=%d' % obj.cid)
	sys.stdout.write(' size=%d' % obj.size)
	sys.stdout.write(' data=%s' % obj.data)
	sys.stdout.write('\n')
def DUMP_BT_GEN_SET_LOCAL_CONFIG_CFM(obj):
	sys.stdout.write('BT_GEN_SET_LOCAL_CONFIG_CFM')
	sys.stdout.write(' status=%d' % obj.status)
	sys.stdout.write(' cid=%d' % obj.cid)
	sys.stdout.write(' length=%d' % obj.length)
	sys.stdout.write(' data=%s' % obj.data)
	sys.stdout.write('\n')
def DUMP_BT_GEN_READ_LOCAL_CONFIG_REQ(obj):
	sys.stdout.write('BT_GEN_READ_LOCAL_CONFIG_REQ')
	sys.stdout.write(' cid=%d' % obj.cid)
	sys.stdout.write('\n')
def DUMP_BT_GEN_READ_LOCAL_CONFIG_CFM(obj):
	sys.stdout.write('BT_GEN_READ_LOCAL_CONFIG_CFM')
	sys.stdout.write(' status=%d' % obj.status)
	sys.stdout.write(' cid=%d' % obj.cid)
	sys.stdout.write(' length=%d' % obj.length)
	sys.stdout.write(' data=%s' % obj.data)
	sys.stdout.write('\n')
def DUMP_BT_GEN_SSP_DEBUG_MODE_REQ(obj):
	sys.stdout.write('BT_GEN_SSP_DEBUG_MODE_REQ')
	sys.stdout.write(' enable=%d' % obj.enable)
	sys.stdout.write('\n')
def DUMP_BT_GEN_SSP_DEBUG_MODE_CFM(obj):
	sys.stdout.write('BT_GEN_SSP_DEBUG_MODE_CFM')
	sys.stdout.write(' status=%d' % obj.status)
	sys.stdout.write('\n')
def DUMP_BT_GEN_SEARCH_REMOTE_DEV_REQ(obj):
	sys.stdout.write('BT_GEN_SEARCH_REMOTE_DEV_REQ')
	sys.stdout.write(' count=%d' % obj.count)
	sys.stdout.write(' timer=%d' % obj.timer)
	sys.stdout.write('\n')
def DUMP_BT_GEN_SEARCH_REMOTE_DEV_CFM(obj):
	sys.stdout.write('BT_GEN_SEARCH_REMOTE_DEV_CFM')
	sys.stdout.write(' status=%d' % obj.status)
	sys.stdout.write('\n')
def DUMP_BT_GEN_SEARCH_REMOTE_DEV_IND(obj):
	sys.stdout.write('BT_GEN_SEARCH_REMOTE_DEV_IND')
	sys.stdout.write(' remote_addr=%s' % obj.remote_addr)
	sys.stdout.write(' cod=%d' % obj.cod)
	sys.stdout.write(' service=%d' % obj.service)
	sys.stdout.write(' length=%d' % obj.length)
	sys.stdout.write(' name=%s' % obj.name)
	sys.stdout.write('\n')
def DUMP_BT_GEN_SEARCH_REMOTE_DEV_COMP_IND(obj):
	sys.stdout.write('BT_GEN_SEARCH_REMOTE_DEV_COMP_IND')
	sys.stdout.write(' status=%d' % obj.status)
	sys.stdout.write('\n')
def DUMP_BT_GEN_SEARCH_REMOTE_DEV_CANCEL_REQ(obj):
	sys.stdout.write('BT_GEN_SEARCH_REMOTE_DEV_CANCEL_REQ')
	sys.stdout.write('\n')
def DUMP_BT_GEN_SEARCH_REMOTE_DEV_CANCEL_CFM(obj):
	sys.stdout.write('BT_GEN_SEARCH_REMOTE_DEV_CANCEL_CFM')
	sys.stdout.write(' status=%d' % obj.status)
	sys.stdout.write('\n')
def DUMP_BT_GEN_SET_LOCAL_NAME_REQ(obj):
	sys.stdout.write('BT_GEN_SET_LOCAL_NAME_REQ')
	sys.stdout.write(' length=%d' % obj.length)
	sys.stdout.write(' name=%s' % obj.name)
	sys.stdout.write('\n')
def DUMP_BT_GEN_SET_LOCAL_NAME_CFM(obj):
	sys.stdout.write('BT_GEN_SET_LOCAL_NAME_CFM')
	sys.stdout.write(' status=%d' % obj.status)
	sys.stdout.write('\n')
def DUMP_BT_GEN_READ_REMOTE_NAME_REQ(obj):
	sys.stdout.write('BT_GEN_READ_REMOTE_NAME_REQ')
	sys.stdout.write(' addr=%s' % obj.addr)
	sys.stdout.write('\n')
def DUMP_BT_GEN_READ_REMOTE_NAME_CFM(obj):
	sys.stdout.write('BT_GEN_READ_REMOTE_NAME_CFM')
	sys.stdout.write(' status=%d' % obj.status)
	sys.stdout.write(' remote=%s' % obj.remote)
	sys.stdout.write(' len=%d' % obj.len)
	sys.stdout.write(' name=%s' % obj.name)
	sys.stdout.write('\n')
def DUMP_BT_GEN_READ_REMOTE_NAME_CANCEL_REQ(obj):
	sys.stdout.write('BT_GEN_READ_REMOTE_NAME_CANCEL_REQ')
	sys.stdout.write(' addr=%s' % obj.addr)
	sys.stdout.write('\n')
def DUMP_BT_GEN_READ_REMOTE_NAME_CANCEL_CFM(obj):
	sys.stdout.write('BT_GEN_READ_REMOTE_NAME_CANCEL_CFM')
	sys.stdout.write(' status=%d' % obj.status)
	sys.stdout.write('\n')
def DUMP_BT_GEN_GET_LINK_QUALITY_REQ(obj):
	sys.stdout.write('BT_GEN_GET_LINK_QUALITY_REQ')
	sys.stdout.write(' addr=%s' % obj.addr)
	sys.stdout.write('\n')
def DUMP_BT_GEN_GET_LINK_QUALITY_CFM(obj):
	sys.stdout.write('BT_GEN_GET_LINK_QUALITY_CFM')
	sys.stdout.write(' status=%d' % obj.status)
	sys.stdout.write(' remote_addr=%s' % obj.remote_addr)
	sys.stdout.write(' linkQuality=%d' % obj.linkquality)
	sys.stdout.write('\n')
def DUMP_BT_GEN_SET_LOCAL_MODE_REQ(obj):
	sys.stdout.write('BT_GEN_SET_LOCAL_MODE_REQ')
	sys.stdout.write(' discovery=%d' % obj.discovery)
	sys.stdout.write(' bonded=%d' % obj.bonded)
	sys.stdout.write(' connectable=%d' % obj.connectable)
	sys.stdout.write('\n')
def DUMP_BT_GEN_SET_LOCAL_MODE_CFM(obj):
	sys.stdout.write('BT_GEN_SET_LOCAL_MODE_CFM')
	sys.stdout.write(' status=%d' % obj.status)
	sys.stdout.write(' discovery=%d' % obj.discovery)
	sys.stdout.write(' bonded=%d' % obj.bonded)
	sys.stdout.write(' connectable=%d' % obj.connectable)
	sys.stdout.write('\n')
def DUMP_BT_GEN_SERVICE_SEARCH_REQ(obj):
	sys.stdout.write('BT_GEN_SERVICE_SEARCH_REQ')
	sys.stdout.write(' addr=%s' % obj.addr)
	sys.stdout.write(' timeout=%d' % obj.timeout)
	sys.stdout.write('\n')
def DUMP_BT_GEN_SERVICE_SEARCH_CFM(obj):
	sys.stdout.write('BT_GEN_SERVICE_SEARCH_CFM')
	sys.stdout.write(' status=%d' % obj.status)
	sys.stdout.write('\n')
def DUMP_BT_GEN_SERVICE_SEARCH_IND(obj):
	sys.stdout.write('BT_GEN_SERVICE_SEARCH_IND')
	sys.stdout.write(' status=%d' % obj.status)
	sys.stdout.write(' remote_addr=%s' % obj.remote_addr)
	sys.stdout.write(' service=%d' % obj.service)
	sys.stdout.write(' version=%d' % obj.version)
	sys.stdout.write('\n')
def DUMP_BT_GEN_SERVICE_SEARCH_COMP_IND(obj):
	sys.stdout.write('BT_GEN_SERVICE_SEARCH_COMP_IND')
	sys.stdout.write(' status=%d' % obj.status)
	sys.stdout.write(' remote_addr=%s' % obj.remote_addr)
	sys.stdout.write(' service=%d' % obj.service)
	sys.stdout.write('\n')
def DUMP_BT_GEN_SDP_SEARCH_CANCEL_REQ(obj):
	sys.stdout.write('BT_GEN_SDP_SEARCH_CANCEL_REQ')
	sys.stdout.write(' addr=%s' % obj.addr)
	sys.stdout.write('\n')
def DUMP_BT_GEN_SERVICE_SEARCH_CANCEL_CFM(obj):
	sys.stdout.write('BT_GEN_SERVICE_SEARCH_CANCEL_CFM')
	sys.stdout.write(' status=%d' % obj.status)
	sys.stdout.write('\n')
def DUMP_BT_GEN_ENTER_TEST_MODE_REQ(obj):
	sys.stdout.write('BT_GEN_ENTER_TEST_MODE_REQ')
	sys.stdout.write('\n')
def DUMP_BT_GEN_DISABLE_TEST_MODE_REQ(obj):
	sys.stdout.write('BT_GEN_DISABLE_TEST_MODE_REQ')
	sys.stdout.write('\n')
def DUMP_BT_GEN_SERVICE_SEARCH_EXT_REQ(obj):
	sys.stdout.write('BT_GEN_SERVICE_SEARCH_EXT_REQ')
	sys.stdout.write(' addr=%s' % obj.addr)
	sys.stdout.write(' uuid=%s' % obj.uuid)
	sys.stdout.write('\n')
def DUMP_BT_GEN_SERVICE_SEARCH_EXT_CFM(obj):
	sys.stdout.write('BT_GEN_SERVICE_SEARCH_EXT_CFM')
	sys.stdout.write(' status=%d' % obj.status)
	sys.stdout.write('\n')
def DUMP_BT_GEN_SERVICE_SEARCH_EXT_IND(obj):
	sys.stdout.write('BT_GEN_SERVICE_SEARCH_EXT_IND')
	sys.stdout.write(' service=%d' % obj.service)
	sys.stdout.write('\n')
def DUMP_BT_GEN_SERVICE_SEARCH_EXT_COMPLETE_IND(obj):
	sys.stdout.write('BT_GEN_SERVICE_SEARCH_EXT_COMPLETE_IND')
	sys.stdout.write(' status=%d' % obj.status)
	sys.stdout.write('\n')
def DUMP_BT_GEN_GET_LOCAL_OOB_DATA_REQ(obj):
	sys.stdout.write('BT_GEN_GET_LOCAL_OOB_DATA_REQ')
	sys.stdout.write('\n')
def DUMP_BT_GEN_GET_LOCAL_OOB_DATA_CFM(obj):
	sys.stdout.write('BT_GEN_GET_LOCAL_OOB_DATA_CFM')
	sys.stdout.write(' status=%d' % obj.status)
	sys.stdout.write(' oobHashC=%s' % obj.oobhashc)
	sys.stdout.write(' oobRandR=%s' % obj.oobrandr)
	sys.stdout.write('\n')
def DUMP_BT_GEN_SET_REMOTE_OOB_DATA_REQ(obj):
	sys.stdout.write('BT_GEN_SET_REMOTE_OOB_DATA_REQ')
	sys.stdout.write(' addr=%s' % obj.addr)
	sys.stdout.write(' oobHashC=%s' % obj.oobhashc)
	sys.stdout.write(' oobRandR=%s' % obj.oobrandr)
	sys.stdout.write('\n')
def DUMP_BT_GEN_SET_REMOTE_OOB_DATA_CFM(obj):
	sys.stdout.write('BT_GEN_SET_REMOTE_OOB_DATA_CFM')
	sys.stdout.write(' status=%d' % obj.status)
	sys.stdout.write('\n')
def DUMP_BT_GEN_SEARCH_DEVICE_INFO_REQ(obj):
	sys.stdout.write('BT_GEN_SEARCH_DEVICE_INFO_REQ')
	sys.stdout.write(' remote=%s' % obj.remote)
	sys.stdout.write(' timeout=%d' % obj.timeout)
	sys.stdout.write('\n')
def DUMP_BT_GEN_FID_SEARCH_DEV_INFO_CFM(obj):
	sys.stdout.write('BT_GEN_FID_SEARCH_DEV_INFO_CFM')
	sys.stdout.write(' status=%d' % obj.status)
	sys.stdout.write('\n')
def DUMP_BT_GEN_FID_SEARCH_DEV_INFO_IND(obj):
	sys.stdout.write('BT_GEN_FID_SEARCH_DEV_INFO_IND')
	sys.stdout.write(' specId=%d' % obj.specid)
	sys.stdout.write(' vendorId=%d' % obj.vendorid)
	sys.stdout.write(' productId=%d' % obj.productid)
	sys.stdout.write(' version=%d' % obj.version)
	sys.stdout.write(' primaryRecord=%d' % obj.primaryrecord)
	sys.stdout.write(' vendorIDSource=%d' % obj.vendoridsource)
	sys.stdout.write('\n')
def DUMP_BT_GEN_FID_SEARCH_DEV_INFO_COMPLETE_IND(obj):
	sys.stdout.write('BT_GEN_FID_SEARCH_DEV_INFO_COMPLETE_IND')
	sys.stdout.write(' status=%d' % obj.status)
	sys.stdout.write(' remote=%s' % obj.remote)
	sys.stdout.write('\n')
def DUMP_BT_GEN_REGISTER_DEVICE_INFO_REQ(obj):
	sys.stdout.write('BT_GEN_REGISTER_DEVICE_INFO_REQ')
	sys.stdout.write(' vendorID=%d' % obj.vendorid)
	sys.stdout.write(' productID=%d' % obj.productid)
	sys.stdout.write(' version=%d' % obj.version)
	sys.stdout.write(' sourceID=%d' % obj.sourceid)
	sys.stdout.write('\n')
def DUMP_BT_GEN_FID_REGISTER_DEVICE_INFO_CFM(obj):
	sys.stdout.write('BT_GEN_FID_REGISTER_DEVICE_INFO_CFM')
	sys.stdout.write(' status=%d' % obj.status)
	sys.stdout.write('\n')
def DUMP_BT_GEN_UNREGISTER_DEVICE_INFO_REQ(obj):
	sys.stdout.write('BT_GEN_UNREGISTER_DEVICE_INFO_REQ')
	sys.stdout.write('\n')
def DUMP_BT_GEN_UNREGISTER_DEVICE_INFO_CFM(obj):
	sys.stdout.write('BT_GEN_UNREGISTER_DEVICE_INFO_CFM')
	sys.stdout.write(' status=%d' % obj.status)
	sys.stdout.write('\n')
def DUMP_BT_GEN_CANCEL_SEARCH_DEVICE_INFO_REQ(obj):
	sys.stdout.write('BT_GEN_CANCEL_SEARCH_DEVICE_INFO_REQ')
	sys.stdout.write('\n')
def DUMP_BT_GEN_CANCEL_SEARCH_DEVICE_INFO_CFM(obj):
	sys.stdout.write('BT_GEN_CANCEL_SEARCH_DEVICE_INFO_CFM')
	sys.stdout.write(' status=%d' % obj.status)
	sys.stdout.write('\n')
def DUMP_BT_CM_PAIRING_REMOTE_DEV_REQ(obj):
	sys.stdout.write('BT_CM_PAIRING_REMOTE_DEV_REQ')
	sys.stdout.write(' addr=%s' % obj.addr)
	sys.stdout.write('\n')
def DUMP_BT_CM_PAIRING_REMOTE_DEV_CFM(obj):
	sys.stdout.write('BT_CM_PAIRING_REMOTE_DEV_CFM')
	sys.stdout.write(' status=%d' % obj.status)
	sys.stdout.write('\n')
def DUMP_BT_CM_PAIRING_CANCEL_DEV_REQ(obj):
	sys.stdout.write('BT_CM_PAIRING_CANCEL_DEV_REQ')
	sys.stdout.write(' addr=%s' % obj.addr)
	sys.stdout.write('\n')
def DUMP_BT_CM_PAIRING_CANCEL_DEV_CFM(obj):
	sys.stdout.write('BT_CM_PAIRING_CANCEL_DEV_CFM')
	sys.stdout.write(' status=%d' % obj.status)
	sys.stdout.write('\n')
def DUMP_BT_CM_PIN_CODE_IND(obj):
	sys.stdout.write('BT_CM_PIN_CODE_IND')
	sys.stdout.write(' remote=%s' % obj.remote)
	sys.stdout.write(' cod=%d' % obj.cod)
	sys.stdout.write(' len=%d' % obj.len)
	sys.stdout.write(' name=%s' % obj.name)
	sys.stdout.write('\n')
def DUMP_BT_CM_PIN_CODE_RES(obj):
	sys.stdout.write('BT_CM_PIN_CODE_RES')
	sys.stdout.write(' remote=%s' % obj.remote)
	sys.stdout.write(' len=%d' % obj.len)
	sys.stdout.write(' pin_code=%s' % obj.pin_code)
	sys.stdout.write('\n')
def DUMP_BT_CM_PASSKEY_NOTIFICATION_IND(obj):
	sys.stdout.write('BT_CM_PASSKEY_NOTIFICATION_IND')
	sys.stdout.write(' remote=%s' % obj.remote)
	sys.stdout.write(' len=%d' % obj.len)
	sys.stdout.write(' name=%s' % obj.name)
	sys.stdout.write(' passkey=%d' % obj.passkey)
	sys.stdout.write('\n')
def DUMP_BT_CM_NUMERIC_CONFIRM_IND(obj):
	sys.stdout.write('BT_CM_NUMERIC_CONFIRM_IND')
	sys.stdout.write(' remote=%s' % obj.remote)
	sys.stdout.write(' len=%d' % obj.len)
	sys.stdout.write(' name=%s' % obj.name)
	sys.stdout.write(' numeric=%d' % obj.numeric)
	sys.stdout.write('\n')
def DUMP_BT_CM_NUM_DISPLAY_IND(obj):
	sys.stdout.write('BT_CM_NUM_DISPLAY_IND')
	sys.stdout.write(' remote=%s' % obj.remote)
	sys.stdout.write(' len=%d' % obj.len)
	sys.stdout.write(' name=%s' % obj.name)
	sys.stdout.write(' numeric=%d' % obj.numeric)
	sys.stdout.write('\n')
def DUMP_BT_CM_PASSKEY_REQ_IND(obj):
	sys.stdout.write('BT_CM_PASSKEY_REQ_IND')
	sys.stdout.write(' remote=%s' % obj.remote)
	sys.stdout.write(' len=%d' % obj.len)
	sys.stdout.write(' name=%s' % obj.name)
	sys.stdout.write('\n')
def DUMP_BT_CM_NUMERIC_CONFIRM_RES(obj):
	sys.stdout.write('BT_CM_NUMERIC_CONFIRM_RES')
	sys.stdout.write(' remote=%s' % obj.remote)
	sys.stdout.write(' accept=%d' % obj.accept)
	sys.stdout.write('\n')
def DUMP_BT_GEN_FID_PAIR_COMPLETE_IND(obj):
	sys.stdout.write('BT_GEN_FID_PAIR_COMPLETE_IND')
	sys.stdout.write(' status=%d' % obj.status)
	sys.stdout.write(' remote=%s' % obj.remote)
	sys.stdout.write('\n')
def DUMP_BT_CM_CON_AUTHORIZE_IND(obj):
	sys.stdout.write('BT_CM_CON_AUTHORIZE_IND')
	sys.stdout.write(' remote=%s' % obj.remote)
	sys.stdout.write(' service=%d' % obj.service)
	sys.stdout.write(' len=%d' % obj.len)
	sys.stdout.write(' name=%s' % obj.name)
	sys.stdout.write('\n')
def DUMP_BT_CM_CON_AUTHORIZE_RES(obj):
	sys.stdout.write('BT_CM_CON_AUTHORIZE_RES')
	sys.stdout.write(' remote=%s' % obj.remote)
	sys.stdout.write(' accept=%d' % obj.accept)
	sys.stdout.write('\n')
def DUMP_BT_CM_SERVICE_CON_REQ(obj):
	sys.stdout.write('BT_CM_SERVICE_CON_REQ')
	sys.stdout.write(' addr=%s' % obj.addr)
	sys.stdout.write(' service=%d' % obj.service)
	sys.stdout.write('\n')
def DUMP_BT_CM_SERVICE_CON_CFM(obj):
	sys.stdout.write('BT_CM_SERVICE_CON_CFM')
	sys.stdout.write(' status=%d' % obj.status)
	sys.stdout.write('\n')
def DUMP_BT_CM_SERVICE_CON_IND(obj):
	sys.stdout.write('BT_CM_SERVICE_CON_IND')
	sys.stdout.write(' status=%d' % obj.status)
	sys.stdout.write(' addr=%s' % obj.addr)
	sys.stdout.write(' function=%d' % obj.function)
	sys.stdout.write(' instanceId=%d' % obj.instanceid)
	sys.stdout.write(' extenParam=%d' % obj.extenparam)
	sys.stdout.write('\n')
def DUMP_BT_CM_SERVICE_CON_COMP_IND(obj):
	sys.stdout.write('BT_CM_SERVICE_CON_COMP_IND')
	sys.stdout.write(' function=%d' % obj.function)
	sys.stdout.write('\n')
def DUMP_BT_CM_SERVICE_CON_CANCEL_REQ(obj):
	sys.stdout.write('BT_CM_SERVICE_CON_CANCEL_REQ')
	sys.stdout.write(' addr=%s' % obj.addr)
	sys.stdout.write('\n')
def DUMP_BT_CM_SERVICE_CON_CANCEL_CFM(obj):
	sys.stdout.write('BT_CM_SERVICE_CON_CANCEL_CFM')
	sys.stdout.write(' status=%d' % obj.status)
	sys.stdout.write('\n')
def DUMP_BT_CM_SERVICE_DISCON_REQ(obj):
	sys.stdout.write('BT_CM_SERVICE_DISCON_REQ')
	sys.stdout.write(' addr=%s' % obj.addr)
	sys.stdout.write(' service=%d' % obj.service)
	sys.stdout.write('\n')
def DUMP_BT_CM_SERVICE_DISCON_CFM(obj):
	sys.stdout.write('BT_CM_SERVICE_DISCON_CFM')
	sys.stdout.write(' status=%d' % obj.status)
	sys.stdout.write('\n')
def DUMP_BT_CM_SERVICE_DISCON_IND(obj):
	sys.stdout.write('BT_CM_SERVICE_DISCON_IND')
	sys.stdout.write(' status=%d' % obj.status)
	sys.stdout.write(' addr=%s' % obj.addr)
	sys.stdout.write(' function=%d' % obj.function)
	sys.stdout.write(' instanceId=%d' % obj.instanceid)
	sys.stdout.write('\n')
def DUMP_BT_CM_SERVICE_DISCON_COMP_IND(obj):
	sys.stdout.write('BT_CM_SERVICE_DISCON_COMP_IND')
	sys.stdout.write(' addr=%s' % obj.addr)
	sys.stdout.write('\n')
def DUMP_BT_HFP_SERVICE_IND(obj):
	sys.stdout.write('BT_HFP_SERVICE_IND')
	sys.stdout.write(' did=%d' % obj.did)
	sys.stdout.write(' value =%d' % obj.value )
	sys.stdout.write('\n')
def DUMP_BT_HFP_SIGNAL_IND(obj):
	sys.stdout.write('BT_HFP_SIGNAL_IND')
	sys.stdout.write(' did=%d' % obj.did)
	sys.stdout.write(' value =%d' % obj.value )
	sys.stdout.write('\n')
def DUMP_BT_HFP_ROAM_IND(obj):
	sys.stdout.write('BT_HFP_ROAM_IND')
	sys.stdout.write(' did=%d' % obj.did)
	sys.stdout.write(' value =%d' % obj.value )
	sys.stdout.write('\n')
def DUMP_BT_HFP_BATTCHG_IND(obj):
	sys.stdout.write('BT_HFP_BATTCHG_IND')
	sys.stdout.write(' did=%d' % obj.did)
	sys.stdout.write(' value =%d' % obj.value )
	sys.stdout.write('\n')
def DUMP_BT_HFP_CALL_RING_IND(obj):
	sys.stdout.write('BT_HFP_CALL_RING_IND')
	sys.stdout.write(' did=%d' % obj.did)
	sys.stdout.write('\n')
def DUMP_BT_HFP_DIAL_OUT_REQ(obj):
	sys.stdout.write('BT_HFP_DIAL_OUT_REQ')
	sys.stdout.write(' did=%d' % obj.did)
	sys.stdout.write(' size=%d' % obj.size)
	sys.stdout.write(' num=%s' % obj.num)
	sys.stdout.write('\n')
def DUMP_BT_HFP_FID_DIAL_CFM(obj):
	sys.stdout.write('BT_HFP_FID_DIAL_CFM')
	sys.stdout.write(' did=%d' % obj.did)
	sys.stdout.write(' status=%d' % obj.status)
	sys.stdout.write('\n')
def DUMP_BT_HFP_CALL_STATE_IND(obj):
	sys.stdout.write('BT_HFP_CALL_STATE_IND')
	sys.stdout.write(' did=%d' % obj.did)
	sys.stdout.write(' state=%d' % obj.state)
	sys.stdout.write('\n')
def DUMP_BT_HFP_LAST_DIAL_REQ(obj):
	sys.stdout.write('BT_HFP_LAST_DIAL_REQ')
	sys.stdout.write(' did=%d' % obj.did)
	sys.stdout.write('\n')
def DUMP_BT_HFP_LAST_DIAL_CFM(obj):
	sys.stdout.write('BT_HFP_LAST_DIAL_CFM')
	sys.stdout.write(' did=%d' % obj.did)
	sys.stdout.write(' status=%d' % obj.status)
	sys.stdout.write('\n')
def DUMP_BT_HFP_MEM_DIAL_REQ(obj):
	sys.stdout.write('BT_HFP_MEM_DIAL_REQ')
	sys.stdout.write(' did=%d' % obj.did)
	sys.stdout.write(' index=%d' % obj.index)
	sys.stdout.write('\n')
def DUMP_BT_HFP_MEM_DIAL_CFM(obj):
	sys.stdout.write('BT_HFP_MEM_DIAL_CFM')
	sys.stdout.write(' status=%d' % obj.status)
	sys.stdout.write('\n')
def DUMP_BT_HFP_CALL_ANSWER_REQ(obj):
	sys.stdout.write('BT_HFP_CALL_ANSWER_REQ')
	sys.stdout.write(' did=%d' % obj.did)
	sys.stdout.write('\n')
def DUMP_BT_HFP_CALL_ANSWER_CFM(obj):
	sys.stdout.write('BT_HFP_CALL_ANSWER_CFM')
	sys.stdout.write(' did=%d' % obj.did)
	sys.stdout.write(' status=%d' % obj.status)
	sys.stdout.write('\n')
def DUMP_BT_HFP_CALL_REJECT_REQ(obj):
	sys.stdout.write('BT_HFP_CALL_REJECT_REQ')
	sys.stdout.write(' did=%d' % obj.did)
	sys.stdout.write('\n')
def DUMP_BT_HFP_CALL_REJECT_CFM(obj):
	sys.stdout.write('BT_HFP_CALL_REJECT_CFM')
	sys.stdout.write(' did=%d' % obj.did)
	sys.stdout.write(' status=%d' % obj.status)
	sys.stdout.write('\n')
def DUMP_BT_HFP_TERMINATE_CALL_REQ(obj):
	sys.stdout.write('BT_HFP_TERMINATE_CALL_REQ')
	sys.stdout.write(' did=%d' % obj.did)
	sys.stdout.write('\n')
def DUMP_BT_HFP_TERMINATE_CALL_CFM(obj):
	sys.stdout.write('BT_HFP_TERMINATE_CALL_CFM')
	sys.stdout.write(' did=%d' % obj.did)
	sys.stdout.write(' status=%d' % obj.status)
	sys.stdout.write('\n')
def DUMP_BT_HFP_CLIP_ENABLE_REQ(obj):
	sys.stdout.write('BT_HFP_CLIP_ENABLE_REQ')
	sys.stdout.write(' did=%d' % obj.did)
	sys.stdout.write(' enable=%d' % obj.enable)
	sys.stdout.write('\n')
def DUMP_BT_HFP_CLIP_ENABLE_CFM(obj):
	sys.stdout.write('BT_HFP_CLIP_ENABLE_CFM')
	sys.stdout.write(' did=%d' % obj.did)
	sys.stdout.write(' status=%d' % obj.status)
	sys.stdout.write('\n')
def DUMP_BT_HFP_CCWA_ENABLE_REQ(obj):
	sys.stdout.write('BT_HFP_CCWA_ENABLE_REQ')
	sys.stdout.write(' did=%d' % obj.did)
	sys.stdout.write(' enable=%d' % obj.enable)
	sys.stdout.write('\n')
def DUMP_BT_HFP_CCWA_ENABLE_CFM(obj):
	sys.stdout.write('BT_HFP_CCWA_ENABLE_CFM')
	sys.stdout.write(' did=%d' % obj.did)
	sys.stdout.write(' status=%d' % obj.status)
	sys.stdout.write('\n')
def DUMP_BT_HFP_INCOMING_CALL_IND(obj):
	sys.stdout.write('BT_HFP_INCOMING_CALL_IND')
	sys.stdout.write(' did=%d' % obj.did)
	sys.stdout.write(' num_size=%d' % obj.num_size)
	sys.stdout.write(' number=%s' % obj.number)
	sys.stdout.write(' len=%d' % obj.len)
	sys.stdout.write(' name=%s' % obj.name)
	sys.stdout.write('\n')
def DUMP_BT_HFP_SECOND_INCOMING_CALL_IND(obj):
	sys.stdout.write('BT_HFP_SECOND_INCOMING_CALL_IND')
	sys.stdout.write(' did=%d' % obj.did)
	sys.stdout.write(' num_size=%d' % obj.num_size)
	sys.stdout.write(' number=%s' % obj.number)
	sys.stdout.write(' len=%d' % obj.len)
	sys.stdout.write(' name=%s' % obj.name)
	sys.stdout.write('\n')
def DUMP_BT_HFP_AUDIO_TRANSFER_REQ(obj):
	sys.stdout.write('BT_HFP_AUDIO_TRANSFER_REQ')
	sys.stdout.write(' did=%d' % obj.did)
	sys.stdout.write(' side=%d' % obj.side)
	sys.stdout.write('\n')
def DUMP_BT_HFP_AUDIO_TRANSFER_CFM(obj):
	sys.stdout.write('BT_HFP_AUDIO_TRANSFER_CFM')
	sys.stdout.write(' did=%d' % obj.did)
	sys.stdout.write(' status=%d' % obj.status)
	sys.stdout.write('\n')
def DUMP_BT_HFP_SCO_IND(obj):
	sys.stdout.write('BT_HFP_SCO_IND')
	sys.stdout.write(' did=%d' % obj.did)
	sys.stdout.write(' side =%d' % obj.side )
	sys.stdout.write('\n')
def DUMP_BT_HFP_SEND_DTMF_REQ(obj):
	sys.stdout.write('BT_HFP_SEND_DTMF_REQ')
	sys.stdout.write(' did=%d' % obj.did)
	sys.stdout.write(' code=%d' % obj.code)
	sys.stdout.write('\n')
def DUMP_BT_HFP_SEND_DTMF_CFM(obj):
	sys.stdout.write('BT_HFP_SEND_DTMF_CFM')
	sys.stdout.write(' did=%d' % obj.did)
	sys.stdout.write(' status=%d' % obj.status)
	sys.stdout.write('\n')
def DUMP_BT_HFP_PESPONSE_AND_HOLD_REQ(obj):
	sys.stdout.write('BT_HFP_PESPONSE_AND_HOLD_REQ')
	sys.stdout.write(' did=%d' % obj.did)
	sys.stdout.write(' action=%d' % obj.action)
	sys.stdout.write('\n')
def DUMP_BT_HFP_PESPONSE_AND_HOLD_CFM(obj):
	sys.stdout.write('BT_HFP_PESPONSE_AND_HOLD_CFM')
	sys.stdout.write(' did=%d' % obj.did)
	sys.stdout.write(' status=%d' % obj.status)
	sys.stdout.write('\n')
def DUMP_BT_HFP_CALL_HOLD_REQ(obj):
	sys.stdout.write('BT_HFP_CALL_HOLD_REQ')
	sys.stdout.write(' did=%d' % obj.did)
	sys.stdout.write(' action=%d' % obj.action)
	sys.stdout.write(' index=%d' % obj.index)
	sys.stdout.write('\n')
def DUMP_BT_HFP_CALL_HOLD_CFM(obj):
	sys.stdout.write('BT_HFP_CALL_HOLD_CFM')
	sys.stdout.write(' did=%d' % obj.did)
	sys.stdout.write(' status=%d' % obj.status)
	sys.stdout.write('\n')
def DUMP_BT_HFP_ANSWER_SECOND_CALL_REQ(obj):
	sys.stdout.write('BT_HFP_ANSWER_SECOND_CALL_REQ')
	sys.stdout.write(' did=%d' % obj.did)
	sys.stdout.write(' hold=%d' % obj.hold)
	sys.stdout.write('\n')
def DUMP_BT_HFP_ANSWER_SECOND_CALL_CFM(obj):
	sys.stdout.write('BT_HFP_ANSWER_SECOND_CALL_CFM')
	sys.stdout.write(' did=%d' % obj.did)
	sys.stdout.write(' status=%d' % obj.status)
	sys.stdout.write('\n')
def DUMP_BT_HFP_TERMINATE_CALL_BY_INDEX_REQ(obj):
	sys.stdout.write('BT_HFP_TERMINATE_CALL_BY_INDEX_REQ')
	sys.stdout.write(' did=%d' % obj.did)
	sys.stdout.write(' index=%d' % obj.index)
	sys.stdout.write('\n')
def DUMP_BT_HFP_TERMINATE_CALL_BY_INDEX_CFM(obj):
	sys.stdout.write('BT_HFP_TERMINATE_CALL_BY_INDEX_CFM')
	sys.stdout.write(' did=%d' % obj.did)
	sys.stdout.write(' status=%d' % obj.status)
	sys.stdout.write('\n')
def DUMP_BT_HFP_SWITCH_CALL_REQ(obj):
	sys.stdout.write('BT_HFP_SWITCH_CALL_REQ')
	sys.stdout.write(' did=%d' % obj.did)
	sys.stdout.write('\n')
def DUMP_BT_HFP_SWITCH_CALL_CFM(obj):
	sys.stdout.write('BT_HFP_SWITCH_CALL_CFM')
	sys.stdout.write(' did=%d' % obj.did)
	sys.stdout.write(' status=%d' % obj.status)
	sys.stdout.write('\n')
def DUMP_BT_HFP_JOIN_CALL_REQ(obj):
	sys.stdout.write('BT_HFP_JOIN_CALL_REQ')
	sys.stdout.write(' did=%d' % obj.did)
	sys.stdout.write('\n')
def DUMP_BT_HFP_JOIN_CALL_CFM(obj):
	sys.stdout.write('BT_HFP_JOIN_CALL_CFM')
	sys.stdout.write(' did=%d' % obj.did)
	sys.stdout.write(' status=%d' % obj.status)
	sys.stdout.write('\n')
def DUMP_BT_HFP_GET_SUBSCRIBER_NUM_REQ(obj):
	sys.stdout.write('BT_HFP_GET_SUBSCRIBER_NUM_REQ')
	sys.stdout.write(' did=%d' % obj.did)
	sys.stdout.write('\n')
def DUMP_BT_HFP_GET_SUBSCRIBER_NUM_CFM(obj):
	sys.stdout.write('BT_HFP_GET_SUBSCRIBER_NUM_CFM')
	sys.stdout.write(' did=%d' % obj.did)
	sys.stdout.write(' status=%d' % obj.status)
	sys.stdout.write(' size=%d' % obj.size)
	sys.stdout.write(' num=%s' % obj.num)
	sys.stdout.write('\n')
def DUMP_BT_HFP_GET_OPERATOR_NAME_REQ(obj):
	sys.stdout.write('BT_HFP_GET_OPERATOR_NAME_REQ')
	sys.stdout.write(' did=%d' % obj.did)
	sys.stdout.write('\n')
def DUMP_BT_HFP_GET_OPERATOR_NAME_CFM(obj):
	sys.stdout.write('BT_HFP_GET_OPERATOR_NAME_CFM')
	sys.stdout.write(' did=%d' % obj.did)
	sys.stdout.write(' status=%d' % obj.status)
	sys.stdout.write(' length=%d' % obj.length)
	sys.stdout.write(' name=%s' % obj.name)
	sys.stdout.write('\n')
def DUMP_BT_HFP_GET_CURRENT_CALL_LIST_REQ(obj):
	sys.stdout.write('BT_HFP_GET_CURRENT_CALL_LIST_REQ')
	sys.stdout.write(' did=%d' % obj.did)
	sys.stdout.write('\n')
def DUMP_BT_HFP_GET_CURRENT_CALL_LIST_CFM(obj):
	sys.stdout.write('BT_HFP_GET_CURRENT_CALL_LIST_CFM')
	sys.stdout.write(' did=%d' % obj.did)
	sys.stdout.write(' status=%d' % obj.status)
	sys.stdout.write('\n')
def DUMP_BT_HFP_GET_CURRENT_CALL_LIST_IND(obj):
	sys.stdout.write('BT_HFP_GET_CURRENT_CALL_LIST_IND')
	sys.stdout.write(' did=%d' % obj.did)
	sys.stdout.write(' idx=%d' % obj.idx)
	sys.stdout.write(' dir=%d' % obj.dir)
	sys.stdout.write(' status=%d' % obj.status)
	sys.stdout.write(' mode=%d' % obj.mode)
	sys.stdout.write(' mpty=%d' % obj.mpty)
	sys.stdout.write(' type=%d' % obj.type)
	sys.stdout.write(' size=%d' % obj.size)
	sys.stdout.write(' num=%s' % obj.num)
	sys.stdout.write('\n')
def DUMP_BT_HFP_GET_CURRENT_CALL_LIST_COMPLETE_IND(obj):
	sys.stdout.write('BT_HFP_GET_CURRENT_CALL_LIST_COMPLETE_IND')
	sys.stdout.write(' did=%d' % obj.did)
	sys.stdout.write(' status=%d' % obj.status)
	sys.stdout.write('\n')
def DUMP_BT_SPP_DATA_SEND_REQ(obj):
	sys.stdout.write('BT_SPP_DATA_SEND_REQ')
	sys.stdout.write(' spp_id=%d' % obj.spp_id)
	sys.stdout.write(' length=%d' % obj.length)
	sys.stdout.write(' data=%s' % obj.data)
	sys.stdout.write('\n')
def DUMP_BT_SPP_DATA_SEND_CFM(obj):
	sys.stdout.write('BT_SPP_DATA_SEND_CFM')
	sys.stdout.write(' status=%d' % obj.status)
	sys.stdout.write(' spp_id=%d' % obj.spp_id)
	sys.stdout.write('\n')
def DUMP_BT_SPP_DATA_RECEIVE_IND(obj):
	sys.stdout.write('BT_SPP_DATA_RECEIVE_IND')
	sys.stdout.write(' spp_id=%d' % obj.spp_id)
	sys.stdout.write(' length=%d' % obj.length)
	sys.stdout.write(' data=%s' % obj.data)
	sys.stdout.write('\n')
def DUMP_BT_SPP_ACTIVE_SERVER_REQ(obj):
	sys.stdout.write('BT_SPP_ACTIVE_SERVER_REQ')
	sys.stdout.write(' uuid=%s' % obj.uuid)
	sys.stdout.write(' length=%d' % obj.length)
	sys.stdout.write(' name=%s' % obj.name)
	sys.stdout.write('\n')
def DUMP_BT_SPP_ACTIVE_SERVER_CFM(obj):
	sys.stdout.write('BT_SPP_ACTIVE_SERVER_CFM')
	sys.stdout.write(' sppId=%d' % obj.sppid)
	sys.stdout.write(' status=%d' % obj.status)
	sys.stdout.write('\n')
def DUMP_BT_SPP_DEACTIVE_SERVER_REQ(obj):
	sys.stdout.write('BT_SPP_DEACTIVE_SERVER_REQ')
	sys.stdout.write(' sppId=%d' % obj.sppid)
	sys.stdout.write('\n')
def DUMP_BT_SPP_DEACTIVE_SERVER_CFM(obj):
	sys.stdout.write('BT_SPP_DEACTIVE_SERVER_CFM')
	sys.stdout.write(' sppId=%d' % obj.sppid)
	sys.stdout.write(' status=%d' % obj.status)
	sys.stdout.write('\n')
def DUMP_BT_AV_AVRCP_CONNECT_IND(obj):
	sys.stdout.write('BT_AV_AVRCP_CONNECT_IND')
	sys.stdout.write(' did=%d' % obj.did)
	sys.stdout.write(' status=%d' % obj.status)
	sys.stdout.write(' version=%d' % obj.version)
	sys.stdout.write(' feature=%d' % obj.feature)
	sys.stdout.write(' addr=%s' % obj.addr)
	sys.stdout.write('\n')
def DUMP_BT_AV_AVRCP_DISCONNECT_IND(obj):
	sys.stdout.write('BT_AV_AVRCP_DISCONNECT_IND')
	sys.stdout.write(' did=%d' % obj.did)
	sys.stdout.write(' status=%d' % obj.status)
	sys.stdout.write('\n')
def DUMP_BT_AV_MEDIA_START_REQ(obj):
	sys.stdout.write('BT_AV_MEDIA_START_REQ')
	sys.stdout.write(' did=%d' % obj.did)
	sys.stdout.write('\n')
def DUMP_BT_AV_MEDIA_START_CFM(obj):
	sys.stdout.write('BT_AV_MEDIA_START_CFM')
	sys.stdout.write(' did=%d' % obj.did)
	sys.stdout.write(' status=%d' % obj.status)
	sys.stdout.write('\n')
def DUMP_BT_AV_MEDIA_STOP_REQ(obj):
	sys.stdout.write('BT_AV_MEDIA_STOP_REQ')
	sys.stdout.write(' did=%d' % obj.did)
	sys.stdout.write('\n')
def DUMP_BT_AV_MEDIA_STOP_CFM(obj):
	sys.stdout.write('BT_AV_MEDIA_STOP_CFM')
	sys.stdout.write(' did=%d' % obj.did)
	sys.stdout.write(' status=%d' % obj.status)
	sys.stdout.write('\n')
def DUMP_BT_AV_MEDIA_PASS_THROUGH_REQ(obj):
	sys.stdout.write('BT_AV_MEDIA_PASS_THROUGH_REQ')
	sys.stdout.write(' did=%d' % obj.did)
	sys.stdout.write(' opid=%d' % obj.opid)
	sys.stdout.write(' state=%d' % obj.state)
	sys.stdout.write('\n')
def DUMP_BT_AV_MEDIA_PASS_THROUGH_CFM(obj):
	sys.stdout.write('BT_AV_MEDIA_PASS_THROUGH_CFM')
	sys.stdout.write(' did=%d' % obj.did)
	sys.stdout.write(' status=%d' % obj.status)
	sys.stdout.write('\n')
def DUMP_BT_AV_GET_CAPBILITY_REQ(obj):
	sys.stdout.write('BT_AV_GET_CAPBILITY_REQ')
	sys.stdout.write(' device_id=%d' % obj.device_id)
	sys.stdout.write(' caps=%d' % obj.caps)
	sys.stdout.write('\n')
def DUMP_BT_AV_GET_CAPBILITY_CFM(obj):
	sys.stdout.write('BT_AV_GET_CAPBILITY_CFM')
	sys.stdout.write(' did=%d' % obj.did)
	sys.stdout.write(' status=%d' % obj.status)
	sys.stdout.write(' caps=%d' % obj.caps)
	sys.stdout.write(' notiMask=%d' % obj.notimask)
	sys.stdout.write(' companyId=%d' % obj.companyid)
	sys.stdout.write('\n')
def DUMP_BT_AV_GET_PLAY_STATUS_REQ(obj):
	sys.stdout.write('BT_AV_GET_PLAY_STATUS_REQ')
	sys.stdout.write(' did=%d' % obj.did)
	sys.stdout.write('\n')
def DUMP_BT_AV_GET_PLAY_STATUS_CFM(obj):
	sys.stdout.write('BT_AV_GET_PLAY_STATUS_CFM')
	sys.stdout.write(' did=%d' % obj.did)
	sys.stdout.write(' status=%d' % obj.status)
	sys.stdout.write(' song_length=%d' % obj.song_length)
	sys.stdout.write(' song_elapsed=%d' % obj.song_elapsed)
	sys.stdout.write(' play_status=%d' % obj.play_status)
	sys.stdout.write('\n')
def DUMP_BT_AV_NOTI_REGISTER_REQ(obj):
	sys.stdout.write('BT_AV_NOTI_REGISTER_REQ')
	sys.stdout.write(' did=%d' % obj.did)
	sys.stdout.write(' Notimask=%d' % obj.notimask)
	sys.stdout.write(' PlaybackInterval=%d' % obj.playbackinterval)
	sys.stdout.write(' configMask=%d' % obj.configmask)
	sys.stdout.write('\n')
def DUMP_BT_AV_NOTI_REGISTER_CFM(obj):
	sys.stdout.write('BT_AV_NOTI_REGISTER_CFM')
	sys.stdout.write(' did=%d' % obj.did)
	sys.stdout.write(' status=%d' % obj.status)
	sys.stdout.write(' notiMask=%d' % obj.notimask)
	sys.stdout.write(' playbackInterval=%d' % obj.playbackinterval)
	sys.stdout.write('\n')
def DUMP_BT_AV_LIST_APP_ATT_ID_REQ(obj):
	sys.stdout.write('BT_AV_LIST_APP_ATT_ID_REQ')
	sys.stdout.write(' did=%d' % obj.did)
	sys.stdout.write('\n')
def DUMP_BT_AV_LIST_APP_ATT_ID_CFM(obj):
	sys.stdout.write('BT_AV_LIST_APP_ATT_ID_CFM')
	sys.stdout.write(' did=%d' % obj.did)
	sys.stdout.write(' status=%d' % obj.status)
	sys.stdout.write(' number_of_attributes=%d' % obj.number_of_attributes)
	sys.stdout.write(' size=%d' % obj.size)
	sys.stdout.write(' attribute=%s' % obj.attribute)
	sys.stdout.write('\n')
def DUMP_BT_AV_LIST_APP_VALUE_ID_REQ(obj):
	sys.stdout.write('BT_AV_LIST_APP_VALUE_ID_REQ')
	sys.stdout.write(' did=%d' % obj.did)
	sys.stdout.write(' attributeid=%d' % obj.attributeid)
	sys.stdout.write('\n')
def DUMP_BT_AV_LIST_APP_VALUE_ID_CFM(obj):
	sys.stdout.write('BT_AV_LIST_APP_VALUE_ID_CFM')
	sys.stdout.write(' did=%d' % obj.did)
	sys.stdout.write(' status=%d' % obj.status)
	sys.stdout.write(' attributeId=%d' % obj.attributeid)
	sys.stdout.write(' number_of_values=%d' % obj.number_of_values)
	sys.stdout.write(' size=%d' % obj.size)
	sys.stdout.write(' value=%s' % obj.value)
	sys.stdout.write('\n')
def DUMP_BT_AV_GET_APP_VALUE_REQ(obj):
	sys.stdout.write('BT_AV_GET_APP_VALUE_REQ')
	sys.stdout.write(' did=%d' % obj.did)
	sys.stdout.write(' attributes=%d' % obj.attributes)
	sys.stdout.write('\n')
def DUMP_BT_AV_GET_APP_VALUE_CFM(obj):
	sys.stdout.write('BT_AV_GET_APP_VALUE_CFM')
	sys.stdout.write(' did=%d' % obj.did)
	sys.stdout.write(' status=%d' % obj.status)
	sys.stdout.write(' attvalPairCount=%d' % obj.attvalpaircount)
	sys.stdout.write(' attIdLen=%d' % obj.attidlen)
	sys.stdout.write(' attId=%s' % obj.attid)
	sys.stdout.write(' valIdLen=%d' % obj.validlen)
	sys.stdout.write(' valId=%s' % obj.valid)
	sys.stdout.write('\n')
def DUMP_BT_AV_SET_APP_VALUE_REQ(obj):
	sys.stdout.write('BT_AV_SET_APP_VALUE_REQ')
	sys.stdout.write(' did=%d' % obj.did)
	sys.stdout.write(' attvalPairCount=%d' % obj.attvalpaircount)
	sys.stdout.write(' attIdLen=%d' % obj.attidlen)
	sys.stdout.write(' attId=%s' % obj.attid)
	sys.stdout.write(' valIdLen=%d' % obj.validlen)
	sys.stdout.write(' valId=%s' % obj.valid)
	sys.stdout.write('\n')
def DUMP_BT_AV_SET_APP_VALUE_CFM(obj):
	sys.stdout.write('BT_AV_SET_APP_VALUE_CFM')
	sys.stdout.write(' did=%d' % obj.did)
	sys.stdout.write(' status=%d' % obj.status)
	sys.stdout.write('\n')
def DUMP_BT_AV_GET_APP_ATT_TXT_REQ(obj):
	sys.stdout.write('BT_AV_GET_APP_ATT_TXT_REQ')
	sys.stdout.write(' did=%d' % obj.did)
	sys.stdout.write(' attributes=%d' % obj.attributes)
	sys.stdout.write('\n')
def DUMP_BT_AV_GET_APP_ATT_TXT_CFM(obj):
	sys.stdout.write('BT_AV_GET_APP_ATT_TXT_CFM')
	sys.stdout.write(' did=%d' % obj.did)
	sys.stdout.write(' status=%d' % obj.status)
	sys.stdout.write('\n')
def DUMP_BT_AV_APP_ATT_TXT_DATA_IND(obj):
	sys.stdout.write('BT_AV_APP_ATT_TXT_DATA_IND')
	sys.stdout.write(' did=%d' % obj.did)
	sys.stdout.write(' attributeid=%d' % obj.attributeid)
	sys.stdout.write(' valueId=%d' % obj.valueid)
	sys.stdout.write(' charSet=%d' % obj.charset)
	sys.stdout.write(' Len=%d' % obj.len)
	sys.stdout.write(' text=%s' % obj.text)
	sys.stdout.write('\n')
def DUMP_BT_AV_APP_ATT_TXT_DATA_COMP_IND(obj):
	sys.stdout.write('BT_AV_APP_ATT_TXT_DATA_COMP_IND')
	sys.stdout.write(' did=%d' % obj.did)
	sys.stdout.write(' status=%d' % obj.status)
	sys.stdout.write('\n')
def DUMP_BT_AV_GET_APP_VALUE_TXT_REQ(obj):
	sys.stdout.write('BT_AV_GET_APP_VALUE_TXT_REQ')
	sys.stdout.write(' did=%d' % obj.did)
	sys.stdout.write(' attribute_id=%d' % obj.attribute_id)
	sys.stdout.write(' valIdCount=%d' % obj.validcount)
	sys.stdout.write(' values=%s' % obj.values)
	sys.stdout.write('\n')
def DUMP_BT_AV_GET_APP_VALUE_TXT_CFM(obj):
	sys.stdout.write('BT_AV_GET_APP_VALUE_TXT_CFM')
	sys.stdout.write(' did=%d' % obj.did)
	sys.stdout.write(' status=%d' % obj.status)
	sys.stdout.write('\n')
def DUMP_BT_AV_APP_VAL_TXT_DATA_IND(obj):
	sys.stdout.write('BT_AV_APP_VAL_TXT_DATA_IND')
	sys.stdout.write(' did=%d' % obj.did)
	sys.stdout.write(' attributeId=%d' % obj.attributeid)
	sys.stdout.write(' valueId=%d' % obj.valueid)
	sys.stdout.write(' charset=%d' % obj.charset)
	sys.stdout.write(' len=%d' % obj.len)
	sys.stdout.write(' text=%s' % obj.text)
	sys.stdout.write('\n')
def DUMP_BT_AV_APP_VAL_TXT_DATA_COMP_IND(obj):
	sys.stdout.write('BT_AV_APP_VAL_TXT_DATA_COMP_IND')
	sys.stdout.write(' did=%d' % obj.did)
	sys.stdout.write(' status=%d' % obj.status)
	sys.stdout.write('\n')
def DUMP_BT_AV_ELEMENT_ATTRIBUTES_REQ(obj):
	sys.stdout.write('BT_AV_ELEMENT_ATTRIBUTES_REQ')
	sys.stdout.write(' did=%d' % obj.did)
	sys.stdout.write(' attributes=%d' % obj.attributes)
	sys.stdout.write('\n')
def DUMP_BT_AV_ELEMENT_ATTRIBUTES_CFM(obj):
	sys.stdout.write('BT_AV_ELEMENT_ATTRIBUTES_CFM')
	sys.stdout.write(' did=%d' % obj.did)
	sys.stdout.write(' status=%d' % obj.status)
	sys.stdout.write(' num=%d' % obj.num)
	sys.stdout.write('\n')
def DUMP_BT_AV_ELEMENT_ATTRIBUTES_DATA_IND(obj):
	sys.stdout.write('BT_AV_ELEMENT_ATTRIBUTES_DATA_IND')
	sys.stdout.write(' did=%d' % obj.did)
	sys.stdout.write(' attributeid=%d' % obj.attributeid)
	sys.stdout.write(' charset=%d' % obj.charset)
	sys.stdout.write(' len=%d' % obj.len)
	sys.stdout.write(' text=%s' % obj.text)
	sys.stdout.write('\n')
def DUMP_BT_AV_ELEMENT_ATTRIBUTES_DATA_COMP_IND(obj):
	sys.stdout.write('BT_AV_ELEMENT_ATTRIBUTES_DATA_COMP_IND')
	sys.stdout.write(' did=%d' % obj.did)
	sys.stdout.write(' status=%d' % obj.status)
	sys.stdout.write('\n')
def DUMP_BT_AV_INFORM_BATTERY_STATUS_REQ(obj):
	sys.stdout.write('BT_AV_INFORM_BATTERY_STATUS_REQ')
	sys.stdout.write(' did=%d' % obj.did)
	sys.stdout.write(' battery_status=%d' % obj.battery_status)
	sys.stdout.write('\n')
def DUMP_BT_AV_INFORM_BATTERY_STATUS_CFM(obj):
	sys.stdout.write('BT_AV_INFORM_BATTERY_STATUS_CFM')
	sys.stdout.write(' did=%d' % obj.did)
	sys.stdout.write(' status=%d' % obj.status)
	sys.stdout.write('\n')
def DUMP_BT_AV_INFORM_CHARSET_REQ(obj):
	sys.stdout.write('BT_AV_INFORM_CHARSET_REQ')
	sys.stdout.write(' did=%d' % obj.did)
	sys.stdout.write(' charsets=%d' % obj.charsets)
	sys.stdout.write('\n')
def DUMP_BT_AV_INFORM_CHARSET_CFM(obj):
	sys.stdout.write('BT_AV_INFORM_CHARSET_CFM')
	sys.stdout.write(' did=%d' % obj.did)
	sys.stdout.write(' status=%d' % obj.status)
	sys.stdout.write('\n')
def DUMP_BT_AV_SET_ABSOLUTE_VOL_REQ(obj):
	sys.stdout.write('BT_AV_SET_ABSOLUTE_VOL_REQ')
	sys.stdout.write(' did=%d' % obj.did)
	sys.stdout.write(' volume=%d' % obj.volume)
	sys.stdout.write('\n')
def DUMP_BT_AV_SET_ABSOLUTE_VOL_CFM(obj):
	sys.stdout.write('BT_AV_SET_ABSOLUTE_VOL_CFM')
	sys.stdout.write(' did=%d' % obj.did)
	sys.stdout.write(' status=%d' % obj.status)
	sys.stdout.write(' volume=%d' % obj.volume)
	sys.stdout.write('\n')
def DUMP_BT_AV_SET_ADDR_PLAYER_REQ(obj):
	sys.stdout.write('BT_AV_SET_ADDR_PLAYER_REQ')
	sys.stdout.write(' did=%d' % obj.did)
	sys.stdout.write(' pid=%d' % obj.pid)
	sys.stdout.write('\n')
def DUMP_BT_AV_SET_ADDR_PLAYER_CFM(obj):
	sys.stdout.write('BT_AV_SET_ADDR_PLAYER_CFM')
	sys.stdout.write(' did=%d' % obj.did)
	sys.stdout.write(' status=%d' % obj.status)
	sys.stdout.write('\n')
def DUMP_BT_AV_PLAY_ITEM_REQ(obj):
	sys.stdout.write('BT_AV_PLAY_ITEM_REQ')
	sys.stdout.write(' did=%d' % obj.did)
	sys.stdout.write(' scope=%d' % obj.scope)
	sys.stdout.write(' uidHigh=%d' % obj.uidhigh)
	sys.stdout.write(' uidLow=%d' % obj.uidlow)
	sys.stdout.write(' uid_counter=%d' % obj.uid_counter)
	sys.stdout.write('\n')
def DUMP_BT_AV_PLAY_ITEM_CFM(obj):
	sys.stdout.write('BT_AV_PLAY_ITEM_CFM')
	sys.stdout.write(' did=%d' % obj.did)
	sys.stdout.write(' status=%d' % obj.status)
	sys.stdout.write('\n')
def DUMP_BT_AV_ADD_NOW_PLAYING_REQ(obj):
	sys.stdout.write('BT_AV_ADD_NOW_PLAYING_REQ')
	sys.stdout.write(' did=%d' % obj.did)
	sys.stdout.write(' scope=%d' % obj.scope)
	sys.stdout.write(' uidHigh=%d' % obj.uidhigh)
	sys.stdout.write(' uidLow=%d' % obj.uidlow)
	sys.stdout.write(' uid_counter=%d' % obj.uid_counter)
	sys.stdout.write('\n')
def DUMP_BT_AV_ADD_NOW_PLAYING_CFM(obj):
	sys.stdout.write('BT_AV_ADD_NOW_PLAYING_CFM')
	sys.stdout.write(' did=%d' % obj.did)
	sys.stdout.write(' status=%d' % obj.status)
	sys.stdout.write('\n')
def DUMP_BT_AV_SET_BROWSED_PLAYER_REQ(obj):
	sys.stdout.write('BT_AV_SET_BROWSED_PLAYER_REQ')
	sys.stdout.write(' did=%d' % obj.did)
	sys.stdout.write(' pid=%d' % obj.pid)
	sys.stdout.write('\n')
def DUMP_BT_AV_SET_BROWSED_PLAYER_CFM(obj):
	sys.stdout.write('BT_AV_SET_BROWSED_PLAYER_CFM')
	sys.stdout.write(' did=%d' % obj.did)
	sys.stdout.write(' status=%d' % obj.status)
	sys.stdout.write(' uid_counter =%d' % obj.uid_counter )
	sys.stdout.write(' num_items=%d' % obj.num_items)
	sys.stdout.write(' folder_depth=%d' % obj.folder_depth)
	sys.stdout.write(' nameLen=%d' % obj.namelen)
	sys.stdout.write(' name=%s' % obj.name)
	sys.stdout.write('\n')
def DUMP_BT_AV_CHANGE_PATH_REQ(obj):
	sys.stdout.write('BT_AV_CHANGE_PATH_REQ')
	sys.stdout.write(' did=%d' % obj.did)
	sys.stdout.write(' direction=%d' % obj.direction)
	sys.stdout.write(' uidHigh=%d' % obj.uidhigh)
	sys.stdout.write(' folder_uid_low=%d' % obj.folder_uid_low)
	sys.stdout.write(' uid_counter=%d' % obj.uid_counter)
	sys.stdout.write('\n')
def DUMP_BT_AV_CHANGE_PATH_CFM(obj):
	sys.stdout.write('BT_AV_CHANGE_PATH_CFM')
	sys.stdout.write(' did=%d' % obj.did)
	sys.stdout.write(' status=%d' % obj.status)
	sys.stdout.write(' num_items=%d' % obj.num_items)
	sys.stdout.write('\n')
def DUMP_BT_AV_GET_ITEM_ATT_REQ(obj):
	sys.stdout.write('BT_AV_GET_ITEM_ATT_REQ')
	sys.stdout.write(' did=%d' % obj.did)
	sys.stdout.write(' scope=%d' % obj.scope)
	sys.stdout.write(' uidHigh=%d' % obj.uidhigh)
	sys.stdout.write(' uidLow=%d' % obj.uidlow)
	sys.stdout.write(' uid_counter=%d' % obj.uid_counter)
	sys.stdout.write(' attributes=%d' % obj.attributes)
	sys.stdout.write('\n')
def DUMP_BT_AV_GET_ITEM_ATT_CFM(obj):
	sys.stdout.write('BT_AV_GET_ITEM_ATT_CFM')
	sys.stdout.write(' did=%d' % obj.did)
	sys.stdout.write(' status=%d' % obj.status)
	sys.stdout.write(' num_attribute=%d' % obj.num_attribute)
	sys.stdout.write('\n')
def DUMP_BT_AV_BROWSE_ITEM_ATTRIBUTES_DATA_IND(obj):
	sys.stdout.write('BT_AV_BROWSE_ITEM_ATTRIBUTES_DATA_IND')
	sys.stdout.write(' did=%d' % obj.did)
	sys.stdout.write(' attributeId=%d' % obj.attributeid)
	sys.stdout.write(' charset=%d' % obj.charset)
	sys.stdout.write(' itemLen=%d' % obj.itemlen)
	sys.stdout.write(' item=%s' % obj.item)
	sys.stdout.write('\n')
def DUMP_BT_AV_BROWSE_ITEM_ATTRIBUTES_DATA_COMP_IND(obj):
	sys.stdout.write('BT_AV_BROWSE_ITEM_ATTRIBUTES_DATA_COMP_IND')
	sys.stdout.write(' did=%d' % obj.did)
	sys.stdout.write(' status=%d' % obj.status)
	sys.stdout.write('\n')
def DUMP_BT_AV_GET_FOLDER_ITEM_REQ(obj):
	sys.stdout.write('BT_AV_GET_FOLDER_ITEM_REQ')
	sys.stdout.write(' did=%d' % obj.did)
	sys.stdout.write(' scope=%d' % obj.scope)
	sys.stdout.write(' start=%d' % obj.start)
	sys.stdout.write(' end=%d' % obj.end)
	sys.stdout.write(' attributeMask=%d' % obj.attributemask)
	sys.stdout.write('\n')
def DUMP_BT_AV_GET_FOLDER_ITEM_CFM(obj):
	sys.stdout.write('BT_AV_GET_FOLDER_ITEM_CFM')
	sys.stdout.write(' did=%d' % obj.did)
	sys.stdout.write(' status=%d' % obj.status)
	sys.stdout.write(' uid_counter=%d' % obj.uid_counter)
	sys.stdout.write(' num_items=%d' % obj.num_items)
	sys.stdout.write('\n')
def DUMP_BT_AV_BROWSE_PLAYER_ITEM_DATA_IND(obj):
	sys.stdout.write('BT_AV_BROWSE_PLAYER_ITEM_DATA_IND')
	sys.stdout.write(' did=%d' % obj.did)
	sys.stdout.write(' playerId=%d' % obj.playerid)
	sys.stdout.write(' majorType=%d' % obj.majortype)
	sys.stdout.write(' subType=%d' % obj.subtype)
	sys.stdout.write(' playbackStatus=%d' % obj.playbackstatus)
	sys.stdout.write(' featureMask1=%d' % obj.featuremask1)
	sys.stdout.write(' featureMask2=%d' % obj.featuremask2)
	sys.stdout.write(' featureMask3=%d' % obj.featuremask3)
	sys.stdout.write(' featureMask4=%d' % obj.featuremask4)
	sys.stdout.write(' charset=%d' % obj.charset)
	sys.stdout.write(' playerNameLen=%d' % obj.playernamelen)
	sys.stdout.write(' playerName=%s' % obj.playername)
	sys.stdout.write('\n')
def DUMP_BT_AV_BROWSE_FOLDER_ITEM_DATA_IND(obj):
	sys.stdout.write('BT_AV_BROWSE_FOLDER_ITEM_DATA_IND')
	sys.stdout.write(' did=%d' % obj.did)
	sys.stdout.write(' folderUidHigh=%d' % obj.folderuidhigh)
	sys.stdout.write(' folderUidLow=%d' % obj.folderuidlow)
	sys.stdout.write(' folderType=%d' % obj.foldertype)
	sys.stdout.write(' playableType=%d' % obj.playabletype)
	sys.stdout.write(' charset=%d' % obj.charset)
	sys.stdout.write(' folderNameLen=%d' % obj.foldernamelen)
	sys.stdout.write(' folderName=%s' % obj.foldername)
	sys.stdout.write('\n')
def DUMP_BT_AV_BROWSE_MEDIA_ITEM_DATA_IND(obj):
	sys.stdout.write('BT_AV_BROWSE_MEDIA_ITEM_DATA_IND')
	sys.stdout.write(' did=%d' % obj.did)
	sys.stdout.write(' mediaUidHigh=%d' % obj.mediauidhigh)
	sys.stdout.write(' mediaUidLow=%d' % obj.mediauidlow)
	sys.stdout.write(' mediaType=%d' % obj.mediatype)
	sys.stdout.write(' charset=%d' % obj.charset)
	sys.stdout.write(' mediaNameLen=%d' % obj.medianamelen)
	sys.stdout.write(' mediaName=%s' % obj.medianame)
	sys.stdout.write('\n')
def DUMP_BT_AV_BROWSE_ITEM_DATA_COMP_IND(obj):
	sys.stdout.write('BT_AV_BROWSE_ITEM_DATA_COMP_IND')
	sys.stdout.write(' did=%d' % obj.did)
	sys.stdout.write(' status=%d' % obj.status)
	sys.stdout.write('\n')
def DUMP_BT_AV_SEARCH_REQ(obj):
	sys.stdout.write('BT_AV_SEARCH_REQ')
	sys.stdout.write(' did=%d' % obj.did)
	sys.stdout.write(' size=%d' % obj.size)
	sys.stdout.write(' str=%s' % obj.str)
	sys.stdout.write('\n')
def DUMP_BT_AV_SEARCH_CFM(obj):
	sys.stdout.write('BT_AV_SEARCH_CFM')
	sys.stdout.write(' did=%d' % obj.did)
	sys.stdout.write(' status=%d' % obj.status)
	sys.stdout.write(' uid_counter =%d' % obj.uid_counter )
	sys.stdout.write(' num_items=%d' % obj.num_items)
	sys.stdout.write('\n')
def DUMP_BT_AV_GET_BROWSE_XML_STREAM_REQ(obj):
	sys.stdout.write('BT_AV_GET_BROWSE_XML_STREAM_REQ')
	sys.stdout.write(' did=%d' % obj.did)
	sys.stdout.write('\n')
def DUMP_BT_AV_GET_BROWSE_XML_STREAM_CFM(obj):
	sys.stdout.write('BT_AV_GET_BROWSE_XML_STREAM_CFM')
	sys.stdout.write(' did=%d' % obj.did)
	sys.stdout.write(' status=%d' % obj.status)
	sys.stdout.write(' length =%d' % obj.length )
	sys.stdout.write(' stream=%s' % obj.stream)
	sys.stdout.write('\n')
def DUMP_BT_AV_PLAYER_STATUS_CHANGE_NOTI_IND(obj):
	sys.stdout.write('BT_AV_PLAYER_STATUS_CHANGE_NOTI_IND')
	sys.stdout.write(' did=%d' % obj.did)
	sys.stdout.write(' playbackstatus=%d' % obj.playbackstatus)
	sys.stdout.write('\n')
def DUMP_BT_AV_TRACK_CHANGE_NOTI_IND(obj):
	sys.stdout.write('BT_AV_TRACK_CHANGE_NOTI_IND')
	sys.stdout.write(' did=%d' % obj.did)
	sys.stdout.write(' track_index_high=%d' % obj.track_index_high)
	sys.stdout.write(' track_index_low=%d' % obj.track_index_low)
	sys.stdout.write('\n')
def DUMP_BT_AV_REACHED_END_NOTI_IND(obj):
	sys.stdout.write('BT_AV_REACHED_END_NOTI_IND')
	sys.stdout.write(' did=%d' % obj.did)
	sys.stdout.write('\n')
def DUMP_BT_AV_REACHED_START_NOTI_IND(obj):
	sys.stdout.write('BT_AV_REACHED_START_NOTI_IND')
	sys.stdout.write(' did=%d' % obj.did)
	sys.stdout.write('\n')
def DUMP_BT_AV_PLAYBACK_POSITION_CHANGE_NOTI_IND(obj):
	sys.stdout.write('BT_AV_PLAYBACK_POSITION_CHANGE_NOTI_IND')
	sys.stdout.write(' did=%d' % obj.did)
	sys.stdout.write(' playback_pos=%d' % obj.playback_pos)
	sys.stdout.write('\n')
def DUMP_BT_AV_BATTERY_STATUS_CHANGE_NOTI_IND(obj):
	sys.stdout.write('BT_AV_BATTERY_STATUS_CHANGE_NOTI_IND')
	sys.stdout.write(' did=%d' % obj.did)
	sys.stdout.write(' battery_status=%d' % obj.battery_status)
	sys.stdout.write('\n')
def DUMP_BT_AV_SYSTEM_STATUS_CHANGE_NOTI_IND(obj):
	sys.stdout.write('BT_AV_SYSTEM_STATUS_CHANGE_NOTI_IND')
	sys.stdout.write(' did=%d' % obj.did)
	sys.stdout.write(' systemStatus=%d' % obj.systemstatus)
	sys.stdout.write('\n')
def DUMP_BT_AV_PLAYING_CONTENT_CHANGE_NOTI_IND(obj):
	sys.stdout.write('BT_AV_PLAYING_CONTENT_CHANGE_NOTI_IND')
	sys.stdout.write(' did=%d' % obj.did)
	sys.stdout.write('\n')
def DUMP_BT_AV_AVAILABLE_PLAYER_CHANGE_NOTI_IND(obj):
	sys.stdout.write('BT_AV_AVAILABLE_PLAYER_CHANGE_NOTI_IND')
	sys.stdout.write(' did=%d' % obj.did)
	sys.stdout.write('\n')
def DUMP_BT_AV_ADDRESSED_PLAYER_CHANGE_NOTI_IND(obj):
	sys.stdout.write('BT_AV_ADDRESSED_PLAYER_CHANGE_NOTI_IND')
	sys.stdout.write(' did=%d' % obj.did)
	sys.stdout.write(' player_id=%d' % obj.player_id)
	sys.stdout.write(' uid_counter=%d' % obj.uid_counter)
	sys.stdout.write('\n')
def DUMP_BT_AV_UID_CHANGE_NOTI_IND(obj):
	sys.stdout.write('BT_AV_UID_CHANGE_NOTI_IND')
	sys.stdout.write(' did=%d' % obj.did)
	sys.stdout.write(' uid_counter=%d' % obj.uid_counter)
	sys.stdout.write('\n')
def DUMP_BT_AV_VOLUME_CHANGE_NOTI_IND(obj):
	sys.stdout.write('BT_AV_VOLUME_CHANGE_NOTI_IND')
	sys.stdout.write(' did=%d' % obj.did)
	sys.stdout.write(' volume=%d' % obj.volume)
	sys.stdout.write('\n')
def DUMP_BT_AVP_FID_EVT_PLAYER_APP_SETTING_CHANGED_IND(obj):
	sys.stdout.write('BT_AVP_FID_EVT_PLAYER_APP_SETTING_CHANGED_IND')
	sys.stdout.write(' did=%d' % obj.did)
	sys.stdout.write(' number_of_attributes=%d' % obj.number_of_attributes)
	sys.stdout.write(' size=%d' % obj.size)
	sys.stdout.write(' attribute=%s' % obj.attribute)
	sys.stdout.write('\n')
def DUMP_BT_AV_A2DP_CONFIGURATION_IND(obj):
	sys.stdout.write('BT_AV_A2DP_CONFIGURATION_IND')
	sys.stdout.write(' channels=%d' % obj.channels)
	sys.stdout.write(' sample_bit=%d' % obj.sample_bit)
	sys.stdout.write(' sample_frep=%d' % obj.sample_frep)
	sys.stdout.write('\n')
def DUMP_BT_AV_A2DP_STREAM_DATA_IND(obj):
	sys.stdout.write('BT_AV_A2DP_STREAM_DATA_IND')
	sys.stdout.write(' pcmData=%s' % obj.pcmdata)
	sys.stdout.write(' pcmLength=%d' % obj.pcmlength)
	sys.stdout.write('\n')
def DUMP_BT_PBDL_ATCMD_START_SERVICE_REQ(obj):
	sys.stdout.write('BT_PBDL_ATCMD_START_SERVICE_REQ')
	sys.stdout.write(' deviceid=%d' % obj.deviceid)
	sys.stdout.write(' serviceid=%d' % obj.serviceid)
	sys.stdout.write('\n')
def DUMP_BT_PBDL_ATCMD_START_SERVICE_CFM(obj):
	sys.stdout.write('BT_PBDL_ATCMD_START_SERVICE_CFM')
	sys.stdout.write(' status=%d' % obj.status)
	sys.stdout.write(' did=%d' % obj.did)
	sys.stdout.write(' serviceid=%d' % obj.serviceid)
	sys.stdout.write('\n')
def DUMP_BT_PBDL_ATCMD_GET_STORAGE_REQ(obj):
	sys.stdout.write('BT_PBDL_ATCMD_GET_STORAGE_REQ')
	sys.stdout.write(' did=%d' % obj.did)
	sys.stdout.write('\n')
def DUMP_BT_PBDL_ATCMD_GET_STORAGE_CFM(obj):
	sys.stdout.write('BT_PBDL_ATCMD_GET_STORAGE_CFM')
	sys.stdout.write(' status=%d' % obj.status)
	sys.stdout.write(' did=%d' % obj.did)
	sys.stdout.write(' storages=%d' % obj.storages)
	sys.stdout.write('\n')
def DUMP_BT_PBDL_ATCMD_GET_CURRENT_STORAGE_REQ(obj):
	sys.stdout.write('BT_PBDL_ATCMD_GET_CURRENT_STORAGE_REQ')
	sys.stdout.write(' did=%d' % obj.did)
	sys.stdout.write('\n')
def DUMP_BT_PBDL_ATCMD_GET_CURRENT_STORAGE_CFM(obj):
	sys.stdout.write('BT_PBDL_ATCMD_GET_CURRENT_STORAGE_CFM')
	sys.stdout.write(' status=%d' % obj.status)
	sys.stdout.write(' did=%d' % obj.did)
	sys.stdout.write(' storages=%d' % obj.storages)
	sys.stdout.write(' used=%d' % obj.used)
	sys.stdout.write(' total=%d' % obj.total)
	sys.stdout.write('\n')
def DUMP_BT_PBDL_ATCMD_SET_STORAGE_REQ(obj):
	sys.stdout.write('BT_PBDL_ATCMD_SET_STORAGE_REQ')
	sys.stdout.write(' did=%d' % obj.did)
	sys.stdout.write(' Storage=%d' % obj.storage)
	sys.stdout.write('\n')
def DUMP_BT_PBDL_ATCMD_SET_STORAGE_CFM(obj):
	sys.stdout.write('BT_PBDL_ATCMD_SET_STORAGE_CFM')
	sys.stdout.write(' status=%d' % obj.status)
	sys.stdout.write(' did=%d' % obj.did)
	sys.stdout.write('\n')
def DUMP_BT_PBDL_ATCMD_READ_PB_ENTRY_REQ(obj):
	sys.stdout.write('BT_PBDL_ATCMD_READ_PB_ENTRY_REQ')
	sys.stdout.write(' did=%d' % obj.did)
	sys.stdout.write(' Start_index=%d' % obj.start_index)
	sys.stdout.write(' End_index=%d' % obj.end_index)
	sys.stdout.write('\n')
def DUMP_BT_PBDL_ATCMD_READ_PB_ENTRY_CFM(obj):
	sys.stdout.write('BT_PBDL_ATCMD_READ_PB_ENTRY_CFM')
	sys.stdout.write(' status=%d' % obj.status)
	sys.stdout.write(' did=%d' % obj.did)
	sys.stdout.write('\n')
def DUMP_BT_PBDL_ATCMD_FIND_PB_ENTRY_REQ(obj):
	sys.stdout.write('BT_PBDL_ATCMD_FIND_PB_ENTRY_REQ')
	sys.stdout.write(' did=%d' % obj.did)
	sys.stdout.write(' textLen=%d' % obj.textlen)
	sys.stdout.write(' text=%s' % obj.text)
	sys.stdout.write('\n')
def DUMP_BT_PBDL_ATCMD_FIND_PB_ENTRY_CFM(obj):
	sys.stdout.write('BT_PBDL_ATCMD_FIND_PB_ENTRY_CFM')
	sys.stdout.write(' status=%d' % obj.status)
	sys.stdout.write(' did=%d' % obj.did)
	sys.stdout.write('\n')
def DUMP_BT_PBDL_ATCMD_ENTRY_DATA_ABORT_REQ(obj):
	sys.stdout.write('BT_PBDL_ATCMD_ENTRY_DATA_ABORT_REQ')
	sys.stdout.write(' did=%d' % obj.did)
	sys.stdout.write('\n')
def DUMP_BT_PBDL_ATCMD_ENTRY_DATA_ABORT_CFM(obj):
	sys.stdout.write('BT_PBDL_ATCMD_ENTRY_DATA_ABORT_CFM')
	sys.stdout.write(' status=%d' % obj.status)
	sys.stdout.write(' did=%d' % obj.did)
	sys.stdout.write('\n')
def DUMP_BT_PBDL_ATCMD_PB_ENTRY_DATA_IND(obj):
	sys.stdout.write('BT_PBDL_ATCMD_PB_ENTRY_DATA_IND')
	sys.stdout.write(' did=%d' % obj.did)
	sys.stdout.write(' Index=%d' % obj.index)
	sys.stdout.write(' number_len=%d' % obj.number_len)
	sys.stdout.write(' number=%s' % obj.number)
	sys.stdout.write(' type=%d' % obj.type)
	sys.stdout.write(' name_len=%d' % obj.name_len)
	sys.stdout.write(' name=%s' % obj.name)
	sys.stdout.write('\n')
def DUMP_BT_PBDL_ATCMD_PB_ENTRY_DATA_COMPLETE_IND(obj):
	sys.stdout.write('BT_PBDL_ATCMD_PB_ENTRY_DATA_COMPLETE_IND')
	sys.stdout.write(' status=%d' % obj.status)
	sys.stdout.write(' did=%d' % obj.did)
	sys.stdout.write('\n')
def DUMP_BT_PBDL_ATCMD_CONNECTION_IND(obj):
	sys.stdout.write('BT_PBDL_ATCMD_CONNECTION_IND')
	sys.stdout.write(' did=%d' % obj.did)
	sys.stdout.write(' addr=%s' % obj.addr)
	sys.stdout.write('\n')
def DUMP_BT_PBDL_ATCMD_DISCONNECTION_IND(obj):
	sys.stdout.write('BT_PBDL_ATCMD_DISCONNECTION_IND')
	sys.stdout.write(' did=%d' % obj.did)
	sys.stdout.write(' addr=%s' % obj.addr)
	sys.stdout.write('\n')
def DUMP_BT_PBDL_PBAP_SET_FOLDER_REQ(obj):
	sys.stdout.write('BT_PBDL_PBAP_SET_FOLDER_REQ')
	sys.stdout.write(' repository=%d' % obj.repository)
	sys.stdout.write(' phonebook=%d' % obj.phonebook)
	sys.stdout.write('\n')
def DUMP_BT_PBDL_PBAP_SET_FOLDER_CFM(obj):
	sys.stdout.write('BT_PBDL_PBAP_SET_FOLDER_CFM')
	sys.stdout.write(' status=%d' % obj.status)
	sys.stdout.write('\n')
def DUMP_BT_PBDL_PBAP_GET_PBSIZE_REQ(obj):
	sys.stdout.write('BT_PBDL_PBAP_GET_PBSIZE_REQ')
	sys.stdout.write(' repository=%d' % obj.repository)
	sys.stdout.write(' phonebook=%d' % obj.phonebook)
	sys.stdout.write('\n')
def DUMP_BT_PBDL_PBAP_GET_PBSIZE_CFM(obj):
	sys.stdout.write('BT_PBDL_PBAP_GET_PBSIZE_CFM')
	sys.stdout.write(' status=%d' % obj.status)
	sys.stdout.write(' pbookSize=%d' % obj.pbooksize)
	sys.stdout.write(' newMissCalls=%d' % obj.newmisscalls)
	sys.stdout.write('\n')
def DUMP_BT_PBDL_PBAP_PULL_PB_REQ(obj):
	sys.stdout.write('BT_PBDL_PBAP_PULL_PB_REQ')
	sys.stdout.write(' repository=%d' % obj.repository)
	sys.stdout.write(' phonebook=%d' % obj.phonebook)
	sys.stdout.write(' ver=%d' % obj.ver)
	sys.stdout.write(' filter_lo=%d' % obj.filter_lo)
	sys.stdout.write(' filter_hi=%d' % obj.filter_hi)
	sys.stdout.write(' start_list=%d' % obj.start_list)
	sys.stdout.write(' max_list=%d' % obj.max_list)
	sys.stdout.write('\n')
def DUMP_BT_PBDL_PBAP_PULL_PB_CFM(obj):
	sys.stdout.write('BT_PBDL_PBAP_PULL_PB_CFM')
	sys.stdout.write(' status=%d' % obj.status)
	sys.stdout.write('\n')
def DUMP_BT_PBDL_PBAP_PULL_VCARD_LIST_REQ(obj):
	sys.stdout.write('BT_PBDL_PBAP_PULL_VCARD_LIST_REQ')
	sys.stdout.write(' order=%d' % obj.order)
	sys.stdout.write(' srchAttr=%d' % obj.srchattr)
	sys.stdout.write(' srchValLen=%d' % obj.srchvallen)
	sys.stdout.write(' SearchValue=%s' % obj.searchvalue)
	sys.stdout.write(' start_list=%d' % obj.start_list)
	sys.stdout.write(' max_list=%d' % obj.max_list)
	sys.stdout.write('\n')
def DUMP_BT_PBDL_PBAP_PULL_VCARD_LIST_CFM(obj):
	sys.stdout.write('BT_PBDL_PBAP_PULL_VCARD_LIST_CFM')
	sys.stdout.write(' status=%d' % obj.status)
	sys.stdout.write('\n')
def DUMP_BT_PBDL_PBAP_PULL_VCARD_ENTRY_REQ(obj):
	sys.stdout.write('BT_PBDL_PBAP_PULL_VCARD_ENTRY_REQ')
	sys.stdout.write(' entry=%d' % obj.entry)
	sys.stdout.write(' filter_lo=%d' % obj.filter_lo)
	sys.stdout.write(' filter_hi=%d' % obj.filter_hi)
	sys.stdout.write(' ver=%d' % obj.ver)
	sys.stdout.write('\n')
def DUMP_BT_PBDL_PBAP_PULL_VCARD_ENTRY_CFM(obj):
	sys.stdout.write('BT_PBDL_PBAP_PULL_VCARD_ENTRY_CFM')
	sys.stdout.write(' status=%d' % obj.status)
	sys.stdout.write('\n')
def DUMP_BT_PBDL_PBAP_PB_ENTRY_DATA_IND(obj):
	sys.stdout.write('BT_PBDL_PBAP_PB_ENTRY_DATA_IND')
	sys.stdout.write(' length=%d' % obj.length)
	sys.stdout.write(' body=%s' % obj.body)
	sys.stdout.write('\n')
def DUMP_BT_PBDL_PBAP_PB_ENTRY_DATA_COMPLETE_IND(obj):
	sys.stdout.write('BT_PBDL_PBAP_PB_ENTRY_DATA_COMPLETE_IND')
	sys.stdout.write(' status=%d' % obj.status)
	sys.stdout.write(' pbSize=%d' % obj.pbsize)
	sys.stdout.write(' newMissedCall=%d' % obj.newmissedcall)
	sys.stdout.write('\n')
def DUMP_BT_PBDL_PBAP_VCARD_LIST_DATA_IND(obj):
	sys.stdout.write('BT_PBDL_PBAP_VCARD_LIST_DATA_IND')
	sys.stdout.write(' length=%d' % obj.length)
	sys.stdout.write(' body=%s' % obj.body)
	sys.stdout.write('\n')
def DUMP_BT_PBDL_PBAP_VCARD_LIST_DATA_COMPLETE_IND(obj):
	sys.stdout.write('BT_PBDL_PBAP_VCARD_LIST_DATA_COMPLETE_IND')
	sys.stdout.write(' status=%d' % obj.status)
	sys.stdout.write(' pbSize=%d' % obj.pbsize)
	sys.stdout.write(' newMissedCall=%d' % obj.newmissedcall)
	sys.stdout.write('\n')
def DUMP_BT_PBDL_PBAP_VCARD_ENTRY_DATA_IND(obj):
	sys.stdout.write('BT_PBDL_PBAP_VCARD_ENTRY_DATA_IND')
	sys.stdout.write(' length=%d' % obj.length)
	sys.stdout.write(' body=%s' % obj.body)
	sys.stdout.write('\n')
def DUMP_BT_PBDL_PBAP_VCARD_ENTRY_DATA_COMPLETE_IND(obj):
	sys.stdout.write('BT_PBDL_PBAP_VCARD_ENTRY_DATA_COMPLETE_IND')
	sys.stdout.write(' status=%d' % obj.status)
	sys.stdout.write('\n')
def DUMP_BT_PBDL_PBAP_PULL_ABORT_REQ(obj):
	sys.stdout.write('BT_PBDL_PBAP_PULL_ABORT_REQ')
	sys.stdout.write('\n')
def DUMP_BT_PBDL_PBAP_PULL_ABORT_CFM(obj):
	sys.stdout.write('BT_PBDL_PBAP_PULL_ABORT_CFM')
	sys.stdout.write(' status=%d' % obj.status)
	sys.stdout.write('\n')
def DUMP_BT_PBDL_OPPS_PUT_FILE_IND(obj):
	sys.stdout.write('BT_PBDL_OPPS_PUT_FILE_IND')
	sys.stdout.write(' nameLength=%d' % obj.namelength)
	sys.stdout.write(' name=%s' % obj.name)
	sys.stdout.write(' type=%d' % obj.type)
	sys.stdout.write(' objectLength=%d' % obj.objectlength)
	sys.stdout.write('\n')
def DUMP_BT_PBDL_OPPS_PUT_BODY_IND(obj):
	sys.stdout.write('BT_PBDL_OPPS_PUT_BODY_IND')
	sys.stdout.write(' length=%d' % obj.length)
	sys.stdout.write(' body=%s' % obj.body)
	sys.stdout.write('\n')
def DUMP_BT_PBDL_OPPS_PUT_COMPLETE_IND(obj):
	sys.stdout.write('BT_PBDL_OPPS_PUT_COMPLETE_IND')
	sys.stdout.write(' status=%d' % obj.status)
	sys.stdout.write('\n')
def DUMP_BT_PBDL_OPPS_PUT_ABORT_IND(obj):
	sys.stdout.write('BT_PBDL_OPPS_PUT_ABORT_IND')
	sys.stdout.write(' status=%d' % obj.status)
	sys.stdout.write('\n')
def DUMP_BT_PBDL_OPPS_PUT_ABORT_REQ(obj):
	sys.stdout.write('BT_PBDL_OPPS_PUT_ABORT_REQ')
	sys.stdout.write('\n')
def DUMP_BT_PBDL_OPPS_PUT_ABORT_CFM(obj):
	sys.stdout.write('BT_PBDL_OPPS_PUT_ABORT_CFM')
	sys.stdout.write(' status=%d' % obj.status)
	sys.stdout.write('\n')
def DUMP_BT_PBDL_PULL_PB_REQ(obj):
	sys.stdout.write('BT_PBDL_PULL_PB_REQ')
	sys.stdout.write('\n')
def DUMP_BT_PBDL_PULL_PB_CFM(obj):
	sys.stdout.write('BT_PBDL_PULL_PB_CFM')
	sys.stdout.write(' status=%d' % obj.status)
	sys.stdout.write('\n')
def DUMP_BT_PBDL_PULL_PB_CMP_IND(obj):
	sys.stdout.write('BT_PBDL_PULL_PB_CMP_IND')
	sys.stdout.write(' status=%d' % obj.status)
	sys.stdout.write('\n')
def DUMP_BT_MAP_GET_DEVICE_LIST_REQ(obj):
	sys.stdout.write('BT_MAP_GET_DEVICE_LIST_REQ')
	sys.stdout.write('\n')
def DUMP_BT_MAP_GET_DEVICE_LIST_CFM(obj):
	sys.stdout.write('BT_MAP_GET_DEVICE_LIST_CFM')
	sys.stdout.write(' status=%d' % obj.status)
	sys.stdout.write(' addr=%s' % obj.addr)
	sys.stdout.write(' masInstId=%d' % obj.masinstid)
	sys.stdout.write(' mapcInstId=%d' % obj.mapcinstid)
	sys.stdout.write('\n')
def DUMP_BT_MAP_GET_SDP_RECORD_REQ(obj):
	sys.stdout.write('BT_MAP_GET_SDP_RECORD_REQ')
	sys.stdout.write(' addr=%s' % obj.addr)
	sys.stdout.write('\n')
def DUMP_BT_MAP_GET_SDP_RECORD_CFM(obj):
	sys.stdout.write('BT_MAP_GET_SDP_RECORD_CFM')
	sys.stdout.write(' status=%d' % obj.status)
	sys.stdout.write('\n')
def DUMP_BT_MAP_GET_SDP_RECORD_IND(obj):
	sys.stdout.write('BT_MAP_GET_SDP_RECORD_IND')
	sys.stdout.write(' InstanceId=%d' % obj.instanceid)
	sys.stdout.write(' len=%d' % obj.len)
	sys.stdout.write(' serviceName=%s' % obj.servicename)
	sys.stdout.write(' supportedMessage=%d' % obj.supportedmessage)
	sys.stdout.write('\n')
def DUMP_BT_MAP_SDP_RECORD_COMPLETE_IND(obj):
	sys.stdout.write('BT_MAP_SDP_RECORD_COMPLETE_IND')
	sys.stdout.write(' status=%d' % obj.status)
	sys.stdout.write('\n')
def DUMP_BT_MAP_ESTABLIST_CONNECTION_REQ(obj):
	sys.stdout.write('BT_MAP_ESTABLIST_CONNECTION_REQ')
	sys.stdout.write(' addr=%s' % obj.addr)
	sys.stdout.write(' masInstId=%d' % obj.masinstid)
	sys.stdout.write('\n')
def DUMP_BT_MAP_ESTABLIST_CONNECTION_CFM(obj):
	sys.stdout.write('BT_MAP_ESTABLIST_CONNECTION_CFM')
	sys.stdout.write(' status=%d' % obj.status)
	sys.stdout.write(' addr=%s' % obj.addr)
	sys.stdout.write(' masInstId=%d' % obj.masinstid)
	sys.stdout.write(' mapcInstId=%d' % obj.mapcinstid)
	sys.stdout.write('\n')
def DUMP_BT_MAP_DESTROY_CONNECTION_REQ(obj):
	sys.stdout.write('BT_MAP_DESTROY_CONNECTION_REQ')
	sys.stdout.write(' mapcInst=%d' % obj.mapcinst)
	sys.stdout.write('\n')
def DUMP_BT_MAP_DESTROY_CONNECTION_CFM(obj):
	sys.stdout.write('BT_MAP_DESTROY_CONNECTION_CFM')
	sys.stdout.write(' mapcInst=%d' % obj.mapcinst)
	sys.stdout.write(' status=%d' % obj.status)
	sys.stdout.write('\n')
def DUMP_BT_MAP_SET_FLODER_REQ(obj):
	sys.stdout.write('BT_MAP_SET_FLODER_REQ')
	sys.stdout.write(' mapcInst=%d' % obj.mapcinst)
	sys.stdout.write(' length=%d' % obj.length)
	sys.stdout.write(' name=%s' % obj.name)
	sys.stdout.write('\n')
def DUMP_BT_MAP_SET_FLODER_BACK_REQ(obj):
	sys.stdout.write('BT_MAP_SET_FLODER_BACK_REQ')
	sys.stdout.write(' mapcInst=%d' % obj.mapcinst)
	sys.stdout.write('\n')
def DUMP_BT_MAP_SET_FLODER_ROOT_REQ(obj):
	sys.stdout.write('BT_MAP_SET_FLODER_ROOT_REQ')
	sys.stdout.write(' mapcInst=%d' % obj.mapcinst)
	sys.stdout.write('\n')
def DUMP_BT_MAP_SET_FLODER_CFM(obj):
	sys.stdout.write('BT_MAP_SET_FLODER_CFM')
	sys.stdout.write(' InstanceId=%d' % obj.instanceid)
	sys.stdout.write(' status=%d' % obj.status)
	sys.stdout.write('\n')
def DUMP_BT_MAP_SET_FLODER_BACK_CFM(obj):
	sys.stdout.write('BT_MAP_SET_FLODER_BACK_CFM')
	sys.stdout.write(' InstanceId=%d' % obj.instanceid)
	sys.stdout.write(' status=%d' % obj.status)
	sys.stdout.write('\n')
def DUMP_BT_MAP_SET_FLODER_ROOT_CFM(obj):
	sys.stdout.write('BT_MAP_SET_FLODER_ROOT_CFM')
	sys.stdout.write(' InstanceId=%d' % obj.instanceid)
	sys.stdout.write(' status=%d' % obj.status)
	sys.stdout.write('\n')
def DUMP_BT_MAP_GET_FLODERLIST_REQ(obj):
	sys.stdout.write('BT_MAP_GET_FLODERLIST_REQ')
	sys.stdout.write(' InstanceId=%d' % obj.instanceid)
	sys.stdout.write(' maxcount=%d' % obj.maxcount)
	sys.stdout.write(' offset=%d' % obj.offset)
	sys.stdout.write('\n')
def DUMP_BT_MAP_GET_FLODERLIST_CFM(obj):
	sys.stdout.write('BT_MAP_GET_FLODERLIST_CFM')
	sys.stdout.write(' mapcInst=%d' % obj.mapcinst)
	sys.stdout.write(' status=%d' % obj.status)
	sys.stdout.write('\n')
def DUMP_BT_MAP_GET_FLODERLIST_IND(obj):
	sys.stdout.write('BT_MAP_GET_FLODERLIST_IND')
	sys.stdout.write(' InstanceId=%d' % obj.instanceid)
	sys.stdout.write(' len=%d' % obj.len)
	sys.stdout.write(' name=%s' % obj.name)
	sys.stdout.write('\n')
def DUMP_BT_MAP_FLODERLIST_COMPLETE_IND(obj):
	sys.stdout.write('BT_MAP_FLODERLIST_COMPLETE_IND')
	sys.stdout.write(' InstanceId=%d' % obj.instanceid)
	sys.stdout.write(' status=%d' % obj.status)
	sys.stdout.write('\n')
def DUMP_BT_MAP_GET_MESSAGELIST_REQ(obj):
	sys.stdout.write('BT_MAP_GET_MESSAGELIST_REQ')
	sys.stdout.write(' mapcInst=%d' % obj.mapcinst)
	sys.stdout.write(' maxcount=%d' % obj.maxcount)
	sys.stdout.write(' offset=%d' % obj.offset)
	sys.stdout.write(' subjectLen=%d' % obj.subjectlen)
	sys.stdout.write(' folderNameLen=%d' % obj.foldernamelen)
	sys.stdout.write(' folderName=%s' % obj.foldername)
	sys.stdout.write(' paramterMask=%d' % obj.paramtermask)
	sys.stdout.write(' filterMessageType=%d' % obj.filtermessagetype)
	sys.stdout.write(' filterPeriodBegin=%s' % obj.filterperiodbegin)
	sys.stdout.write(' filterPeriodEnd=%s' % obj.filterperiodend)
	sys.stdout.write(' filterReadStatus=%d' % obj.filterreadstatus)
	sys.stdout.write(' recipientLen=%d' % obj.recipientlen)
	sys.stdout.write(' filterRecipient=%s' % obj.filterrecipient)
	sys.stdout.write(' originatorLen=%d' % obj.originatorlen)
	sys.stdout.write(' filterOriginator=%s' % obj.filteroriginator)
	sys.stdout.write(' filterPriority=%d' % obj.filterpriority)
	sys.stdout.write('\n')
def DUMP_BT_MAP_GET_MESSAGELIST_CFM(obj):
	sys.stdout.write('BT_MAP_GET_MESSAGELIST_CFM')
	sys.stdout.write(' InstanceId=%d' % obj.instanceid)
	sys.stdout.write(' status=%d' % obj.status)
	sys.stdout.write('\n')
def DUMP_BT_MAP_GET_MESSAGELIST_IND(obj):
	sys.stdout.write('BT_MAP_GET_MESSAGELIST_IND')
	sys.stdout.write(' mapcInst=%d' % obj.mapcinst)
	sys.stdout.write(' len=%d' % obj.len)
	sys.stdout.write(' date=%s' % obj.date)
	sys.stdout.write('\n')
def DUMP_BT_MAP_GET_MESSAGELIST_COMPLETE_IND(obj):
	sys.stdout.write('BT_MAP_GET_MESSAGELIST_COMPLETE_IND')
	sys.stdout.write(' mapcInst=%d' % obj.mapcinst)
	sys.stdout.write(' status=%d' % obj.status)
	sys.stdout.write('\n')
def DUMP_BT_MAP_GET_MESSAGE_REQ(obj):
	sys.stdout.write('BT_MAP_GET_MESSAGE_REQ')
	sys.stdout.write(' instanceId=%d' % obj.instanceid)
	sys.stdout.write(' handlerLen=%d' % obj.handlerlen)
	sys.stdout.write(' handle=%s' % obj.handle)
	sys.stdout.write(' attachment=%d' % obj.attachment)
	sys.stdout.write(' charset=%d' % obj.charset)
	sys.stdout.write(' fractionRequest=%d' % obj.fractionrequest)
	sys.stdout.write('\n')
def DUMP_BT_MAP_GET_MESSAGE_CFM(obj):
	sys.stdout.write('BT_MAP_GET_MESSAGE_CFM')
	sys.stdout.write(' mapcInst=%d' % obj.mapcinst)
	sys.stdout.write(' status=%d' % obj.status)
	sys.stdout.write('\n')
def DUMP_BT_MAP_GET_MESSAGE_IND(obj):
	sys.stdout.write('BT_MAP_GET_MESSAGE_IND')
	sys.stdout.write(' instanceId=%d' % obj.instanceid)
	sys.stdout.write(' len=%d' % obj.len)
	sys.stdout.write(' content=%s' % obj.content)
	sys.stdout.write('\n')
def DUMP_BT_MAP_FID_MESSAGE_COMPLETE_IND(obj):
	sys.stdout.write('BT_MAP_FID_MESSAGE_COMPLETE_IND')
	sys.stdout.write(' status=%d' % obj.status)
	sys.stdout.write('\n')
def DUMP_BT_MAP_SET_MESSAGE_STATUS_REQ(obj):
	sys.stdout.write('BT_MAP_SET_MESSAGE_STATUS_REQ')
	sys.stdout.write(' mapcInst=%d' % obj.mapcinst)
	sys.stdout.write(' value=%d' % obj.value)
	sys.stdout.write(' handlerLen=%d' % obj.handlerlen)
	sys.stdout.write(' handle=%s' % obj.handle)
	sys.stdout.write('\n')
def DUMP_BT_MAP_SET_MESSAGE_STATUS_CFM(obj):
	sys.stdout.write('BT_MAP_SET_MESSAGE_STATUS_CFM')
	sys.stdout.write(' InstanceId=%d' % obj.instanceid)
	sys.stdout.write(' status=%d' % obj.status)
	sys.stdout.write('\n')
def DUMP_BT_MAP_PUT_MESSAGE_REQ(obj):
	sys.stdout.write('BT_MAP_PUT_MESSAGE_REQ')
	sys.stdout.write(' mapcInst=%d' % obj.mapcinst)
	sys.stdout.write(' length=%d' % obj.length)
	sys.stdout.write(' content=%s' % obj.content)
	sys.stdout.write(' transparent=%d' % obj.transparent)
	sys.stdout.write(' retry=%d' % obj.retry)
	sys.stdout.write(' charset=%d' % obj.charset)
	sys.stdout.write('\n')
def DUMP_BT_MAP_PUT_MESSAGE_CFM(obj):
	sys.stdout.write('BT_MAP_PUT_MESSAGE_CFM')
	sys.stdout.write(' instanceId=%d' % obj.instanceid)
	sys.stdout.write(' status=%d' % obj.status)
	sys.stdout.write('\n')
def DUMP_BT_MAP_UPDATE_INBOX_REQ(obj):
	sys.stdout.write('BT_MAP_UPDATE_INBOX_REQ')
	sys.stdout.write(' mapcInst=%d' % obj.mapcinst)
	sys.stdout.write('\n')
def DUMP_BT_MAP_UPDATE_INBOX_CFM(obj):
	sys.stdout.write('BT_MAP_UPDATE_INBOX_CFM')
	sys.stdout.write(' instanceId=%d' % obj.instanceid)
	sys.stdout.write(' status=%d' % obj.status)
	sys.stdout.write('\n')
def DUMP_BT_MAP_REGISTER_NOTIFICATION_REQ(obj):
	sys.stdout.write('BT_MAP_REGISTER_NOTIFICATION_REQ')
	sys.stdout.write(' mapcInst=%d' % obj.mapcinst)
	sys.stdout.write(' status=%d' % obj.status)
	sys.stdout.write('\n')
def DUMP_BT_MAP_REGISTER_NOTIFICATION_CFM(obj):
	sys.stdout.write('BT_MAP_REGISTER_NOTIFICATION_CFM')
	sys.stdout.write(' mapcInst=%d' % obj.mapcinst)
	sys.stdout.write(' status=%d' % obj.status)
	sys.stdout.write('\n')
def DUMP_BT_MAP_MESSAGE_NOTIFICATION_OFF_IND(obj):
	sys.stdout.write('BT_MAP_MESSAGE_NOTIFICATION_OFF_IND')
	sys.stdout.write(' mapcInst=%d' % obj.mapcinst)
	sys.stdout.write('\n')
def DUMP_BT_MAP_MESSAGE_NOTIFICATION_IND(obj):
	sys.stdout.write('BT_MAP_MESSAGE_NOTIFICATION_IND')
	sys.stdout.write(' mapcInst=%d' % obj.mapcinst)
	sys.stdout.write(' type=%d' % obj.type)
	sys.stdout.write(' msgtype=%d' % obj.msgtype)
	sys.stdout.write(' len=%d' % obj.len)
	sys.stdout.write(' handle=%s' % obj.handle)
	sys.stdout.write('\n')
def DUMP_BT_AT_SMS_CONNECTION_IND(obj):
	sys.stdout.write('BT_AT_SMS_CONNECTION_IND')
	sys.stdout.write(' did=%d' % obj.did)
	sys.stdout.write(' addr=%s' % obj.addr)
	sys.stdout.write('\n')
def DUMP_BT_AT_SMS_DISCONNECTION_IND(obj):
	sys.stdout.write('BT_AT_SMS_DISCONNECTION_IND')
	sys.stdout.write(' did=%d' % obj.did)
	sys.stdout.write(' addr=%s' % obj.addr)
	sys.stdout.write('\n')
def DUMP_BT_MSG_SUPPORT_SMS_FORMAT_REQ(obj):
	sys.stdout.write('BT_MSG_SUPPORT_SMS_FORMAT_REQ')
	sys.stdout.write(' did=%d' % obj.did)
	sys.stdout.write('\n')
def DUMP_BT_MSG_SUPPORT_SMS_FORMAT_CFM(obj):
	sys.stdout.write('BT_MSG_SUPPORT_SMS_FORMAT_CFM')
	sys.stdout.write(' did=%d' % obj.did)
	sys.stdout.write(' status=%d' % obj.status)
	sys.stdout.write(' format=%d' % obj.format)
	sys.stdout.write('\n')
def DUMP_BT_MSG_CURRENT_SMS_FORMAT_REQ(obj):
	sys.stdout.write('BT_MSG_CURRENT_SMS_FORMAT_REQ')
	sys.stdout.write(' did=%d' % obj.did)
	sys.stdout.write('\n')
def DUMP_BT_MSG_CURRENT_SMS_FORMAT_CFM(obj):
	sys.stdout.write('BT_MSG_CURRENT_SMS_FORMAT_CFM')
	sys.stdout.write(' did=%d' % obj.did)
	sys.stdout.write(' status=%d' % obj.status)
	sys.stdout.write(' format=%d' % obj.format)
	sys.stdout.write('\n')
def DUMP_BT_MSG_SET_SMS_FORMAT_REQ(obj):
	sys.stdout.write('BT_MSG_SET_SMS_FORMAT_REQ')
	sys.stdout.write(' did=%d' % obj.did)
	sys.stdout.write(' format=%d' % obj.format)
	sys.stdout.write('\n')
def DUMP_BT_MSG_SET_SMS_FORMAT_CFM(obj):
	sys.stdout.write('BT_MSG_SET_SMS_FORMAT_CFM')
	sys.stdout.write(' did=%d' % obj.did)
	sys.stdout.write(' status=%d' % obj.status)
	sys.stdout.write('\n')
def DUMP_BT_MSG_GET_SUPPORT_SMS_STORAGE_REQ(obj):
	sys.stdout.write('BT_MSG_GET_SUPPORT_SMS_STORAGE_REQ')
	sys.stdout.write(' did=%d' % obj.did)
	sys.stdout.write('\n')
def DUMP_BT_MSG_GET_SUPPORT_SMS_STORAGE_CFM(obj):
	sys.stdout.write('BT_MSG_GET_SUPPORT_SMS_STORAGE_CFM')
	sys.stdout.write(' status=%d' % obj.status)
	sys.stdout.write(' did=%d' % obj.did)
	sys.stdout.write(' storage=%d' % obj.storage)
	sys.stdout.write('\n')
def DUMP_BT_MSG_GET_CURRENT_SMS_STORAGE_REQ(obj):
	sys.stdout.write('BT_MSG_GET_CURRENT_SMS_STORAGE_REQ')
	sys.stdout.write(' did=%d' % obj.did)
	sys.stdout.write('\n')
def DUMP_BT_MSG_GET_CURRENT_SMS_STORAGE_CFM(obj):
	sys.stdout.write('BT_MSG_GET_CURRENT_SMS_STORAGE_CFM')
	sys.stdout.write(' status=%d' % obj.status)
	sys.stdout.write(' did=%d' % obj.did)
	sys.stdout.write(' mem1used=%d' % obj.mem1used)
	sys.stdout.write(' mem1total=%d' % obj.mem1total)
	sys.stdout.write(' mem2used=%d' % obj.mem2used)
	sys.stdout.write(' mem2total=%d' % obj.mem2total)
	sys.stdout.write(' mem3used=%d' % obj.mem3used)
	sys.stdout.write(' mem3total=%d' % obj.mem3total)
	sys.stdout.write(' storage=%d' % obj.storage)
	sys.stdout.write('\n')
def DUMP_BT_MSG_SELECT_SMS_STORAGE_REQ(obj):
	sys.stdout.write('BT_MSG_SELECT_SMS_STORAGE_REQ')
	sys.stdout.write(' did=%d' % obj.did)
	sys.stdout.write(' mem1=%d' % obj.mem1)
	sys.stdout.write(' mem2=%d' % obj.mem2)
	sys.stdout.write(' mem3=%d' % obj.mem3)
	sys.stdout.write('\n')
def DUMP_BT_MSG_SELECT_SMS_STORAGE_CFM(obj):
	sys.stdout.write('BT_MSG_SELECT_SMS_STORAGE_CFM')
	sys.stdout.write(' status=%d' % obj.status)
	sys.stdout.write(' did=%d' % obj.did)
	sys.stdout.write(' nem1used=%d' % obj.nem1used)
	sys.stdout.write(' mem1total=%d' % obj.mem1total)
	sys.stdout.write(' mem2used=%d' % obj.mem2used)
	sys.stdout.write(' mem2total=%d' % obj.mem2total)
	sys.stdout.write(' mem3used=%d' % obj.mem3used)
	sys.stdout.write(' mem3total=%d' % obj.mem3total)
	sys.stdout.write('\n')
def DUMP_BT_MSG_GET_SUPPORT_LIST_SMS_REQ(obj):
	sys.stdout.write('BT_MSG_GET_SUPPORT_LIST_SMS_REQ')
	sys.stdout.write(' did=%d' % obj.did)
	sys.stdout.write('\n')
def DUMP_BT_MSG_GET_SUPPORT_LIST_SMS_CFM(obj):
	sys.stdout.write('BT_MSG_GET_SUPPORT_LIST_SMS_CFM')
	sys.stdout.write(' did=%d' % obj.did)
	sys.stdout.write(' status=%d' % obj.status)
	sys.stdout.write(' format=%d' % obj.format)
	sys.stdout.write('\n')
def DUMP_BT_MSG_LIST_SMS_REQ(obj):
	sys.stdout.write('BT_MSG_LIST_SMS_REQ')
	sys.stdout.write(' did=%d' % obj.did)
	sys.stdout.write(' stat=%d' % obj.stat)
	sys.stdout.write('\n')
def DUMP_BT_MSG_LIST_SMS_CFM(obj):
	sys.stdout.write('BT_MSG_LIST_SMS_CFM')
	sys.stdout.write(' did=%d' % obj.did)
	sys.stdout.write(' status=%d' % obj.status)
	sys.stdout.write('\n')
def DUMP_BT_MSG_GET_CONTENT_IND(obj):
	sys.stdout.write('BT_MSG_GET_CONTENT_IND')
	sys.stdout.write(' did=%d' % obj.did)
	sys.stdout.write(' format=%d' % obj.format)
	sys.stdout.write(' addrlen=%d' % obj.addrlen)
	sys.stdout.write(' address=%s' % obj.address)
	sys.stdout.write(' datalen=%d' % obj.datalen)
	sys.stdout.write(' data=%s' % obj.data)
	sys.stdout.write('\n')
def DUMP_BT_MSG_GET_CONTENT_COMPLETED_IND(obj):
	sys.stdout.write('BT_MSG_GET_CONTENT_COMPLETED_IND')
	sys.stdout.write(' did=%d' % obj.did)
	sys.stdout.write(' status=%d' % obj.status)
	sys.stdout.write('\n')
def DUMP_BT_MSG_READ_SMS_REQ(obj):
	sys.stdout.write('BT_MSG_READ_SMS_REQ')
	sys.stdout.write(' did=%d' % obj.did)
	sys.stdout.write(' index=%d' % obj.index)
	sys.stdout.write('\n')
def DUMP_BT_MSG_READ_SMS_CFM(obj):
	sys.stdout.write('BT_MSG_READ_SMS_CFM')
	sys.stdout.write(' did=%d' % obj.did)
	sys.stdout.write(' status=%d' % obj.status)
	sys.stdout.write('\n')
def DUMP_BT_MSG_DELETE_SMS_REQ(obj):
	sys.stdout.write('BT_MSG_DELETE_SMS_REQ')
	sys.stdout.write(' did=%d' % obj.did)
	sys.stdout.write(' index=%d' % obj.index)
	sys.stdout.write('\n')
def DUMP_BT_MSG_DELETE_SMS_CFM(obj):
	sys.stdout.write('BT_MSG_DELETE_SMS_CFM')
	sys.stdout.write(' did=%d' % obj.did)
	sys.stdout.write(' status=%d' % obj.status)
	sys.stdout.write('\n')
def DUMP_BT_MSG_SET_SMS_NOTIFICATION_REQ(obj):
	sys.stdout.write('BT_MSG_SET_SMS_NOTIFICATION_REQ')
	sys.stdout.write(' did=%d' % obj.did)
	sys.stdout.write(' state=%d' % obj.state)
	sys.stdout.write('\n')
def DUMP_BT_MSG_SET_SMS_NOTIFICATION_CFM(obj):
	sys.stdout.write('BT_MSG_SET_SMS_NOTIFICATION_CFM')
	sys.stdout.write(' did=%d' % obj.did)
	sys.stdout.write(' status=%d' % obj.status)
	sys.stdout.write('\n')
def DUMP_BT_MSG_SEND_SMS_REQ(obj):
	sys.stdout.write('BT_MSG_SEND_SMS_REQ')
	sys.stdout.write(' did=%d' % obj.did)
	sys.stdout.write(' addrLen=%d' % obj.addrlen)
	sys.stdout.write(' address=%s' % obj.address)
	sys.stdout.write(' dataLen=%d' % obj.datalen)
	sys.stdout.write(' data=%s' % obj.data)
	sys.stdout.write('\n')
def DUMP_BT_MSG_SEND_SMS_CFM(obj):
	sys.stdout.write('BT_MSG_SEND_SMS_CFM')
	sys.stdout.write(' did=%d' % obj.did)
	sys.stdout.write(' status=%d' % obj.status)
	sys.stdout.write('\n')
def DUMP_BT_HID_CONNECT_REQ(obj):
	sys.stdout.write('BT_HID_CONNECT_REQ')
	sys.stdout.write(' addr=%s' % obj.addr)
	sys.stdout.write('\n')
def DUMP_BT_HID_CONNECT_CFM(obj):
	sys.stdout.write('BT_HID_CONNECT_CFM')
	sys.stdout.write(' status=%d' % obj.status)
	sys.stdout.write('\n')
def DUMP_BT_HID_DISCONNECT_REQ(obj):
	sys.stdout.write('BT_HID_DISCONNECT_REQ')
	sys.stdout.write('\n')
def DUMP_BT_HID_DISCONNECT_CFM(obj):
	sys.stdout.write('BT_HID_DISCONNECT_CFM')
	sys.stdout.write(' status=%d' % obj.status)
	sys.stdout.write('\n')
def DUMP_BT_HID_DATA_REQ(obj):
	sys.stdout.write('BT_HID_DATA_REQ')
	sys.stdout.write(' key=%d' % obj.key)
	sys.stdout.write(' xRef=%d' % obj.xref)
	sys.stdout.write(' yRef=%d' % obj.yref)
	sys.stdout.write(' wheelRef=%d' % obj.wheelref)
	sys.stdout.write('\n')
def DUMP_BT_HID_DATA_CFM(obj):
	sys.stdout.write('BT_HID_DATA_CFM')
	sys.stdout.write(' status=%d' % obj.status)
	sys.stdout.write('\n')
def DUMP_BT_HID_STATUS_IND(obj):
	sys.stdout.write('BT_HID_STATUS_IND')
	sys.stdout.write(' deviceAddr=%s' % obj.deviceaddr)
	sys.stdout.write(' status=%d' % obj.status)
	sys.stdout.write('\n')
