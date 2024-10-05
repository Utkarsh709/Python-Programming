#1

echo "Enter your name: "
read name

echo "Enter your age: "
read age

echo "Enter your favorite programming language: "
read language

# Display the entered values
echo "Your name is: $name"
echo "Your age is: $age"
echo "Your favorite programming language is: $language"






#2

# Prompt the user to enter the file name
echo "Enter the file name: "
read file_name

# Check if the file exists
if [ -f "$file_name" ]; then
    # Use wc -l to count the number of lines in the file
    line_count=$(wc -l < "$file_name")
    echo "The file '$file_name' has $line_count lines."
else
    echo "File '$file_name' not found!"
fi






#3
# Prompt the user to enter their birth year
echo "Enter your birth year: "
read birth_year

# Get the current year using the date command
current_year=$(date +"%Y")

# Calculate the age
age=$((current_year - birth_year))

# Display the calculated age
echo "You are $age years old."




#4

# Display current date and time
echo "Current Date and Time: $(date)"

# Display the current user's name
echo "Username: $(whoami)"

# Display the current working directory
echo "Current Directory: $(pwd)"






#5

# Prompt the user to enter the first file name
echo "Enter the first file name: "
read file1

# Prompt the user to enter the second file name
echo "Enter the second file name: "
read file2

# Check if both files exist
if [[ -f "$file1" && -f "$file2" ]]; then
    # Compare the two files using diff
    if diff "$file1" "$file2" > /dev/null; then
        echo "The files are identical."
    else
        echo "The files are different."
    fi
else
    echo "One or both files do not exist. Please check the file names."
fi




#6

# Create and assign values to variables
name="Utkarsh"
age=25
city="Nanded"

# Print the values of the variables
echo "Name: $name"
echo "Age: $age"
echo "City: $city"





#7

# Prompt the user to enter two numbers
echo "Enter the first number: "
read a

echo "Enter the second number: "
read b

# Display original values
echo "Before swapping: a = $a, b = $b"

# Swapping without using a third variable
a=$((a + b))  # Step 1: a becomes a + b
b=$((a - b))  # Step 2: b becomes (a + b) - b, which is a
a=$((a - b))  # Step 3: a becomes (a + b) - a, which is b

# Display swapped values
echo "After swapping: a = $a, b = $b"




#8

# Prompt the user to enter the principal amount, rate of interest, and time period
echo "Enter the principal amount: "
read principal

echo "Enter the rate of interest (in %): "
read rate

echo "Enter the time period (in years): "
read time

# Calculate simple interest using the formula: SI = (P * R * T) / 100
simple_interest=$(( (principal * rate * time) / 100 ))

# Display the calculated simple interest
echo "The Simple Interest is: $simple_interest"





#9

# Prompt the user to enter three numbers
echo "Enter the first number: "
read a

echo "Enter the second number: "
read b

echo "Enter the third number: "
read c

# Compare the numbers to find the largest
if [[ $a -ge $b && $a -ge $c ]]; then
    echo "The largest number is: $a"
elif [[ $b -ge $a && $b -ge $c ]]; then
    echo "The largest number is: $b"
else
    echo "The largest number is: $c"
    
    
fi





#10

# Prompt the user to enter a number
echo "Enter a number: "
read number

# Initialize variables
reverse=0
n=$number

# Loop to reverse the number
while [ $n -gt 0 ]
do
    remainder=$((n % 10))         # Get the last digit
    reverse=$((reverse * 10 + remainder))  # Append it to the reversed number
    n=$((n / 10))                 # Remove the last digit from the original number
done

# Display the reversed number
echo "The reverse of $number is: $reverse"





#11

# Prompt the user to enter a number
echo "Enter a number: "
read number

# Initialize factorial to 1
factorial=1

# Check if the number is negative
if [ $number -lt 0 ]; then
    echo "Factorial is not defined for negative numbers."
    exit 1
fi

# Loop to calculate the factorial
for (( i=1; i<=number; i++ ))
do
    factorial=$((factorial * i))
done

# Display the factorial
echo "The factorial of $number is: $factorial"





#12

# Prompt the user to enter a year
echo "Enter a year: "
read year

# Check if the year is a leap year
if (( (year % 4 == 0 && year % 100 != 0) || (year % 400 == 0) )); then
    echo "$year is a leap year."
else
    echo "$year is not a leap year."
fi


