def BMI_Calc(feet, inches, weight_lbs):
  try:
    #convert height to inches first
    height = feet * 12 + inches
    #convert height in inches to height in cm
    height = height * 0.025
    #convert weight in lbs to weight in kg
    weight_kg = weight_lbs * 0.45
    #square the height
    height = height * height
    #divide weight by height^2
    BMI = weight_kg / height
    #find Category
    category = Category_Calc(BMI)
    #return BMI and category (will be used in the html)
    return BMI, category
  except:
    print("Error")
  
def Category_Calc(BMI):
  # -inf < x < 18.5
  if (BMI < 18.5):
    return "Underweight"
  # 18.5 <= x < 25
  elif (BMI >=18.5 and BMI < 25):
    return "Normal Weight"
  # 25 <= x < 30
  elif (BMI >= 25 and BMI < 30):
    return "Overweight"
  # 30 <= x < inf
  elif (BMI >= 30):
    return "Obese"
