import streamlit as st
import pandas as pd

@st.cache_data
def load_data():
    data = pd.read_csv('Financials.csv')
    return data

st.title(":blue[Welcome..]")
st.header(":violet[Advance Excel Tasks]")

st.subheader(":orange[Dataset Information:]")
st.markdown("""Imagine you have a big shopping list from different stores (countries), and for each thing you buy (product), there's a price tag and sometimes a discount. You keep track of how many items you buy, how much they cost you, how much you saved with discounts, and how much you ended up paying. Also, you note down when you bought them (date), what kind of store it was (market segment), and how much you had to pay the shop to get these things (cost of goods). In the end, you also figure out if you spent more than you should have or saved money (profit).

### Dataset Description:
The dataset is a collection of financial transactions with attributes organized in columns, encompassing various aspects such as market segments, geographical regions (countries), product details, pricing, sales, and profitability metrics. Key attributes include:
- **Segment:** The market segment to which the sale belongs, indicating the type of customer (e.g., Government, Midmarket).
- **Country:** The geographical location of the sale.
- **Product:** The specific product sold.
- **Discount Band:** The category of discount applied to the sale, if any.
- **Units Sold:** The quantity of product units sold in the transaction.
- **Manufacturing Price:** The cost to manufacture one unit of the product.
- **Sale Price:** The price at which one unit of the product is sold to the customer.
- **Gross Sales:** The total revenue generated from the sale before discounts.
- **Discounts:** The total amount of discounts applied to the sale.
- **Sales:** The net sales revenue after applying discounts.
- **COGS (Cost of Goods Sold):** The direct costs attributable to the production of the goods sold.
- **Profit:** The net profit generated from the sale, calculated as Sales minus COGS.
- **Date, Month Number, Month Name, Year:** Temporal details of when the transaction occurred.

This dataset can be used to analyze business performance across different dimensions, such as profitability by product or region, effectiveness of discount strategies, and sales trends over time.
""")
with st.expander(":orange[**View Dataset**]"):
    st.write(load_data())

st.markdown("Download Dataset from [HERE](https://www.kaggle.com/datasets/atharvaarya25/financials?resource=download)")