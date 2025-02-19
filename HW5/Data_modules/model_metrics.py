from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

class ModelMetrics:
    def __init__(self):
        self.result = {}
        return
    
    def get_all_models_metrics(self, y_test, models):
        for model in models:
            self.result[model] = self.get_one_model_metrics(y_test, models[model])
            print('----------------------')
            print(f'{model} model metrics:')
            print(f"MSE: {self.result[model]['mse']:.4f}")
            print(f"MAE: {self.result[model]['mae']:.4f}")
            print(f"R2: {self.result[model]['r2']:.4f}")
            print('----------------------')
        return self.result
    
    def get_all_models_r2(self):
        if len(self.result) > 0:
            r2_arr = {}
            for model in self.result:
                r2_arr[model] = "{:.4f}".format(self.result[model]['r2'])
            return dict(sorted(r2_arr.items(), key=lambda item: item[1]))
        else:
            print('Please, run models accuracy test before.')
    
    @staticmethod
    def get_one_model_metrics(y_test, y_pred):
        mse = mean_squared_error(y_test, y_pred)
        mae = mean_absolute_error(y_test, y_pred)
        r2 = r2_score(y_test, y_pred)
        return {'mse': mse, 'mae': mae, 'r2': r2}