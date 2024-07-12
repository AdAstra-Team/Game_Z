import requests
import json

class CommandSender:
    def __init__(self, api_key, url):
        self.api_key = api_key
        self.url = url
        self.headers = {
            'X-Auth-Token': self.api_key,
            'Content-Type': 'application/json'
        }
        self.commands = {
            'build': [],
            'attack': [],
            'moveBase': []
        }

    def add_command(self, command_type, command):
        if command_type in self.commands:
            self.commands[command_type].append(command)
        else:
            raise ValueError("Unsupported command type")

    def send_commands(self):
        payload = {
            'build': self.commands['build'],
            'attack': self.commands['attack'],
            'moveBase': self.commands['moveBase']
        }
        response = requests.post(self.url, headers=self.headers, data=json.dumps(payload))
        if response.status_code == 200:
            print('Commands sent successfully')
        else:
            print('Failed to send commands:', response.status_code, response.text)
        # Clear commands after sending
        self.commands = {
            'build': [],
            'attack': []
        }
