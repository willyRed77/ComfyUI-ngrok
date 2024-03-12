import ngrok
from comfy.cli_args import args
import paho.mqtt.publish as publish
# #########################################################
# Replace None on the line below this with your Authtoken.
# Your Authtoken can be found at https://dashboard.ngrok.com/get-started/your-authtoken
# Don't forget to enclose it in quotation marks!

ngrok_token = ""

# #########################################################

print("### Load ngrok")

def connect():
    # Connect if ngrok token is set
    if ngrok_token is not None:
        print("trying to connect ngrok...\n")
        options = {"authtoken": ngrok_token, "session_metadata": "ComfyUI"}
        print("------------------------")
        print(f"{args.listen}:{args.port}")
        try:
            ngrok_url = ngrok.forward(f"{args.listen}:{args.port}", **options).url()
        except Exception as e:
            print("Failed to connect to ngrok.")
        else:
            print(f"\n\033[32m\033[1m##\n## Connection to ngrok established.\n##\n## URL: {ngrok_url}\n##\n\033[0m\033[0m")

            client_name = "comfyuiurl"
            host_name = "***.***.***.***"
            username = "******"
            password = "******"

            isRegistro = False

            topic_config = "homeassistant/sensor/comfyui/config"
            topic_state = "homeassistant/sensor/comfyui/state"
            retain = True  # "True" or "False"
            payload_config = '{"name": "Comfy UI MQTT", "state_topic": "homeassistant/sensor/comfyui/state", "unique_id": "comfyui_url_1", "device": {"identifiers": ["comfyui_i"], "name": "URL ComfyUI" }}'
            payload_state = ngrok_url

            if(isRegistro):
                topic = topic_config
                payload = payload_config
            else:
                topic = topic_state
                payload = payload_state

            broker_auth = {'username': username, 'password': password}
            publish.single(topic=topic, payload=payload, retain=retain,
                           hostname=host_name, client_id=client_name,
                           auth=broker_auth)


connect()
