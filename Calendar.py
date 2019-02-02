day = 0
month_list = ["January","February","March","April","May","June","July","August","September","October","November","December"]

for month in range(len(month_list)):
	day = 0
	while day != 31:
		day = day + 1
		print(month_list[month],day)
		

