import numpy as np
from sklearn.datasets import make_classification
from sklearn.metrics import accuracy_score, log_loss, roc_auc_score
from sklearn.model_selection import train_test_split

from hyperband import settings


def load_data():
    """El objetivo de esta funcion es devolver un dataset
    para un problema de clasificacion.

    :returns:
        Retorna un diccionario con los datos para el entrenamiento.
    """

    data = {}

    data["X"], data["y"] = make_classification(
        n_samples=settings.DS_N_SAMPLES,
        n_features=settings.DS_N_FEATURES,
        n_classes=settings.DS_N_CLASS,
        n_informative=4,
        n_redundant=1,
        n_repeated=2,
        random_state=1,
    )
    return data


def handle_integers(params):
    """El objetivo de esta funcion es evitar que en el futuro
    haya problema con el tipo de datos para los parametros.

    :param params:
        Configuracion a evaluar.

    :returns:
        Retorna la configuracion con el tratamiento correspondiente.
    """
    new_params = {}
    for k, v in params.items():
        if type(v) == float and int(v) == v:
            new_params[k] = int(v)
        else:
            new_params[k] = v
    return new_params


def train_and_eval_sklearn_classifier(clf, data):
    """El objetivo de esta funcion es evaluar una configuracion determinada.

    :param clf:
        Modelo a entrenar.

    :param data:
        Dataset para entrenar al modelo.

    :returns:
        Retorna un diccionario con los score correspondientes de evaluacion.
    """
    X = data["X"]
    y = data["y"]

    x_train, x_test, y_train, y_test = train_test_split(X, y)
    clf.fit(x_train, y_train)

    try:
        p = clf.predict_proba(x_train)[:, 1]  # sklearn convention
    except IndexError:
        p = clf.predict_proba(x_train)

    ll = log_loss(y_train, p)
    auc = roc_auc_score(y_train, p)
    acc = accuracy_score(y_train, np.round(p))

    print(
        "\n# training | log loss: {:.2%}, AUC: {:.2%}, accuracy: {:.2%}".format(
            ll, auc, acc
        )
    )

    try:
        p = clf.predict_proba(x_test)[:, 1]  # sklearn convention
    except IndexError:
        p = clf.predict_proba(x_test)

    ll = log_loss(y_test, p)
    auc = roc_auc_score(y_test, p)
    acc = accuracy_score(y_test, np.round(p))

    print(
        "# testing  | log loss: {:.2%}, AUC: {:.2%}, accuracy: {:.2%}".format(
            ll, auc, acc
        )
    )

    return {"loss": ll, "log_loss": ll, "auc": auc}
