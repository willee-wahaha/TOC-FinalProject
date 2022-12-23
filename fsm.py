import os
import requests
import time
from transitions.extensions import GraphMachine
from PIL import Image

from utils import send_text_message, send_image_url, channel_access_token

#need change
class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)

    def is_going_to_user(self, event):
        text = event.message.text
        return text.lower() == "go to user"

    def is_going_to_state1(self, event):
        text = event.message.text
        return text.lower() == "go to state1"

    def is_going_to_state2(self, event):
        text = event.message.text
        return text.lower() == "go to state2"

    def is_going_to_state3(self, event):
        text = event.message.text
        return text.lower() == "go to state3"
    
    def is_going_to_state4(self, event):
        text = event.message.text
        return text.lower() == "go to state4"

    def is_going_to_state5(self, event):
        text = event.message.text
        return text.lower() == "go to state5"
    
    def is_going_to_state6(self, event):
        text = event.message.text
        return text.lower() == "go to state6"

    def is_going_to_state7(self, event):
        text = event.message.text
        return text.lower() == "go to state7"
    
    def is_going_to_state8(self, event):
        text = event.message.text
        return text.lower() == "fsm"

    def on_enter_user(self, event):
        print("I'm entering user")

        reply_token = event.reply_token
        send_text_message(reply_token, "Trigger user")

    def on_enter_state1(self, event):
        print("I'm entering state1")

        reply_token = event.reply_token
        send_text_message(reply_token, "Trigger state1")

    def on_enter_state2(self, event):
        print("I'm entering state2")

        reply_token = event.reply_token
        
        r = requests.get("http://localhost:4040/api/tunnels")
        tunnels = r.json()['tunnels']
        
        for tunnel in tunnels:
            if tunnel['proto'] == "http" or tunnel['proto'] == "https":
                send_image_url(reply_token, (str(tunnel['public_url']) +  "/get_image?value=FR9W2eDXoAAMv-j"))
                break
        #send_text_message(reply_token, "Trigger state2")

    def on_enter_state3(self, event):
        print("I'm entering state3")

        reply_token = event.reply_token
        send_text_message(reply_token, "Trigger state3")

    def on_enter_state4(self, event):
        print("I'm entering state4")

        reply_token = event.reply_token
        send_text_message(reply_token, "Trigger state4")

    def on_enter_state5(self, event):
        print("I'm entering state5")

        reply_token = event.reply_token
        send_text_message(reply_token, "Trigger state5")

    def on_enter_state6(self, event):
        print("I'm entering state6")

        reply_token = event.reply_token
        send_text_message(reply_token, "Trigger state6")

    def on_enter_state7(self, event):
        print("I'm entering state7")

        reply_token = event.reply_token
        send_text_message(reply_token, "Trigger state7")

    def on_enter_state8(self, event):
        print("I'm entering state8")

        reply_token = event.reply_token
        err_mes = ""
        try:
            err_mes = "draw fsm"
            requests.get("http://localhost:8000/show-fsm")

            err_mes = "open image"
            image = Image.open('fsm.png')
            file_name = str(int(time.time()))
            
            err_mes = "link to route"
            app_root = os.path.dirname(os.path.abspath(__file__))
            static_dir = os.path.join(app_root, 'image')
            err_mes = "save image"
            image.save(os.path.join(static_dir, file_name + '.png'))

            err_mes = "get current ip"
            r = requests.get("http://localhost:4040/api/tunnels")
            tunnels = r.json()['tunnels']
            
            err_mes = "get ip list"
            for tunnel in tunnels:
                if tunnel['proto'] == "http" or tunnel['proto'] == "https":
                    err_mes = "send message"
                    send_image_url(reply_token, (str(tunnel['public_url']) +  "/get_image?value=" + file_name))
                    break
        except:
            send_text_message(reply_token, "Error : " + err_mes)
        
        

        self.go_back()

    def on_exit_state8(self):
        print("Leaving state8")
