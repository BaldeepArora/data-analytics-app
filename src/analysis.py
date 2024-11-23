import pandas as pd

def run_analysis():
    # Load data
    data = pd.read_csv('data/sample.csv')
    
    # Perform analysis: calculate mean of 'Salary'
    if 'Salary' in data.columns:
        mean_value = data['Salary'].mean()
    else:
        raise KeyError("'Salary' column not found in the data")
    
    return {'mean': mean_value}
