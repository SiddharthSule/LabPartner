# -*- coding: utf-8 -*-
"""
Siddharth Sule
2 June 2020
"""
#------------------------------------------------------------------------------
import sympy as sp
#------------------------------------------------------------------------------
sp.init_printing()
#------------------------------------------------------------------------------
startup_info = """
Error Propagation Tool
----------------------
This software uses the SymPy module to symbolically
differentiate functions to derive the for the error
on the dependant variable.

Inputting Common Functions
--------------------------
coefficient : ax = a*x
polynomials : x^b = x**b
exponential : e^(x) = exp(x)
logarithmic : ln(x) =  log(x), log_b(x) = log(x, b)
trig functs : sin(x) = sin(x), cos(x) = cos(x), tan(x) = tan(x)
square root : √x = sqrt(x)

Greek Alphabet (For Variables)
------------------------------
Α α, Β β, Γ γ, Δ δ, Ε ε, Ζ ζ, Η η, Θ θ,
Ι ι, Κ κ, Λ λ, Μ μ, Ν ν, Ξ ξ, Ο ο, Π π,
Ρ ρ, Σ σ, Τ τ, Υ υ, Φ φ, Χ χ, Ψ ψ, Ω ω"""
#------------------------------------------------------------------------------
def print_error_startup_info():
    
    return print(startup_info)
#------------------------------------------------------------------------------
def propagate_error():
    
    #STEP 1: TAKE INPUT AND CREATE FUNCTIONS AND VARIABLES
    func_name = input("Enter Dependant Variable : ")
    num_var = int(input("Enter Number of Independant/Control Variables : "))
    
    func = sp.Function(func_name)
    
    var_list = []
    
    for i in range(num_var):
        
        input_text = input(("Enter Variable " + str(i+1) + " : "))
        
        var = sp.Symbol(input_text)
        var_list.append(var)
        
    func_lhs_vars = str(var_list).replace("[","").replace("]","")
    func_lhs = func_name + "(" + func_lhs_vars + ")"
    
    func_input = input(("Enter " + func_lhs +  " : "))
    func = sp.parsing.sympy_parser.parse_expr(func_input)
    
    #STEP 2: DIFFERENTIATE FUNCTION WITH RESPECT TO EACH VARIABLE
    deriv_list = []
    
    for var in var_list:
        
        deriv = sp.diff(func, var)
        deriv_list.append(deriv)
        
    
    #STEP 3: FORMAT OUTPUT
    print("")
    full_output = "Δ" + func_name + " = "
    
    if num_var == 1:
        
        output = "(" + str(deriv_list[0]) + ")Δ" + str(var_list[0])
        full_output = full_output + output
    
    else:
        
        full_output = full_output + "sqrt("
        
        for i in range(num_var):
        
            err_individual = "(" + str(deriv_list[i]) + ")Δ" + str(var_list[i])
            full_output = full_output + "(" + err_individual + ")**2"
        
            if i < (num_var - 1):
            
                full_output = full_output + " + "
                
            else:
                
                full_output = full_output + ")"
    
    return print(full_output)
#------------------------------------------------------------------------------