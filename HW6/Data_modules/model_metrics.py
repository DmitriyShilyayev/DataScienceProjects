from sklearn.metrics import accuracy_score, classification_report, confusion_matrix, mean_squared_error, mean_absolute_error, r2_score

class ModelMetrics:
    def __init__(self):
        self.result = {'classification' : {}, 'regression': {}}
        return
    
    def get_classification_models_metrics(self, y_test, models):
        for model in models:
            self.result['classification'][model] = self.get_classification_model_metrics(y_test, models[model]['predict'])
            print('----------------------')
            print(f'{model} model metrics:')
            print(f"Model accuracy: {self.result['classification'][model]['accuracy']:.4f}")
            print("Classification Report:")
            print(self.result['classification'][model]['report'])
            print("Confusion Matrix:")
            print(self.result['classification'][model]['matrix'])
            print('----------------------')
        return self.result['classification']
    
    def get_all_models_accuracy(self):
        if len(self.result) > 0:
            accuracy_arr = {}
            for model in self.result['classification']:
                accuracy_arr[model] = "{:.4f}".format(self.result['classification'][model]['accuracy'])
            return dict(sorted(accuracy_arr.items(), key=lambda item: item[1]))
        else:
            print('Please, run models accuracy test before.')
    
    @staticmethod
    def get_classification_model_metrics(y_test, y_pred):
        accuracy = accuracy_score(y_test, y_pred)
        cl_report = classification_report(y_test, y_pred)
        conf_matrix = confusion_matrix(y_test, y_pred)
        return {'accuracy': accuracy, 'report': cl_report, 'matrix': conf_matrix}
    
    def get_regression_models_metrics(self, y_test, models):
        for model in models:
            self.result['regression'][model] = self.get_regression_model_metrics(y_test, models[model]['predict'])
            print('----------------------')
            print(f'{model} model metrics:')
            print(f"MSE: {self.result['regression'][model]['mse']:.4f}")
            print(f"MAE: {self.result['regression'][model]['mae']:.4f}")
            print(f"R2: {self.result['regression'][model]['r2']:.4f}")
            print('----------------------')
        return self.result['regression']
    
    def get_all_models_r2(self):
        if len(self.result) > 0:
            r2_arr = {}
            for model in self.result['regression']:
                r2_arr[model] = "{:.4f}".format(self.result['regression'][model]['r2'])
            return dict(sorted(r2_arr.items(), key=lambda item: item[1]))
        else:
            print('Please, run models accuracy test before.')
    
    @staticmethod
    def get_regression_model_metrics(y_test, y_pred):
        mse = mean_squared_error(y_test, y_pred)
        mae = mean_absolute_error(y_test, y_pred)
        r2 = r2_score(y_test, y_pred)
        return {'mse': mse, 'mae': mae, 'r2': r2}