import xml.etree.ElementTree
import io


e = xml.etree.ElementTree.parse('../emoji substitutions.plist').getroot()

emoji_list = u''
emoji = u''
for idx, value in enumerate(e.findall('./array/dict/string')):
    # print(idx + ':' + value.text)
    if idx % 2 == 0:
        emoji += ',' + value.text
    else:
        emoji = value.text + emoji + '\n'
        emoji_list += emoji
        emoji = u''
emoji_list = emoji_list.strip(u'\n')

start = u'''<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<array>
	<dict>
		<key>Activate</key>
		<string>Normal</string>
		<key>IsActive</key>
		<true/>
		<key>Macros</key>
		<array>
			<dict>
				<key>Actions</key>
				<array>
					<dict>
						<key>IsActive</key>
						<true/>
						<key>IsDisclosed</key>
						<true/>
						<key>MacroActionType</key>
						<string>SetVariableToText</string>
						<key>Text</key>
						<string>%TriggerValue%</string>
						<key>Variable</key>
						<string>emoji</string>
					</dict>
					<dict>
						<key>IsActive</key>
						<true/>
						<key>IsDisclosed</key>
						<true/>
						<key>MacroActionType</key>
						<string>SetVariableToText</string>
						<key>Text</key>
						<string>'''
end = u'''</string>
						<key>Variable</key>
						<string>emoji_list</string>
					</dict>
					<dict>
						<key>IsActive</key>
						<true/>
						<key>IsDisclosed</key>
						<true/>
						<key>MacroActionType</key>
						<string>SetVariableToText</string>
						<key>Text</key>
						<string>%Variable%emoji%</string>
						<key>Variable</key>
						<string>emoji_out</string>
					</dict>
					<dict>
						<key>Action</key>
						<string>IgnoreCaseString</string>
						<key>IsActive</key>
						<true/>
						<key>IsDisclosed</key>
						<true/>
						<key>MacroActionType</key>
						<string>SearchReplaceVariable</string>
						<key>Replace</key>
						<string>\+</string>
						<key>Search</key>
						<string>+</string>
						<key>Variable</key>
						<string>emoji</string>
					</dict>
					<dict>
						<key>Action</key>
						<string>IgnoreCaseRegEx</string>
						<key>Captures</key>
						<array>
							<string></string>
							<string>emoji_out</string>
						</array>
						<key>IsActive</key>
						<true/>
						<key>IsDisclosed</key>
						<true/>
						<key>MacroActionType</key>
						<string>SearchVariable</string>
						<key>Search</key>
						<string>%Variable%emoji%,(.+)</string>
						<key>Variable</key>
						<string>emoji_list</string>
					</dict>
					<dict>
						<key>Action</key>
						<string>ByPasting</string>
						<key>IsActive</key>
						<true/>
						<key>IsDisclosed</key>
						<true/>
						<key>MacroActionType</key>
						<string>InsertText</string>
						<key>Paste</key>
						<true/>
						<key>Text</key>
						<string>%Variable%emoji_out%</string>
					</dict>
				</array>
				<key>IsActive</key>
				<true/>
				<key>ModificationDate</key>
				<real>489967638.325351</real>
				<key>Name</key>
				<string>Emojis</string>
				<key>Triggers</key>
				<array>
					<dict>
						<key>Case</key>
						<string>Match</string>
						<key>DiacriticalsMatter</key>
						<true/>
						<key>MacroTriggerType</key>
						<string>TypedString</string>
						<key>OnlyAfterWordBreak</key>
						<false/>
						<key>SimulateDeletes</key>
						<true/>
						<key>TypedString</key>
						<string>:[^ :]+:</string>
					</dict>
				</array>
				<key>UID</key>
				<string>F2CC6E0A-4957-4F2A-AD57-66AED2A97555</string>
			</dict>
		</array>
		<key>Name</key>
		<string>My Stuff</string>
		<key>UID</key>
		<string>AE600F45-3378-4238-B241-2BE2EF1C6E96</string>
	</dict>
</array>
</plist>
'''

with io.open('../emojis-km6.kmmacros', 'w', encoding='utf8') as f:
    f.write(start + emoji_list + end)
