# RIME_LaTeX

Difficulty typing mathematical symbols?

Try Rime-latex for Latex-based Symbols:)


## Use with other schemas

For instance, to use with 朙月拼音（·简化字）, in `luna_pinyin.custom.yaml` (`luna_pinyin_simp.custom.yaml`)

```yaml
patch:
  engine/translators:
    - punct_translator
    - r10n_translator
    - reverse_lookup_translator
# meaning of the regex: ^ start of line, \\ the starting \, .+ any char 1 or more time, $ end 
  recognizer/patterns/reverse_lookup: '^\\.+$'
  schema/dependencies:
    - latex
  abc_segmentor/extra_tags:
    - reverse_lookup
  reverse_lookup:
    dictionary: latex
    enable_completion: false
    tips: latex
```

## RIME_LaTeX's extension to tex symbols

### superscript/subscript

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

## Plans

+ Sanitize the more.
  + The symbols table should only contains those which are in both unicode & Latex
  + Complete Latex Symbols: <http://tug.ctan.org/info/symbols/comprehensive/symbols-a4.pdf>
  + Unicode <https://en.wikipedia.org/wiki/Mathematical_operators_and_symbols_in_Unicode>

+ Fuzzy match?
