import mechanize, sys, configparser, datetime, string

br=mechanize.Browser()
cp= configparser.ConfigParser()
d=datetime.date.today()
isRestDay=True

days_schedule=["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
days=["mon", "tues", "wed", "thur", "fri", "sat", "sun"]

cp.read("macros.txt")
if len(sys.argv)==1:
	if(cp.has_section("schedule")):
		print("Schedule section exists")
		d=datetime.date.today()
		day=d.weekday()
		print("%s is: %s"%(days_schedule[day], cp.get('schedule', days[day])))
		if cp.get('schedule', days[day])=="W":
			isRestDay=False
	else:
		print("No scheduling information")
		sys.exit()
elif len(sys.argv)==2:
	if sys.argv[1]=="W":
		isRestDay=False;
		print("Manual selection: W")
	elif sys.argv[1]=="R":
		isRestDay=True;
		print("Manual selection: R")
else:
	print("Usage statement goes here.")
	sys.exit()

if isRestDay==True:
	targetSection="rest"
else:
	targetSection="workout"

if cp.has_section(targetSection)==False:
	print("Error: targets section doesn't exist")
	sys.exit()

if cp.has_option(targetSection, "calories")==False:
	print("No calorie target")
	sys.exit()
targetCalories=cp.get(targetSection, "calories")
if cp.has_option(targetSection, "protein")==False:
	print("No protein target")
	sys.exit()
targetProtein=cp.get(targetSection, "protein")
if cp.has_option(targetSection, "carb")==False:
	print("No carb target")
	sys.exit()
targetCarb=cp.get(targetSection, "carb")
if cp.has_option(targetSection, "fat")==False:
	print("No fat target")
	sys.exit()
targetFat=cp.get(targetSection, "fat")

if cp.has_section("login")==False:
	print("No login section exists")
	sys.exit()

if cp.has_option("login", "username")==False:
	print("No username provided")
	sys.exit()
username=cp.get("login", "username")
if cp.has_option("login", "password")==False:
	print("No password provided")
	sys.exit()
password=cp.get("login", "password")
print("All configuration options present")

print("Logging in")
br.open("https://www.myfitnesspal.com/account/login")
br.select_form(nr=2)
br.form["username"]=username
br.form["password"]=password
print("Login sent")
r=br.submit();
print("Login response received")

#if string "Username:" appears in response of br.submit(), then login failed
if string.count(r.read(), "Incorrect username or password")!=0:
	print("Bad username or password.")
	sys.exit()
print("Login successful")
print("Opening custom goals page")
br.open("http://www.myfitnesspal.com/account/change_goals_custom")
print("Custom goals page loaded")
br.select_form(nr=0)
br.form["goals[daily_energy_goal]"]=targetCalories
br.form["goals[carb_ratio]"]=[targetCarb]
br.form["goals[protein_ratio]"]=[targetProtein]
br.form["goals[fat_ratio]"]=[targetFat]
print("Submitting custom goals page")
br.submit()
print("Custom goals page submitted")

print("Opening logout page")
br.open("http://www.myfitnesspal.com/account/logout")
print("Logged out")
