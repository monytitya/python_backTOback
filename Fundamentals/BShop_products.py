total_price = 300

if total_price > 100:
    final_price = total_price * 0.8   # dis 20%

elif total_price >= 50:
    final_price = total_price * 0.9   # dis 10%

else:
    final_price = total_price         # no dis
print("Final Price:", final_price)

