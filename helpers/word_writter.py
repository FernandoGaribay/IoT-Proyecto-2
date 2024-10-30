from docx import Document
from models.contact import Contact
from helpers.quantumbank_email_methods import QuantumBankMethods

class WordWritter():
    def replace_variables_in_template(self, template_path, contact, output_path):
        doc = Document(template_path)
        bank_methods = QuantumBankMethods()

        replacements = {
            '{id}': str(contact.id),
            '{name}': contact.name,
            '{surname1}': contact.surname1,
            '{surname2}': contact.surname2,
            '{job_title}': contact.job_title,
            '{company}': contact.company,
            '{street}': contact.street,
            '{ext_number}': str(contact.ext_number),
            '{int_number}': str(contact.int_number),
            '{neighborhood}': contact.neighborhood,
            '{city}': contact.city,
            '{state}': contact.state,
            '{postal_code}': str(contact.postal_code),
            '{phone}': contact.phone,
            '{email}': contact.email,
            '{birth_date}': contact.birth_date,
            '{age}': str(contact.age),
            '{bank_name}': bank_methods.BANK_NAME,
            '{bank_contact_info}': bank_methods.BANK_CONTACT_INFO,
            '{bank_email}': bank_methods.BANK_EMAIL,
            '{bank_address}': bank_methods.BANK_ADDRESS,
            '{account_number}': bank_methods.get_account_number(),
            '{current_balance}': bank_methods.get_current_balance(),
            '{previous_balance}': bank_methods.get_current_balance(),
            '{total_deposits}': bank_methods.get_current_balance(),
            '{total_withdrawals}': bank_methods.get_current_balance(),
            '{service_charges}': bank_methods.get_current_balance(),
            '{interest_earned}': bank_methods.get_current_balance(),
            '{current_date}': bank_methods.get_current_date(),
            '{previous_month_end}': bank_methods.get_previous_month_start(),
            '{credit_limit}': bank_methods.get_credit_limit(),
            '{billing_date}': bank_methods.get_billing_date(),
            '{due_date}': bank_methods.get_due_date(),
            '{account_type}': bank_methods.get_account_type(),
            '{account_opening_date}': bank_methods.get_account_opening_date(),
            '{total_amount}': bank_methods.get_total_amount(),
            '{invoice_description}': bank_methods.get_invoice_description(),
        }

        for paragraph in doc.paragraphs:
            for key, value in replacements.items():
                if key in paragraph.text:
                    paragraph.text = paragraph.text.replace(key, str(value))

        doc.save(output_path)
        print(f'Documento guardado como {output_path}')
