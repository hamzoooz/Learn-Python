def seperotor():
    print("#"*50)

class Member:

    user_not_alowed = ["hell", "God", "shit"]
    number_of_member = 0


    def __init__(self, f_name, m_name, l_name, gender ):

        self.fname = f_name
        self.mname = m_name
        self.lname = l_name
        self.gender = gender 
        Member.number_of_member +=1

    def full_name(self):
        # return f" {self.fname} {self.mname} {self.lname}"
        if self.fname in Member.user_not_alowed:
            return "You Can't Use This Name "
        else:
            return f" {self.fname} {self.mname} {self.lname}"

    def name_with_title(self):

        if self.fname in Member.user_not_alowed:
            return "You Can't Use This Name "
            # raise ValueError("Name Note Allowed ")
        else:
            return f" {self.fname} {self.mname} {self.lname}"

        if self.gender == "mail":
             return f" Hello Mr {self.full_name()} "
        elif self.gender == "famail":
            return f" Hello Miss {self.full_name()} "
        else :
            return f" Hello {self.full_name()} "
    @classmethod
    def count_member(cls):
        print(f"We Have {cls.number_of_member} in Our System ")
        # Member.number_of_member +=1 


    def delete_member(self):
        Member.number_of_member -=1 
        return f"{self.fname} Was Deleted ! "

seperotor() # seperotor
member_one = Member("hamza", "banga", "ahmed","mail")
member_tow = Member("osama", "ali", "hassa", "unkonwn")
member_three = Member("mona", "esea", "hamza", "famail" )
member_foure = Member("hell", "esea", "hamza", "famail" )

seperotor() # seperotor
print(f"Count Of User : {Member.number_of_member}")
print(member_three.delete_member())
print(f"Count Of User after deleted : {Member.number_of_member}")

seperotor() # seperotor
print(member_one.fname, member_one.mname, member_one.lname)
print(member_tow.fname, member_tow.mname, member_tow.lname)
print(member_three.fname, member_three.mname, member_three.lname)

seperotor() # seperotor
print(member_one.full_name())
print(member_foure.full_name())



seperotor() # seperotor
print(member_one.name_with_title())
print(member_tow.name_with_title())
print(member_three.name_with_title())
print(member_foure.name_with_title())


