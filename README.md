![How Macmoji works 😁](https://github.com/warpling/Macmoji/blob/master/gifs/what%20is%20it.gif?raw=true)

# How to install Macmoji
## It's as easy as 🔢

1. [Download `emoji substitutions.plist`](https://raw.githubusercontent.com/warpling/Macmoji/master/emoji%20substitutions.plist) (make sure it has the extension `.plist`)
1. Open System Preferences and navigate to **Keyboard** > **Text**
3. Drag the `emoji substitutions.plist` to the list of substitutions to add them
4. Type something like `:boom:` or `:blackbox:` and hit space after! 💥⬛️

#### Gif instructions:
![How to "install" Macmoji](https://github.com/warpling/Macmoji/blob/master/gifs/how%20to%20install.gif?raw=true)


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
Well it's [what Slack does](https://get.slack.help/hc/en-us/articles/202931348-Emoji-and-emoticons) *and* it prevents mac os's autocomplete from being too aggressive when you're just trying to type normal sentences like, "ghost bananas are cool." 👻🍌🆒 

#### 🖐🏽 What about skin tones?
Type your skin-tonable emoji, then type `:skin-tone-3:` (any number 1-5) to add the skintone. They should combine!

#### 😱 I have suggestions and mistakes to point out!
Let me know in the issues *orrr* file a [pull request](https://yangsu.github.io/pull-request-tutorial/)!

#### 😯 Can I back-up or share my substitutions?
Yep! Highlight and drag out the ones you want to back-up or share and you'll get a neat little `.plist`. Drag them back in and only the unique ones will be added.


## Known Problems

#### 😫 Macmoji isn't working in Chrome 
Yeah it's bummer. Chrome uses their own text engine and bypasses the system's autocomplete and a few other things, but fun work around is to open Spotlight (`cmd + space`) type your emojis there, copy, paste, and you're good to go! 👍 

#### 😠 Sometimes it just stops working in some applications
No clue. Beats me. Have a hunch why? I'd love to know too.

## Change Log

The best way to update is to remove all previously added substitutions and then drag in the plist again (hold `shift` to select all the colon clad substitutions).
**Tip:** You can always back-up substitutions by selecting and dragging them out of the list!

|       Date       |       Commit       |       Changes       |
| ---------------- | ------------------ | ------------------- |
| July 12, 2016 | [2872b66](https://github.com/warpling/Macmoji/pull/11/commits/2872b66354779bc446c68b71c94d67bf43b0247c) | 📞☎️ Add shortcut for call, and telephone |
| July 8, 2016 | [e7225c2](https://github.com/warpling/Macmoji/commit/e7225c24157385f319f99910ecf5e737016c796b) | 🐴🍷🙎🖖 Add shortcut for mustang, wine, pouting, and spock |
| July 8, 2016 | [2f84c61](https://github.com/warpling/Macmoji/commit/2f84c6169546a22246f42a4b56eaec7d8ef979d5) | ⚽⚾️⛄⛅ Fix mismatched shortcuts for soccer, baseball, snowman, and partially_sunny |
