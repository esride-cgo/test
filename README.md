[Download ZIP](../../archive/master.zip)

* [Installation](#installation)
* [ohne explizites anchor-Element](#prerequisites)

First Header | Second Header
------------ | -------------
Content from cell 1 | Content from cell 2
Content in the first column | Content in the second column

Markdown | Less | Pretty
--- | --- | ---
*Still* | `renders` | **nicely**
1 | 2 | 3

| Left-aligned | Center-aligned | Right-aligned |
| :---         |     :---:      |          ---: |
| git status   | git status     | git status    |
| git diff     | git diff       | git diff      |

(http://esri.de "Esri DE")

![GitHub Logo](/images/logo.png)
Format: ![Alt Text](url)

- [x] @mentions, #refs, [links](), **formatting**, and <del>tags</del> supported
- [x] list syntax required (any unordered or ordered list supported)
- [x] this is a complete item
- [ ] this is an incomplete item

<dl>
  <dt>Definition list</dt>
  <dd>Is something people use sometimes.</dd>

  <dt>Markdown in HTML</dt>
  <dd>Does *not* work **very** well. Use HTML <em>tags</em>.</dd>
</dl>

Three or more...

---

Hyphens

***

Asterisks

___

Underscores

<a href="http://www.youtube.com/watch?feature=player_embedded&v=YOUTUBE_VIDEO_ID_HERE
" target="_blank"><img src="http://img.youtube.com/vi/YOUTUBE_VIDEO_ID_HERE/0.jpg" 
alt="IMAGE ALT TEXT HERE" width="240" height="180" border="10" /></a>

Or, in pure Markdown, but losing the image sizing and border:

[![IMAGE ALT TEXT HERE](http://img.youtube.com/vi/YOUTUBE_VIDEO_ID_HERE/0.jpg)](http://www.youtube.com/watch?v=YOUTUBE_VIDEO_ID_HERE)


```javascript
var s = "JavaScript syntax highlighting";
alert(s);
```
 
```python
s = "Python syntax highlighting"
print s
```
 
```
No language indicated, so no syntax highlighting. 
But let's throw in a <b>tag</b>.
```

```ruby
require 'redcarpet'
markdown = Redcarpet.new("Hello World!")
puts markdown.to_html
```
- [x] Finish my changes
- [ ] Push my commits to GitHub
- [ ] Open a pull request

# H1
## H2
### H3
#### H4
##### H5
###### H6

Alternatively, for H1 and H2, an underline-ish style:

Alt-H1
======

Alt-H2
------

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

hi<sup>1</sup> low<sub>2</sub>

Bullet list:

  * apples
  * oranges
  * pears

Numbered list:

  1. apples
  2. oranges
  3. pears

1. Anfang:
  Eingerückt, hollahieh.
2. Mitte:
  Auch eingerückt.

[I'm an inline-style link](https://www.google.com)

[I'm an inline-style link with title](https://www.google.com "Google's Homepage")

[I'm a reference-style link][Arbitrary case-insensitive reference text]

[I'm a relative reference to a repository file](../master/LICENSE)

[You can use numbers for reference-style link definitions][1]

Or leave it empty and use the [link text itself].

URLs and URLs in angle brackets will automatically get turned into links. 
http://www.example.com or <http://www.example.com> and sometimes 
example.com (but not on Github, for example).

Some text to show that the reference links can follow later.

[arbitrary case-insensitive reference text]: https://www.mozilla.org
[1]: http://slashdot.org
[link text itself]: http://www.reddit.com

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

Inline-style: 
![alt Suche](doc/Search.png "Such such...")

Reference-style: 
![alt text][logo]

[logo]: https://github.com/adam-p/markdown-here/raw/master/src/common/images/icon48.png "Logo Title Text 2"

![](http://w3.org/Icons/valid-xhtml10)

⛯ Tip:  
<img src='doc/Search.png' alt='Search' title='Search'/>
![alt tag](doc/Download.png)

// Include file
{"gitdown": "include", "file":"LICENSE"}

