import requests
import json
import requests
import json

class AttackCommand:
    def __init__(self, block_id, target_x, target_y):
        self.block_id = block_id
        self.target = {
            'x': target_x,
            'y': target_y
        }

    def to_dict(self):
        return {
            'blockId': self.block_id,
            'target': self.target
        }

class BuildCommand:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def to_dict(self):
        return {
            'x': self.x,
            'y': self.y
        }

class MoveBaseCommand:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def to_dict(self):
        return {
            'x': self.x,
            'y': self.y
        }
    
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
            'attack': [],
            'moveBase': []
        }

# Инициализация отправителя команд
api_key = '668eaa760f55f668eaa760f563'
url = 'https://example.com/api/endpoint'
command_sender = CommandSender(api_key, url)

# Создание команд
build_command = BuildCommand(x=10, y=20)
# attack_command = AttackCommand(block_id='some-uuid', target_x=5, target_y=15)

# Добавление команд в отправитель
command_sender.add_command('build', build_command.to_dict())
# command_sender.add_command('attack', attack_command.to_dict())

# Отправка команд
command_sender.send_commands()
