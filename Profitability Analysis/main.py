import numpy_financial
import pandas as pd
import numpy as np
from numpy_financial import irr,npv
import plotly.graph_objects as go

data = pd.read_excel("C:\\Users\\moazm\\Desktop\\Calculating Metrics\\_financial_data.xlsx")

#Calculate NPV

rate = 0.1
cash_flow=data["Cash Flow"]
npv = numpy_financial.npv(rate,cash_flow).round(5)

#Calculate IRR

irr = numpy_financial.irr(cash_flow)


#Calculate PayBack Period

intial_cash_flow=cash_flow[0]
payback_period=0
Cummilative_cash_flow=0
for period_id , csh_flow in enumerate(cash_flow):
    Cummilative_cash_flow += csh_flow
    if (Cummilative_cash_flow >= intial_cash_flow):
        payback_period = period_id+1
        break

#Calculate PI

pi = npv / abs(cash_flow[0])


#Printing the result
print(f'NPV: $ {npv :.2f}')
print(f'IRR: $ {irr :.2%}')
print(f'Payback Period: $ {payback_period} year')
print(f'PI: $ {pi :.2f}')


fig =go.Figure()
fig.add_trace(go.Scatter(x=data["Period"],y=data["Cash Flow"],mode="lines",name="cash flow"))

fig.update_layout(
    title="Cash Flow over time",
    xaxis_title="Cash Flow",
    yaxis_title="Year",
)
fig.show()