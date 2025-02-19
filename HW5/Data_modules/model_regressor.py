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

    def get_all_models(self, X_train, X_test, y_train):
        result = {}
        for model in self.models:
            result[model] = self.models[model](X_train, X_test, y_train)
        return result
    
    @staticmethod
    def get_gradient_boosting(X_train, X_test, y_train):
        gb_model = GradientBoostingRegressor()
        gb_model.fit(X_train, y_train)

        y_pred = gb_model.predict(X_test)

        return y_pred

    @staticmethod
    def get_ada_boost(X_train, X_test, y_train):
        gb_model = AdaBoostRegressor()
        gb_model.fit(X_train, y_train)

        y_pred = gb_model.predict(X_test)

        return y_pred

    @staticmethod
    def get_extra_trees(X_train, X_test, y_train):
        gb_model = ExtraTreesRegressor()
        gb_model.fit(X_train, y_train)

        y_pred = gb_model.predict(X_test)

        return y_pred

    @staticmethod
    def get_k_neighbors(X_train, X_test, y_train):
        gb_model = KNeighborsRegressor()
        gb_model.fit(X_train, y_train)

        y_pred = gb_model.predict(X_test)

        return y_pred

    @staticmethod
    def get_decision_tree(X_train, X_test, y_train):
        gb_model = DecisionTreeRegressor()
        gb_model.fit(X_train, y_train)

        y_pred = gb_model.predict(X_test)

        return y_pred

    @staticmethod
    def get_svm(X_train, X_test, y_train):
        gb_model = SVR()
        gb_model.fit(X_train, y_train)

        y_pred = gb_model.predict(X_test)

        return y_pred

    @staticmethod
    def get_extreme_gbm(X_train, X_test, y_train):
        gb_model = XGBRegressor()
        gb_model.fit(X_train, y_train)

        y_pred = gb_model.predict(X_test)

        return y_pred

    @staticmethod
    def get_light_gbm(X_train, X_test, y_train):
        gb_model = LGBMRegressor()
        gb_model.fit(X_train, y_train)

        y_pred = gb_model.predict(X_test)

        return y_pred

    @staticmethod
    def get_cat_boost(X_train, X_test, y_train):
        gb_model = CatBoostRegressor()
        gb_model.fit(X_train, y_train)

        y_pred = gb_model.predict(X_test)

        return y_pred
