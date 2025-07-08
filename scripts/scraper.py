import requests
from bs4 import BeautifulSoup
import pandas as pd

def extract_contact_info(contacts_list):
    data = []
    for contact in contacts_list:
        main_department = contact.find('h3', class_='ws-section-title')
        main_department = main_department.text.strip() if main_department else ''
        other_department = contact.find('h4', itemprop='Department')
        other_department = other_department.text.strip() if other_department else ''

        address = contact.find('div', itemtype='http://schema.org/PostalAddress')
        street_address = address.find('span', itemprop='streetAddress').text.strip() if address else 'N/A'
        postal_code = address.find('span', itemprop='postalCode').text.strip() if address else 'N/A'
        locality = address.find('span', itemprop='addressLocality').text.strip() if address else 'N/A'

        phone_tag = contact.find('a', href=lambda x: x and x.startswith('tel:'))
        phone_number = phone_tag.text.strip() if phone_tag else 'N/A'
        fax_tag = contact.find('div', itemprop='faxNumber')
        fax_number = fax_tag.text.strip() if fax_tag else 'N/A'
        email_tag = contact.find('a', href=lambda x: x and x.startswith('mailto:'))
        email_address = email_tag.text.strip() if email_tag else 'N/A'
        website_tag = contact.find('a', href=lambda x: x and x.startswith('http'))
        website_url = website_tag.text.strip() if website_tag else 'N/A'

        hours = 'N/A'
        hours_divs = contact.find_all('div', class_='ws-general-content__address-card-item')
        for div in hours_divs:
            if div.find('span', class_='icon icon-working-hours'):
                label = div.find('span', class_='label')
                if label:
                    hours = label.text.strip()
                    break

        data.append({
            'Department': main_department if main_department else other_department,
            'Street Address': street_address,
            'Postal Code': postal_code,
            'Locality': locality,
            'Phone Number': phone_number,
            'Fax Number': fax_number,
            'Email Address': email_address,
            'Website URL': website_url,
            'Working Hours': hours
        })

    return pd.DataFrame(data)

def extract_fields_from_page(page_url):
    soup = BeautifulSoup(page_url.text, 'html.parser')
    form_rows = soup.find_all('div', attrs={'class': 'ws-form__row'})
    labels = []
    for row in form_rows:
        label_tags = row.find_all('label', class_='ws-field-label')
        for label in label_tags:
            label_text = label.get_text(strip=True)
            if label_text:
                labels.append(label_text)
    return pd.DataFrame(labels, columns=["Field Label"])

def scrape_conselho_geral(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    main = soup.find_all('section', class_='contacts__address')
    other_div = soup.find('div', id='services')
    other = other_div.find_all('div', class_='col-xs-auto contacts__details-col') if other_div else []
    df = pd.concat([
        extract_contact_info(main),
        extract_contact_info(other)
    ], ignore_index=True)
    return df

def scrape_fields_page(url):
    response = requests.get(url)
    return extract_fields_from_page(response)
