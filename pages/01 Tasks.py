import streamlit as st

st.title(":blue[Tasks Page]")
st.header(":violet[Welcome User for Excel Challenge]")

st.subheader(":orange[Tasks]")

st.markdown("""Based on the dataset, here are some data analysis ideas that you can do in MS Excel, ranging from easy to hard levels:

**Easy Level:**
1. **Sales by Country:** Sum up the sales for each country to see which country has the highest sales.
2. **Profit Analysis:** Calculate the profit margin (Profit as a percentage of Sales) to see overall profitability.
3. **Product Performance:** Identify which product has the highest sales volume.

**Medium Level:**
1. **Monthly Sales Trend:** Use a line graph to visualize the trend of sales over the months for a year.
2. **Discount Impact Analysis:** Analyze how different discount bands affect the sales and profitability.
3. **Segment Analysis:** Compare the performance across different market segments (Government, Midmarket, etc.) to see which segment brings in the most sales.

**Hard Level:**
1. **Year-over-Year Growth:** Calculate the year-over-year growth in sales and profit to understand the growth trajectory.
2. **Product Mix Efficiency:** Analyze the product mix within each country to see which products are driving the most value.
3. **Predictive Analysis:** Use regression analysis to predict future sales based on historical data. Excel has basic forecasting tools that you can utilize for simple predictive models.

Remember, for some of these analyses, especially the harder ones, you might need to use Excel features like PivotTables, Charting for visualization, and the Analysis ToolPak for regression analysis.""")