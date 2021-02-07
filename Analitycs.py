import pandas
import numpy

worst = pandas.read_csv("data_task3.csv", encoding='utf-8', sep='\t+', engine='python')
del worst['uid']
print(worst)

conditions = [
    (worst['jud'] > worst['cjud']) ,
    worst['jud'] < worst['cjud']]

choices = [worst['jud'], worst['cjud']]
worst['equals'] = numpy.select(conditions, choices, default=numpy.nan)
print(worst)

Fake = pandas.DataFrame (worst, columns=['login', 'jud', 'cjud', 'equals' ]).nsmallest(250000, 'equals')
print(Fake)
del Fake['jud']
del Fake['cjud']

Worstworker = Fake.groupby(by=['login']).sum().groupby(level=[0]).cumsum()
print(Worstworker)
Worstworker_TOP10= pandas.DataFrame (Worstworker, columns=[ 'equals' ]).nlargest(10, 'equals')
print(Worstworker_TOP10)