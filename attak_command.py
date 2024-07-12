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
