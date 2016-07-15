import xml.etree.ElementTree
import io
import json


with open('settings.json') as settings_file:
    settings = json.load(settings_file)

e = xml.etree.ElementTree.parse('../emoji substitutions.plist').getroot()

formatted_data = {}
for idx, value in enumerate(e.findall('./array/dict/string')):
    if idx % 2 == 0:
        emoji = value.text
    else:
        placeholder = value.text
        for setting in settings:
            if setting['name'] in formatted_data:
                formatted_data[setting['name']] += setting['data_format'].format(
                    placeholder=placeholder, emoji=emoji)
            else:
                formatted_data[setting['name']] = setting['data_format'].format(
                    placeholder=placeholder, emoji=emoji)

for settings in settings:
    with io.open('../templates/' + setting['name'] + '.template', 'r', encoding='utf8') as s:
        template = s.read()
    with io.open('../' + setting['name'], 'w', encoding='utf8') as f:
        f.write(template.format(formatted_data[setting['name']]))
