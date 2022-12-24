import os
import requests
import time
import random
from transitions.extensions import GraphMachine
from PIL import Image

from utils import send_text_message, send_image_url, channel_access_token

from data import *

class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)

    def is_going_to_user(self, event):
        text = event.message.text
        return text.lower() == "quit game"

    def play_game(self, event):
        text = event.message.text
        return text.lower() == "play"

    def output_character_image(self, event):
        text = event.message.text
        return text.lower() == "show my photo"

    def saving(self, event):
        text = event.message.text
        return text.lower() == "save"

    def no_save_check(self, event):
        text = event.message.text
        return text.lower() == "quit game"
    
    def open_new_game(self, event):
        text = event.message.text
        return text.lower() == "new game"

    def open_load_game(self, event):
        text = event.message.text
        return text.lower() == "load game"
    
    def create_new_player(self, event):
        text = event.message.text
        return text.lower() == "create"

    def meet_a_monster(self, event):
        text = event.message.text
        return text.lower() == "find monster"

    def on_fight(self, event):
        text = event.message.text
        return text.lower() == "fight"
    
    def draw_and_show_fsm(self, event):
        text = event.message.text
        return text.lower() == "show fsm"

    def on_enter_user(self, event):
        print("I'm entering user")

        reply_token = event.reply_token
        send_text_message(reply_token, "Trigger user")

    def on_enter_in_game(self, event):
        print("I'm entering state1")
        
        reply_token = event.reply_token
        if(get_level() == -1):
            send_text_message(reply_token, "No cahracter yet")
        else:
            send_text_message(reply_token, "Character's name : " + get_name() + "\nCharacter's level : " + str(get_level()))

    def on_enter_output_image(self, event):

        reply_token = event.reply_token

        if(get_level() == -1):
            send_text_message(reply_token, "No cahracter yet")
        else:
            r = requests.get("http://localhost:4040/api/tunnels")
            tunnels = r.json()['tunnels']
            
            for tunnel in tunnels:
                if tunnel['proto'] == "http" or tunnel['proto'] == "https":
                    print(str(tunnel['public_url']) +  "/get_image?value=" + get_photo())
                    send_image_url(reply_token, (str(tunnel['public_url']) +  "/get_image?value=" + get_photo()))
                    break

        self.go_back()

    def on_exit_output_image(self):
        print("Leaving image")

    def on_enter_save(self, event):
        print("I'm entering state2")

        save()

        reply_token = event.reply_token

        send_text_message(reply_token, "Save Success!")

    def on_enter_no_save(self, event):
        print("I'm entering state3")

        reply_token = event.reply_token
        send_text_message(reply_token, "Not save yet!")

    def on_enter_new_game(self, event):
        print("I'm entering state4")

        reset()

        reply_token = event.reply_token
        send_text_message(reply_token, "open a new game")

    def on_enter_load_game(self, event):
        print("I'm entering state5")

        load()

        reply_token = event.reply_token
        send_text_message(reply_token, "loading game")

    def on_enter_create_player(self, event):
        print("I'm entering state6")

        create()
        print(get_name())
        print(get_photo())

        reply_token = event.reply_token
        send_text_message(reply_token, "New character created named : " + get_name() + "\nCharacter's level : " + str(get_level()))

    def on_enter_meet_monster(self, event):
        print("I'm entering state7")
        
        reply_token = event.reply_token
        if(get_level() == -1):
            send_text_message(reply_token, "No cahracter yet")
        else:
            new_monster()
            send_text_message(reply_token, "Monster name : " + get_monster_name() + "\nMonster level : " + str(get_monster_level()))

    def on_enter_fighting(self, event):

        reply_token = event.reply_token

        if(get_level() == -1):
            send_text_message(reply_token, "No cahracter yet")
        elif(get_monster_level() == -1):
            send_text_message(reply_token, "No Monster yet")
        else:
            result = fight_with_monster()
            if(result == 1):
                send_text_message(reply_token, "Win!!\nCharacter's name : " + get_name() + "\nCharacter's level : " + str(get_level()))
            else:
                send_text_message(reply_token, "Lose\nYour character died, please create new character.")

        self.go_back()

    def on_enter_draw(self, event):
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

    def on_exit_draw(self):
        print("Leaving fsm")
