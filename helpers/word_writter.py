import sys
import os

from docx import Document
from models.contact import Contact

class WordWritter():
    def replace_variables_in_template(self, template_path, contact, output_path):
        doc = Document(template_path)

        replacements = {
            '{name}': contact.name,
            '{surname1}': contact.surname1,
            '{surname2}': contact.surname2,
            '{job_title}': contact.job_title,
            '{company}': contact.company,
            '{street}': contact.street,
            '{ext_number}': contact.ext_number,
            '{int_number}': contact.int_number,
            '{neighborhood}': contact.neighborhood,
            '{city}': contact.city,
            '{state}': contact.state,
            '{postal_code}': contact.postal_code,
            '{phone}': contact.phone,
            '{email}': contact.email,
            '{birth_date}': contact.birth_date,
            '{age}': str(contact.age),
        }

        for paragraph in doc.paragraphs:
            for key, value in replacements.items():
                if key in paragraph.text:
                    paragraph.text = paragraph.text.replace(key, value)

        doc.save(output_path)
        print(f'Documento guardado como {output_path}')
