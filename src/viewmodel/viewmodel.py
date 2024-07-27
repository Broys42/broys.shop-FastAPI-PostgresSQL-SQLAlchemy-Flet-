from src.viewmodel.headphones import HeadphonesViewModel
from src.model.model import Model


class ViewModel():
    def __init__(self, model: Model):
        self.model = model
        self.headphones = HeadphonesViewModel(model)
