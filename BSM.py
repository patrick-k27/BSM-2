import streamlit as st
import numpy as np
from scipy.stats import norm

def black_scholes(S, X, T, r, sigma, option_type='call'):
    d1 = (np.log(S / X) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    
    if option_type == 'call':
        price = S * norm.cdf(d1) - X * np.exp(-r * T) * norm.cdf(d2)
    elif option_type == 'put':
        price = X * np.exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1)
    else:
        raise ValueError("Invalid option type. Use 'call' or 'put'.")
    
    return price

# Streamlit App
st.title('Black-Scholes Option Pricing Model')

st.sidebar.header('Input Parameters')
S = st.sidebar.number_input('Current Stock Price (S)', min_value=0.0, value=100.0)
X = st.sidebar.number_input('Strike Price (X)', min_value=0.0, value=100.0)
T = st.sidebar.number_input('Time to Maturity (T, in years)', min_value=0.0, value=1.0)
r = st.sidebar.number_input('Risk-free Interest Rate (r)', min_value=0.0, max_value=1.0, value=0.05)
sigma = st.sidebar.number_input('Volatility (σ)', min_value=0.0, max_value=1.0, value=0.2)
option_type = st.sidebar.selectbox('Option Type', ('call', 'put'))

price = black_scholes(S, X, T, r, sigma, option_type)

st.write(f'The {option_type} option price is: ${price:.2f}')
