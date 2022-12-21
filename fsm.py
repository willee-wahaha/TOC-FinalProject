from transitions.extensions import GraphMachine

from utils import send_text_message

#need change
class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)

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
        return text.lower() == "go to state8"

    def on_enter_state1(self, event):
        print("I'm entering state1")

        reply_token = event.reply_token
        send_text_message(reply_token, "Trigger state1")
        self.go_back()

    def on_exit_state1(self):
        print("Leaving state1")

    def on_enter_state2(self, event):
        print("I'm entering state2")

        reply_token = event.reply_token
        send_text_message(reply_token, "Trigger state2")
        self.go_back()

    def on_exit_state2(self):
        print("Leaving state2")

    def on_enter_state3(self, event):
        print("I'm entering state3")

        reply_token = event.reply_token
        send_text_message(reply_token, "Trigger state3")
        self.go_back()

    def on_exit_state3(self):
        print("Leaving state3")

    def on_enter_state4(self, event):
        print("I'm entering state4")

        reply_token = event.reply_token
        send_text_message(reply_token, "Trigger state4")
        self.go_back()

    def on_exit_state4(self):
        print("Leaving state4")

    def on_enter_state5(self, event):
        print("I'm entering state5")

        reply_token = event.reply_token
        send_text_message(reply_token, "Trigger state5")
        self.go_back()

    def on_exit_state5(self):
        print("Leaving state5")

    def on_enter_state6(self, event):
        print("I'm entering state6")

        reply_token = event.reply_token
        send_text_message(reply_token, "Trigger state6")
        self.go_back()

    def on_exit_state6(self):
        print("Leaving state6")

    def on_enter_state7(self, event):
        print("I'm entering state7")

        reply_token = event.reply_token
        send_text_message(reply_token, "Trigger state7")
        self.go_back()

    def on_exit_state7(self):
        print("Leaving state7")

    def on_enter_state8(self, event):
        print("I'm entering state8")

        reply_token = event.reply_token
        send_text_message(reply_token, "Trigger state8")
        self.go_back()

    def on_exit_state8(self):
        print("Leaving state8")
