import streamlit as st

st.title(":blue[Hints Page]")
st.header(":violet[Welcome User for Excel Challenge]")

st.subheader(":orange[Hints]")

st.markdown("""Alright! Let’s expand on the analysis ideas with hints and then dive into some more complex (difficult level) analyses you can perform with this dataset in Excel.

### Medium Level Hints:
1. **Monthly Sales Trend:**
   - Use the SUMIF function to aggregate sales by month.
   - Plot the aggregated sales data using a line chart for visual trend analysis.

2. **Discount Impact Analysis:**
   - Group data by the "Discount Band" column.
   - Calculate average sales and profit for each discount band using AVERAGEIF or PivotTables.
   - Use bar charts to compare the impact visually.

3. **Segment Analysis:**
   - PivotTable is your friend here. Drag the "Segment" to the rows, and the "Sales" to the values.
   - Use a PivotChart for a visual comparison.

### Hard Level Hints:
1. **Year-over-Year Growth:**
   - First, aggregate sales and profit by year.
   - Use the formula `=(This Year - Last Year)/Last Year` to calculate growth percentage.
   - Display this data in a column chart for visual analysis.

2. **Product Mix Efficiency:**
   - Create a PivotTable with "Country" as rows and "Product" as columns. Sum "Sales" as values.
   - This helps identify which products are selling best in which countries.
   - Consider Conditional Formatting to highlight top-performing products.

3. **Predictive Analysis:**
   - You can use the Forecast Sheet feature in Excel. Select your historical sales data as input.
   - Excel will generate a forecast chart and table predicting future values.

### Difficult Level:
1. **Market Basket Analysis (Association Rule Learning):**
   - Hint: This is complex and not directly supported by Excel's standard features. You’d typically look for patterns such as, if customers buy Product A, they are likely to buy Product B. Excel doesn't have direct support for this, but you can manually analyze product combinations or use external tools to preprocess the data.

2. **Segmentation and Clustering:**
   - Hint: Use Excel’s k-means clustering by leveraging the Analysis ToolPak. You’d need to numerically code your categorical data and then apply k-means to cluster, say, countries based on sales metrics. Excel is not inherently designed for this without some manual setup.

3. **Time Series Decomposition:**
   - Hint: This involves breaking down your sales data into trend, seasonal, and residual components. Excel doesn’t have a direct function, but you can use a combination of moving averages and seasonal indices to approximate this analysis.

4. **Advanced Forecasting with Multiple Variables:**
   - Hint: Use the regression tool in the Analysis ToolPak. You'll need to set your sales as the dependent variable and other factors (like discount, month, or even product type) as independent variables to see how they collectively impact sales.

For the difficult level analyses, Excel might not be the most efficient tool due to its limitations with complex statistical modeling and machine learning. Tools like Python or R are more suited for these kinds of analyses. However, pushing Excel with creative approaches and external add-ons could provide insights at a basic level.""")