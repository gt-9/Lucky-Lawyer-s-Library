lucky_lawyer_description = "Lucky Lawyer. by Graham goodfellow. Winnipeg: Tutor's Press, 1988."
lucky_lawyer_price = 25.00
On_Not_Giving_Up_description = "On Not Giving Up. by Richard Paul Astely, Newton-le-Willows: Lancashire Press, 1987"
On_Not_Giving_Up_price = 18.50
space_law_description = "Space Law. by Yuri Lightyear. Munich: Timetravel Press, 1892."
space_law_price = 1961.00
sales_tax = .088
customer_one_total = 0
customer_one_itemization = ""
customer_one_total += lucky_lawyer_price
customer_one_itemization += lucky_lawyer_description
customer_one_total += On_Not_Giving_Up_price
customer_one_itemization += On_Not_Giving_Up_description
customer_one_tax = customer_one_total * sales_tax
customer_one_total += customer_one_tax
print("Customer One Items")
print(customer_one_itemization)
print("Customer One Total")
print(customer_one_total)