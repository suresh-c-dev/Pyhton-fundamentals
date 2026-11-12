#                      ---Program 1: Name Fixer---

print("\n------program 1 output------\n")


raw = "  suresh KUMAR | suresh.kumar@Gmail.COM | turuvekere  "
clean=raw.strip()

s=clean.split("|")
capital_1=s[0].split()[0].capitalize()
capital_2=s[0].split()[1].capitalize()
capital="".join([capital_1," ",capital_2])

gmail=s[1].strip().lower()
div=gmail.partition("@")
city=s[2].strip().capitalize()

valid_id=gmail.endswith("@gmail.com")

print(f"{capital} | {div[0]} | {valid_id} | {city}")

#                              ---Program 2: Signup Form Check---

print("\n------program 2 output------\n")



email = "  Suresh@Yahoo.COM  "
password = "udaya2026"
age = 17
has_parent_consent = True
is_blocked = False


clean_mail=email.strip().lower()
username=clean_mail.partition("@")
if not is_blocked:
    if clean_mail.endswith(("@gmail.com","@yahoo.com")):

        if len(password) >=8 and (username[0] not in password):
            
            if age>=18 or has_parent_consent:
                print(f"welcome {username[0]}")
            else:
                    print("need parent consent")
        else:
             print("weak password")
    else:            
        print("invalid email")
    
else:
    print("Acount blocked")

#                              ---Program 3: Class Marks Report---


print("\n------program 3 output------\n")

entries = ["  uday SURYA : 85 ", "suresh kumar:42", "  anu   NAIK : 67", "bad entry", "ravi : 30","parker : 90"]
passed=0

for entry in entries:
    if ":" in  entry:
        fix=[]
        student=entry.split(":")
        name=student[0].split()
        for x in name:
            fix.append(x.capitalize())
        name=" ".join(fix)
        
        marks=int(student[1].strip())
        if marks >=80:
            grade="A"
        elif marks >=60:
            grade="B"
        elif marks >=40:
            
            grade="C"
            
        else:
            grade="Fail"
        if marks>=40:
            passed=passed+1
        
        print(f"{name} | {marks}  |  {grade}")
    else:
        print("skipped",entry)

print("passed students: ",passed)
    