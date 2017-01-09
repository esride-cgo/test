* [Installation](#installation)
* [ohne explizites anchor-Element](#prerequisites)

First Header | Second Header
------------ | -------------
Content from cell 1 | Content from cell 2
Content in the first column | Content in the second column



```ruby
require 'redcarpet'
markdown = Redcarpet.new("Hello World!")
puts markdown.to_html
```
- [x] Finish my changes
- [ ] Push my commits to GitHub
- [ ] Open a pull request

# Heading

## Sub-heading

### Another deeper heading
 
Paragraphs are separated
by a blank line.

Two spaces at the end of a line leave a  
line break.

Text attributes _italic_, *italic*, __bold__, **bold**, `monospace`.

Horizontal rule:

---

Bullet list:

  * apples
  * oranges
  * pears

Numbered list:

  1. apples
  2. oranges
  3. pears

Besser ohne explizite Nummern:

0. Ja.
0. Vielleicht.
0. Nein.

A [Markdown](https://en.wikipedia.org/wiki/Markdown).  
GitHub Flavored Markdown (GFM) treats newlines in paragraph-like content as real line breaks, ignores underscores in words, and adds syntax highlighting, task lists,[36] and tables.[37]

> Quoted Text = Border(left)

Dieser Satz ~~k~~ein Fehler.

## <a name="installation"></a>Installation

### Prerequisites:
"Customize" ▸ "ArcMap Options..." ▸ "Raster Catalog" ▸ "Display selected rasters with transparency: 0%" (default is 30%, which appears very hazy)

📓 Note:  
• eins  
• zwo  

⛯ Tip:  
<img src='doc/Search.png' alt='Search' title='Search'/>
![alt tag](doc/Download.png)
