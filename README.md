# TestingQAHW

Assignment-2:

Contributors: Claire Justis, cgj127, ClaireG-J
Language: Python, Pytest

Functions:

BMI_Calc(feet, inches, weight_lbs)
  * Recieves input as parameters
  * Calculates BMI from parameters
  * Prints out the result to console

Category_Calc(BMI)
  * Recieves a BMI value as a parameter
  * Evaluates the Category the BMI falls under
      * x < 18.5 : Underweight
      * 18.5 <= x < 25 : Normal Weight
      * 25 <= x < 30 : Overweight
      * x >= 30 : Obese
  * Returns a string containing the category

main()
  * Prints out welcome message to console
  * Takes user input for feet
  * Takes user input for inches
  * Takes user input for weight (in lbs)
