class MockCRM:
    def __init__(self):
        self.contacts = {}
        self.deals = {}
        self.contact_id_counter = 1
        self.deal_id_counter = 1

    def create_contact(self, name, email):
        contact_id = str(self.contact_id_counter)
        self.contacts[contact_id] = {"name": name, "email": email}
        self.contact_id_counter += 1
        return {"status": "success", "contact_id": contact_id, "name": name, "email": email}

    def update_contact(self, contact_id, name=None, email=None):
        if contact_id in self.contacts:
            if name:
                self.contacts[contact_id]["name"] = name
            if email:
                self.contacts[contact_id]["email"] = email
            return {"status": "success", "contact_id": contact_id, "updated_contact": self.contacts[contact_id]}
        else:
            return {"status": "error", "message": "Contact not found."}

    def create_deal(self, deal_name, amount, contact_id):
        if contact_id in self.contacts:
            deal_id = str(self.deal_id_counter)
            self.deals[deal_id] = {
                "deal_name": deal_name,
                "amount": amount,
                "contact_id": contact_id,
            }
            self.deal_id_counter += 1
            return {"status": "success", "deal_id": deal_id, "deal_name": deal_name, "amount": amount, "contact_id": contact_id}
        else:
            return {"status": "error", "message": "Contact not found. Cannot create deal."}


if __name__ == "__main__":
    crm = MockCRM()

    print("\nCreating contact:")
    print(crm.create_contact("Adil Iqbal", "adil@example.com"))

    print("\nUpdating contact:")
    print(crm.update_contact("1", name="Adil Updated", email="newemail@example.com"))

    print("\nCreating deal:")
    print(crm.create_deal("Important Deal", 10000.0, "1"))

    print("\nTrying to create deal for non-existing contact:")
    print(crm.create_deal("Failing Deal", 5000.0, "999"))
