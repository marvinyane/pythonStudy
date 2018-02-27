import bluetec_pb2
def DUMP_BT_GEN_POWER_ON_REQ(obj):
	print('BT_GEN_POWER_ON_REQ')
	print('%s' % obj.local_addr)
def DUMP_BT_GEN_POWER_ON_CFM(obj):
	print('BT_GEN_POWER_ON_CFM')
	print('%d' % obj.status)
	print('%d' % obj.version)
	print('%d' % obj.supportservice)
def DUMP_BT_GEN_POWER_OFF_REQ(obj):
	print('BT_GEN_POWER_OFF_REQ')
def DUMP_BT_GEN_POWER_OFF_CFM(obj):
	print('BT_GEN_POWER_OFF_CFM')
	print('%d' % obj.status)
def DUMP_BT_GEN_GET_LOCAL_STATUS_REQ(obj):
	print('BT_GEN_GET_LOCAL_STATUS_REQ')
	print('%d' % obj.sid)
def DUMP_BT_GEN_GET_LOCAL_STATUS_CFM(obj):
	print('BT_GEN_GET_LOCAL_STATUS_CFM')
	print('%d' % obj.sid)
	print('%s' % obj.data)
def DUMP_BT_GEN_SET_LOCAL_CONFIG_REQ(obj):
	print('BT_GEN_SET_LOCAL_CONFIG_REQ')
	print('%d' % obj.cid)
	print('%d' % obj.size)
	print('%s' % obj.data)
def DUMP_BT_GEN_SET_LOCAL_CONFIG_CFM(obj):
	print('BT_GEN_SET_LOCAL_CONFIG_CFM')
	print('%d' % obj.status)
	print('%d' % obj.cid)
	print('%d' % obj.length)
	print('%s' % obj.data)
def DUMP_BT_GEN_READ_LOCAL_CONFIG_REQ(obj):
	print('BT_GEN_READ_LOCAL_CONFIG_REQ')
	print('%d' % obj.cid)
def DUMP_BT_GEN_READ_LOCAL_CONFIG_CFM(obj):
	print('BT_GEN_READ_LOCAL_CONFIG_CFM')
	print('%d' % obj.status)
	print('%d' % obj.cid)
	print('%d' % obj.length)
	print('%s' % obj.data)
def DUMP_BT_GEN_SSP_DEBUG_MODE_REQ(obj):
	print('BT_GEN_SSP_DEBUG_MODE_REQ')
	print('%d' % obj.enable)
def DUMP_BT_GEN_SSP_DEBUG_MODE_CFM(obj):
	print('BT_GEN_SSP_DEBUG_MODE_CFM')
	print('%d' % obj.status)
def DUMP_BT_GEN_SEARCH_REMOTE_DEV_REQ(obj):
	print('BT_GEN_SEARCH_REMOTE_DEV_REQ')
	print('%d' % obj.count)
	print('%d' % obj.timer)
def DUMP_BT_GEN_SEARCH_REMOTE_DEV_CFM(obj):
	print('BT_GEN_SEARCH_REMOTE_DEV_CFM')
	print('%d' % obj.status)
def DUMP_BT_GEN_SEARCH_REMOTE_DEV_IND(obj):
	print('BT_GEN_SEARCH_REMOTE_DEV_IND')
	print('%s' % obj.remote_addr)
	print('%d' % obj.cod)
	print('%d' % obj.service)
	print('%d' % obj.length)
	print('%s' % obj.name)
def DUMP_BT_GEN_SEARCH_REMOTE_DEV_COMP_IND(obj):
	print('BT_GEN_SEARCH_REMOTE_DEV_COMP_IND')
	print('%d' % obj.status)
def DUMP_BT_GEN_SEARCH_REMOTE_DEV_CANCEL_REQ(obj):
	print('BT_GEN_SEARCH_REMOTE_DEV_CANCEL_REQ')
def DUMP_BT_GEN_SEARCH_REMOTE_DEV_CANCEL_CFM(obj):
	print('BT_GEN_SEARCH_REMOTE_DEV_CANCEL_CFM')
	print('%d' % obj.status)
def DUMP_BT_GEN_SET_LOCAL_NAME_REQ(obj):
	print('BT_GEN_SET_LOCAL_NAME_REQ')
	print('%d' % obj.length)
	print('%s' % obj.name)
def DUMP_BT_GEN_SET_LOCAL_NAME_CFM(obj):
	print('BT_GEN_SET_LOCAL_NAME_CFM')
	print('%d' % obj.status)
def DUMP_BT_GEN_READ_REMOTE_NAME_REQ(obj):
	print('BT_GEN_READ_REMOTE_NAME_REQ')
	print('%s' % obj.addr)
def DUMP_BT_GEN_READ_REMOTE_NAME_CFM(obj):
	print('BT_GEN_READ_REMOTE_NAME_CFM')
	print('%d' % obj.status)
	print('%s' % obj.remote)
	print('%d' % obj.len)
	print('%s' % obj.name)
def DUMP_BT_GEN_READ_REMOTE_NAME_CANCEL_REQ(obj):
	print('BT_GEN_READ_REMOTE_NAME_CANCEL_REQ')
	print('%s' % obj.addr)
def DUMP_BT_GEN_READ_REMOTE_NAME_CANCEL_CFM(obj):
	print('BT_GEN_READ_REMOTE_NAME_CANCEL_CFM')
	print('%d' % obj.status)
def DUMP_BT_GEN_GET_LINK_QUALITY_REQ(obj):
	print('BT_GEN_GET_LINK_QUALITY_REQ')
	print('%s' % obj.addr)
def DUMP_BT_GEN_GET_LINK_QUALITY_CFM(obj):
	print('BT_GEN_GET_LINK_QUALITY_CFM')
	print('%d' % obj.status)
	print('%s' % obj.remote_addr)
	print('%d' % obj.linkquality)
def DUMP_BT_GEN_SET_LOCAL_MODE_REQ(obj):
	print('BT_GEN_SET_LOCAL_MODE_REQ')
	print('%d' % obj.discovery)
	print('%d' % obj.bonded)
	print('%d' % obj.connectable)
def DUMP_BT_GEN_SET_LOCAL_MODE_CFM(obj):
	print('BT_GEN_SET_LOCAL_MODE_CFM')
	print('%d' % obj.status)
	print('%d' % obj.discovery)
	print('%d' % obj.bonded)
	print('%d' % obj.connectable)
def DUMP_BT_GEN_SERVICE_SEARCH_REQ(obj):
	print('BT_GEN_SERVICE_SEARCH_REQ')
	print('%s' % obj.addr)
	print('%d' % obj.timeout)
def DUMP_BT_GEN_SERVICE_SEARCH_CFM(obj):
	print('BT_GEN_SERVICE_SEARCH_CFM')
	print('%d' % obj.status)
def DUMP_BT_GEN_SERVICE_SEARCH_IND(obj):
	print('BT_GEN_SERVICE_SEARCH_IND')
	print('%d' % obj.status)
	print('%s' % obj.remote_addr)
	print('%d' % obj.service)
	print('%d' % obj.version)
def DUMP_BT_GEN_SERVICE_SEARCH_COMP_IND(obj):
	print('BT_GEN_SERVICE_SEARCH_COMP_IND')
	print('%d' % obj.status)
	print('%s' % obj.remote_addr)
	print('%d' % obj.service)
def DUMP_BT_GEN_SDP_SEARCH_CANCEL_REQ(obj):
	print('BT_GEN_SDP_SEARCH_CANCEL_REQ')
	print('%s' % obj.addr)
def DUMP_BT_GEN_SERVICE_SEARCH_CANCEL_CFM(obj):
	print('BT_GEN_SERVICE_SEARCH_CANCEL_CFM')
	print('%d' % obj.status)
def DUMP_BT_GEN_ENTER_TEST_MODE_REQ(obj):
	print('BT_GEN_ENTER_TEST_MODE_REQ')
def DUMP_BT_GEN_DISABLE_TEST_MODE_REQ(obj):
	print('BT_GEN_DISABLE_TEST_MODE_REQ')
def DUMP_BT_GEN_SERVICE_SEARCH_EXT_REQ(obj):
	print('BT_GEN_SERVICE_SEARCH_EXT_REQ')
	print('%s' % obj.addr)
	print('%s' % obj.uuid)
def DUMP_BT_GEN_SERVICE_SEARCH_EXT_CFM(obj):
	print('BT_GEN_SERVICE_SEARCH_EXT_CFM')
	print('%d' % obj.status)
def DUMP_BT_GEN_SERVICE_SEARCH_EXT_IND(obj):
	print('BT_GEN_SERVICE_SEARCH_EXT_IND')
	print('%d' % obj.service)
def DUMP_BT_GEN_SERVICE_SEARCH_EXT_COMPLETE_IND(obj):
	print('BT_GEN_SERVICE_SEARCH_EXT_COMPLETE_IND')
	print('%d' % obj.status)
def DUMP_BT_GEN_GET_LOCAL_OOB_DATA_REQ(obj):
	print('BT_GEN_GET_LOCAL_OOB_DATA_REQ')
def DUMP_BT_GEN_GET_LOCAL_OOB_DATA_CFM(obj):
	print('BT_GEN_GET_LOCAL_OOB_DATA_CFM')
	print('%d' % obj.status)
	print('%s' % obj.oobhashc)
	print('%s' % obj.oobrandr)
def DUMP_BT_GEN_SET_REMOTE_OOB_DATA_REQ(obj):
	print('BT_GEN_SET_REMOTE_OOB_DATA_REQ')
	print('%s' % obj.addr)
	print('%s' % obj.oobhashc)
	print('%s' % obj.oobrandr)
def DUMP_BT_GEN_SET_REMOTE_OOB_DATA_CFM(obj):
	print('BT_GEN_SET_REMOTE_OOB_DATA_CFM')
	print('%d' % obj.status)
def DUMP_BT_GEN_SEARCH_DEVICE_INFO_REQ(obj):
	print('BT_GEN_SEARCH_DEVICE_INFO_REQ')
	print('%s' % obj.remote)
	print('%d' % obj.timeout)
def DUMP_BT_GEN_FID_SEARCH_DEV_INFO_CFM(obj):
	print('BT_GEN_FID_SEARCH_DEV_INFO_CFM')
	print('%d' % obj.status)
def DUMP_BT_GEN_FID_SEARCH_DEV_INFO_IND(obj):
	print('BT_GEN_FID_SEARCH_DEV_INFO_IND')
	print('%d' % obj.specid)
	print('%d' % obj.vendorid)
	print('%d' % obj.productid)
	print('%d' % obj.version)
	print('%d' % obj.primaryrecord)
	print('%d' % obj.vendoridsource)
def DUMP_BT_GEN_FID_SEARCH_DEV_INFO_COMPLETE_IND(obj):
	print('BT_GEN_FID_SEARCH_DEV_INFO_COMPLETE_IND')
	print('%d' % obj.status)
	print('%s' % obj.remote)
def DUMP_BT_GEN_REGISTER_DEVICE_INFO_REQ(obj):
	print('BT_GEN_REGISTER_DEVICE_INFO_REQ')
	print('%d' % obj.vendorid)
	print('%d' % obj.productid)
	print('%d' % obj.version)
	print('%d' % obj.sourceid)
def DUMP_BT_GEN_FID_REGISTER_DEVICE_INFO_CFM(obj):
	print('BT_GEN_FID_REGISTER_DEVICE_INFO_CFM')
	print('%d' % obj.status)
def DUMP_BT_GEN_UNREGISTER_DEVICE_INFO_REQ(obj):
	print('BT_GEN_UNREGISTER_DEVICE_INFO_REQ')
def DUMP_BT_GEN_UNREGISTER_DEVICE_INFO_CFM(obj):
	print('BT_GEN_UNREGISTER_DEVICE_INFO_CFM')
	print('%d' % obj.status)
def DUMP_BT_GEN_CANCEL_SEARCH_DEVICE_INFO_REQ(obj):
	print('BT_GEN_CANCEL_SEARCH_DEVICE_INFO_REQ')
def DUMP_BT_GEN_CANCEL_SEARCH_DEVICE_INFO_CFM(obj):
	print('BT_GEN_CANCEL_SEARCH_DEVICE_INFO_CFM')
	print('%d' % obj.status)
def DUMP_BT_CM_PAIRING_REMOTE_DEV_REQ(obj):
	print('BT_CM_PAIRING_REMOTE_DEV_REQ')
	print('%s' % obj.addr)
def DUMP_BT_CM_PAIRING_REMOTE_DEV_CFM(obj):
	print('BT_CM_PAIRING_REMOTE_DEV_CFM')
	print('%d' % obj.status)
def DUMP_BT_CM_PAIRING_CANCEL_DEV_REQ(obj):
	print('BT_CM_PAIRING_CANCEL_DEV_REQ')
	print('%s' % obj.addr)
def DUMP_BT_CM_PAIRING_CANCEL_DEV_CFM(obj):
	print('BT_CM_PAIRING_CANCEL_DEV_CFM')
	print('%d' % obj.status)
def DUMP_BT_CM_PIN_CODE_IND(obj):
	print('BT_CM_PIN_CODE_IND')
	print('%s' % obj.remote)
	print('%d' % obj.cod)
	print('%d' % obj.len)
	print('%s' % obj.name)
def DUMP_BT_CM_PIN_CODE_RES(obj):
	print('BT_CM_PIN_CODE_RES')
	print('%s' % obj.remote)
	print('%d' % obj.len)
	print('%s' % obj.pin_code)
def DUMP_BT_CM_PASSKEY_NOTIFICATION_IND(obj):
	print('BT_CM_PASSKEY_NOTIFICATION_IND')
	print('%s' % obj.remote)
	print('%d' % obj.len)
	print('%s' % obj.name)
	print('%d' % obj.passkey)
def DUMP_BT_CM_NUMERIC_CONFIRM_IND(obj):
	print('BT_CM_NUMERIC_CONFIRM_IND')
	print('%s' % obj.remote)
	print('%d' % obj.len)
	print('%s' % obj.name)
	print('%d' % obj.numeric)
def DUMP_BT_CM_NUM_DISPLAY_IND(obj):
	print('BT_CM_NUM_DISPLAY_IND')
	print('%s' % obj.remote)
	print('%d' % obj.len)
	print('%s' % obj.name)
	print('%d' % obj.numeric)
def DUMP_BT_CM_PASSKEY_REQ_IND(obj):
	print('BT_CM_PASSKEY_REQ_IND')
	print('%s' % obj.remote)
	print('%d' % obj.len)
	print('%s' % obj.name)
def DUMP_BT_CM_NUMERIC_CONFIRM_RES(obj):
	print('BT_CM_NUMERIC_CONFIRM_RES')
	print('%s' % obj.remote)
	print('%d' % obj.accept)
def DUMP_BT_GEN_FID_PAIR_COMPLETE_IND(obj):
	print('BT_GEN_FID_PAIR_COMPLETE_IND')
	print('%d' % obj.status)
	print('%s' % obj.remote)
def DUMP_BT_CM_CON_AUTHORIZE_IND(obj):
	print('BT_CM_CON_AUTHORIZE_IND')
	print('%s' % obj.remote)
	print('%d' % obj.service)
	print('%d' % obj.len)
	print('%s' % obj.name)
def DUMP_BT_CM_CON_AUTHORIZE_RES(obj):
	print('BT_CM_CON_AUTHORIZE_RES')
	print('%s' % obj.remote)
	print('%d' % obj.accept)
def DUMP_BT_CM_SERVICE_CON_REQ(obj):
	print('BT_CM_SERVICE_CON_REQ')
	print('%s' % obj.addr)
	print('%d' % obj.service)
def DUMP_BT_CM_SERVICE_CON_CFM(obj):
	print('BT_CM_SERVICE_CON_CFM')
	print('%d' % obj.status)
def DUMP_BT_CM_SERVICE_CON_IND(obj):
	print('BT_CM_SERVICE_CON_IND')
	print('%d' % obj.status)
	print('%s' % obj.addr)
	print('%d' % obj.function)
	print('%d' % obj.instanceid)
	print('%d' % obj.extenparam)
def DUMP_BT_CM_SERVICE_CON_COMP_IND(obj):
	print('BT_CM_SERVICE_CON_COMP_IND')
	print('%d' % obj.function)
def DUMP_BT_CM_SERVICE_CON_CANCEL_REQ(obj):
	print('BT_CM_SERVICE_CON_CANCEL_REQ')
	print('%s' % obj.addr)
def DUMP_BT_CM_SERVICE_CON_CANCEL_CFM(obj):
	print('BT_CM_SERVICE_CON_CANCEL_CFM')
	print('%d' % obj.status)
def DUMP_BT_CM_SERVICE_DISCON_REQ(obj):
	print('BT_CM_SERVICE_DISCON_REQ')
	print('%s' % obj.addr)
	print('%d' % obj.service)
def DUMP_BT_CM_SERVICE_DISCON_CFM(obj):
	print('BT_CM_SERVICE_DISCON_CFM')
	print('%d' % obj.status)
def DUMP_BT_CM_SERVICE_DISCON_IND(obj):
	print('BT_CM_SERVICE_DISCON_IND')
	print('%d' % obj.status)
	print('%s' % obj.addr)
	print('%d' % obj.function)
	print('%d' % obj.instanceid)
def DUMP_BT_CM_SERVICE_DISCON_COMP_IND(obj):
	print('BT_CM_SERVICE_DISCON_COMP_IND')
	print('%s' % obj.addr)
def DUMP_BT_HFP_SERVICE_IND(obj):
	print('BT_HFP_SERVICE_IND')
	print('%d' % obj.did)
	print('%d' % obj.value )
def DUMP_BT_HFP_SIGNAL_IND(obj):
	print('BT_HFP_SIGNAL_IND')
	print('%d' % obj.did)
	print('%d' % obj.value )
def DUMP_BT_HFP_ROAM_IND(obj):
	print('BT_HFP_ROAM_IND')
	print('%d' % obj.did)
	print('%d' % obj.value )
def DUMP_BT_HFP_BATTCHG_IND(obj):
	print('BT_HFP_BATTCHG_IND')
	print('%d' % obj.did)
	print('%d' % obj.value )
def DUMP_BT_HFP_CALL_RING_IND(obj):
	print('BT_HFP_CALL_RING_IND')
	print('%d' % obj.did)
def DUMP_BT_HFP_DIAL_OUT_REQ(obj):
	print('BT_HFP_DIAL_OUT_REQ')
	print('%d' % obj.did)
	print('%d' % obj.size)
	print('%s' % obj.num)
def DUMP_BT_HFP_FID_DIAL_CFM(obj):
	print('BT_HFP_FID_DIAL_CFM')
	print('%d' % obj.did)
	print('%d' % obj.status)
def DUMP_BT_HFP_CALL_STATE_IND(obj):
	print('BT_HFP_CALL_STATE_IND')
	print('%d' % obj.did)
	print('%d' % obj.state)
def DUMP_BT_HFP_LAST_DIAL_REQ(obj):
	print('BT_HFP_LAST_DIAL_REQ')
	print('%d' % obj.did)
def DUMP_BT_HFP_LAST_DIAL_CFM(obj):
	print('BT_HFP_LAST_DIAL_CFM')
	print('%d' % obj.did)
	print('%d' % obj.status)
def DUMP_BT_HFP_MEM_DIAL_REQ(obj):
	print('BT_HFP_MEM_DIAL_REQ')
	print('%d' % obj.did)
	print('%d' % obj.index)
def DUMP_BT_HFP_MEM_DIAL_CFM(obj):
	print('BT_HFP_MEM_DIAL_CFM')
	print('%d' % obj.status)
def DUMP_BT_HFP_CALL_ANSWER_REQ(obj):
	print('BT_HFP_CALL_ANSWER_REQ')
	print('%d' % obj.did)
def DUMP_BT_HFP_CALL_ANSWER_CFM(obj):
	print('BT_HFP_CALL_ANSWER_CFM')
	print('%d' % obj.did)
	print('%d' % obj.status)
def DUMP_BT_HFP_CALL_REJECT_REQ(obj):
	print('BT_HFP_CALL_REJECT_REQ')
	print('%d' % obj.did)
def DUMP_BT_HFP_CALL_REJECT_CFM(obj):
	print('BT_HFP_CALL_REJECT_CFM')
	print('%d' % obj.did)
	print('%d' % obj.status)
def DUMP_BT_HFP_TERMINATE_CALL_REQ(obj):
	print('BT_HFP_TERMINATE_CALL_REQ')
	print('%d' % obj.did)
def DUMP_BT_HFP_TERMINATE_CALL_CFM(obj):
	print('BT_HFP_TERMINATE_CALL_CFM')
	print('%d' % obj.did)
	print('%d' % obj.status)
def DUMP_BT_HFP_CLIP_ENABLE_REQ(obj):
	print('BT_HFP_CLIP_ENABLE_REQ')
	print('%d' % obj.did)
	print('%d' % obj.enable)
def DUMP_BT_HFP_CLIP_ENABLE_CFM(obj):
	print('BT_HFP_CLIP_ENABLE_CFM')
	print('%d' % obj.did)
	print('%d' % obj.status)
def DUMP_BT_HFP_CCWA_ENABLE_REQ(obj):
	print('BT_HFP_CCWA_ENABLE_REQ')
	print('%d' % obj.did)
	print('%d' % obj.enable)
def DUMP_BT_HFP_CCWA_ENABLE_CFM(obj):
	print('BT_HFP_CCWA_ENABLE_CFM')
	print('%d' % obj.did)
	print('%d' % obj.status)
def DUMP_BT_HFP_INCOMING_CALL_IND(obj):
	print('BT_HFP_INCOMING_CALL_IND')
	print('%d' % obj.did)
	print('%d' % obj.num_size)
	print('%s' % obj.number)
	print('%d' % obj.len)
	print('%s' % obj.name)
def DUMP_BT_HFP_SECOND_INCOMING_CALL_IND(obj):
	print('BT_HFP_SECOND_INCOMING_CALL_IND')
	print('%d' % obj.did)
	print('%d' % obj.num_size)
	print('%s' % obj.number)
	print('%d' % obj.len)
	print('%s' % obj.name)
def DUMP_BT_HFP_AUDIO_TRANSFER_REQ(obj):
	print('BT_HFP_AUDIO_TRANSFER_REQ')
	print('%d' % obj.did)
	print('%d' % obj.side)
def DUMP_BT_HFP_AUDIO_TRANSFER_CFM(obj):
	print('BT_HFP_AUDIO_TRANSFER_CFM')
	print('%d' % obj.did)
	print('%d' % obj.status)
def DUMP_BT_HFP_SCO_IND(obj):
	print('BT_HFP_SCO_IND')
	print('%d' % obj.did)
	print('%d' % obj.side )
def DUMP_BT_HFP_SEND_DTMF_REQ(obj):
	print('BT_HFP_SEND_DTMF_REQ')
	print('%d' % obj.did)
	print('%d' % obj.code)
def DUMP_BT_HFP_SEND_DTMF_CFM(obj):
	print('BT_HFP_SEND_DTMF_CFM')
	print('%d' % obj.did)
	print('%d' % obj.status)
def DUMP_BT_HFP_PESPONSE_AND_HOLD_REQ(obj):
	print('BT_HFP_PESPONSE_AND_HOLD_REQ')
	print('%d' % obj.did)
	print('%d' % obj.action)
def DUMP_BT_HFP_PESPONSE_AND_HOLD_CFM(obj):
	print('BT_HFP_PESPONSE_AND_HOLD_CFM')
	print('%d' % obj.did)
	print('%d' % obj.status)
def DUMP_BT_HFP_CALL_HOLD_REQ(obj):
	print('BT_HFP_CALL_HOLD_REQ')
	print('%d' % obj.did)
	print('%d' % obj.action)
	print('%d' % obj.index)
def DUMP_BT_HFP_CALL_HOLD_CFM(obj):
	print('BT_HFP_CALL_HOLD_CFM')
	print('%d' % obj.did)
	print('%d' % obj.status)
def DUMP_BT_HFP_ANSWER_SECOND_CALL_REQ(obj):
	print('BT_HFP_ANSWER_SECOND_CALL_REQ')
	print('%d' % obj.did)
	print('%d' % obj.hold)
def DUMP_BT_HFP_ANSWER_SECOND_CALL_CFM(obj):
	print('BT_HFP_ANSWER_SECOND_CALL_CFM')
	print('%d' % obj.did)
	print('%d' % obj.status)
def DUMP_BT_HFP_TERMINATE_CALL_BY_INDEX_REQ(obj):
	print('BT_HFP_TERMINATE_CALL_BY_INDEX_REQ')
	print('%d' % obj.did)
	print('%d' % obj.index)
def DUMP_BT_HFP_TERMINATE_CALL_BY_INDEX_CFM(obj):
	print('BT_HFP_TERMINATE_CALL_BY_INDEX_CFM')
	print('%d' % obj.did)
	print('%d' % obj.status)
def DUMP_BT_HFP_SWITCH_CALL_REQ(obj):
	print('BT_HFP_SWITCH_CALL_REQ')
	print('%d' % obj.did)
def DUMP_BT_HFP_SWITCH_CALL_CFM(obj):
	print('BT_HFP_SWITCH_CALL_CFM')
	print('%d' % obj.did)
	print('%d' % obj.status)
def DUMP_BT_HFP_JOIN_CALL_REQ(obj):
	print('BT_HFP_JOIN_CALL_REQ')
	print('%d' % obj.did)
def DUMP_BT_HFP_JOIN_CALL_CFM(obj):
	print('BT_HFP_JOIN_CALL_CFM')
	print('%d' % obj.did)
	print('%d' % obj.status)
def DUMP_BT_HFP_GET_SUBSCRIBER_NUM_REQ(obj):
	print('BT_HFP_GET_SUBSCRIBER_NUM_REQ')
	print('%d' % obj.did)
def DUMP_BT_HFP_GET_SUBSCRIBER_NUM_CFM(obj):
	print('BT_HFP_GET_SUBSCRIBER_NUM_CFM')
	print('%d' % obj.did)
	print('%d' % obj.status)
	print('%d' % obj.size)
	print('%s' % obj.num)
def DUMP_BT_HFP_GET_OPERATOR_NAME_REQ(obj):
	print('BT_HFP_GET_OPERATOR_NAME_REQ')
	print('%d' % obj.did)
def DUMP_BT_HFP_GET_OPERATOR_NAME_CFM(obj):
	print('BT_HFP_GET_OPERATOR_NAME_CFM')
	print('%d' % obj.did)
	print('%d' % obj.status)
	print('%d' % obj.length)
	print('%s' % obj.name)
def DUMP_BT_HFP_GET_CURRENT_CALL_LIST_REQ(obj):
	print('BT_HFP_GET_CURRENT_CALL_LIST_REQ')
	print('%d' % obj.did)
def DUMP_BT_HFP_GET_CURRENT_CALL_LIST_CFM(obj):
	print('BT_HFP_GET_CURRENT_CALL_LIST_CFM')
	print('%d' % obj.did)
	print('%d' % obj.status)
def DUMP_BT_HFP_GET_CURRENT_CALL_LIST_IND(obj):
	print('BT_HFP_GET_CURRENT_CALL_LIST_IND')
	print('%d' % obj.did)
	print('%d' % obj.idx)
	print('%d' % obj.dir)
	print('%d' % obj.status)
	print('%d' % obj.mode)
	print('%d' % obj.mpty)
	print('%d' % obj.type)
	print('%d' % obj.size)
	print('%s' % obj.num)
def DUMP_BT_HFP_GET_CURRENT_CALL_LIST_COMPLETE_IND(obj):
	print('BT_HFP_GET_CURRENT_CALL_LIST_COMPLETE_IND')
	print('%d' % obj.did)
	print('%d' % obj.status)
def DUMP_BT_SPP_DATA_SEND_REQ(obj):
	print('BT_SPP_DATA_SEND_REQ')
	print('%d' % obj.spp_id)
	print('%d' % obj.length)
	print('%s' % obj.data)
def DUMP_BT_SPP_DATA_SEND_CFM(obj):
	print('BT_SPP_DATA_SEND_CFM')
	print('%d' % obj.status)
	print('%d' % obj.spp_id)
def DUMP_BT_SPP_DATA_RECEIVE_IND(obj):
	print('BT_SPP_DATA_RECEIVE_IND')
	print('%d' % obj.spp_id)
	print('%d' % obj.length)
	print('%s' % obj.data)
def DUMP_BT_SPP_ACTIVE_SERVER_REQ(obj):
	print('BT_SPP_ACTIVE_SERVER_REQ')
	print('%s' % obj.uuid)
	print('%d' % obj.length)
	print('%s' % obj.name)
def DUMP_BT_SPP_ACTIVE_SERVER_CFM(obj):
	print('BT_SPP_ACTIVE_SERVER_CFM')
	print('%d' % obj.sppid)
	print('%d' % obj.status)
def DUMP_BT_SPP_DEACTIVE_SERVER_REQ(obj):
	print('BT_SPP_DEACTIVE_SERVER_REQ')
	print('%d' % obj.sppid)
def DUMP_BT_SPP_DEACTIVE_SERVER_CFM(obj):
	print('BT_SPP_DEACTIVE_SERVER_CFM')
	print('%d' % obj.sppid)
	print('%d' % obj.status)
def DUMP_BT_AV_AVRCP_CONNECT_IND(obj):
	print('BT_AV_AVRCP_CONNECT_IND')
	print('%d' % obj.did)
	print('%d' % obj.status)
	print('%d' % obj.version)
	print('%d' % obj.feature)
	print('%s' % obj.addr)
def DUMP_BT_AV_AVRCP_DISCONNECT_IND(obj):
	print('BT_AV_AVRCP_DISCONNECT_IND')
	print('%d' % obj.did)
	print('%d' % obj.status)
def DUMP_BT_AV_MEDIA_START_REQ(obj):
	print('BT_AV_MEDIA_START_REQ')
	print('%d' % obj.did)
def DUMP_BT_AV_MEDIA_START_CFM(obj):
	print('BT_AV_MEDIA_START_CFM')
	print('%d' % obj.did)
	print('%d' % obj.status)
def DUMP_BT_AV_MEDIA_STOP_REQ(obj):
	print('BT_AV_MEDIA_STOP_REQ')
	print('%d' % obj.did)
def DUMP_BT_AV_MEDIA_STOP_CFM(obj):
	print('BT_AV_MEDIA_STOP_CFM')
	print('%d' % obj.did)
	print('%d' % obj.status)
def DUMP_BT_AV_MEDIA_PASS_THROUGH_REQ(obj):
	print('BT_AV_MEDIA_PASS_THROUGH_REQ')
	print('%d' % obj.did)
	print('%d' % obj.opid)
	print('%d' % obj.state)
def DUMP_BT_AV_MEDIA_PASS_THROUGH_CFM(obj):
	print('BT_AV_MEDIA_PASS_THROUGH_CFM')
	print('%d' % obj.did)
	print('%d' % obj.status)
def DUMP_BT_AV_GET_CAPBILITY_REQ(obj):
	print('BT_AV_GET_CAPBILITY_REQ')
	print('%d' % obj.device_id)
	print('%d' % obj.caps)
def DUMP_BT_AV_GET_CAPBILITY_CFM(obj):
	print('BT_AV_GET_CAPBILITY_CFM')
	print('%d' % obj.did)
	print('%d' % obj.status)
	print('%d' % obj.caps)
	print('%d' % obj.notimask)
	print('%d' % obj.companyid)
def DUMP_BT_AV_GET_PLAY_STATUS_REQ(obj):
	print('BT_AV_GET_PLAY_STATUS_REQ')
	print('%d' % obj.did)
def DUMP_BT_AV_GET_PLAY_STATUS_CFM(obj):
	print('BT_AV_GET_PLAY_STATUS_CFM')
	print('%d' % obj.did)
	print('%d' % obj.status)
	print('%d' % obj.song_length)
	print('%d' % obj.song_elapsed)
	print('%d' % obj.play_status)
def DUMP_BT_AV_NOTI_REGISTER_REQ(obj):
	print('BT_AV_NOTI_REGISTER_REQ')
	print('%d' % obj.did)
	print('%d' % obj.notimask)
	print('%d' % obj.playbackinterval)
	print('%d' % obj.configmask)
def DUMP_BT_AV_NOTI_REGISTER_CFM(obj):
	print('BT_AV_NOTI_REGISTER_CFM')
	print('%d' % obj.did)
	print('%d' % obj.status)
	print('%d' % obj.notimask)
	print('%d' % obj.playbackinterval)
def DUMP_BT_AV_LIST_APP_ATT_ID_REQ(obj):
	print('BT_AV_LIST_APP_ATT_ID_REQ')
	print('%d' % obj.did)
def DUMP_BT_AV_LIST_APP_ATT_ID_CFM(obj):
	print('BT_AV_LIST_APP_ATT_ID_CFM')
	print('%d' % obj.did)
	print('%d' % obj.status)
	print('%d' % obj.number_of_attributes)
	print('%d' % obj.size)
	print('%s' % obj.attribute)
def DUMP_BT_AV_LIST_APP_VALUE_ID_REQ(obj):
	print('BT_AV_LIST_APP_VALUE_ID_REQ')
	print('%d' % obj.did)
	print('%d' % obj.attributeid)
def DUMP_BT_AV_LIST_APP_VALUE_ID_CFM(obj):
	print('BT_AV_LIST_APP_VALUE_ID_CFM')
	print('%d' % obj.did)
	print('%d' % obj.status)
	print('%d' % obj.attributeid)
	print('%d' % obj.number_of_values)
	print('%d' % obj.size)
	print('%s' % obj.value)
def DUMP_BT_AV_GET_APP_VALUE_REQ(obj):
	print('BT_AV_GET_APP_VALUE_REQ')
	print('%d' % obj.did)
	print('%d' % obj.attributes)
def DUMP_BT_AV_GET_APP_VALUE_CFM(obj):
	print('BT_AV_GET_APP_VALUE_CFM')
	print('%d' % obj.did)
	print('%d' % obj.status)
	print('%d' % obj.attvalpaircount)
	print('%d' % obj.attidlen)
	print('%s' % obj.attid)
	print('%d' % obj.validlen)
	print('%s' % obj.valid)
def DUMP_BT_AV_SET_APP_VALUE_REQ(obj):
	print('BT_AV_SET_APP_VALUE_REQ')
	print('%d' % obj.did)
	print('%d' % obj.attvalpaircount)
	print('%d' % obj.attidlen)
	print('%s' % obj.attid)
	print('%d' % obj.validlen)
	print('%s' % obj.valid)
def DUMP_BT_AV_SET_APP_VALUE_CFM(obj):
	print('BT_AV_SET_APP_VALUE_CFM')
	print('%d' % obj.did)
	print('%d' % obj.status)
def DUMP_BT_AV_GET_APP_ATT_TXT_REQ(obj):
	print('BT_AV_GET_APP_ATT_TXT_REQ')
	print('%d' % obj.did)
	print('%d' % obj.attributes)
def DUMP_BT_AV_GET_APP_ATT_TXT_CFM(obj):
	print('BT_AV_GET_APP_ATT_TXT_CFM')
	print('%d' % obj.did)
	print('%d' % obj.status)
def DUMP_BT_AV_APP_ATT_TXT_DATA_IND(obj):
	print('BT_AV_APP_ATT_TXT_DATA_IND')
	print('%d' % obj.did)
	print('%d' % obj.attributeid)
	print('%d' % obj.valueid)
	print('%d' % obj.charset)
	print('%d' % obj.len)
	print('%s' % obj.text)
def DUMP_BT_AV_APP_ATT_TXT_DATA_COMP_IND(obj):
	print('BT_AV_APP_ATT_TXT_DATA_COMP_IND')
	print('%d' % obj.did)
	print('%d' % obj.status)
def DUMP_BT_AV_GET_APP_VALUE_TXT_REQ(obj):
	print('BT_AV_GET_APP_VALUE_TXT_REQ')
	print('%d' % obj.did)
	print('%d' % obj.attribute_id)
	print('%d' % obj.validcount)
	print('%s' % obj.values)
def DUMP_BT_AV_GET_APP_VALUE_TXT_CFM(obj):
	print('BT_AV_GET_APP_VALUE_TXT_CFM')
	print('%d' % obj.did)
	print('%d' % obj.status)
def DUMP_BT_AV_APP_VAL_TXT_DATA_IND(obj):
	print('BT_AV_APP_VAL_TXT_DATA_IND')
	print('%d' % obj.did)
	print('%d' % obj.attributeid)
	print('%d' % obj.valueid)
	print('%d' % obj.charset)
	print('%d' % obj.len)
	print('%s' % obj.text)
def DUMP_BT_AV_APP_VAL_TXT_DATA_COMP_IND(obj):
	print('BT_AV_APP_VAL_TXT_DATA_COMP_IND')
	print('%d' % obj.did)
	print('%d' % obj.status)
def DUMP_BT_AV_ELEMENT_ATTRIBUTES_REQ(obj):
	print('BT_AV_ELEMENT_ATTRIBUTES_REQ')
	print('%d' % obj.did)
	print('%d' % obj.attributes)
def DUMP_BT_AV_ELEMENT_ATTRIBUTES_CFM(obj):
	print('BT_AV_ELEMENT_ATTRIBUTES_CFM')
	print('%d' % obj.did)
	print('%d' % obj.status)
	print('%d' % obj.num)
def DUMP_BT_AV_ELEMENT_ATTRIBUTES_DATA_IND(obj):
	print('BT_AV_ELEMENT_ATTRIBUTES_DATA_IND')
	print('%d' % obj.did)
	print('%d' % obj.attributeid)
	print('%d' % obj.charset)
	print('%d' % obj.len)
	print('%s' % obj.text)
def DUMP_BT_AV_ELEMENT_ATTRIBUTES_DATA_COMP_IND(obj):
	print('BT_AV_ELEMENT_ATTRIBUTES_DATA_COMP_IND')
	print('%d' % obj.did)
	print('%d' % obj.status)
def DUMP_BT_AV_INFORM_BATTERY_STATUS_REQ(obj):
	print('BT_AV_INFORM_BATTERY_STATUS_REQ')
	print('%d' % obj.did)
	print('%d' % obj.battery_status)
def DUMP_BT_AV_INFORM_BATTERY_STATUS_CFM(obj):
	print('BT_AV_INFORM_BATTERY_STATUS_CFM')
	print('%d' % obj.did)
	print('%d' % obj.status)
def DUMP_BT_AV_INFORM_CHARSET_REQ(obj):
	print('BT_AV_INFORM_CHARSET_REQ')
	print('%d' % obj.did)
	print('%d' % obj.charsets)
def DUMP_BT_AV_INFORM_CHARSET_CFM(obj):
	print('BT_AV_INFORM_CHARSET_CFM')
	print('%d' % obj.did)
	print('%d' % obj.status)
def DUMP_BT_AV_SET_ABSOLUTE_VOL_REQ(obj):
	print('BT_AV_SET_ABSOLUTE_VOL_REQ')
	print('%d' % obj.did)
	print('%d' % obj.volume)
def DUMP_BT_AV_SET_ABSOLUTE_VOL_CFM(obj):
	print('BT_AV_SET_ABSOLUTE_VOL_CFM')
	print('%d' % obj.did)
	print('%d' % obj.status)
	print('%d' % obj.volume)
def DUMP_BT_AV_SET_ADDR_PLAYER_REQ(obj):
	print('BT_AV_SET_ADDR_PLAYER_REQ')
	print('%d' % obj.did)
	print('%d' % obj.pid)
def DUMP_BT_AV_SET_ADDR_PLAYER_CFM(obj):
	print('BT_AV_SET_ADDR_PLAYER_CFM')
	print('%d' % obj.did)
	print('%d' % obj.status)
def DUMP_BT_AV_PLAY_ITEM_REQ(obj):
	print('BT_AV_PLAY_ITEM_REQ')
	print('%d' % obj.did)
	print('%d' % obj.scope)
	print('%d' % obj.uidhigh)
	print('%d' % obj.uidlow)
	print('%d' % obj.uid_counter)
def DUMP_BT_AV_PLAY_ITEM_CFM(obj):
	print('BT_AV_PLAY_ITEM_CFM')
	print('%d' % obj.did)
	print('%d' % obj.status)
def DUMP_BT_AV_ADD_NOW_PLAYING_REQ(obj):
	print('BT_AV_ADD_NOW_PLAYING_REQ')
	print('%d' % obj.did)
	print('%d' % obj.scope)
	print('%d' % obj.uidhigh)
	print('%d' % obj.uidlow)
	print('%d' % obj.uid_counter)
def DUMP_BT_AV_ADD_NOW_PLAYING_CFM(obj):
	print('BT_AV_ADD_NOW_PLAYING_CFM')
	print('%d' % obj.did)
	print('%d' % obj.status)
def DUMP_BT_AV_SET_BROWSED_PLAYER_REQ(obj):
	print('BT_AV_SET_BROWSED_PLAYER_REQ')
	print('%d' % obj.did)
	print('%d' % obj.pid)
def DUMP_BT_AV_SET_BROWSED_PLAYER_CFM(obj):
	print('BT_AV_SET_BROWSED_PLAYER_CFM')
	print('%d' % obj.did)
	print('%d' % obj.status)
	print('%d' % obj.uid_counter )
	print('%d' % obj.num_items)
	print('%d' % obj.folder_depth)
	print('%d' % obj.namelen)
	print('%s' % obj.name)
def DUMP_BT_AV_CHANGE_PATH_REQ(obj):
	print('BT_AV_CHANGE_PATH_REQ')
	print('%d' % obj.did)
	print('%d' % obj.direction)
	print('%d' % obj.uidhigh)
	print('%d' % obj.folder_uid_low)
	print('%d' % obj.uid_counter)
def DUMP_BT_AV_CHANGE_PATH_CFM(obj):
	print('BT_AV_CHANGE_PATH_CFM')
	print('%d' % obj.did)
	print('%d' % obj.status)
	print('%d' % obj.num_items)
def DUMP_BT_AV_GET_ITEM_ATT_REQ(obj):
	print('BT_AV_GET_ITEM_ATT_REQ')
	print('%d' % obj.did)
	print('%d' % obj.scope)
	print('%d' % obj.uidhigh)
	print('%d' % obj.uidlow)
	print('%d' % obj.uid_counter)
	print('%d' % obj.attributes)
def DUMP_BT_AV_GET_ITEM_ATT_CFM(obj):
	print('BT_AV_GET_ITEM_ATT_CFM')
	print('%d' % obj.did)
	print('%d' % obj.status)
	print('%d' % obj.num_attribute)
def DUMP_BT_AV_BROWSE_ITEM_ATTRIBUTES_DATA_IND(obj):
	print('BT_AV_BROWSE_ITEM_ATTRIBUTES_DATA_IND')
	print('%d' % obj.did)
	print('%d' % obj.attributeid)
	print('%d' % obj.charset)
	print('%d' % obj.itemlen)
	print('%s' % obj.item)
def DUMP_BT_AV_BROWSE_ITEM_ATTRIBUTES_DATA_COMP_IND(obj):
	print('BT_AV_BROWSE_ITEM_ATTRIBUTES_DATA_COMP_IND')
	print('%d' % obj.did)
	print('%d' % obj.status)
def DUMP_BT_AV_GET_FOLDER_ITEM_REQ(obj):
	print('BT_AV_GET_FOLDER_ITEM_REQ')
	print('%d' % obj.did)
	print('%d' % obj.scope)
	print('%d' % obj.start)
	print('%d' % obj.end)
	print('%d' % obj.attributemask)
def DUMP_BT_AV_GET_FOLDER_ITEM_CFM(obj):
	print('BT_AV_GET_FOLDER_ITEM_CFM')
	print('%d' % obj.did)
	print('%d' % obj.status)
	print('%d' % obj.uid_counter)
	print('%d' % obj.num_items)
def DUMP_BT_AV_BROWSE_PLAYER_ITEM_DATA_IND(obj):
	print('BT_AV_BROWSE_PLAYER_ITEM_DATA_IND')
	print('%d' % obj.did)
	print('%d' % obj.playerid)
	print('%d' % obj.majortype)
	print('%d' % obj.subtype)
	print('%d' % obj.playbackstatus)
	print('%d' % obj.featuremask1)
	print('%d' % obj.featuremask2)
	print('%d' % obj.featuremask3)
	print('%d' % obj.featuremask4)
	print('%d' % obj.charset)
	print('%d' % obj.playernamelen)
	print('%s' % obj.playername)
def DUMP_BT_AV_BROWSE_FOLDER_ITEM_DATA_IND(obj):
	print('BT_AV_BROWSE_FOLDER_ITEM_DATA_IND')
	print('%d' % obj.did)
	print('%d' % obj.folderuidhigh)
	print('%d' % obj.folderuidlow)
	print('%d' % obj.foldertype)
	print('%d' % obj.playabletype)
	print('%d' % obj.charset)
	print('%d' % obj.foldernamelen)
	print('%s' % obj.foldername)
def DUMP_BT_AV_BROWSE_MEDIA_ITEM_DATA_IND(obj):
	print('BT_AV_BROWSE_MEDIA_ITEM_DATA_IND')
	print('%d' % obj.did)
	print('%d' % obj.mediauidhigh)
	print('%d' % obj.mediauidlow)
	print('%d' % obj.mediatype)
	print('%d' % obj.charset)
	print('%d' % obj.medianamelen)
	print('%s' % obj.medianame)
def DUMP_BT_AV_BROWSE_ITEM_DATA_COMP_IND(obj):
	print('BT_AV_BROWSE_ITEM_DATA_COMP_IND')
	print('%d' % obj.did)
	print('%d' % obj.status)
def DUMP_BT_AV_SEARCH_REQ(obj):
	print('BT_AV_SEARCH_REQ')
	print('%d' % obj.did)
	print('%d' % obj.size)
	print('%s' % obj.str)
def DUMP_BT_AV_SEARCH_CFM(obj):
	print('BT_AV_SEARCH_CFM')
	print('%d' % obj.did)
	print('%d' % obj.status)
	print('%d' % obj.uid_counter )
	print('%d' % obj.num_items)
def DUMP_BT_AV_GET_BROWSE_XML_STREAM_REQ(obj):
	print('BT_AV_GET_BROWSE_XML_STREAM_REQ')
	print('%d' % obj.did)
def DUMP_BT_AV_GET_BROWSE_XML_STREAM_CFM(obj):
	print('BT_AV_GET_BROWSE_XML_STREAM_CFM')
	print('%d' % obj.did)
	print('%d' % obj.status)
	print('%d' % obj.length )
	print('%s' % obj.stream)
def DUMP_BT_AV_PLAYER_STATUS_CHANGE_NOTI_IND(obj):
	print('BT_AV_PLAYER_STATUS_CHANGE_NOTI_IND')
	print('%d' % obj.did)
	print('%d' % obj.playbackstatus)
def DUMP_BT_AV_TRACK_CHANGE_NOTI_IND(obj):
	print('BT_AV_TRACK_CHANGE_NOTI_IND')
	print('%d' % obj.did)
	print('%d' % obj.track_index_high)
	print('%d' % obj.track_index_low)
def DUMP_BT_AV_REACHED_END_NOTI_IND(obj):
	print('BT_AV_REACHED_END_NOTI_IND')
	print('%d' % obj.did)
def DUMP_BT_AV_REACHED_START_NOTI_IND(obj):
	print('BT_AV_REACHED_START_NOTI_IND')
	print('%d' % obj.did)
def DUMP_BT_AV_PLAYBACK_POSITION_CHANGE_NOTI_IND(obj):
	print('BT_AV_PLAYBACK_POSITION_CHANGE_NOTI_IND')
	print('%d' % obj.did)
	print('%d' % obj.playback_pos)
def DUMP_BT_AV_BATTERY_STATUS_CHANGE_NOTI_IND(obj):
	print('BT_AV_BATTERY_STATUS_CHANGE_NOTI_IND')
	print('%d' % obj.did)
	print('%d' % obj.battery_status)
def DUMP_BT_AV_SYSTEM_STATUS_CHANGE_NOTI_IND(obj):
	print('BT_AV_SYSTEM_STATUS_CHANGE_NOTI_IND')
	print('%d' % obj.did)
	print('%d' % obj.systemstatus)
def DUMP_BT_AV_PLAYING_CONTENT_CHANGE_NOTI_IND(obj):
	print('BT_AV_PLAYING_CONTENT_CHANGE_NOTI_IND')
	print('%d' % obj.did)
def DUMP_BT_AV_AVAILABLE_PLAYER_CHANGE_NOTI_IND(obj):
	print('BT_AV_AVAILABLE_PLAYER_CHANGE_NOTI_IND')
	print('%d' % obj.did)
def DUMP_BT_AV_ADDRESSED_PLAYER_CHANGE_NOTI_IND(obj):
	print('BT_AV_ADDRESSED_PLAYER_CHANGE_NOTI_IND')
	print('%d' % obj.did)
	print('%d' % obj.player_id)
	print('%d' % obj.uid_counter)
def DUMP_BT_AV_UID_CHANGE_NOTI_IND(obj):
	print('BT_AV_UID_CHANGE_NOTI_IND')
	print('%d' % obj.did)
	print('%d' % obj.uid_counter)
def DUMP_BT_AV_VOLUME_CHANGE_NOTI_IND(obj):
	print('BT_AV_VOLUME_CHANGE_NOTI_IND')
	print('%d' % obj.did)
	print('%d' % obj.volume)
def DUMP_BT_AVP_FID_EVT_PLAYER_APP_SETTING_CHANGED_IND(obj):
	print('BT_AVP_FID_EVT_PLAYER_APP_SETTING_CHANGED_IND')
	print('%d' % obj.did)
	print('%d' % obj.number_of_attributes)
	print('%d' % obj.size)
	print('%s' % obj.attribute)
def DUMP_BT_AV_A2DP_CONFIGURATION_IND(obj):
	print('BT_AV_A2DP_CONFIGURATION_IND')
	print('%d' % obj.channels)
	print('%d' % obj.sample_bit)
	print('%d' % obj.sample_frep)
def DUMP_BT_AV_A2DP_STREAM_DATA_IND(obj):
	print('BT_AV_A2DP_STREAM_DATA_IND')
	print('%s' % obj.pcmdata)
	print('%d' % obj.pcmlength)
def DUMP_BT_PBDL_ATCMD_START_SERVICE_REQ(obj):
	print('BT_PBDL_ATCMD_START_SERVICE_REQ')
	print('%d' % obj.deviceid)
	print('%d' % obj.serviceid)
def DUMP_BT_PBDL_ATCMD_START_SERVICE_CFM(obj):
	print('BT_PBDL_ATCMD_START_SERVICE_CFM')
	print('%d' % obj.status)
	print('%d' % obj.did)
	print('%d' % obj.serviceid)
def DUMP_BT_PBDL_ATCMD_GET_STORAGE_REQ(obj):
	print('BT_PBDL_ATCMD_GET_STORAGE_REQ')
	print('%d' % obj.did)
def DUMP_BT_PBDL_ATCMD_GET_STORAGE_CFM(obj):
	print('BT_PBDL_ATCMD_GET_STORAGE_CFM')
	print('%d' % obj.status)
	print('%d' % obj.did)
	print('%d' % obj.storages)
def DUMP_BT_PBDL_ATCMD_GET_CURRENT_STORAGE_REQ(obj):
	print('BT_PBDL_ATCMD_GET_CURRENT_STORAGE_REQ')
	print('%d' % obj.did)
def DUMP_BT_PBDL_ATCMD_GET_CURRENT_STORAGE_CFM(obj):
	print('BT_PBDL_ATCMD_GET_CURRENT_STORAGE_CFM')
	print('%d' % obj.status)
	print('%d' % obj.did)
	print('%d' % obj.storages)
	print('%d' % obj.used)
	print('%d' % obj.total)
def DUMP_BT_PBDL_ATCMD_SET_STORAGE_REQ(obj):
	print('BT_PBDL_ATCMD_SET_STORAGE_REQ')
	print('%d' % obj.did)
	print('%d' % obj.storage)
def DUMP_BT_PBDL_ATCMD_SET_STORAGE_CFM(obj):
	print('BT_PBDL_ATCMD_SET_STORAGE_CFM')
	print('%d' % obj.status)
	print('%d' % obj.did)
def DUMP_BT_PBDL_ATCMD_READ_PB_ENTRY_REQ(obj):
	print('BT_PBDL_ATCMD_READ_PB_ENTRY_REQ')
	print('%d' % obj.did)
	print('%d' % obj.start_index)
	print('%d' % obj.end_index)
def DUMP_BT_PBDL_ATCMD_READ_PB_ENTRY_CFM(obj):
	print('BT_PBDL_ATCMD_READ_PB_ENTRY_CFM')
	print('%d' % obj.status)
	print('%d' % obj.did)
def DUMP_BT_PBDL_ATCMD_FIND_PB_ENTRY_REQ(obj):
	print('BT_PBDL_ATCMD_FIND_PB_ENTRY_REQ')
	print('%d' % obj.did)
	print('%d' % obj.textlen)
	print('%s' % obj.text)
def DUMP_BT_PBDL_ATCMD_FIND_PB_ENTRY_CFM(obj):
	print('BT_PBDL_ATCMD_FIND_PB_ENTRY_CFM')
	print('%d' % obj.status)
	print('%d' % obj.did)
def DUMP_BT_PBDL_ATCMD_ENTRY_DATA_ABORT_REQ(obj):
	print('BT_PBDL_ATCMD_ENTRY_DATA_ABORT_REQ')
	print('%d' % obj.did)
def DUMP_BT_PBDL_ATCMD_ENTRY_DATA_ABORT_CFM(obj):
	print('BT_PBDL_ATCMD_ENTRY_DATA_ABORT_CFM')
	print('%d' % obj.status)
	print('%d' % obj.did)
def DUMP_BT_PBDL_ATCMD_PB_ENTRY_DATA_IND(obj):
	print('BT_PBDL_ATCMD_PB_ENTRY_DATA_IND')
	print('%d' % obj.did)
	print('%d' % obj.index)
	print('%d' % obj.number_len)
	print('%s' % obj.number)
	print('%d' % obj.type)
	print('%d' % obj.name_len)
	print('%s' % obj.name)
def DUMP_BT_PBDL_ATCMD_PB_ENTRY_DATA_COMPLETE_IND(obj):
	print('BT_PBDL_ATCMD_PB_ENTRY_DATA_COMPLETE_IND')
	print('%d' % obj.status)
	print('%d' % obj.did)
def DUMP_BT_PBDL_ATCMD_CONNECTION_IND(obj):
	print('BT_PBDL_ATCMD_CONNECTION_IND')
	print('%d' % obj.did)
	print('%s' % obj.addr)
def DUMP_BT_PBDL_ATCMD_DISCONNECTION_IND(obj):
	print('BT_PBDL_ATCMD_DISCONNECTION_IND')
	print('%d' % obj.did)
	print('%s' % obj.addr)
def DUMP_BT_PBDL_PBAP_SET_FOLDER_REQ(obj):
	print('BT_PBDL_PBAP_SET_FOLDER_REQ')
	print('%d' % obj.repository)
	print('%d' % obj.phonebook)
def DUMP_BT_PBDL_PBAP_SET_FOLDER_CFM(obj):
	print('BT_PBDL_PBAP_SET_FOLDER_CFM')
	print('%d' % obj.status)
def DUMP_BT_PBDL_PBAP_GET_PBSIZE_REQ(obj):
	print('BT_PBDL_PBAP_GET_PBSIZE_REQ')
	print('%d' % obj.repository)
	print('%d' % obj.phonebook)
def DUMP_BT_PBDL_PBAP_GET_PBSIZE_CFM(obj):
	print('BT_PBDL_PBAP_GET_PBSIZE_CFM')
	print('%d' % obj.status)
	print('%d' % obj.pbooksize)
	print('%d' % obj.newmisscalls)
def DUMP_BT_PBDL_PBAP_PULL_PB_REQ(obj):
	print('BT_PBDL_PBAP_PULL_PB_REQ')
	print('%d' % obj.repository)
	print('%d' % obj.phonebook)
	print('%d' % obj.ver)
	print('%d' % obj.filter_lo)
	print('%d' % obj.filter_hi)
	print('%d' % obj.start_list)
	print('%d' % obj.max_list)
def DUMP_BT_PBDL_PBAP_PULL_PB_CFM(obj):
	print('BT_PBDL_PBAP_PULL_PB_CFM')
	print('%d' % obj.status)
def DUMP_BT_PBDL_PBAP_PULL_VCARD_LIST_REQ(obj):
	print('BT_PBDL_PBAP_PULL_VCARD_LIST_REQ')
	print('%d' % obj.order)
	print('%d' % obj.srchattr)
	print('%d' % obj.srchvallen)
	print('%s' % obj.searchvalue)
	print('%d' % obj.start_list)
	print('%d' % obj.max_list)
def DUMP_BT_PBDL_PBAP_PULL_VCARD_LIST_CFM(obj):
	print('BT_PBDL_PBAP_PULL_VCARD_LIST_CFM')
	print('%d' % obj.status)
def DUMP_BT_PBDL_PBAP_PULL_VCARD_ENTRY_REQ(obj):
	print('BT_PBDL_PBAP_PULL_VCARD_ENTRY_REQ')
	print('%d' % obj.entry)
	print('%d' % obj.filter_lo)
	print('%d' % obj.filter_hi)
	print('%d' % obj.ver)
def DUMP_BT_PBDL_PBAP_PULL_VCARD_ENTRY_CFM(obj):
	print('BT_PBDL_PBAP_PULL_VCARD_ENTRY_CFM')
	print('%d' % obj.status)
def DUMP_BT_PBDL_PBAP_PB_ENTRY_DATA_IND(obj):
	print('BT_PBDL_PBAP_PB_ENTRY_DATA_IND')
	print('%d' % obj.length)
	print('%s' % obj.body)
def DUMP_BT_PBDL_PBAP_PB_ENTRY_DATA_COMPLETE_IND(obj):
	print('BT_PBDL_PBAP_PB_ENTRY_DATA_COMPLETE_IND')
	print('%d' % obj.status)
	print('%d' % obj.pbsize)
	print('%d' % obj.newmissedcall)
def DUMP_BT_PBDL_PBAP_VCARD_LIST_DATA_IND(obj):
	print('BT_PBDL_PBAP_VCARD_LIST_DATA_IND')
	print('%d' % obj.length)
	print('%s' % obj.body)
def DUMP_BT_PBDL_PBAP_VCARD_LIST_DATA_COMPLETE_IND(obj):
	print('BT_PBDL_PBAP_VCARD_LIST_DATA_COMPLETE_IND')
	print('%d' % obj.status)
	print('%d' % obj.pbsize)
	print('%d' % obj.newmissedcall)
def DUMP_BT_PBDL_PBAP_VCARD_ENTRY_DATA_IND(obj):
	print('BT_PBDL_PBAP_VCARD_ENTRY_DATA_IND')
	print('%d' % obj.length)
	print('%s' % obj.body)
def DUMP_BT_PBDL_PBAP_VCARD_ENTRY_DATA_COMPLETE_IND(obj):
	print('BT_PBDL_PBAP_VCARD_ENTRY_DATA_COMPLETE_IND')
	print('%d' % obj.status)
def DUMP_BT_PBDL_PBAP_PULL_ABORT_REQ(obj):
	print('BT_PBDL_PBAP_PULL_ABORT_REQ')
def DUMP_BT_PBDL_PBAP_PULL_ABORT_CFM(obj):
	print('BT_PBDL_PBAP_PULL_ABORT_CFM')
	print('%d' % obj.status)
def DUMP_BT_PBDL_OPPS_PUT_FILE_IND(obj):
	print('BT_PBDL_OPPS_PUT_FILE_IND')
	print('%d' % obj.namelength)
	print('%s' % obj.name)
	print('%d' % obj.type)
	print('%d' % obj.objectlength)
def DUMP_BT_PBDL_OPPS_PUT_BODY_IND(obj):
	print('BT_PBDL_OPPS_PUT_BODY_IND')
	print('%d' % obj.length)
	print('%s' % obj.body)
def DUMP_BT_PBDL_OPPS_PUT_COMPLETE_IND(obj):
	print('BT_PBDL_OPPS_PUT_COMPLETE_IND')
	print('%d' % obj.status)
def DUMP_BT_PBDL_OPPS_PUT_ABORT_IND(obj):
	print('BT_PBDL_OPPS_PUT_ABORT_IND')
	print('%d' % obj.status)
def DUMP_BT_PBDL_OPPS_PUT_ABORT_REQ(obj):
	print('BT_PBDL_OPPS_PUT_ABORT_REQ')
def DUMP_BT_PBDL_OPPS_PUT_ABORT_CFM(obj):
	print('BT_PBDL_OPPS_PUT_ABORT_CFM')
	print('%d' % obj.status)
def DUMP_BT_PBDL_PULL_PB_REQ(obj):
	print('BT_PBDL_PULL_PB_REQ')
def DUMP_BT_PBDL_PULL_PB_CFM(obj):
	print('BT_PBDL_PULL_PB_CFM')
	print('%d' % obj.status)
def DUMP_BT_PBDL_PULL_PB_CMP_IND(obj):
	print('BT_PBDL_PULL_PB_CMP_IND')
	print('%d' % obj.status)
def DUMP_BT_MAP_GET_DEVICE_LIST_REQ(obj):
	print('BT_MAP_GET_DEVICE_LIST_REQ')
def DUMP_BT_MAP_GET_DEVICE_LIST_CFM(obj):
	print('BT_MAP_GET_DEVICE_LIST_CFM')
	print('%d' % obj.status)
	print('%s' % obj.addr)
	print('%d' % obj.masinstid)
	print('%d' % obj.mapcinstid)
def DUMP_BT_MAP_GET_SDP_RECORD_REQ(obj):
	print('BT_MAP_GET_SDP_RECORD_REQ')
	print('%s' % obj.addr)
def DUMP_BT_MAP_GET_SDP_RECORD_CFM(obj):
	print('BT_MAP_GET_SDP_RECORD_CFM')
	print('%d' % obj.status)
def DUMP_BT_MAP_GET_SDP_RECORD_IND(obj):
	print('BT_MAP_GET_SDP_RECORD_IND')
	print('%d' % obj.instanceid)
	print('%d' % obj.len)
	print('%s' % obj.servicename)
	print('%d' % obj.supportedmessage)
def DUMP_BT_MAP_SDP_RECORD_COMPLETE_IND(obj):
	print('BT_MAP_SDP_RECORD_COMPLETE_IND')
	print('%d' % obj.status)
def DUMP_BT_MAP_ESTABLIST_CONNECTION_REQ(obj):
	print('BT_MAP_ESTABLIST_CONNECTION_REQ')
	print('%s' % obj.addr)
	print('%d' % obj.masinstid)
def DUMP_BT_MAP_ESTABLIST_CONNECTION_CFM(obj):
	print('BT_MAP_ESTABLIST_CONNECTION_CFM')
	print('%d' % obj.status)
	print('%s' % obj.addr)
	print('%d' % obj.masinstid)
	print('%d' % obj.mapcinstid)
def DUMP_BT_MAP_DESTROY_CONNECTION_REQ(obj):
	print('BT_MAP_DESTROY_CONNECTION_REQ')
	print('%d' % obj.mapcinst)
def DUMP_BT_MAP_DESTROY_CONNECTION_CFM(obj):
	print('BT_MAP_DESTROY_CONNECTION_CFM')
	print('%d' % obj.mapcinst)
	print('%d' % obj.status)
def DUMP_BT_MAP_SET_FLODER_REQ(obj):
	print('BT_MAP_SET_FLODER_REQ')
	print('%d' % obj.mapcinst)
	print('%d' % obj.length)
	print('%s' % obj.name)
def DUMP_BT_MAP_SET_FLODER_BACK_REQ(obj):
	print('BT_MAP_SET_FLODER_BACK_REQ')
	print('%d' % obj.mapcinst)
def DUMP_BT_MAP_SET_FLODER_ROOT_REQ(obj):
	print('BT_MAP_SET_FLODER_ROOT_REQ')
	print('%d' % obj.mapcinst)
def DUMP_BT_MAP_SET_FLODER_CFM(obj):
	print('BT_MAP_SET_FLODER_CFM')
	print('%d' % obj.instanceid)
	print('%d' % obj.status)
def DUMP_BT_MAP_SET_FLODER_BACK_CFM(obj):
	print('BT_MAP_SET_FLODER_BACK_CFM')
	print('%d' % obj.instanceid)
	print('%d' % obj.status)
def DUMP_BT_MAP_SET_FLODER_ROOT_CFM(obj):
	print('BT_MAP_SET_FLODER_ROOT_CFM')
	print('%d' % obj.instanceid)
	print('%d' % obj.status)
def DUMP_BT_MAP_GET_FLODERLIST_REQ(obj):
	print('BT_MAP_GET_FLODERLIST_REQ')
	print('%d' % obj.instanceid)
	print('%d' % obj.maxcount)
	print('%d' % obj.offset)
def DUMP_BT_MAP_GET_FLODERLIST_CFM(obj):
	print('BT_MAP_GET_FLODERLIST_CFM')
	print('%d' % obj.mapcinst)
	print('%d' % obj.status)
def DUMP_BT_MAP_GET_FLODERLIST_IND(obj):
	print('BT_MAP_GET_FLODERLIST_IND')
	print('%d' % obj.instanceid)
	print('%d' % obj.len)
	print('%s' % obj.name)
def DUMP_BT_MAP_FLODERLIST_COMPLETE_IND(obj):
	print('BT_MAP_FLODERLIST_COMPLETE_IND')
	print('%d' % obj.instanceid)
	print('%d' % obj.status)
def DUMP_BT_MAP_GET_MESSAGELIST_REQ(obj):
	print('BT_MAP_GET_MESSAGELIST_REQ')
	print('%d' % obj.mapcinst)
	print('%d' % obj.maxcount)
	print('%d' % obj.offset)
	print('%d' % obj.subjectlen)
	print('%d' % obj.foldernamelen)
	print('%s' % obj.foldername)
	print('%d' % obj.paramtermask)
	print('%d' % obj.filtermessagetype)
	print('%s' % obj.filterperiodbegin)
	print('%s' % obj.filterperiodend)
	print('%d' % obj.filterreadstatus)
	print('%d' % obj.recipientlen)
	print('%s' % obj.filterrecipient)
	print('%d' % obj.originatorlen)
	print('%s' % obj.filteroriginator)
	print('%d' % obj.filterpriority)
def DUMP_BT_MAP_GET_MESSAGELIST_CFM(obj):
	print('BT_MAP_GET_MESSAGELIST_CFM')
	print('%d' % obj.instanceid)
	print('%d' % obj.status)
def DUMP_BT_MAP_GET_MESSAGELIST_IND(obj):
	print('BT_MAP_GET_MESSAGELIST_IND')
	print('%d' % obj.mapcinst)
	print('%d' % obj.len)
	print('%s' % obj.date)
def DUMP_BT_MAP_GET_MESSAGELIST_COMPLETE_IND(obj):
	print('BT_MAP_GET_MESSAGELIST_COMPLETE_IND')
	print('%d' % obj.mapcinst)
	print('%d' % obj.status)
def DUMP_BT_MAP_GET_MESSAGE_REQ(obj):
	print('BT_MAP_GET_MESSAGE_REQ')
	print('%d' % obj.instanceid)
	print('%d' % obj.handlerlen)
	print('%s' % obj.handle)
	print('%d' % obj.attachment)
	print('%d' % obj.charset)
	print('%d' % obj.fractionrequest)
def DUMP_BT_MAP_GET_MESSAGE_CFM(obj):
	print('BT_MAP_GET_MESSAGE_CFM')
	print('%d' % obj.mapcinst)
	print('%d' % obj.status)
def DUMP_BT_MAP_GET_MESSAGE_IND(obj):
	print('BT_MAP_GET_MESSAGE_IND')
	print('%d' % obj.instanceid)
	print('%d' % obj.len)
	print('%s' % obj.content)
def DUMP_BT_MAP_FID_MESSAGE_COMPLETE_IND(obj):
	print('BT_MAP_FID_MESSAGE_COMPLETE_IND')
	print('%d' % obj.status)
def DUMP_BT_MAP_SET_MESSAGE_STATUS_REQ(obj):
	print('BT_MAP_SET_MESSAGE_STATUS_REQ')
	print('%d' % obj.mapcinst)
	print('%d' % obj.value)
	print('%d' % obj.handlerlen)
	print('%s' % obj.handle)
def DUMP_BT_MAP_SET_MESSAGE_STATUS_CFM(obj):
	print('BT_MAP_SET_MESSAGE_STATUS_CFM')
	print('%d' % obj.instanceid)
	print('%d' % obj.status)
def DUMP_BT_MAP_PUT_MESSAGE_REQ(obj):
	print('BT_MAP_PUT_MESSAGE_REQ')
	print('%d' % obj.mapcinst)
	print('%d' % obj.length)
	print('%s' % obj.content)
	print('%d' % obj.transparent)
	print('%d' % obj.retry)
	print('%d' % obj.charset)
def DUMP_BT_MAP_PUT_MESSAGE_CFM(obj):
	print('BT_MAP_PUT_MESSAGE_CFM')
	print('%d' % obj.instanceid)
	print('%d' % obj.status)
def DUMP_BT_MAP_UPDATE_INBOX_REQ(obj):
	print('BT_MAP_UPDATE_INBOX_REQ')
	print('%d' % obj.mapcinst)
def DUMP_BT_MAP_UPDATE_INBOX_CFM(obj):
	print('BT_MAP_UPDATE_INBOX_CFM')
	print('%d' % obj.instanceid)
	print('%d' % obj.status)
def DUMP_BT_MAP_REGISTER_NOTIFICATION_REQ(obj):
	print('BT_MAP_REGISTER_NOTIFICATION_REQ')
	print('%d' % obj.mapcinst)
	print('%d' % obj.status)
def DUMP_BT_MAP_REGISTER_NOTIFICATION_CFM(obj):
	print('BT_MAP_REGISTER_NOTIFICATION_CFM')
	print('%d' % obj.mapcinst)
	print('%d' % obj.status)
def DUMP_BT_MAP_MESSAGE_NOTIFICATION_OFF_IND(obj):
	print('BT_MAP_MESSAGE_NOTIFICATION_OFF_IND')
	print('%d' % obj.mapcinst)
def DUMP_BT_MAP_MESSAGE_NOTIFICATION_IND(obj):
	print('BT_MAP_MESSAGE_NOTIFICATION_IND')
	print('%d' % obj.mapcinst)
	print('%d' % obj.type)
	print('%d' % obj.msgtype)
	print('%d' % obj.len)
	print('%s' % obj.handle)
def DUMP_BT_AT_SMS_CONNECTION_IND(obj):
	print('BT_AT_SMS_CONNECTION_IND')
	print('%d' % obj.did)
	print('%s' % obj.addr)
def DUMP_BT_AT_SMS_DISCONNECTION_IND(obj):
	print('BT_AT_SMS_DISCONNECTION_IND')
	print('%d' % obj.did)
	print('%s' % obj.addr)
def DUMP_BT_MSG_SUPPORT_SMS_FORMAT_REQ(obj):
	print('BT_MSG_SUPPORT_SMS_FORMAT_REQ')
	print('%d' % obj.did)
def DUMP_BT_MSG_SUPPORT_SMS_FORMAT_CFM(obj):
	print('BT_MSG_SUPPORT_SMS_FORMAT_CFM')
	print('%d' % obj.did)
	print('%d' % obj.status)
	print('%d' % obj.format)
def DUMP_BT_MSG_CURRENT_SMS_FORMAT_REQ(obj):
	print('BT_MSG_CURRENT_SMS_FORMAT_REQ')
	print('%d' % obj.did)
def DUMP_BT_MSG_CURRENT_SMS_FORMAT_CFM(obj):
	print('BT_MSG_CURRENT_SMS_FORMAT_CFM')
	print('%d' % obj.did)
	print('%d' % obj.status)
	print('%d' % obj.format)
def DUMP_BT_MSG_SET_SMS_FORMAT_REQ(obj):
	print('BT_MSG_SET_SMS_FORMAT_REQ')
	print('%d' % obj.did)
	print('%d' % obj.format)
def DUMP_BT_MSG_SET_SMS_FORMAT_CFM(obj):
	print('BT_MSG_SET_SMS_FORMAT_CFM')
	print('%d' % obj.did)
	print('%d' % obj.status)
def DUMP_BT_MSG_GET_SUPPORT_SMS_STORAGE_REQ(obj):
	print('BT_MSG_GET_SUPPORT_SMS_STORAGE_REQ')
	print('%d' % obj.did)
def DUMP_BT_MSG_GET_SUPPORT_SMS_STORAGE_CFM(obj):
	print('BT_MSG_GET_SUPPORT_SMS_STORAGE_CFM')
	print('%d' % obj.status)
	print('%d' % obj.did)
	print('%d' % obj.storage)
def DUMP_BT_MSG_GET_CURRENT_SMS_STORAGE_REQ(obj):
	print('BT_MSG_GET_CURRENT_SMS_STORAGE_REQ')
	print('%d' % obj.did)
def DUMP_BT_MSG_GET_CURRENT_SMS_STORAGE_CFM(obj):
	print('BT_MSG_GET_CURRENT_SMS_STORAGE_CFM')
	print('%d' % obj.status)
	print('%d' % obj.did)
	print('%d' % obj.mem1used)
	print('%d' % obj.mem1total)
	print('%d' % obj.mem2used)
	print('%d' % obj.mem2total)
	print('%d' % obj.mem3used)
	print('%d' % obj.mem3total)
	print('%d' % obj.storage)
def DUMP_BT_MSG_SELECT_SMS_STORAGE_REQ(obj):
	print('BT_MSG_SELECT_SMS_STORAGE_REQ')
	print('%d' % obj.did)
	print('%d' % obj.mem1)
	print('%d' % obj.mem2)
	print('%d' % obj.mem3)
def DUMP_BT_MSG_SELECT_SMS_STORAGE_CFM(obj):
	print('BT_MSG_SELECT_SMS_STORAGE_CFM')
	print('%d' % obj.status)
	print('%d' % obj.did)
	print('%d' % obj.nem1used)
	print('%d' % obj.mem1total)
	print('%d' % obj.mem2used)
	print('%d' % obj.mem2total)
	print('%d' % obj.mem3used)
	print('%d' % obj.mem3total)
def DUMP_BT_MSG_GET_SUPPORT_LIST_SMS_REQ(obj):
	print('BT_MSG_GET_SUPPORT_LIST_SMS_REQ')
	print('%d' % obj.did)
def DUMP_BT_MSG_GET_SUPPORT_LIST_SMS_CFM(obj):
	print('BT_MSG_GET_SUPPORT_LIST_SMS_CFM')
	print('%d' % obj.did)
	print('%d' % obj.status)
	print('%d' % obj.format)
def DUMP_BT_MSG_LIST_SMS_REQ(obj):
	print('BT_MSG_LIST_SMS_REQ')
	print('%d' % obj.did)
	print('%d' % obj.stat)
def DUMP_BT_MSG_LIST_SMS_CFM(obj):
	print('BT_MSG_LIST_SMS_CFM')
	print('%d' % obj.did)
	print('%d' % obj.status)
def DUMP_BT_MSG_GET_CONTENT_IND(obj):
	print('BT_MSG_GET_CONTENT_IND')
	print('%d' % obj.did)
	print('%d' % obj.format)
	print('%d' % obj.addrlen)
	print('%s' % obj.address)
	print('%d' % obj.datalen)
	print('%s' % obj.data)
def DUMP_BT_MSG_GET_CONTENT_COMPLETED_IND(obj):
	print('BT_MSG_GET_CONTENT_COMPLETED_IND')
	print('%d' % obj.did)
	print('%d' % obj.status)
def DUMP_BT_MSG_READ_SMS_REQ(obj):
	print('BT_MSG_READ_SMS_REQ')
	print('%d' % obj.did)
	print('%d' % obj.index)
def DUMP_BT_MSG_READ_SMS_CFM(obj):
	print('BT_MSG_READ_SMS_CFM')
	print('%d' % obj.did)
	print('%d' % obj.status)
def DUMP_BT_MSG_DELETE_SMS_REQ(obj):
	print('BT_MSG_DELETE_SMS_REQ')
	print('%d' % obj.did)
	print('%d' % obj.index)
def DUMP_BT_MSG_DELETE_SMS_CFM(obj):
	print('BT_MSG_DELETE_SMS_CFM')
	print('%d' % obj.did)
	print('%d' % obj.status)
def DUMP_BT_MSG_SET_SMS_NOTIFICATION_REQ(obj):
	print('BT_MSG_SET_SMS_NOTIFICATION_REQ')
	print('%d' % obj.did)
	print('%d' % obj.state)
def DUMP_BT_MSG_SET_SMS_NOTIFICATION_CFM(obj):
	print('BT_MSG_SET_SMS_NOTIFICATION_CFM')
	print('%d' % obj.did)
	print('%d' % obj.status)
def DUMP_BT_MSG_SEND_SMS_REQ(obj):
	print('BT_MSG_SEND_SMS_REQ')
	print('%d' % obj.did)
	print('%d' % obj.addrlen)
	print('%s' % obj.address)
	print('%d' % obj.datalen)
	print('%s' % obj.data)
def DUMP_BT_MSG_SEND_SMS_CFM(obj):
	print('BT_MSG_SEND_SMS_CFM')
	print('%d' % obj.did)
	print('%d' % obj.status)
def DUMP_BT_HID_CONNECT_REQ(obj):
	print('BT_HID_CONNECT_REQ')
	print('%s' % obj.addr)
def DUMP_BT_HID_CONNECT_CFM(obj):
	print('BT_HID_CONNECT_CFM')
	print('%d' % obj.status)
def DUMP_BT_HID_DISCONNECT_REQ(obj):
	print('BT_HID_DISCONNECT_REQ')
def DUMP_BT_HID_DISCONNECT_CFM(obj):
	print('BT_HID_DISCONNECT_CFM')
	print('%d' % obj.status)
def DUMP_BT_HID_DATA_REQ(obj):
	print('BT_HID_DATA_REQ')
	print('%d' % obj.key)
	print('%d' % obj.xref)
	print('%d' % obj.yref)
	print('%d' % obj.wheelref)
def DUMP_BT_HID_DATA_CFM(obj):
	print('BT_HID_DATA_CFM')
	print('%d' % obj.status)
def DUMP_BT_HID_STATUS_IND(obj):
	print('BT_HID_STATUS_IND')
	print('%s' % obj.deviceaddr)
	print('%d' % obj.status)
