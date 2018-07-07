def format_columns(df):

    '''formats columns by
    1. remove whitestrip from columns
    2. rename: all values lowercase
    3. rename: all column headers lowercase
    '''
    # rename: remove whitestrip from columns
    df = df.rename(columns=lambda x: x.strip())
    
    # rename: all column headers lowercase
    df.columns = map(str.lower, df.columns)
    
    # rename: all values lowercase
    df = df.apply(lambda x: x.astype(str).str.lower())

    return df