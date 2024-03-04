def BMI_Calc(feet, inches, weight_lbs):
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
  #Output message to console
  print(f'\nThis person\'s BMI is {BMI:.1f}, which is {category}\n')
  
def Category_Calc(BMI):

main():
  feet = int(input("Enter the height in feet: "))
  inches = int(input("Enter the additional inches: "))
  weight_lbs = int(input("Enter the weight in lbs: "))

  BMI_Calc(feet, inches, weight_lbs)

  return 0


#run main
main()
