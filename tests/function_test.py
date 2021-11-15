from re import X
from toolbox.functions import initialize_model

def init_model_test():
    assert initialize_model(X) != None
