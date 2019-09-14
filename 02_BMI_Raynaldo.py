height = float(input("height : "))
weight = float(input("weight : "))
gender = int(input("gender : "))

base = 0.0

def ideal_calc (base, height):
    return base + (2.3 * ((height - 150) / 2.5))

if gender == 0: #Male
    base = ideal_calc(50, height)
elif gender == 1: #Female
    base = ideal_calc(45.5, height)

IpW = base/weight
print("IpW : ", IpW)

if IpW == 1:
    print("Ideal, ", base)
elif IpW < 1 and IpW >= 0.5:
    print("Overweight, ", base)
elif IpW < 0.5:
    print("Obese, ", base)
elif IpW > 1 and IpW <= 2:
    print("Underweight, ", base)
elif IpW > 2:
    print("Anorexic, ", base)
    
print(base)