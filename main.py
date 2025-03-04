#Viplav Dodeja
#20425
#HW2


import datetime

class Applicant:
    def __init__(self, full_name, date_of_birth, sex, home_address, phone_home, phone_mobile, email):
        self.full_name = full_name
        self.date_of_birth = date_of_birth
        self.sex = sex
        self.home_address = home_address
        self.phone_home = phone_home
        self.phone_mobile = phone_mobile
        self.email = email

class LanguageSkill:
    def __init__(self, language, read_level, write_level, speak_level):
        self.language = language
        self.read_level = read_level
        self.write_level = write_level
        self.speak_level = speak_level

class EducationRecord:
    def __init__(self, institution_name, location, attended_from, attended_to, certificates, field_of_study):
        self.institution_name = institution_name
        self.location = location
        self.attended_from = attended_from
        self.attended_to = attended_to
        self.certificates = certificates
        self.field_of_study = field_of_study

class ApplicationForm:
    def __init__(self, applicant):
        self.applicant = applicant
        self.language_skills = []
        self.education_records = []
    
    def add_language_skill(self, language_skill):
        self.language_skills.append(language_skill)
    
    def add_education_record(self, education_record):
        self.education_records.append(education_record)
    
    def display_application(self):
        print("Applicant Information:")
        print(f"Name: {self.applicant.full_name}")
        print(f"DOB: {self.applicant.date_of_birth}")
        print(f"Sex: {self.applicant.sex}")
        print(f"Address: {self.applicant.home_address}")
        print(f"Home Phone: {self.applicant.phone_home}, Mobile: {self.applicant.phone_mobile}")
        print(f"Email: {self.applicant.email}")
        print("\nLanguages:")
        for lang in self.language_skills:
            print(f"{lang.language} - Read: {lang.read_level}, Write: {lang.write_level}, Speak: {lang.speak_level}")
        print("\nEducation:")
        for edu in self.education_records:
            print(f"Institution: {edu.institution_name}, Location: {edu.location}, Field: {edu.field_of_study}, Attended: {edu.attended_from} - {edu.attended_to}, Certificates: {edu.certificates}")

class ApplicationManager:
    def __init__(self):
        self.applications = []
    
    def add_application(self, application):
        self.applications.append(application)
    
    def list_applications(self):
        for idx, app in enumerate(self.applications):
            print(f"{idx+1}. {app.applicant.full_name}")
    
    def search_application(self, name):
        for app in self.applications:
            if app.applicant.full_name.lower() == name.lower():
                app.display_application()
                return
        print("Application not found.")
    
    def delete_application(self, name):
        for app in self.applications:
            if app.applicant.full_name.lower() == name.lower():
                self.applications.remove(app)
                print("Application deleted.")
                return
        print("Application not found.")
    
    def update_application(self, name):
        for app in self.applications:
            if app.applicant.full_name.lower() == name.lower():
                print("Updating applicant details...")
                app.applicant.home_address = input(f"Enter new home address (leave blank to keep {app.applicant.home_address}): ") or app.applicant.home_address
                app.applicant.phone_home = input(f"Enter new home phone (leave blank to keep {app.applicant.phone_home}): ") or app.applicant.phone_home
                app.applicant.phone_mobile = input(f"Enter new mobile phone (leave blank to keep {app.applicant.phone_mobile}): ") or app.applicant.phone_mobile
                app.applicant.email = input(f"Enter new email (leave blank to keep {app.applicant.email}): ") or app.applicant.email
                print("Applicant details updated successfully.")
                return
        print("Application not found.")
    
# User menu function in main
def main():
    manager = ApplicationManager()
    
    while True:
        print("\nApplication Manager Menu:")
        print("1. Add Applicant")
        print("2. List Applicants")
        print("3. Search Applicant")
        print("4. Update Applicant")
        print("5. Delete Applicant")
        print("6. Exit")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            name = input("Full Name: ")
            
            while True:
                dob = input("Date of Birth (DD/MM/YYYY): ")
                try:
                    datetime.datetime.strptime(dob, "%d/%m/%Y")
                    break
                except ValueError:
                    print("Invalid date format. Please enter in DD/MM/YYYY format.")
            
            while True:
                sex = input("Sex (Male/Female): ").strip().lower()
                if sex in ["male", "female"]:
                    sex = sex.capitalize()
                    break
                else:
                    print("Invalid input. Please enter 'Male' or 'Female'.")
            
            address = input("Home Address: ")
            phone_home = input("Home Phone: ")
            phone_mobile = input("Mobile Phone: ")
            email = input("Email: ")
            applicant = Applicant(name, dob, sex, address, phone_home, phone_mobile, email)
            application = ApplicationForm(applicant)
            
            for lang in ["English", "Spanish"]:
                print(f"Enter {lang} proficiency levels:")
                read_level = input("Reading (Very Good/Good/Weak): ")
                write_level = input("Writing (Very Good/Good/Weak): ")
                speak_level = input("Speaking (Very Good/Good/Weak): ")
                application.add_language_skill(LanguageSkill(lang, read_level, write_level, speak_level))
            
            while True:
                language = input("Enter another language (or type 'done' to finish): ")
                if language.lower() == 'done':
                    break
                read_level = input("Reading proficiency (Very Good/Good/Weak): ")
                write_level = input("Writing proficiency (Very Good/Good/Weak): ")
                speak_level = input("Speaking proficiency (Very Good/Good/Weak): ")
                application.add_language_skill(LanguageSkill(language, read_level, write_level, speak_level))
            
            while True:
                institution = input("Enter institution name (or type 'done' to finish): ")
                if institution.lower() == 'done':
                    break
                location = input("Institution location: ")
                attended_from = input("Attended from (year): ")
                attended_to = input("Attended to (year): ")
                certificates = input("Certificates/Degrees earned: ")
                field_of_study = input("Field of study: ")
                application.add_education_record(EducationRecord(institution, location, attended_from, attended_to, certificates, field_of_study))
            
            manager.add_application(application)
            print("Applicant added successfully.")
        
        elif choice == "2":
            print("\n--- Application List ---")
            manager.list_applications()
        
        elif choice == "3":
            name = input("Enter the name of the applicant to search: ")
            manager.search_application(name)
        
        elif choice == "4":
            name = input("Enter the name of the applicant to update: ")
            manager.update_application(name)
        
        elif choice == "5":
            name = input("Enter the name of the applicant to delete: ")
            manager.delete_application(name)
        
        elif choice == "6":
            print("Exiting program.")
            break
        
        else:
            print("Invalid choice. Please try again.")
    
if __name__ == "__main__":
    main()
