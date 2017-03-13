from __future__ import unicode_literals

import binascii
import io
import json
import os
import plistlib
import sys
import unicodedata
import zipfile


def make_random_uid():
    return binascii.b2a_hex(os.urandom(15))


def titlecase_phrase(phrase):
    return ' '.join([word.title() for word in phrase])


def make_emoji_name(emoji, shortcut):
    try:
        return titlecase_phrase(unicodedata.name(emoji).split())
    except (ValueError, TypeError):
        return titlecase_phrase(shortcut.strip(':').split('_'))


def fill_single_file_templates(settings, emoji_substitutions, scripts_directory):
    formatted_data = {}
    for item in emoji_substitutions:
        emoji, placeholder = item['phrase'], item['shortcut']
        for setting in settings:
            if setting['name'] in formatted_data:
                formatted_data[setting['name']] += setting['data_format'].format(
                    placeholder=placeholder, emoji=emoji)
            else:
                formatted_data[setting['name']] = setting['data_format'].format(
                    placeholder=placeholder, emoji=emoji)

    # Fill out each template
    for setting in settings:
        template_file = os.path.join(
            scripts_directory,
            '../templates/{}.template'.format(setting['name'])
        )
        with io.open(template_file, 'r', encoding='utf8') as s:
            template = s.read()
        with io.open('../' + setting['name'], 'w', encoding='utf8') as f:
            f.write(template.format(formatted_data[setting['name']]))


def generate_alfred_snippets(emoji_substitutions):
    alfred_outfile = '../Emoji.alfredsnippets'
    with zipfile.ZipFile(alfred_outfile, 'w') as snippets:
        for item in emoji_substitutions:
            phrase, shortcut = item['phrase'], item['shortcut']
            uid = make_random_uid()
            name = make_emoji_name(phrase, shortcut)
            snippets.writestr(
                '{} [{}].json'.format(name, uid),
                json.dumps({
                    "alfredsnippet" : {
                        "snippet" : phrase,
                        "uid" : uid,
                        "name" : name,
                        "keyword" : shortcut
                    }
                })
            )


def main():
    # Gets the script's directory so we can access files relative to it
    scripts_directory = os.path.dirname(os.path.realpath(__file__))

    settings_file_dir = os.path.join(scripts_directory, 'settings.json')
    with open(settings_file_dir) as settings_file:
        settings = json.load(settings_file)

    # Load in the canonical emoji substitutions
    emoji_substitutions_file = os.path.join(scripts_directory, '../emoji substitutions.plist')
    emoji_substitutions = plistlib.readPlist(emoji_substitutions_file)

    generate_alfred_snippets(emoji_substitutions)
    fill_single_file_templates(settings, emoji_substitutions, scripts_directory)


if __name__ == "__main__":
    sys.exit(main())
