import pandas as pd
import matplotlib.pyplot as plt
from openpyxl import load_workbook

############### DIVIDING DATASET ###############

df = pd.read_csv('Kaggle_Books-Selling-Records-.csv')

##### replacing days and gender values #####

df['Category'].replace('School', 'high school', inplace=True)
df.rename(columns={'Author ': 'Author'}, inplace=True)

df['Day'].replace(1, 'Monday', inplace=True)
df['Day'].replace(2, 'Tuesday', inplace=True)
df['Day'].replace(3, 'Wednesday', inplace=True)
df['Day'].replace(4, 'Thursday', inplace=True)
df['Day'].replace(5, 'Friday', inplace=True)
df['Day'].replace(6, 'Saturday', inplace=True)
df['Day'].replace(7, 'Sunday', inplace=True)

df['Gender'].replace(0, 'F', inplace=True)
df['Gender'].replace(1, 'M', inplace=True)

##### spliting data by year #####

df_2018 = df.loc[df['Year'] == 2018]
df_2019 = df.loc[df['Year'] == 2019]

##### spliting data by sale offers #####

df_during_sale_offers = df.loc[df['Online Sale Offers '] == 1]
df_no_sale_offers = df.loc[df['Online Sale Offers '] == 0]

df_during_sale_offers_2018 = df_2018.loc[df_2018['Online Sale Offers '] == 1]
df_no_sale_offers_2018 = df_2018.loc[df_2018['Online Sale Offers '] == 0]

sales_with_discount_2018 = df_during_sale_offers_2018['Quantity'].sum()
sales_without_discount_2018 = df_no_sale_offers_2018['Quantity'].sum()


df_during_sale_offers_2019 = df_2019.loc[df_2019['Online Sale Offers '] == 1]
df_no_sale_offers_2019 = df_2019.loc[df_2019['Online Sale Offers '] == 0]

sales_with_discount_2019 = df_during_sale_offers_2019['Quantity'].sum()
sales_without_discount_2019 = df_no_sale_offers_2019['Quantity'].sum()

##### units sold and gross profit per year #####

units_sold_2018 = df_2018['Quantity'].sum()
units_sold_2019 = df_2019['Quantity'].sum()

profit_2018 = df_2018['Profit (INR)'].sum().round(2)
profit_2019 = df_2019['Profit (INR)'].sum().round(2)

cost_price_2018 = df_2018['Cost Price'].sum().round(2)
cost_price_2019 = df_2019['Cost Price'].sum().round(2)

item_price_2018 = df_2018['Item Price'].sum().round(2)
item_price_2019 = df_2019['Item Price'].sum().round(2)

##### average profit per unit #####

avg_profit_2018 = (df_2018['Profit (INR)'].sum()/units_sold_2018).round(2)
avg_profit_2019 = (df_2019['Profit (INR)'].sum()/units_sold_2019).round(2)

##### gross profit percentage for year #####

profit_per_2018 = (100 - (cost_price_2018/item_price_2018)*100).round(2)
profit_per_2019 = (100 - (cost_price_2019/item_price_2019)*100).round(2)

##### gross profit by category #####

profit_by_category_2018 = df_2018.groupby('Category')['Profit (INR)'].sum().round(2).reset_index()
profit_by_category_2018.rename(columns={'Profit (INR)': '2018'}, inplace=True)


profit_by_category_2019 = df_2019.groupby('Category')['Profit (INR)'].sum().round(2).reset_index()
profit_by_category_2019.rename(columns={'Profit (INR)': '2019'}, inplace=True)
profit_by_category_2019.drop(columns='Category', inplace=True)

profit_by_category = pd.concat([profit_by_category_2018, profit_by_category_2019], axis=1)

##### gross profit by author #####

profit_by_author_2018 = df_2018.groupby('Author')['Profit (INR)'].sum().round(2).reset_index()
top10_authors_2018 = profit_by_author_2018.sort_values(by='Profit (INR)', ascending=False).head(10)
bottom10_authors_2018 = profit_by_author_2018.sort_values(by='Profit (INR)', ascending=True).head(10)


profit_by_author_2019 = df_2019.groupby('Author')['Profit (INR)'].sum().round(2).reset_index()
top10_authors_2019 = profit_by_author_2019.sort_values(by='Profit (INR)', ascending=False).head(10)
bottom10_authors_2019 = profit_by_author_2019.sort_values(by='Profit (INR)', ascending=True).head(10)

##### most and least sold authors #####

most_sold_author_2018 = df_2018.groupby('Author')['Quantity'].sum().reset_index()
most_sold_author_2018.rename(columns={'Quantity' : 'Units sold'}, inplace=True)

top10_authors_sales_2018 = most_sold_author_2018.sort_values(by='Units sold', ascending=False).head(10)
bottom10_authors_sales_2018 = most_sold_author_2018.sort_values(by='Units sold', ascending=True).head(10)

top_sold_authors_2018 = top10_authors_sales_2018['Units sold'].sum()
other_sales_2018 = units_sold_2018 - top_sold_authors_2018


most_sold_author_2019 = df_2019.groupby('Author')['Quantity'].sum().reset_index()
most_sold_author_2019.rename(columns={'Quantity' : 'Units sold'}, inplace=True)

top10_authors_sales_2019 = most_sold_author_2019.sort_values(by='Units sold', ascending=False).head(10)
bottom10_authors_sales_2019 = most_sold_author_2019.sort_values(by='Units sold', ascending=True).head(10)

top_sold_authors_2019 = top10_authors_sales_2019['Units sold'].sum()
other_sales_2019 = units_sold_2019 - top_sold_authors_2019

##### gross profit by product #####

profit_by_product = df.groupby('Product-Name')['Profit (INR)'].sum().reset_index()

top10_products_profit = profit_by_product.sort_values(by='Profit (INR)', ascending=False).head(10)

bottom10_products_profit = profit_by_product.sort_values(by='Profit (INR)', ascending=True).head(10)

##### most and least sold products #####

most_sold_product_2018 = df_2018.groupby('Product-Name')['Quantity'].sum().reset_index()
top10_products_sold_2018 = most_sold_product_2018.sort_values(by='Quantity', ascending=False).head(10)
bottom10_products_sold_2018 = most_sold_product_2018.sort_values(by='Quantity', ascending=True).head(10)

top_sold_products_2018 = top10_products_sold_2018['Quantity'].sum()
other_products_sales_2018 = units_sold_2018 - top_sold_products_2018

most_sold_product_2019 = df_2019.groupby('Product-Name')['Quantity'].sum().reset_index()
top10_products_sold_2019 = most_sold_product_2019.sort_values(by='Quantity', ascending=False).head(10)
bottom10_products_sold_2019 = most_sold_product_2019.sort_values(by='Quantity', ascending=True).head(10)

top_sold_products_2019 = top10_products_sold_2019['Quantity'].sum()
top_other_products_sales_2019 = units_sold_2019 - top_sold_products_2019

##### data by quarters #####

profit_by_quarter = df.groupby('Quarter')['Profit (INR)'].sum().round(2).reset_index()

sales_by_quarter = df.groupby('Quarter')['Quantity'].sum().reset_index()

sale = df.groupby('Quarter')['Profit (INR)'].sum().round(2).reset_index()
profit = df.groupby('Quarter')['Quantity'].sum().reset_index()
profit.rename(columns={'Quantity' : 'Units sold'}, inplace=True)
profit.drop(columns='Quarter', inplace=True)

quarter_data = pd.concat([sale, profit], axis=1)
quarter_data['Profit per sale'] = (quarter_data['Profit (INR)'] / quarter_data['Units sold']).round(2)

##### data by quarters on special offers #####

sale_dis = df_during_sale_offers.groupby('Quarter')['Profit (INR)'].sum().round(2).reset_index()
profit_dis = df_during_sale_offers.groupby('Quarter')['Quantity'].sum().reset_index()
profit_dis.drop(columns='Quarter', inplace=True)

quarter_data_dis = pd.concat([sale_dis, profit_dis], axis=1)
quarter_data_dis['Profit per sale'] = (quarter_data_dis['Profit (INR)'] / quarter_data_dis['Quantity']).round(2)


sale_no_dis = df_no_sale_offers.groupby('Quarter')['Profit (INR)'].sum().round(2).reset_index()
profit_no_dis = df_no_sale_offers.groupby('Quarter')['Quantity'].sum().reset_index()
profit_no_dis.drop(columns='Quarter', inplace=True)

quarter_data_no_dis = pd.concat([sale_no_dis, profit_no_dis], axis=1)
quarter_data_no_dis['Profit per sale'] = (quarter_data_no_dis['Profit (INR)'] / quarter_data_no_dis['Quantity']).round(2)

##### data by part of the day #####

sales_morning = df.groupby('Quarter')['Morning'].sum().reset_index()
sales_afternoon = df.groupby('Quarter')['Afternoon'].sum().reset_index()
sales_afternoon.drop(columns=['Quarter'], inplace=True)
sales_evening = df.groupby('Quarter')['Evening'].sum().reset_index()
sales_evening.drop(columns=['Quarter'], inplace=True)
sales_night = df.groupby('Quarter')['Night'].sum().reset_index()
sales_night.drop(columns=['Quarter'], inplace=True)

sales_on_part_day = pd.concat([sales_morning, sales_afternoon, sales_evening, sales_night], axis=1)

##### data by the day #####
days = ['Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
df_monday = df.loc[df['Day'] == 'Monday']
week = df_monday.groupby('Quarter')['Day'].count().reset_index()
week.rename(columns={'Day': 'Monday'}, inplace=True)

for i in days:
    df_day = df.loc[df['Day'] == i]
    sales_day = df_day.groupby('Quarter')['Day'].count().reset_index()
    sales_day.rename(columns={'Day': i}, inplace=True)
    sales_day.drop(columns=['Quarter'], inplace=True)
    week = pd.concat([week, sales_day], axis=1)

##### creating dataframes #####

balance = pd.DataFrame({'Balance': ['Revenue', 'Cost of revenue', 'Gross profit', 'Gross profit percentage, %', 'Units sold per year', 'Average profit per unit sold'],
                        '2018' : [f'{item_price_2018}', f'{cost_price_2018}', f'{profit_2018}', f'{profit_per_2018}', f'{units_sold_2018}', f'{avg_profit_2018}'],
                        '2019' : [f'{item_price_2019}', f'{cost_price_2019}', f'{profit_2019}', f'{profit_per_2019}', f'{units_sold_2019}', f'{avg_profit_2019}']})
balance['2018'] = pd.to_numeric(balance['2018'])
balance['2019'] = pd.to_numeric(balance['2019'])

sale_offers = pd.DataFrame({'Sale offer' : ['Sale quantity during sale offer', 'Sale quantity on regular price'],
                            '2018' : [f'{sales_with_discount_2018}', f'{sales_without_discount_2018}'],
                            '2019' : [f'{sales_with_discount_2019}', f'{sales_without_discount_2019}']})

sale_offers['2018'] = pd.to_numeric(sale_offers['2018'])
sale_offers['2019'] = pd.to_numeric(sale_offers['2019'])

##### sales by gender #####

sales_m_2018 = df_2018.loc[df['Gender'] == 'M']
sales_m_2018 = sales_m_2018['Quantity'].sum()
sales_m_2019 = df_2019.loc[df['Gender'] == 'M']
sales_m_2019 = sales_m_2019['Quantity'].sum()

sales_f_2018 = df_2018.loc[df['Gender'] == 'F']
sales_f_2018 = sales_f_2018['Quantity'].sum()
sales_f_2019 = df_2019.loc[df['Gender'] == 'F']
sales_f_2019 = sales_f_2019['Quantity'].sum()

gender_sales = pd.DataFrame({'Gender' : ['Male sales', 'Female sales'],
                            '2018' : [f'{sales_m_2018}', f'{sales_f_2018}'],
                            '2019' : [f'{sales_m_2019}', f'{sales_f_2019}']})

gender_sales['2018'] = pd.to_numeric(gender_sales['2018'])
gender_sales['2019'] = pd.to_numeric(gender_sales['2019'])

############### FORMATING ANALYSIS ###############

print("\n*Values are in Indian rupee (INR)")
print(f"\nBalance sheet: \n{balance}")

print(f"\nProfit by category: \n{profit_by_category}")

print(f"\nSales data regarding sale offers: \n{sale_offers}")

print(f"\nData by quarter: \n{quarter_data}")

print(f"\nProfit per sale on discounted units: \n{quarter_data_dis}")
print(f"\nProfit per unit on regular price: \n{quarter_data_no_dis}")

print(f"\nTop 10 most profitable authors 2018: \n{top10_authors_2018}")
print(f"\nTop 10 most profitable authors 2019: \n{top10_authors_2019}")

print(f"\nTop 10 best selling authors 2018: \n{top10_authors_sales_2018}")
print(f"\nTop 10 best selling authors 2019: \n{top10_authors_sales_2019}")

print(f"\nTop 10 best selling products 2018: \n{top10_products_sold_2018}")
print(f"\nTop 10 best selling products 2019: \n{top10_products_sold_2019}")

print(f"\nSales per quarter by the part of the day: \n{sales_on_part_day}")

print(f"\nSales per quarter by day of the week: \n{week}")

print(f"\n Sales by gender: \n{gender_sales}")

############### CREATING EXCEL FILE WITH TABLES ###############

balance.to_excel("Balance.xlsx", index=False, header=True, startrow=1, sheet_name='Balance')

with pd.ExcelWriter("Balance.xlsx", mode="a", engine="openpyxl", if_sheet_exists="overlay") as writer:
    ws = pd.read_excel('Balance.xlsx', sheet_name='Balance')
    row = len(ws) + 5
    profit_by_category.to_excel(writer, index=False, header=True, startrow=row, sheet_name='Balance')
    quarter_data.to_excel(writer, index=False, header=True, startrow=1, sheet_name='Quarters')
    top10_authors_2018.to_excel(writer, index=False, header=True, startrow=1, sheet_name='Top')

with pd.ExcelWriter("Balance.xlsx", mode="a", engine="openpyxl", if_sheet_exists="overlay") as writer:
    ws = pd.read_excel('Balance.xlsx', sheet_name='Balance')
    wq = pd.read_excel('Balance.xlsx', sheet_name='Quarters')
    wt = pd.read_excel('Balance.xlsx', sheet_name='Top')
    row = len(ws) + 5
    row_q = len(wq) + 5
    row_t = len(wt) + 5
    sale_offers.to_excel(writer, index=False, header=True, startrow=row, sheet_name='Balance')
    quarter_data_dis.to_excel(writer, index=False, header=True, startrow=row_q, sheet_name='Quarters')
    top10_authors_2019.to_excel(writer, index=False, header=True, startrow=row_t, sheet_name='Top')

with pd.ExcelWriter("Balance.xlsx", mode="a", engine="openpyxl", if_sheet_exists="overlay") as writer:
    wq = pd.read_excel('Balance.xlsx', sheet_name='Quarters')
    wt = pd.read_excel('Balance.xlsx', sheet_name='Top')
    row_q = len(wq) + 5
    row_t = len(wt) + 5
    quarter_data_no_dis.to_excel(writer, index=False, header=True, startrow=row_q, sheet_name='Quarters')
    top10_authors_sales_2018.to_excel(writer, index=False, header=True, startrow=row_t, sheet_name='Top')

with pd.ExcelWriter("Balance.xlsx", mode="a", engine="openpyxl", if_sheet_exists="overlay") as writer:
    wt = pd.read_excel('Balance.xlsx', sheet_name='Top')
    wq = pd.read_excel('Balance.xlsx', sheet_name='Quarters')
    row_t = len(wt) + 5
    row_q = len(wq) + 5
    top10_authors_sales_2019.to_excel(writer, index=False, header=True, startrow=row_t, sheet_name='Top')
    sales_on_part_day.to_excel(writer, index=False, header=True, startrow=row_q, sheet_name='Quarters')

with pd.ExcelWriter("Balance.xlsx", mode="a", engine="openpyxl", if_sheet_exists="overlay") as writer:
    wt = pd.read_excel('Balance.xlsx', sheet_name='Top')
    wq = pd.read_excel('Balance.xlsx', sheet_name='Quarters')
    row_t = len(wt) + 5
    row_q = len(wq) + 5
    top10_products_sold_2018.to_excel(writer, index=False, header=True, startrow=row_t, sheet_name='Top')
    week.to_excel(writer, index=False, header=True, startrow=row_q, sheet_name='Quarters')

with pd.ExcelWriter("Balance.xlsx", mode="a", engine="openpyxl", if_sheet_exists="overlay") as writer:
    wt = pd.read_excel('Balance.xlsx', sheet_name='Top')
    wq = pd.read_excel('Balance.xlsx', sheet_name='Quarters')
    row_t = len(wt) + 5
    row_q = len(wq) + 5
    top10_products_sold_2019.to_excel(writer, index=False, header=True, startrow=row_t, sheet_name='Top')
    gender_sales.to_excel(writer, index=False, header=True, startrow=row_q, sheet_name='Quarters')

##### naming tables in excel #####

wb = load_workbook("Balance.xlsx")
ws_balance = wb['Balance']
ws_quarter = wb['Quarters']
ws_top = wb['Top']

ws_balance['A1'] = 'Balance sheet:'
ws_balance['A12'] = 'Profit by category:'
ws_balance['A21'] = 'Sales data regarding sale offers:'

ws_quarter['A1'] = 'Profit by quarter (overall):'
ws_quarter['A14'] = 'Discounted units profit:'
ws_quarter['A27'] = 'Regular price units profit:'
ws_quarter['A40'] = 'Sales per quarter by the part of the day:'
ws_quarter['A53'] = 'Sales per quarter by day of the week:'
ws_quarter['A66'] = 'Sales by gender:'

ws_top['A1'] = 'Top 10 most profitable authors 2018'
ws_top['A16'] = 'Top 10 most profitable authors 2019'
ws_top['A31'] = 'Top 10 best selling authors 2018'
ws_top['A46'] = 'Top 10 best selling authors 2019'
ws_top['A61'] = 'Top 10 best selling products 2018'
ws_top['A76'] = 'Top 10 best selling products 2019'

wb.save("Balance.xlsx")

############### CREATING GRAPHS ###############

plt.figure(figsize=(10,6))
plt.plot(week['Quarter'], week['Monday'], marker = 'o', color = 'coral')
plt.plot(week['Tuesday'], marker = 'o', color = 'cornflowerblue')
plt.plot(week['Wednesday'], marker = 'o', color = 'indigo')
plt.plot(week['Thursday'], marker = 'o', color = 'gold')
plt.plot(week['Friday'], marker = 'o', color = 'red')
plt.plot(week['Saturday'], marker = 'o', color = 'darkgray')
plt.plot(week['Sunday'], marker = 'o', color = 'green')
plt.ylabel('Sales amount')
plt.title('SALES BY DAY OF THE WEEK')
plt.grid(axis='y')
plt.legend(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])
plt.savefig('SALES BY DAY OF THE WEEK.png')
# plt.show()

##### profit by category graph #####

plt.figure(figsize=(10,6))
plt.plot(sales_on_part_day['Quarter'], sales_on_part_day['Morning'], marker = 'o', color = 'coral')
plt.plot(sales_on_part_day['Afternoon'], marker = 'o', color = 'cornflowerblue')
plt.plot(sales_on_part_day['Evening'], marker = 'o', color = 'indigo')
plt.plot(sales_on_part_day['Night'], marker = 'o', color = 'gold')
plt.ylabel('Sales amount')
plt.title('SALES BY THE PART OF THE DAY')
plt.legend(['Morning', 'Afternoon', 'Evening', 'Night'])
plt.grid(axis='y')
plt.savefig('SALES BY THE PART OF THE DAY.png')
# plt.show()

##### profit by category graph #####

plt.figure(figsize=(13,6))
plt.title('PROFIT BY CATEGORY')
plt.axis('off')
colors_pro = ['mistyrose', 'salmon', 'sandybrown', 'rosybrown']
labels_pro = 'college', 'competition', 'high school', 'school'

def profit_autopct(profit_pie):
    def my_autopct(pct):
        total = sum(profit_pie)
        val = int(round(pct*total/100.0))
        return '{p:.1f}% \n({v:d})'.format(p=pct,v=val)
    return my_autopct

profit_pie_2018 = profit_by_category['2018'].tolist()
plt.subplot(121)
plt.pie(profit_pie_2018, labels=labels_pro, shadow=True, colors=colors_pro, autopct=profit_autopct(profit_pie_2018), pctdistance=0.85, startangle=180)
plt.title('2018')
plt.subplot(122)

profit_pie_2019 = profit_by_category['2019'].tolist()
plt.pie(profit_pie_2019, labels=labels_pro, shadow=True, colors=colors_pro, autopct=profit_autopct(profit_pie_2019), startangle=90)
plt.title('2019')
plt.savefig('PROFIT BY CATEGORY.png')
# plt.show()

##### sales on discount and regular price graphs #####

plt.figure(figsize=(10,6))
plt.title('SALES DEPENDING ON OFFERS')
plt.axis('off')
colors_dis = ['cornflowerblue', 'coral']
labels_dis = 'During sale offers', 'Without discount'
def sales_autopct(sales_pie_2018):
    def my_autopct(pct):
        total = sum(sales_pie_2018)
        val = int(round(pct*total/100.0))
        return '{p:.1f}% \n({v:d})'.format(p=pct,v=val)
    return my_autopct

plt.subplot(121)
sales_pie_2018 = [sales_with_discount_2018, sales_without_discount_2018]
plt.pie(sales_pie_2018, labels=labels_dis, explode=(0, 0.15), shadow=True, colors=colors_dis, autopct=sales_autopct(sales_pie_2018), startangle=90)
plt.title('2018')

plt.subplot(122)
sales_pie_2019 = [sales_with_discount_2019, sales_without_discount_2019]
plt.pie(sales_pie_2019, labels=labels_dis, explode=(0, 0.15), shadow=True, colors=colors_dis, autopct=sales_autopct(sales_pie_2019), startangle=90)
plt.title('2019')
plt.savefig('SALES DEPENDING ON OFFERS.png')
# plt.show()

##### profit by quarter graph #####

plt.figure(figsize=(10,6))
profit_by_quarter_graph = plt.bar(profit_by_quarter['Quarter'], profit_by_quarter['Profit (INR)'], color='sandybrown', edgecolor='chocolate')
plt.title('PROFIT BY QUARTER')
plt.ylabel('Profit (INR)')
plt.xlabel('Quarter')
plt.bar_label(profit_by_quarter_graph)
plt.savefig('PROFIT BY QUARTER.png')
# plt.show()

##### sales by quarter graph #####

plt.figure(figsize=(10,6))
sales_by_quarter_graph = plt.bar(sales_by_quarter['Quarter'], sales_by_quarter['Quantity'], color='bisque', edgecolor='chocolate')
plt.title('SALES BY QUARTER')
plt.ylabel('Sales')
plt.xlabel('Quarter')
plt.bar_label(sales_by_quarter_graph)
plt.savefig('SALES BY QUARTER.png')
# plt.show()

##### profit per sale by quarter graph #####

plt.figure(figsize=(10,6))
plt.plot(quarter_data_dis['Quarter'], quarter_data_dis['Profit per sale'], marker = 'o', color = 'coral')
plt.plot(quarter_data_no_dis['Profit per sale'], marker = 'o', color = 'cornflowerblue')
plt.ylabel('Profit per sale, INR')
plt.title('PROFIT PER SALE BY QUARTER')
plt.legend(['On sale', 'Without sale'])
plt.grid(axis='y')
plt.savefig('PROFIT PER SALE BY QUARTER.png')
# plt.show()

##### top 10 best selling authors 2018 and 2019 graph #####

plt.figure(figsize=(10,6))
plt.title('BEST SELLING AUTHORS')
plt.axis('off')
colors_aut = ['thistle', 'violet']
labels_aut = 'Other authors sales', 'Top 10 authors sales'
def author_autopct(author_pie):
    def my_autopct(pct):
        total = sum(author_pie)
        val = int(round(pct*total/100.0))
        return '{p:.1f}% \n({v:d})'.format(p=pct,v=val)
    return my_autopct

plt.subplot(121)
author_pie_2018 = [other_sales_2018, top_sold_authors_2018]
plt.pie(author_pie_2018, labels=labels_aut, explode=(0, 0.1), shadow=True, colors=colors_aut, autopct=author_autopct(author_pie_2018), startangle=180)
plt.title('2018')

plt.subplot(122)
author_pie_2019 = [other_sales_2019, top_sold_authors_2019]
plt.pie(author_pie_2019, labels=labels_aut, explode=(0, 0.1,), shadow=True, colors=colors_aut, autopct=author_autopct(author_pie_2019), startangle=90)
plt.title('2019')
plt.legend(['Other authors', 'Top 10 authors'], loc='upper right', fontsize='small')
plt.savefig('BEST SELLING AUTHORS.png')
# plt.show()

##### top 10 best selling products 2018 and 2019 graph #####

plt.figure(figsize=(10,6))
plt.title('BEST SELLING PRODUCTS')
plt.axis('off')
colors_aut = ['darkseagreen', 'lightgreen']
labels_aut = 'Other products sales', 'Top 10 products sales'
def product_autopct(product_pie):
    def my_autopct(pct):
        total = sum(product_pie)
        val = int(round(pct*total/100.0))
        return '{p:.1f}% \n({v:d})'.format(p=pct,v=val)
    return my_autopct

plt.subplot(121)
product_pie_2018 = [other_products_sales_2018, top_sold_products_2018]
plt.pie(product_pie_2018, labels=labels_aut, explode=(0, 0.1), shadow=True, colors=colors_aut, autopct=product_autopct(author_pie_2018), startangle=160)
plt.title('2018')
plt.legend(['Other products', 'Top 10 products'], loc='upper left', fontsize='x-small')

plt.subplot(122)
product_pie_2019 = [top_other_products_sales_2019, top_sold_products_2019]
plt.pie(product_pie_2019, labels=labels_aut, explode=(0, 0.1,), shadow=True, colors=colors_aut, autopct=product_autopct(product_pie_2019), startangle=160)
plt.title('2019')
plt.savefig('BEST SELLING PRODUCTS.png')
plt.show()