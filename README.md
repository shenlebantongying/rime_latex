# RIME_LaTeX

Difficulty typing mathematical symbols?

Try Rime-latex for Latex-based Symbols:)

## RIME_LaTeX's extension to tex symbols

### Number superscript/subscript

`^1` and `_1` to type over\under position numbers to type `¹₁`, 
```
X₁¹ <- ^1 _1 
```
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

## Use with other schemas

For instance, to use with 朙月拼音（·简化字）, in `luna_pinyin.custom.yaml` (`luna_pinyin_simp.custom.yaml`)

```yaml
patch:
  engine/translators:
    - punct_translator
    - r10n_translator
    - reverse_lookup_translator
  recognizer/patterns/reverse_lookup: '\D+'
  schema/dependencies:
    - latex
  abc_segmentor/extra_tags:
    - reverse_lookup
  reverse_lookup:
    dictionary: latex
    enable_completion: false
    tips: latex
```

The configuration above allows only latex symbols start with '\\' and without any digits to avoid conflicts.

## Credits

The latex math symbols table sources:

https://github.com/hubutui/fcitx-table-unicode-latex
https://github.com/moebiuscurve/ibus-table-others/blob/master/tables/latex.txt

## Plans

+ Sanitize the more.
  + The symbols table should only contains those which are in both unicode & Latex
  + Complete Latex Symbols: <http://tug.ctan.org/info/symbols/comprehensive/symbols-a4.pdf>
  + Unicode <https://en.wikipedia.org/wiki/Mathematical_operators_and_symbols_in_Unicode>

+ Fuzzy match?
