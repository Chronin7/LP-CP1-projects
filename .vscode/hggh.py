staff = 32+1-3
students = 100-1
gest = 100*2-15
table = (staff+students+gest)/12
if type(table)==float:
	table = table+.5
print(f"we need {round(table)} tables")
