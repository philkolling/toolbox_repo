from tensorflow.keras import Sequential, layers


def initialize_model(X):

    # Model architecture
    model = Sequential()
    model.add(layers.Dense(20, activation='relu', input_dim=X.shape[1]))
    model.add(layers.Dense(15, activation='relu'))
    model.add(layers.Dense(15, activation='relu'))
    model.add(layers.Dense(20, activation='relu'))
    model.add(layers.Dense(1, activation='linear'))

    # Recommended compilator hyperparams
    model.compile(
        optimizer='adam',
        loss='msle',  # we directly optimize for the kaggle's metric!
    )

    return model
