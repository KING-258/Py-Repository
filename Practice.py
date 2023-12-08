import numpy as np
import pandas as pd
import matplotlib as plt
import seaborn as sns
def main():
    a = pd.date_range('20231029', periods=7)
    b = pd.DataFrame(np.arange(21).reshape([7,3]), index=a, columns=['A','B','C'])
    print(b)
if __name__ == "__main__" :
    main()