import xml.etree.ElementTree
import io
import json
import os, sys

# Gets the script's directory so we can access files relative to it
scripts_directory = os.path.dirname(os.path.realpath(__file__))

settings_file_dir = os.path.join(scripts_directory, 'settings.json')
with open(settings_file_dir) as settings_file:
    settings = json.load(settings_file)

# Load in the canonical emoji substitutions
emoji_substitutions_file = os.path.join(scripts_directory, '../emoji substitutions.plist')
e = xml.etree.ElementTree.parse(emoji_substitutions_file).getroot()

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

# Fill out each template
for settings in settings:
    template_file = os.path.join(scripts_directory, '../templates/' + setting['name'] + '.template')
    with io.open(template_file, 'r', encoding='utf8') as s:
        template = s.read()
    with io.open('../' + setting['name'], 'w', encoding='utf8') as f:
        f.write(template.format(formatted_data[setting['name']]))
