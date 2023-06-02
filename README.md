# RIME_LaTeX

Difficulty typing mathematical symbols?

Try Rime-latex for Latex-based Symbols:)


## Use with other schemas

For instance, to use with 朙月拼音（·简化字）, in `luna_pinyin.custom.yaml` (`luna_pinyin_simp.custom.yaml`)

```yaml
patch:
# type '\' will pull in English punctuation, so need to switch to Chinese punctuation
  switches/+:
    - name: ascii_punct # 
      states: [ ¥, $ ]
      reset: 0
# make '\' go into the candidate box
  speller/alphabet: zyxwvutsrqponmlkjihgfedcba\\
# or customize punctuator to make '\' go into the candidate box like below(please uncomment yourself)
#  punctuator/half_shape:
#    "\\": ["\\"]
#  punctuator/full_shape:
#    "\\": ["、", "＼"]

  engine/translators:
    - punct_translator
    - table_translator
    - table_translator@latex_input
# meaning of the regex: ^ (start of line), \\(the starting \), .+(any char 1 or more time), $(end)
# first '\\' is recognized as a symbol(half_shape or full_shape). double '\\' make it to be recognized as a pattern
# translator's prefix will consume one '\\'. so user only type once '\' key
  "recognizer/patterns/latex_input": "^\\\\.+$"
  schema/dependencies/+:
    - latex
  latex_input:
    tag: latex_input
    dictionary: latex
    prefix: "\\"
    enable_sentence: false
    enable_completion: true # enable autocomplete
    enable_user_dict: true # enable word frequency,  use with user_dict
    user_dict: custom_latex_user # generate a file name custom_latex_user.txt
    db_class: tabledb
    tips: "[LaTex]"
```

## RIME_LaTeX's extension to tex symbols

### superscript/subscript
user type once '\' key and input latex with autocomplete prompt
```
\^1 \_1 -> X₁¹
\^a \_b -> Xᵃᵦ
```

> [Unicode doesn't have a full set of super/sub scripts, you probably should use text styles or markup in rich text, instead.](https://www.unicode.org/faq/ligature_digraph.html#Pf8)

### Degree
```
° \degree 
```
### MISC
```
→ \to
⇒ \To
⇛ \TO
```


## Credits

The latex math symbols table sources:

https://github.com/hubutui/fcitx-table-unicode-latex
https://github.com/moebiuscurve/ibus-table-others/blob/master/tables/latex.txt

Rime schema description:
https://github.com/LEOYoon-Tsaw/Rime_collections/blob/master/Rime_description.md

## Plans

+ Sanitize the more.
  + The symbols table should only contains those which are in both unicode & Latex
  + Complete Latex Symbols: <http://tug.ctan.org/info/symbols/comprehensive/symbols-a4.pdf>
  + Unicode <https://en.wikipedia.org/wiki/Mathematical_operators_and_symbols_in_Unicode>

+ Fuzzy match?
