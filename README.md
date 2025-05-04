# 📘 Assignment with Solutions

**Assignment with Solutions** is a Python-based project designed to provide a selection of programming challenges and their corresponding solutions. The application enables users to register or log in to access a curated list of assignments. It offers a seamless user experience with functionalities like user authentication, assignment selection, and solution display.

---

## 🌟 Features

- **User Registration and Login**: 
  - Allows users to register with a unique username, email, and password.
  - Login functionality with password validation and recovery options.
  
- **Assignment Repository**:
  - Provides a list of assignments on various programming topics.
  - Solutions are pre-stored and displayed upon selection.
  
- **Interactive Menu**:
  - Users can navigate through the options to register, log in, or exit the application.
  - Assignments are categorized for easy access.

- **Pre-written Assignment Solutions**:
  - Sample solutions for fundamental programming problems such as prime number checks, Armstrong numbers, calculating triangle areas, and more.

---

## 🛠️ Technologies Used

- **Python**:
  - Backend logic for registration, login, and assignment handling.
  - File I/O operations for storing and retrieving user data and assignment solutions.

- **Text Files**:
  - Used for storing assignment solutions (`ch1.txt`, `ch10.txt`, etc.) and user data (`records.txt`).

---

## 🚀 Getting Started

### Prerequisites

- **Python 3.x** installed on your machine.
- Basic understanding of Python programming.

---

### Installation & Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/divyanshi116/Assignment-with-solutions.git
   ```
2. Navigate to the project directory:
   ```bash
   cd Assignment-with-solutions
   ```
3. Ensure all required files (`Register_and_Login.py`, `STP_2022.py`, assignment `.txt` files) are present in the project directory.

4. Run the program:
   ```bash
   python STP_2022.py
   ```

---

## 🖥️ Usage

1. When the application starts, you will see the following options:
   - **register**: Create a new account.
   - **login**: Log in to an existing account.
   - **exit**: Quit the application.

2. After logging in or registering:
   - Select an assignment from the provided list by entering its number.
   - View the solution directly in the console.

3. Example Workflow:
   - Register with a unique username and password.
   - Log in using the registered credentials.
   - Select an assignment (e.g., "Write a program to check if a number is prime or not").
   - View the corresponding solution.

---

## 📂 Project Structure

This project consists of the following files:

1. **`Register_and_Login.py`**:
   - Handles user registration, login, and data validation.
   - Stores user information in a text file (`records.txt`).

2. **`STP_2022.py`**:
   - Main application file.
   - Provides the interactive menu for user navigation and assignment selection.

3. **Assignment Files**:
   - `ch1.txt`, `ch10.txt`, etc.: Contain pre-written solutions for assignments.

4. **Sample Assignments**:
   - **Prime Number Check**: Determine if a number is prime.
   - **Armstrong Number Check**: Verify if a number is an Armstrong number.
   - **ASCII Value Finder**: Find the ASCII value of a character.
   - **Triangle Area Calculation**: Compute the area of a triangle.

---

## 🎯 Example Assignments

### 1. Check if a Number is Prime
```python
# Program to check if a number is prime or not
num = 407

if num > 1:
   for i in range(2, num):
       if (num % i) == 0:
           print(num, "is not a prime number")
           break
   else:
       print(num, "is a prime number")
else:
   print(num, "is not a prime number")
```

### 2. Armstrong Number Checker
```python
# Python program to check if the number is an Armstrong number or not

num = int(input("Enter a number: "))
sum = 0
temp = num
while temp > 0:
   digit = temp % 10
   sum += digit ** 3
   temp //= 10

if num == sum:
   print(num, "is an Armstrong number")
else:
   print(num, "is not an Armstrong number")
```

### 3. Triangle Area Calculation
```python
# Python Program to find the area of a triangle

a = 5
b = 6
c = 7
s = (a + b + c) / 2
area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
print('The area of the triangle is %0.2f' % area)
```

---

## 📋 Features Breakdown

### User Registration (`Register_and_Login.py`)
- Validates username uniqueness.
- Validates email format.
- Ensures password confirmation.

### User Login (`Register_and_Login.py`)
- Validates credentials.
- Provides recovery options for forgotten IDs or passwords.

### Assignment Selection (`STP_2022.py`)
- Displays a menu of assignment topics.
- Reads and displays solutions from `.txt` files based on user selection.

---

## 🔧 Possible Enhancements

- **Dynamic Assignment Loading**:
  - Allow users to add new assignments and solutions dynamically.
  
- **GUI Integration**:
  - Replace the terminal-based interface with a graphical user interface for better usability.

- **Encryption**:
  - Encrypt user credentials for added security.

---

## 🤝 Contributing

Contributions are welcome! If you have suggestions for improvements or new features, feel free to fork the repository and open a pull request.

### Steps to Contribute:
1. Fork the repository.
2. Create a new branch for your feature:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add feature-name"
   ```
4. Push to your branch:
   ```bash
   git push origin feature-name
   ```
5. Open a pull request and describe your changes.

---

## 📜 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## 📧 Contact

For questions or feedback, feel free to reach out to [divyanshi116](https://github.com/divyanshi116). 🚀
