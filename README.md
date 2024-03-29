# Books sales analysis

Created by [Rosvaldas Šlekys](https://github.com/RosSlek) 

This project was made to improve in data analysis.

## The main goals for this project were to:
#### • Analyze dataset.
#### • Offer some insights related to data.
#### • Create a [PowerBI](https://github.com/RosSlek/Books_sales_analysis/blob/master/Books%20sales%20analysis.pbix) visualization.
#### • Improve and have fun.

## Main steps:
#### • Chose dataset from [Kaggle](https://www.kaggle.com/datasets/shilpikulshrestha/books-sold-dataset).
#### • Clean, divide, reshape and analyse data.
#### • Save results to [excel](https://github.com/RosSlek/Books_sales_analysis/blob/master/Balance.xlsx) for easy access (there is more information then covered in analysis below).
#### • Make some insights and suggestions of analysis.

## About data:
Dataset of educational books sold in year 2018-2019. This dataset has four categories of books sold, also provide information about author, publication, information about sales made on discounted books, cost price and profit. Books are sold in India, values are in Indian rupee (INR), which at the period under consideration was equal to around 0.012 Euro (Eur).

## Visualization:
After dataset is cleaned and balance table is created, both tables are saved in a PostgreSQL database. Then this data is taken to Power bi and visualizations are created.
![image](https://github.com/RosSlek/Books_sales_analysis/assets/149397027/015e904f-bfed-4d15-96b0-7ce88e9703cc)

![image](https://github.com/RosSlek/Books_sales_analysis/assets/149397027/47dd19f7-5e83-495e-b4b8-859080142b92)

![image](https://github.com/RosSlek/Books_sales_analysis/assets/149397027/950c0687-b518-4b20-8567-bbfa9da469e5)

## Analysis:
Firstly let`s find the most important stats and combine them into balance sheet type table. As we can see revenue slightly increased from 652,271k in year 2018 to 662,290k in 2019. Gross profit grew by 8.6% and gross profit percentage increased to 16.36% while cost of revenue rose insignificantly. However, amount of units sold per year almost doubled, so operating expenses most likely grew, thus reducing net profit. Gross profit per unit sold shrank almost in half. 

![image](https://github.com/RosSlek/Books_sales_analysis/assets/149397027/f77631d0-d0c8-4062-a865-478dda0981c0)

Now let`s look at some data by quarters. Gross profit per quarter was not stable, it heavily decreased for a year until Q2 of 2019, then it increased 6 fold compared to the quarter before. These irregularities might be a consequence of educational product nature. It is not evenly required year to year or month to month so a lot of unknown factors could have impact for company's profitability and sales.

![image](https://github.com/RosSlek/Books_sales_analysis/assets/149397027/2b9db41e-b3e8-4287-b47c-f5696915fe8d)

Amount of units sold by quarter sharply droped after Q2 of year 2018 and stayed low until Q2 of 2019. Q2 and Q3 account for 82.6% of 2019 sales, however gross profit per unit sold was lowest in Q2 - 2019 throughout both years.

![image](https://github.com/RosSlek/Books_sales_analysis/assets/149397027/81553bd7-236f-44ab-903a-28b535889e24)

From the table we see, that most of the sold books in 2019 were published by NCERT (National Council of Education Research and Training), so that might indicate some changes in educational program of India. New releases or regulations could also explain why sales rose so quickly in Q2 and Q3 but profit per sale was all time low.

![image](https://github.com/RosSlek/Books_sales_analysis/assets/149397027/fa5c4592-8120-4de7-8671-8497aa5dfa5d)

Majority of sold books in 2018 fall into either college or competition category, books for middle and high school accounted for only 6.8%. 2019 is a different story with a bigger part of the pie (59.3%) for school books and more even overall distribution.

![image](https://github.com/RosSlek/Books_sales_analysis/assets/149397027/ab8139be-2f36-4298-b852-d4d356d4e315)

After a quick search, we can see that actual changes in educational policy were made for year 2019, with a focus "to create a more holistic, unified education system, with greater continuity, foci on longer free and compulsory education (from age three to 18), and a Foundation stage that ensures greater school readiness when children begin primary school." This event perfectly explains why NCERT was the most sold author and school books took a bigger part of sales in 2019. Sources:
https://educationforallinindia.com/wp-content/uploads/2020/12/national-policy-on-education-final-english_55pages.pdf
https://www.britishcouncil.in/sites/default/files/school_education_system_in_india_report_2019_final_web.pdf

![image](https://github.com/RosSlek/Books_sales_analysis/assets/149397027/2d322aec-f25f-4b91-a2d2-d0dd363705e3)

Since selling product is educational, it is bought by necessity, so special offers does not have a big impact on sales. Following pie chart shows, that less than 15% of sales are made on discounted books. It is also possible, that discount culture is not so common in region.

![image](https://github.com/RosSlek/Books_sales_analysis/assets/149397027/51902b7e-d824-489a-b22e-4bd6bf128c3d)

Gross profit generated by discounted books does not differ much from regular price profit for the period, except Q1 - 2019. If hypothesis about new releases of books is correct, there might have been sale offers before new version came out. Or it might have been a special offer in order to increase sales, which were steadily declining and lowest for the recorded period at the time.

![image](https://github.com/RosSlek/Books_sales_analysis/assets/149397027/5336615e-2368-4747-9529-d2d07dfbfbc8)

Sales by day of the week or part of the day also does not show any meaningful deviations. More sales are done in the first half of the day, but that is normal, so other factors should be considered while making a marketing strategy.

![image](https://github.com/RosSlek/Books_sales_analysis/assets/149397027/9298534a-1251-406e-9fd1-5a8c69fda94b)

![image](https://github.com/RosSlek/Books_sales_analysis/assets/149397027/fef63a6e-5bc7-49bf-abcd-bd3c21493170)

Same goes for gender factor, sales are distributed pretty evenly, with a slight edge to females, indicating, that more and more women are reaching for better education in India.

![image](https://github.com/RosSlek/Books_sales_analysis/assets/149397027/baaa448b-5594-4a68-bbfc-2c9cde331111)

From the pie charts we can see, that ten most sold authors (out of 183 author) account for 53.3% of sales in 2018 and 85% in 2019, again, because most of the sales come from single author mentioned above in the analysis (NCERT).

![image](https://github.com/RosSlek/Books_sales_analysis/assets/149397027/723103fe-d776-4408-9da5-dafeda931d22)

Top 10 books are responsible for roughly 50% of the sales (out of 251 different book). This concentration could be marked as a weak spot and to widen the range of different products sold would be advisable.

![image](https://github.com/RosSlek/Books_sales_analysis/assets/149397027/8a7d3646-d082-40c2-97e6-bbd1a4fa9c16)

## Conslusion
From analysis we can see that business is not at a fast growing pace in a given period, even with a huge increase in books sold at year 2019, profits does not show significant improvement and strongly vary from quarter to quarter. Factors which are out of business control can have a huge impact on sales, because of the nature of selling goods. Clear example of this is second quarter of 2019, when National Education Policy changes took place. Sales have normal distribution between genders, days of the week or parts of the day. Special offers also does not play significant role. Also small percentage of products is responsible for half the sales, so a strategy to improve sales of other products might be an idea worth of consideration.
