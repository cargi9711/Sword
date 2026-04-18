class Blade:
    def __init__(self, material, sharpness):
        self.material = material
        self.sharpness = sharpness

    def cut(self):
        return f"The {self.material} blade cuts with sharpness {self.sharpness}."
