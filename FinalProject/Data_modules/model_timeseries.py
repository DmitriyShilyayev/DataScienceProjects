from pycaret.time_series import TSForecastingExperiment
from pmdarima import auto_arima


class ModelTimeSeries:
    def __init__(self):
        self.models = {
            'Pycaret': self.get_pycaret,
            'Auto ARIMA': self.get_auto_arima,
        }
        self.params = {
            'Pycaret': {},
            'Auto ARIMA': {},
        }

    def get_all_models(self, X):
        result = {}
        for model in self.models:
            result[model] = self.models[model](X)
        return result
    
    @staticmethod
    def get_pycaret(X):
        model = TSForecastingExperiment()
        model_exp = model.setup(data=X, index='date', target='value', fh = 100)

        best_model = model_exp.compare_models()
        model = model_exp.create_model(best_model)
        
        y_pred = model_exp.predict_model(model, fh = 100)

        return {'model': model, 'predict': y_pred}
    
    @staticmethod
    def get_auto_arima(X):
        model = auto_arima(y=X['value'])

        
        y_pred = model.predict(100)

        return {'model': model, 'predict': y_pred}
