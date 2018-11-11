![How Macmoji works 😁](https://github.com/warpling/Macmoji/blob/master/gifs/what%20is%20it.gif?raw=true)

# Installing Macmoji: as easy as 🔢

1. [Download `emoji substitutions.plist`](https://raw.githubusercontent.com/warpling/Macmoji/master/emoji%20substitutions.plist) (make sure it has the extension `.plist`)
2. Open System Preferences and navigate to **Keyboard** > **Text**
3. Drag the `emoji substitutions.plist` to the list of substitutions to add them
4. Type something like `:boom:` or `:blackbox:` and hit space after! 💥⬛️

##### Know bash?
1. Just run `./scripts/macmoji install` (or even `uninstall`!)
(Thanks [mshick](https://github.com/mshick)!)

#### Gif instructions:
![How to "install" Macmoji](https://github.com/warpling/Macmoji/blob/master/gifs/how%20to%20install.gif?raw=true)

## Other Installations
Thanks to the fantastic work of [rael9](https://github.com/rael9) Macmoji now has a script for generating other template files (Maestro, Alfred, etc) from the latest emoji substitutions list. If you add emoji substitutions to the base `plist` simply run `python scripts/update-output.py` from the base directory and the various outputs based on the templates in `templates/*` will be generated in the base directory. Creating new templates is [easy and highly encouraged](https://github.com/warpling/Macmoji/pull/14#issuecomment-232850622)!

### Keyboard Maestro Version

If you'd prefer to use Keyboard Maestro to handle the substitutions, import the emojis-km6.kmmacros file in the Keyboard Maestro Editor.

*(This macro was created and tested using version 6. It has not been tested with other versions.)*

### Alfred Version

If you'd prefer to import these shortcuts with Alfred as Snippets just drag the `.alfredsnippets` into Alfred's Snippet preferences!  

## FAQ

#### 🤔 Can I change/remove substitutions?
Yep! Macmoji substitutions are ordinary text substitutions. Double click an entry to change it; highlight and hit delete to remove it. To highlight multiple substitutions select one and then while holding shift select another. You can always add your own too of course!

Some fun recommendations:

| replace  | with           |
| :------- | :------------- |
| ehh      | ¯\\\_(ツ)\_/¯   |
| tflip    | (╯°□°）╯︵ ┻━┻ |
| eml      | your@email.com |

#### 💩 Why the colons?
Well it's what [Slack](https://get.slack.help/hc/en-us/articles/202931348-Emoji-and-emoticons)/GitHub/Trello does *and* it prevents macOS's autocomplete from being too aggressive when you're just trying to type normal sentences like, "ghost bananas are cool." 👻🍌🆒

#### 🖐🏽 What about skin tones?
Type your skin-tonable emoji, then type `:skin-tone-3:` (any number 1-5) to add the skintone. They should combine!

#### 😱 I have suggestions and mistakes to point out!
Let me know in the issues *orrr* file a [pull request](https://yangsu.github.io/pull-request-tutorial/)!

#### 😯 Can I back-up or share my substitutions?
Yep! Highlight and drag out the ones you want to back-up or share and you'll get a neat little `.plist`. Drag them back in and only the unique ones will be added.


## Known Problems

#### 😫 Macmoji isn't working in Chrome
Yeah it's a bummer. Chrome bypasses the system's autocomplete (and a few other things), but a passable work around is to open Spotlight (`cmd + space`) type your emojis there, copy, paste, and you're good to go! 👍

#### 😫 The substitutions are showing up on my iPhone in weird ways…
Keyboard text substitutions sync across iCloud. I haven't found a way to disable it short of removing the substitutions and iOS seems to ignore colons 🤕. I will update this if I learn of a solution.

#### 😠 Sometimes it just stops working in some applications
No clue. Beats me. Have a hunch why? I'd love to hear it!

#### ☹️ `realpath: command not found`
You may need to install [Homebrew](https://brew.sh/) and then run the following to install `coreutils`. Please comment on [issue #35](https://github.com/warpling/Macmoji/issues/35) if you experience this!
```
brew install coreutils
```

## Change Log

The best way to update is to remove all previously added substitutions and then drag in the plist again (hold `shift` to select all the colon clad substitutions).
**Tip:** You can always back-up substitutions by selecting and dragging them out of the list!

|       Date       |       Commit       |       Changes       |
| ---------------- | ------------------ | ------------------- |
| March 12, 2017 | [9bcbb39](https://github.com/warpling/Macmoji/commit/4b6b55cad36cc14ad522418cad758bf6856d7cf9) | 🎩 Add Alfred snippets. (Thanks @valrus!) |
| July 15, 2016 | [9bcbb39](https://github.com/warpling/Macmoji/commit/9bcbb396a2a91d026b7df15392e7ae69cc0b36d0) | 🤖 Add templating script and Keyboard Maestro version! |
| July 12, 2016 | [2872b66](https://github.com/warpling/Macmoji/pull/11/commits/2872b66354779bc446c68b71c94d67bf43b0247c) | 📞☎️ Add shortcut for call, and telephone |
| July 11, 2016 | [781926c](https://github.com/warpling/Macmoji/commit/781926c97496937346a64c68ace755b32f3059fe) | Added Keyboard Maestro macro version. |
| July 8, 2016 | [e7225c2](https://github.com/warpling/Macmoji/commit/e7225c24157385f319f99910ecf5e737016c796b) | 🐴🍷🙎🖖 Add shortcut for mustang, wine, pouting, and spock. |
| July 8, 2016 | [2f84c61](https://github.com/warpling/Macmoji/commit/2f84c6169546a22246f42a4b56eaec7d8ef979d5) | ⚽⚾️⛄⛅ Fix mismatched shortcuts for soccer, baseball, snowman, and partially_sunny. |
