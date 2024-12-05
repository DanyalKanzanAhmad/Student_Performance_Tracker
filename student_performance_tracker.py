class UserAuthentication:
    def __init__(self):
        self.credentials = {}

    def signup(self):
        print("\n--- Signup ---")
        while True:
            username = input("Enter a username: ").strip()
            if username in self.credentials:
                print("Username already exists. Please try another.")
            elif not username:
                print("Username cannot be empty. Please try again.")
            else:
                break

        while True:
            password = input("Enter a password: ").strip()
            if not password:
                print("Password cannot be empty. Please try again.")
            else:
                break

        self.credentials[username] = password
        print("Signup successful! You can now log in.")

    def login(self):
        print("\n--- Login ---")
        while True:
            username = input("Enter your username: ").strip()
            password = input("Enter your password: ").strip()

            if username in self.credentials and self.credentials[username] == password:
                print("Login successful! Welcome to the Student Performance Tracker.")
                return True
            else:
                print("Invalid username or password. Please try again.")


class Student:
    def __init__(self, name):
        self.name = name
        self.scores = []

    def add_scores(self, scores):
        self.scores.extend(scores)

    def calculate_average(self):
        if self.scores:
            return sum(self.scores) / len(self.scores)
        return 0

    def is_passing(self, passing_mark=40):
        return all(score >= passing_mark for score in self.scores)


class PerformanceTracker:
    def __init__(self):
        self.students = {}

    def add_student(self, name, scores):
        if name not in self.students:
            student = Student(name)
            student.add_scores(scores)
            self.students[name] = student
        else:
            print(f"Student {name} already exists. Updating scores.")
            self.students[name].add_scores(scores)

    def calculate_class_average(self):
        if not self.students:
            print("No students have been added yet.")
            return 0
        total_scores = 0
        total_subjects = 0
        for student in self.students.values():
            total_scores += sum(student.scores)
            total_subjects += len(student.scores)
        return total_scores / total_subjects if total_subjects else 0

    def display_student_performance(self):
        if not self.students:
            print("No students have been added yet.")
            return
        for name, student in self.students.items():
            avg = student.calculate_average()
            status = "Passing" if student.is_passing() else "Failing"
            print(f"{name}: Average: {avg:.2f}, Status: {status}")

    def display_class_average(self):
        class_avg = self.calculate_class_average()
        if class_avg != 0:
            print(f"Class Average: {class_avg:.2f}")


def get_scores():
    scores = []
    subjects = ["Math", "Urdu", "English"]
    for subject in subjects:
        while True:
            try:
                score = int(input(f"Enter {subject} score: "))
                if 0 <= score <= 100:  # Ensure the score is valid
                    scores.append(score)
                    break
                else:
                    print("Score must be between 0 and 100. Please try again.")
            except ValueError:
                print("Invalid input. Please enter an integer.")
    return scores


def main():
    auth = UserAuthentication()
    tracker = PerformanceTracker()

    # Signup/Login Flow
    while True:
        print(
            "\nWelcome to the Student Performance Tracker \nAuthenticate Person only 'Please Signup'"
        )
        print("1. Signup")
        print("2. Login")
        print("3. Exit")
        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            auth.signup()
        elif choice == "2":
            if auth.login():
                break
        elif choice == "3":
            print("Exiting the program. Goodbye Have a Great Day!")
            return
        else:
            print("Invalid choice. Please try again.")

    # Student Performance Tracker
    while True:
        print("\n--- Student Performance Tracker ---")
        print("1. Add a Student")
        print("2. View Student Performances")
        print("3. View Class Average")
        print("4. Logout")
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            name = input("Enter student name: ").strip()
            if name:
                scores = get_scores()
                tracker.add_student(name, scores)
            else:
                print("Student name cannot be empty. Please try again.")
        elif choice == "2":
            tracker.display_student_performance()
        elif choice == "3":
            tracker.display_class_average()
        elif choice == "4":
            print("Logging out. Returning to main menu.")
            main()
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
