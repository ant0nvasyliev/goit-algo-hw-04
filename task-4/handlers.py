def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return f"Контакт {name} додано!"


def change_contact(args, contacts):
    name, new_phone = args 
    if name in contacts:
        contacts[name] = new_phone
        return f"Контакт {name} оновлено!"
    else:
        return f"Контакт {name} не знайдено!"
    

def show_phone(args, contacts):
    name = args[0]
    phone = contacts.get(name)
    if phone: 
        return phone
    else: 
        return "Контакт не знайдено!"
    

def show_all(contacts):
    if contacts == {}:
        return "Покищо контактів немає!"
    
    return contacts
    