from rulocal import *

with open('input.txt') as f_in:
    text = ''
    for line in f_in:
        text += line
sal_f, sal_m, pay_t, pay_p, pay_s, food_s, com_cost, mun_ser, ent, food_b, cost_cl, loan, trav = text.split()
sal_F = int(sal_f)
sal_M = int(sal_m)
pay_T = int(pay_t)
pay_S = int(pay_s)
food_S = int(food_s)
Com_cost = int(com_cost)
Mun_ser = int(mun_ser)
Ent = int(ent)
food_B = int(food_b)
cost_CL = int(cost_cl)
Loan = int(loan)
Trav = int(trav)

income = sal_F + sal_M
cost = pay_T + pay_S + food_S + Com_cost + Mun_ser + Ent + food_B + cost_CL + Loan
profit = income - cost
time = round(Trav / profit)

txt = " "
txt += (INCOME + str(income) + "руб.\n")
txt += (PROFIT + str(profit) + "руб.\n")
txt += (MONT + str(time))
with open('output.txt', 'w') as f_out:
    f_out.write(txt)
