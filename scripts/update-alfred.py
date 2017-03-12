from __future__ import unicode_literals

import binascii
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


def main():
    scripts_directory = os.path.dirname(os.path.realpath(__file__))
    emoji_substitutions_file = os.path.join(scripts_directory,
                                            '../emoji substitutions.plist')
    emoji_substitutions = plistlib.readPlist(emoji_substitutions_file)
    outfile = '../Emoji.alfredsnippets'
    with zipfile.ZipFile(outfile, 'w') as snippets:
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


if __name__ == "__main__":
    sys.exit(main())
