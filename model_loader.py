import tensorflow as tf
from model_compile import compile_model
from SimuV1 import SimuV1
from SimuV2 import SimuV2
from SimuV3 import SimuV3
from SimuV4 import SimuV4
from SimuV5 import SimuV5

# Configurações de cada modelo: classe e hidden_dim
MODEL_CONFIGS = {
    0: (SimuV1, 128),
    1: (SimuV2, 256),
    2: (SimuV3, 128),
    3: (SimuV4, 256),
    4: (SimuV5, 128),
    5: (SimuV5, 256),
}

def load_model(index, learning_rate):
    if index not in MODEL_CONFIGS:
        raise ValueError(f"[FATAL] Índice de modelo inválido: {index}")

    model_class, hidden_dim = MODEL_CONFIGS[index]
    model = model_class(hidden_dim=hidden_dim)
    model = compile_model(model, lr=learning_rate)

    # Removido: chamada com dummy_input que causava problemas de shape
    # A inicialização real deve ser feita no main.py com X_train

    return model
