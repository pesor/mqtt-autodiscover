'''
MQTT Autodiscover Home Assistant
'''
KEY_TOPIC = 'topic'
KEY_PAYLOAD = 'payload'
KEY_RETAIN = 'retain'
KEY_QOS = 'qos'

retain = True
qos = 0

# Send discovery topics
def send_discovery_topics():

#    print("in send_discovery_topics")
    device_payload = {
        'identifiers': [f"{'Fronius Data Manager'}"],
        'manufacturer': "Fronius, programmed by Per Rose",
        'model':'IG Plus 60 V-2',   
        'name':  'Solar_Power',
        'sw_version':  '2.0.0'
    }
    entity_payloads = {
        'sensorname': {
            'name': 'Fronius',
            'unit_of_meas': ""
        },
        'timeStamp': {
            'name': 'Fronius_Date',
            'unit_of_meas': "",             
            'icon': 'mdi:calendar'
        },
        'FAC': {
            'name': 'Fronius_FAC',
            'unit_of_meas': "Hz", 
            'icon': 'mdi:metronome-tick', 
        }, 
        'IAC': {
            'name': 'Fronius_IAC',
            'unit_of_meas': "A", 
            'icon':'mdi:alpha-a-circle-outline'
        }, 
        'IDC': {
            'name': 'Fronius_IDC',
            'unit_of_meas': "A", 
            'icon':'mdi:alpha-a-circle-outline'
        }, 
        'PAC': {
            'name': 'Fronius_PAC',
            'unit_of_meas': "V", 
            'icon':'mdi:alpha-v-circle-outline'
        }, 
        'TOTAL_ENERGY': {
            'name': 'Fronius_TOTAL_ENERGY',
            'unit_of_meas': "kWh", 
            'icon':'mdi:solar-power'
        }, 
        'UAC': {
            'name': 'Fronius_UAC',
            'unit_of_meas': "V", 
            'icon':'mdi:alpha-v-circle-outline'
        }, 
         'UDC': {
            'name': 'Fronius_UDC',
            'unit_of_meas': "V", 
            'icon':'mdi:alpha-v-circle-outline'
        }, 
        'Day_Energy': {
            'name': 'Fronius_Day_Energy',
            'unit_of_meas': "kW", 
            'icon':'mdi:solar-power'
        }, 
        'YEAR_ENERGY': {
            'name': 'Fronius_YEAR_ENERGY',
            'unit_of_meas': "kW", 
            'icon':'mdi:solar-power'
        }, 
        'code': {
            'name': 'Fronius_code',
            'unit_of_meas': "", 
            'icon':'mdi:code-parentheses-box'
        }, 
        'reason': {
            'name': 'Fronius_reason',
            'unit_of_meas': "", 
            'icon':'mdi:message-alert-outline'
        }, 
         'UserMessage': {
            'name': 'Fronius_UserMessage',
            'unit_of_meas': "", 
            'icon':'mdi:message-alert-outline'
        }, 
         'MONTH_ENERGY': {
            'name': 'Fronius_MONTH_ENERGY',
            'unit_of_meas': "kWh", 
            'icon':'mdi:solar-power'
        }, 
         'Jan': {
            'name': 'Fronius_Jan',
            'unit_of_meas': "kW", 
            'icon':'mdi:solar-power'
        }, 
         'Feb': {
            'name': 'Fronius_Feb',
            'unit_of_meas': "kW", 
            'icon':'mdi:solar-power'
        }, 
         'Mar': {
            'name': 'Fronius_Mar',
            'unit_of_meas': "kW", 
            'icon':'mdi:solar-power'
        }, 
         'Apr': {
            'name': 'Fronius_Apr',
            'unit_of_meas': "kW", 
            'icon':'mdi:solar-power'
        }, 
         'Maj': {
            'name': 'Fronius_Maj',
            'unit_of_meas': "kW", 
            'icon':'mdi:solar-power'
        }, 
         'Jun': {
            'name': 'Fronius_Jun',
            'unit_of_meas': "kW", 
            'icon':'mdi:solar-power'
        }, 
         'Jul': {
            'name': 'Fronius_Jul',
            'unit_of_meas': "kW", 
            'icon':'mdi:solar-power'
        }, 
         'Aug': {
            'name': 'Fronius_Aug',
            'unit_of_meas': "kW", 
            'icon':'mdi:solar-power'
        }, 
         'Sep': {
            'name': 'Fronius_Sep',
            'unit_of_meas': "kW", 
            'icon':'mdi:solar-power'
        }, 
         'Okt': {
            'name': 'Fronius_Okt',
            'unit_of_meas': "kW", 
            'icon':'mdi:solar-power'
        }, 
         'Nov': {
            'name': 'Fronius_Nov',
            'unit_of_meas': "kW", 
            'icon':'mdi:solar-power'
        }, 
         'Dec': {
            'name': 'Fronius_Dec',
            'unit_of_meas': "kW", 
            'icon':'mdi:solar-power'
        }, 
         'lastTwelve': {
            'name': 'Fronius_lastTwelve',
            'unit_of_meas': "kW", 
            'icon':'mdi:solar-power'
        }, 
         'thirteen': {
            'name': 'Fronius_thirteen',
            'unit_of_meas': "kW", 
            'icon':'mdi:solar-power'
        }, 
         'fourteen': {
            'name': 'Fronius_fourteen',
            'unit_of_meas': "kW", 
            'icon':'mdi:solar-power'
        }, 
         'fifteen': {
            'name': 'Fronius_fifteen',
            'unit_of_meas': "kW", 
            'icon':'mdi:solar-power'
        }, 
         'sixteen': {
            'name': 'Fronius_sixteen',
            'unit_of_meas': "kW", 
            'icon':'mdi:solar-power'
        }, 
         'seventeen': {
            'name': 'Fronius_seventeen',
            'unit_of_meas': "kW", 
            'icon':'mdi:solar-power'
        }, 
         'eightteen': {
            'name': 'Fronius_eightteen',
            'unit_of_meas': "kW", 
            'icon':'mdi:solar-power'
        }, 
         'nineteen': {
            'name': 'Fronius_nineteen',
            'unit_of_meas': "kW", 
            'icon':'mdi:solar-power'
        }, 
         'twenty': {
            'name': 'Fronius_twenty',
            'unit_of_meas': "kW", 
            'icon':'mdi:solar-power'
        }, 
         'twentyone': {
            'name': 'Fronius_twentyone',
            'unit_of_meas': "kW", 
            'icon':'mdi:solar-power'
        }, 
         'twentytwo': {
            'name': 'Fronius_twentytwo',
            'unit_of_meas': "kW", 
            'icon':'mdi:solar-power'
        }, 
         'twentythree': {
            'name': 'Fronius_twentythree',
            'unit_of_meas': "kW", 
            'icon':'mdi:solar-power'
        }, 
         'twentyfour': {
            'name': 'Fronius_twentyfour',
            'unit_of_meas': "kW", 
            'icon':'mdi:solar-power'
        }, 
         'twentyfive': {
            'name': 'Fronius_twentyfive',
            'unit_of_meas': "kW", 
            'icon':'mdi:solar-power'
        }, 
 
 
    }
   
    for entity, entity_payload in entity_payloads.items():
        entity_payload['val_tpl'] = f"{{{{ value_json.now.{entity} }}}}"
        entity_payload['uniq_id'] = f"{'Fronius_'}{entity}"
        entity_payload['stat_t'] =  f"{'Fronius'}/{'online'}"
        entity_payload['dev'] = device_payload
        sensor_type = ("sensor")
        entity_topic = f"{'homeassistant'}/{sensor_type}/{'Fronius_'}/{entity}/config"
#        print( entity_topic, my_load)
#        payload=json.dumps(entity_payload)
        """Publish data to MQTT broker."""
        service_data = {
        KEY_TOPIC: entity_topic,
        KEY_PAYLOAD: str(entity_payload).replace("'", '"').replace("^", "'"),
        KEY_RETAIN: retain,
        KEY_QOS: qos,
    }

        hass.services.call("mqtt", "publish", service_data)  # noqa: F821

send_discovery_topics()   
