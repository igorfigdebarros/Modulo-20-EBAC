import pandas as pd
import seaborn as sns
gasolina_df = pd.read_csv('gasolina.csv', sep=',')
gasolina_df
grafico = sns.lineplot(data=gasolina_df, x='dia',y='venda')
grafico.get_figure().savefig('gasolina.png')
!touch ./gasolina.py