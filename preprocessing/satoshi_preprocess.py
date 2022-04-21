from .base_preprocess import PreProcess
from sympy import isprime

class SatoshiPreprocess(PreProcess):   
    def transform(self, df):
        df['even_number'] = df['b'] % 2 # result == 0 is odd
        df['prime_number'] = df['b'].apply(isprime)
        df['odd_number'] = df['b'] % 2 # result > 0 is odd

        data = {
            'max_number': df['b'].max(),
            'min_number': df['b'].min(),
            'first_number': df.iloc[0, 1], 
            'last_number': df.iloc[-1, 1], 
            'number_of_prime_numbers': len(df[df['prime_number'] == True]), 
            'number_of_even_numbers': len(df[df['even_number'] == 0]), 
            'number_of_odd_numbers': len(df[df['odd_number'] > 0])
        }

        return data
