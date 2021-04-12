from math import log
from pprint import pprint

from hyperopt import hp
from hyperopt.pyll.stochastic import sample
from xgboost import XGBClassifier as XGB

from hyperband import settings
from hyperband.commons.helper import (
    handle_integers,
    load_data,
    train_and_eval_sklearn_classifier,
)

data = load_data()

trees_per_iteration = settings.XGB_TREES_PER_ITERATION

space = {
    "learning_rate": hp.choice("lr", ["default", hp.uniform("lr_", 0.01, 0.2)]),
    "max_depth": hp.choice("md", ["default", hp.quniform("md_", 2, 10, 1)]),
    "min_child_weight": hp.choice("mcw", ["default", hp.quniform("mcw_", 1, 10, 1)]),
    "subsample": hp.choice("ss", ["default", hp.uniform("ss_", 0.5, 1.0)]),
    "colsample_bytree": hp.choice("cbt", ["default", hp.uniform("cbt_", 0.5, 1.0)]),
    "colsample_bylevel": hp.choice("cbl", ["default", hp.uniform("cbl_", 0.5, 1.0)]),
    "gamma": hp.choice("g", ["default", hp.uniform("g_", 0, 1)]),
    "reg_alpha": hp.choice("ra", ["default", hp.loguniform("ra_", log(1e-10), log(1))]),
    "reg_lambda": hp.choice("rl", ["default", hp.uniform("rl_", 0.1, 10)]),
    "base_score": hp.choice("bs", ["default", hp.uniform("bs_", 0.1, 0.9)]),
    "scale_pos_weight": hp.choice("spw", ["default", hp.uniform("spw", 0.1, 10)]),
}


def get_params():
    """El objetivo de esta funcion es seleccionar aleatoriamente una configuracion
    determinada.

    :returns:
        Retorna una configuracion para el modelo correspondiente.
    """
    params = sample(space)
    params = {k: v for k, v in params.items() if v is not "default"}
    return handle_integers(params)


def try_params(n_iterations, params):
    """El objetivo de esta funcion es evaluar las diferentes configuraciones
    obtenidas de la muestra.

    :param n_iterations:
        Aumento de estimadores del arbol que se agregaran por iteracion.

    :param params:
        Configuracion para el modelo correspondiente.

    :returns:
        Retorna la configuracion con el tratamiento correspondiente.
    """
    n_estimators = int(round(n_iterations * trees_per_iteration))
    print("n_estimators:", n_estimators)
    pprint(params)

    clf = XGB(n_estimators=n_estimators, nthread=-1, **params)

    return train_and_eval_sklearn_classifier(clf, data)
