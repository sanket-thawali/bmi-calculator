def calculate_bmi(weight,height):
    try:
        weight=float(weight)
        height=float(height)
        
        if weight<=0 and height<=0:
            return "Invalid input.Weight and height must be positive"
        
        bmi=weight/(height**2)
        if bmi<18.5:
            category="Underweight"
        elif 18.5<=bmi<24.9:
            category="Normal weight"
        elif 24.9<=bmi<29.9:
            category="Overweight"
        else:
            category="Obese"
            
        return f"Your BMI is {bmi:.2f} and Your are categorized as {category}"
    
    except ValueError:
        return "Valid Input.Please input valid weight and height"
    
def main():
    print("BMI calculator")
    weight=input("Enter the weight in kg: ")
    height=input("Enter the height in m: ")
    
    result=calculate_bmi(weight,height)
    print(result)
    
if __name__=="__main__":
    main()

    
    