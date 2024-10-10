class Rhombus:
    def __init__(self, side, corner_a):
        self.side = side
        self.corner_a = corner_a
        self.corner_b = 180 - corner_a

    def __setattr__(self, key, value):
        if key == 'side' and value <= 0:
            raise ValueError('Side must be more than 0 cm')
        if key == 'corner_a' and (value <= 0 or value >= 180):
            raise ValueError('Corner "α" must be more than 0° and less than 180°')

        super().__setattr__(key, value)

    def __str__(self):
        result = (f'Side: {self.side} cm\n'
                  f'Corner "α": {self.corner_a}°\n'
                  f'Corner "β": {self.corner_b}°')
        return result
