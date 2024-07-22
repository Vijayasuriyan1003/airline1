import xml.etree.ElementTree as ET

api_key = "17cca6da41d9a82"
secret_key = "71e0f28b7a2c0c9"

def dict_to_xml(tag, d):
    elem = ET.Element(tag)
    for key, val in d.items():
        child = ET.SubElement(elem, key)
        child.text = str(val)
    return elem

root = dict_to_xml('data', data['data'])

api_key_elem = ET.Element('api_key')
api_key_elem.text = api_key

secret_key_elem = ET.Element('secret_key')
secret_key_elem.text = secret_key

root.append(api_key_elem)
root.append(secret_key_elem)

xml_str = ET.tostring(root, encoding='unicode', method='xml')

print(xml_str)
