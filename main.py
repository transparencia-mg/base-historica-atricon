import ipdb
from xlsx2csv import Xlsx2csv
from io import StringIO
import pandas as pd

file_path = 'W:/Silviana Aparecida de Faria/BASE_HISTORICA_ATRICON_201901_202306.xlsx'
def read_excel(path: str) -> pd.DataFrame:
    buffer = StringIO()
    Xlsx2csv(path, outputencoding="utf-8").convert(buffer)
    buffer.seek(0)
    df = pd.read_csv(buffer)
    return df

df = read_excel(file_path)
ipdb.set_trace(context=10)