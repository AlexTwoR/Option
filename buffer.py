
    

def vanilla_call_price(S, K, r, v, T):
    """Price of a European call option struck at K, with spot S, 
    constant rate r, constant vol v (over the life of the option) and time to maturity T"""
    return S*sto.norm_cdf(d_j(1, S, K, r, v, T))-K*exp(-r*T) * sto.norm_cdf(d_j(2, S, K, r, v, T))
    
def vanilla_put_price(S, K, r, v, T):
    """Price of a European put option struck at K, with spot S, 
    constant rate r, constant vol v (over the life of the option) and time to maturity T"""
    return -S*sto.norm_cdf(-d_j(1, S, K, r, v, T))+K*exp(-r*T) * sto.norm_cdf(-d_j(2, S, K, r, v, T))
    
