# tools/crm_tools.py

from langchain.tools import StructuredTool
from mock_crm import MockCRM
from tools.email_tools import send_email

# Initialize mock CRM
crm = MockCRM()

# Wrapped CRM actions with automatic emails
def create_contact_with_notification(name: str, email: str):
    result = crm.create_contact(name, email)
    if result["status"] == "success":
        send_email(
            recipient=email,
            subject="Welcome",
            body="Your account has been successfully created."
        )
    return result

def update_contact_with_notification(contact_id: str, name: str, email: str):
    result = crm.update_contact(contact_id, name, email)
    if result["status"] == "success":
        send_email(
            recipient=email,
            subject="Welcome",
            body="Your account has been successfully updated."
        )
    return result

def create_deal_with_notification(deal_name: str, amount: float, contact_id: str, email: str):
    result = crm.create_deal(deal_name, amount, contact_id)
    if result["status"] == "success":
        send_email(
            recipient=email,
            subject="Deal",
            body="Deal successfully done."
        )
    return result

# Register as tools
create_contact_tool = StructuredTool.from_function(
    func=create_contact_with_notification,
    name="create_contact",
    description="Create a contact and send an automatic welcome email."
)

update_contact_tool = StructuredTool.from_function(
    func=update_contact_with_notification,
    name="update_contact",
    description="Update a contact and send an automatic update email."
)

create_deal_tool = StructuredTool.from_function(
    func=create_deal_with_notification,
    name="create_deal",
    description="Create a deal for a contact and send an automatic confirmation email."
)
