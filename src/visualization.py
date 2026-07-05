import seaborn as sns
import matplotlib.pyplot as plt

def correlation_heatmap(df):

    sns.heatmap(df.corr(), annot=True)

    plt.show()