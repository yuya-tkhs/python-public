import numpy as np



def equation( x ,P ,R ) :
    return P * x**( R + 1 ) + ( 1 - P ) - x



class fixed_amount():
 
    def __init__( self ,win_pct ,risk_reward ,risk_rate ):
        self.win_pct     = win_pct
        self.risk_reward = risk_reward
        self.risk_rate   = risk_rate
        if self.is_error() : raise
 
    def is_error( self ) :
        if self.win_pct     == 0 \
        or self.risk_reward == 0 \
        or self.risk_rate   == 0 :
            print(f'win: {win_pct}, rr: {risk_reward}, risk: {risk_rate}')
            return True
        elif not 0 <= self.win_pct <= 1   \
        or   not 0 <  self.risk_reward    \
        or   not 0 <= self.risk_rate <= 1 :
            print(f'win: {win_pct}, rr: {risk_reward}, risk: {risk_rate}')
            return True
        else : 
            return False

    def solve_equation( self ) :
        S ,P ,R = 0 ,self.win_pct ,self.risk_reward
        while equation( S ,P ,R ) > 0:
            S += 1e-4
        if S >= 1 : S = 1
        return S

    def calc( self ) :
        S = self.solve_equation()
        return S ** ( 1 / self.risk_rate )    



class fixed_rate():
 
    def __init__( self ,win_pct ,risk_reward ,risk_rate ,funds ,ruin_line ):
        self.win_pct     = win_pct
        self.risk_reward = risk_reward
        self.risk_rate   = risk_rate
        self.funds       = funds
        self.ruin_line   = ruin_line
        if self.is_error() : 
            print(f'win: {win_pct}, rr: {risk_reward}, risk: {risk_rate}')
            raise
 
    def is_error( self ) :
        if self.win_pct     == 0 \
        or self.risk_reward == 0 \
        or self.risk_rate   == 0 \
        or self.ruin_line   == 0 :
            print(f'win: {win_pct}, rr: {risk_reward}, risk: {risk_rate}, ruin line: {ruin_line}')
            return True
        elif not 0 <= self.win_pct <= 1   \
        or   not 0 <  self.risk_reward    \
        or   not 0 <= self.risk_rate <= 1 \
        or self.funds < 0                 \
        or self.ruin_line < 0             \
        or self.ruin_line > self.funds :
            print(f'win: {win_pct}, rr: {risk_reward}, risk: {risk_rate}, fund: {funds}, ruin line: {ruin_line}')
            return True
        else : 
            return False

    def solve_equation( self ,win_pct ,R ) :
        S ,P = 0 ,win_pct
        while equation( S ,P ,R ) > 0:
            S += 1e-4
        if S >= 1 : S = 1
        return S

    def calc( self ) :
        a = np.log( 1 + self.risk_reward * self.risk_rate )
        b = abs( np.log( 1 - self.risk_rate ) )
        n = np.log( self.funds / self.ruin_line )
        R = a / b
        S = self.solve_equation( self.win_pct ,R )
        return S ** ( n / b )
