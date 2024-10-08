import pandas as pd

def load_csv(file_path):
    df = pd.read_csv(file_path)
    return df

def describe_data(df):
    return df.describe().to_html(classes='table table-striped table-bordered')

def head_data(df):
    return df.head().to_html(classes='table table-striped table-bordered')

def no_columns(df):
    return ','.join(df.columns)

def get_row(df,row_number):
    try:
        return df.iloc[[row_number]].to_html(classes='table table-striped table-bordered')
    except IndexError:
        return f"Invalid row  Number Please choose a Row netween 0 t0 {len(df)-1}"
    
def help_command():
    help_text = (
        "<h4>Available Commands:</h4>"
        "<ul>"
        "<li><strong>describe</strong>: Get summary statistics of the dataset.</li>"
        "<li><strong>head</strong>: View the top rows of the dataset.</li>"
        "<li><strong>columns</strong>: List all column names in the dataset.</li>"
        "<li><strong>row &lt;number&gt;</strong>: View a specific row by number.</li>"
        "<li><strong>help</strong>: Show this list of available commands.</li>"
        "</ul>"
    )
    return help_text

    

