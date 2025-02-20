from sklearn.ensemble import GradientBoostingClassifier, AdaBoostClassifier, ExtraTreesClassifier
from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from xgboost import XGBClassifier
from lightgbm import LGBMClassifier
from catboost import CatBoostClassifier


class ModelClassifier:
    def __init__(self):
        self.models = {
            'Gradient Boosting': self.get_gradient_boosting,
            'Ada Boost': self.get_ada_boost,
            'Extra Trees': self.get_extra_trees,
            'Quadratic Discriminant Analysis': self.get_quadratic_discriminant,
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
        gb_model = GradientBoostingClassifier()
        gb_model.fit(X_train, y_train)

        y_pred = gb_model.predict(X_test)

        return y_pred

    @staticmethod
    def get_ada_boost(X_train, X_test, y_train):
        gb_model = AdaBoostClassifier()
        gb_model.fit(X_train, y_train)

        y_pred = gb_model.predict(X_test)

        return y_pred

    @staticmethod
    def get_extra_trees(X_train, X_test, y_train):
        gb_model = ExtraTreesClassifier()
        gb_model.fit(X_train, y_train)

        y_pred = gb_model.predict(X_test)

        return y_pred

    @staticmethod
    def get_quadratic_discriminant(X_train, X_test, y_train):
        gb_model = QuadraticDiscriminantAnalysis()
        gb_model.fit(X_train, y_train)

        y_pred = gb_model.predict(X_test)

        return y_pred

    @staticmethod
    def get_k_neighbors(X_train, X_test, y_train):
        gb_model = KNeighborsClassifier()
        gb_model.fit(X_train, y_train)

        y_pred = gb_model.predict(X_test)

        return y_pred

    @staticmethod
    def get_decision_tree(X_train, X_test, y_train):
        gb_model = DecisionTreeClassifier()
        gb_model.fit(X_train, y_train)

        y_pred = gb_model.predict(X_test)

        return y_pred

    @staticmethod
    def get_svm(X_train, X_test, y_train):
        gb_model = SVC()
        gb_model.fit(X_train, y_train)

        y_pred = gb_model.predict(X_test)

        return y_pred

    @staticmethod
    def get_extreme_gbm(X_train, X_test, y_train):
        gb_model = XGBClassifier()
        gb_model.fit(X_train, y_train)

        y_pred = gb_model.predict(X_test)

        return y_pred

    @staticmethod
    def get_light_gbm(X_train, X_test, y_train):
        gb_model = LGBMClassifier()
        gb_model.fit(X_train, y_train)

        y_pred = gb_model.predict(X_test)

        return y_pred

    @staticmethod
    def get_cat_boost(X_train, X_test, y_train):
        gb_model = CatBoostClassifier()
        gb_model.fit(X_train, y_train)

        y_pred = gb_model.predict(X_test)

        return y_pred
