from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

class ModelMetrics:
    def __init__(self):
        self.result = {}
        return
    
    def get_all_models_metrics(self, y_test, models):
        for model in models:
            self.result[model] = self.get_one_model_metrics(y_test, models[model])
            print('----------------------')
            print(f'{model} model metrics:')
            print(f"Model accuracy: {self.result[model]['accuracy']:.4f}")
            print("Classification Report:")
            print(self.result[model]['report'])
            print("Confusion Matrix:")
            print(self.result[model]['matrix'])
            print('----------------------')
        return self.result
    
    def get_all_models_accuracy(self):
        if len(self.result) > 0:
            accuracy_arr = {}
            for model in self.result:
                accuracy_arr[model] = "{:.4f}".format(self.result[model]['accuracy'])
            return dict(sorted(accuracy_arr.items(), key=lambda item: item[1]))
        else:
            print('Please, run models accuracy test before.')
    
    @staticmethod
    def get_one_model_metrics(y_test, y_pred):
        accuracy = accuracy_score(y_test, y_pred)
        cl_report = classification_report(y_test, y_pred)
        conf_matrix = confusion_matrix(y_test, y_pred)
        return {'accuracy': accuracy, 'report': cl_report, 'matrix': conf_matrix}