from tkinter import *

class ContactManager:
    def __init__(self, master):
        self.master = master
        master.title("contact manager")

        self.contacts = []

        Label(master, text="name:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.name = Entry(master, width=50)
        self.name.grid(row=0, column=1, columnspan=5, padx=5, pady=5)

        Label(master, text="surname:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.surname = Entry(master, width=50)
        self.surname.grid(row=1, column=1, columnspan=5, padx=5, pady=5)

        Label(master, text="phone:").grid(row=2, column=0, padx=5, pady=5, sticky="e")
        self.phone = Entry(master, width=50)
        self.phone.grid(row=2, column=1, columnspan=5, padx=5, pady=5)

        Label(master, text="contact list:").grid(row=3, column=0, padx=5, pady=5, sticky="w")
        self.contact_listbox = Listbox(master, height=10, width=60)
        self.contact_listbox.grid(row=4, column=0, columnspan=3, padx=5, pady=5)

        self.create_button('add', 3, 0)
        self.create_button('update', 3, 1)
        self.create_button('delete', 3, 2)

        self.current_string = ""
        self.equation = ""

    def create_button(self, value, row, column, columnspan=1):
        button = Button(self.master, text=value, width=10, 
        command=lambda: self.click_button(value))
        button.grid(row=row, column=column, columnspan=columnspan, padx=5, pady=5)

    def click_button(self, value):
        if value == "add":
            name = self.name.get()
            surname = self.surname.get()
            phone = self.phone.get()

            if name and surname and phone:
                contact = (f"{name} {surname}, {phone}")
                self.contacts.append(contact)
                self.update_contact_listbox()
                self.clear_entries()
                print(f"{name} {surname}, {phone} added!")
            else:
                print("fill all the fields!")

        elif value == "update":
            selected_index = self.contact_listbox.curselection()
            if selected_index:
                name = self.name.get()
                surname = self.surname.get()
                phone = self.phone.get()
            
                if name and surname and phone:
                    updated = (f"{name} {surname}, {phone}")
                    self.contacts[selected_index[0]] = updated
                    self.update_contact_listbox()
                    self.clear_entries()
                    print(f"{name} {surname}, {phone} updated!")
                else:
                    print("fill all the fields!")
            else:
                print("choose a contact!")
        
        elif value == "delete":
            selected_index = self.contact_listbox.curselection()
            if selected_index:
                del self.contacts[selected_index[0]]
                self.update_contact_listbox()
                self.clear_entries()
                print(f"{name} {surname}, {phone} deleted")
            else:
                print("choose a contact!")

    def update_contact_listbox(self): #update of the contact list
        self.contact_listbox.delete(0, END)
        for contact in self.contacts:
            self.contact_listbox.insert(END, contact)

    def clear_entries(self):#clear of the entrie fields
        self.name.delete(0, END)
        self.surname.delete(0, END)
        self.phone.delete(0, END)    


def main():
    root = Tk()
    app = ContactManager(root)
    root.mainloop()

if __name__ == "__main__":
    main()