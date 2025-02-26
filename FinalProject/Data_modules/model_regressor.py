from sklearn.ensemble import GradientBoostingRegressor, AdaBoostRegressor, ExtraTreesRegressor
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.svm import SVR
from xgboost import XGBRegressor
from lightgbm import LGBMRegressor
from catboost import CatBoostRegressor


class ModelRegressor:
    def __init__(self):
        self.models = {
            'Gradient Boosting': self.get_gradient_boosting,
            'Ada Boost': self.get_ada_boost,
            'Extra Trees': self.get_extra_trees,
            'K Neighbors': self.get_k_neighbors,
            'Decision Tree': self.get_decision_tree,
            'SVM': self.get_svm,
            'eXtreme GBM': self.get_extreme_gbm,
            'Light GBM': self.get_light_gbm,
            'Cat Boost': self.get_cat_boost
        }
        self.params = {
            'Gradient Boosting': {},
            'Ada Boost': {},
            'Extra Trees': {},
            'K Neighbors': {},
            'Decision Tree': {},
            'SVM': {},
            'eXtreme GBM': {},
            'Light GBM': {},
            'Cat Boost': {}
        }

    def get_all_models(self, X_train, X_test, y_train):
        result = {}
        for model in self.models:
            result[model] = self.models[model](X_train, X_test, y_train)
        return result
    
    @staticmethod
    def get_gradient_boosting(X_train, X_test, y_train):
        model = GradientBoostingRegressor()
        model.fit(X_train, y_train)

        y_pred = model.predict(X_test)

        return {'model': model, 'predict': y_pred}

    @staticmethod
    def get_ada_boost(X_train, X_test, y_train):
        model = AdaBoostRegressor()
        model.fit(X_train, y_train)

        y_pred = model.predict(X_test)

        return {'model': model, 'predict': y_pred}

    @staticmethod
    def get_extra_trees(X_train, X_test, y_train):
        model = ExtraTreesRegressor()
        model.fit(X_train, y_train)

        y_pred = model.predict(X_test)

        return {'model': model, 'predict': y_pred}

    @staticmethod
    def get_k_neighbors(X_train, X_test, y_train):
        model = KNeighborsRegressor()
        model.fit(X_train, y_train)

        y_pred = model.predict(X_test)

        return {'model': model, 'predict': y_pred}

    @staticmethod
    def get_decision_tree(X_train, X_test, y_train):
        model = DecisionTreeRegressor()
        model.fit(X_train, y_train)

        y_pred = model.predict(X_test)

        return {'model': model, 'predict': y_pred}

    @staticmethod
    def get_svm(X_train, X_test, y_train):
        model = SVR()
        model.fit(X_train, y_train)

        y_pred = model.predict(X_test)

        return {'model': model, 'predict': y_pred}

    @staticmethod
    def get_extreme_gbm(X_train, X_test, y_train):
        model = XGBRegressor()
        model.fit(X_train, y_train)

        y_pred = model.predict(X_test)

        return {'model': model, 'predict': y_pred}

    @staticmethod
    def get_light_gbm(X_train, X_test, y_train):
        model = LGBMRegressor()
        model.fit(X_train, y_train)

        y_pred = model.predict(X_test)

        return {'model': model, 'predict': y_pred}

    @staticmethod
    def get_cat_boost(X_train, X_test, y_train):
        model = CatBoostRegressor()
        model.fit(X_train, y_train)

        y_pred = model.predict(X_test)

        return {'model': model, 'predict': y_pred}
