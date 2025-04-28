def calculate_bmi(height_m: float, weight_kg: float) -> float:
    """Calculate Body Mass Index (BMI) given height in meters and weight in kilograms."""
    if height_m <= 0:
        raise ValueError("Height must be greater than zero.")
    return weight_kg / (height_m ** 2)

def calculate_bmr(height_cm: float, weight_kg: float, age: int, gender: str) -> float:
    """Calculate Basal Metabolic Rate (BMR) using the Harris-Benedict equation."""
    gender = gender.lower()
    if gender == 'male':
        return 88.362 + (13.397 * weight_kg) + (4.799 * height_cm) - (5.677 * age)
    elif gender == 'female':
        return 447.593 + (9.247 * weight_kg) + (3.098 * height_cm) - (4.330 * age)
    else:
        raise ValueError("Gender must be 'male' or 'female'.")
