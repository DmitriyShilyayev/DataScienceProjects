import matplotlib.pyplot as plt
import seaborn as sns
import math
from pandas import DataFrame

class Visualizer:
    def __init__(self):
        self.palette=['#FF0000', '#0000FF', '#008000', '#FFFF00', '#660066']
        sns.set(style="darkgrid")

    def show_histogram(self, data: DataFrame, column: str = '') -> None:
        if column:
            plt.figure(figsize=(10, 10))
            sns.histplot(data[column], color='lightblue', edgecolor='black').set_title(f'Histogram of {column}')
        else:
            fig, axes = plt.subplots(int(math.ceil(len(data.columns) / 2)), 2, figsize=(15, 50))
            kws = data.columns
            for kw, ax in zip(kws, axes.flat):
                sns.histplot(data=data, color='lightblue', x=kw, ax=ax)
                ax.set_title(f'Histogram of {kw}')
        plt.tight_layout()
        plt.show()

    def show_lineplot(self, data: DataFrame, x_column: str, y_column: str, hue: str = '') -> None:
        plt.figure(figsize=(10, 10))
        if hue:
            ax = sns.lineplot(data=data, x=x_column, y=y_column, hue=hue)
        else:
            ax = sns.lineplot(data=data, x=x_column, y=y_column)
        ax.set_xlabel(x_column)
        ax.set_ylabel(y_column)
        ax.set_title(f'Line Plot of {y_column} vs {x_column}')
        plt.tight_layout()
        plt.show()

    def show_pairplot(self, data: DataFrame, columns: list = list(), hue: str = '') -> None:
        if len(columns) == 0:
            columns = data.columns
        if hue:
            g = sns.pairplot(data[columns + [hue]], kind='kde', hue=hue, palette=self.palette, height=4)
            g.map_offdiag(sns.scatterplot)
        else:
            g = sns.pairplot(data[columns], palette=self.palette, height=4)
        plt.show()
