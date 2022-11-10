import sympy as sp
import numpy as np
import pandas as pd
import math
import matplotlib.pyplot as plt
import scipy as spy
import equations as eq

P3_EM = 2000000  # MPA
T3_EM = 814  # K
m3_EM = 18.1  # kg/s
T4_EM = 1600  # K
mComb_EM = 0.427  # kg/s

P3_MA = 700000  # MPA
T3_MA = 707  # K
m3_MA = 6.8  # kg/s
T4_MA = 1387  # K
mComb_MA = 0.132  # kg/s

P3_CRU = 1800000  # MPA
T3_CRU = 1060  # K
m3_CRU = 14.2  # kg/s
T4_CRU = 1393  # K
mComb_CRU = 0.140  # kg/s

P3_IDLE = 150000  # MPA
T3_IDLE = 343  # K
m3_IDLE = 1.05  # kg/s
T4_IDLE = 703  # K
mComb_IDLE = 0.0091  # kg/s

R_ar = 143.5  # J/kg*K
theta = 73000000
D_int = 0.01717
phi_zp = 1.05
phi_zs = 8
phi_estq = 0.06818
b = 170*(2-math.log(phi_zp))
m_dot_zp = 0.245

perda_pressao_total = 0.06  # deltaP3-4/P3
fator_perda_pressao = 20  # deltaP3-4/qRef

# Determinação de parametros de operação

A_ref_aero_EM = eq.A_ref_aerodinamico(
    R_ar, m3_EM, T3_EM, P3_EM, perda_pressao_total, fator_perda_pressao)
A_ref_aero_MA = eq.A_ref_aerodinamico(
    R_ar, m3_MA, T3_MA, P3_MA, perda_pressao_total, fator_perda_pressao)
A_ref_aero_CRU = eq.A_ref_aerodinamico(
    R_ar, m3_CRU, T3_CRU, P3_CRU, perda_pressao_total, fator_perda_pressao)
A_ref_aero_IDLE = eq.A_ref_aerodinamico(
    R_ar, m3_IDLE, T3_IDLE, P3_IDLE, perda_pressao_total, fator_perda_pressao)

D_ref_aero_EM = eq.D_ref(A_ref_aero_EM, D_int)
D_ref_aero_MA = eq.D_ref(A_ref_aero_MA, D_int)
D_ref_aero_CRU = eq.D_ref(A_ref_aero_CRU, D_int)
D_ref_aero_IDLE = eq.D_ref(A_ref_aero_IDLE, D_int)

A_ref_quim_EM = eq.A_ref_quimico(
    m3_EM, T3_EM, P3_EM, theta, D_ref_aero_EM, b)
A_ref_quim_MA = eq.A_ref_quimico(
    m3_MA, T3_MA, P3_MA, theta, D_ref_aero_MA, b)
A_ref_quim_CRU = eq.A_ref_quimico(
    m3_CRU, T3_CRU, P3_CRU, theta, D_ref_aero_CRU, b)
A_ref_quim_IDLE = eq.A_ref_quimico(
    m3_IDLE, T3_IDLE, P3_IDLE, theta, D_ref_aero_IDLE, b)

D_ref_quim_EM = eq.D_ref(A_ref_quim_EM, D_int)
D_ref_quim_MA = eq.D_ref(A_ref_quim_MA, D_int)
D_ref_quim_CRU = eq.D_ref(A_ref_quim_CRU, D_int)
D_ref_quim_IDLE = eq.D_ref(A_ref_quim_IDLE, D_int)

A_ft_aero_EM = eq.A_ft(A_ref_aero_EM)
A_ft_aero_MA = eq.A_ft(A_ref_aero_MA)
A_ft_aero_CRU = eq.A_ft(A_ref_aero_CRU)
A_ft_aero_IDLE = eq.A_ft(A_ref_aero_IDLE)

A_ft_quim_EM = eq.A_ft(A_ref_quim_EM)
A_ft_quim_MA = eq.A_ft(A_ref_quim_MA)
A_ft_quim_CRU = eq.A_ft(A_ref_quim_CRU)
A_ft_quim_IDLE = eq.A_ft(A_ref_quim_IDLE)

D_ft_aero_EM = eq.D_ft(A_ft_aero_EM, D_int, D_ref_aero_EM)
D_ft_aero_MA = eq.D_ft(A_ft_aero_MA, D_int, D_ref_aero_MA)
D_ft_aero_CRU = eq.D_ft(A_ft_aero_CRU, D_int, D_ref_aero_CRU)
D_ft_aero_IDLE = eq.D_ft(A_ft_aero_IDLE, D_int, D_ref_aero_IDLE)

D_ft_quim_EM = eq.D_ft(A_ft_quim_EM, D_int, D_ref_quim_EM)
D_ft_quim_MA = eq.D_ft(A_ft_quim_MA, D_int, D_ref_quim_MA)
D_ft_quim_CRU = eq.D_ft(A_ft_quim_CRU, D_int, D_ref_quim_CRU)
D_ft_quim_IDLE = eq.D_ft(A_ft_quim_IDLE, D_int, D_ref_quim_IDLE)

A_ref_maior = A_ref_quim_IDLE
D_ref_maior = D_ref_quim_IDLE
A_ft_maior = A_ft_quim_IDLE
D_ft_maior = D_ft_quim_IDLE


# Determinação dos comprimentos da camara

l_zp = (3 / 4) * D_ft_maior
l_zs = (1 / 2) * D_ft_maior
l_zd = (3 / 2) * D_ft_maior
l_cc = l_zp + l_zs + l_zd

# Razões estequimetricas

phi_global_EM = eq.phi_global(mComb_EM, m3_EM, phi_estq)
phi_global_MA = eq.phi_global(mComb_MA, m3_MA, phi_estq)
phi_global_CRU = eq.phi_global(mComb_CRU, m3_CRU, phi_estq)
phi_global_IDLE = eq.phi_global(mComb_IDLE, m3_IDLE, phi_estq)

phi_rico_EM = eq.phi_rico(T3_EM)
phi_rico_MA = eq.phi_rico(T3_MA)
phi_rico_CRU = eq.phi_rico(T3_CRU)
phi_rico_IDLE = eq.phi_rico(T3_IDLE)

phi_pobre_EM = eq.phi_pobre(T3_EM)
phi_pobre_MA = eq.phi_pobre(T3_MA)
phi_pobre_CRU = eq.phi_pobre(T3_CRU)
phi_pobre_IDLE = eq.phi_pobre(T3_IDLE)


# Continuando apenas com os dados do ponto de projeto MaximoEmpuxo

difference_phis_rico = phi_global_MA/phi_rico_MA

difference_phis_pobre = phi_global_MA/phi_pobre_MA

# Definição da porcentagem de ar na zona primeira a partir dos criterios 1-3 pag 53
air_zp_min = phi_global_MA/1.07  # 0.266
air_zp_max = phi_global_MA/1.5  # 0.1898

air_zp_per_cent = 0.24  # Valor intermediario

phi_zp = eq.phi_zp(phi_global_MA, air_zp_per_cent)
