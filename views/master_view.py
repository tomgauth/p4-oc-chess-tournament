# This is the masterview. It can print anything


class MasterView:

    def custom_message(self, message):
        print(message)

    def get_input(self, prompt):
        input_ = input(prompt)
        return input_
