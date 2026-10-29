"""
ITC University Curriculum - Labs 8 to 14 Data Module
CS-111 Introduction to Computing & ITC Lab (Hamdard Institute of Engineering & Technology)
Verbatim transcription from 'Lab Manual ITC Update 2021 (1).docx' with zero truncation.
Includes complete source code, console sessions, lab exercise tasks, sample programs, outputs,
inline assets, quizzes, and flashcards.
"""

from typing import List, Dict, Any

LABS_8_TO_14: List[Dict[str, Any]] = [
    # -------------------------------------------------------------------------
    # LAB 8: INTRODUCTION TO HTML
    # -------------------------------------------------------------------------
    {
        "order": 8,
        "title": "Lab 8: Introduction to HTML  -  Document Structure, Headings & Paragraphs",
        "codeSnippet": """<!DOCTYPE html>
<html>
<head>
    <title>Heading Example</title>
</head>
<body>
    <h1>This is heading 1</h1>
    <h2>This is heading 2</h2>
    <h3>This is heading 3</h3>
    <h4>This is heading 4</h4>
    <h5>This is heading 5</h5>
    <h6>This is heading 6</h6>
    <p>Here is a first paragraph of text.</p>
    <p>Here is a second paragraph of text.</p>
</body>
</html>""",
        "content": """# Lab 8: Introduction to HTML

![University Header](assets/images/university/itc/lab0_hamdard_logo.png)

## Course & Lab Information
- **Course Title**: Introduction to Computing & ITC Lab
- **Course Code**: CS - 111
- **Program**: BSCS / Engineering
- **Department**: Department of Computing, Hamdard Institute of Engineering & Technology
- **Dated**: _______________

---

## 1. Objective
Learn to create web page using HTML.

---

## 2. Theory: What is HTML?
**HTML** stands for **Hypertext Markup Language**, and it is the most widely used language to write Web Pages.

- **Hypertext**: Refers to the way in which Web pages (HTML documents) are linked together. Thus, the link available on a webpage is called Hypertext.
- **Markup Language**: As its name suggests, HTML is a Markup Language which means you use HTML to simply "mark-up" a text document with tags that tell a Web browser how to structure it to display.

Originally, HTML was developed with the intent of defining the structure of documents like headings, paragraphs, lists, and so forth to facilitate the sharing of scientific information between researchers.

Now, HTML is being widely used to format web pages with the help of different tags available in HTML language.

> **W3C Recommendation**: The World Wide Web Consortium (W3C) recommends using **lowercase tags** starting from HTML 4.

---

## 3. Basic HTML Document
In its simplest form, following is an example of an HTML document:

```html
<!DOCTYPE html>
<html>
<head>
    <title>This is document title</title>
    Hi there !
</head>
<body>
    <h1>This is a heading</h1>
    <p>Document content goes here.....</p>
</body>
</html>
```

### HTML Tags
As told earlier, HTML is a markup language and makes use of various tags to format the content. These tags are enclosed within angle braces `<Tag Name>`. Except few tags, most of the tags have their corresponding closing tags. For example, `<html>` has its closing tag `</html>` and `<body>` tag has its closing tag `</body>` tag etc.

Above example of HTML document uses the following tags:

| Sr. No | Tag | Description |
|:---:|:---|:---|
| **1** | `<!DOCTYPE...>` | This tag defines the document type and HTML version. |
| **2** | `<html>` | This tag encloses the complete HTML document and mainly comprises of document header which is represented by `<head>...</head>` and document body which is represented by `<body>...</body>` tags. |
| **3** | `<head>` | This tag represents the document's header which can keep other HTML tags like `<title>`, `<link>` etc. |
| **4** | `<title>` | The `<title>` tag is used inside the `<head>` tag to mention the document title. |
| **5** | `<body>` | This tag represents the document's body which keeps other HTML tags like `<h1>`, `<div>`, `<p>` etc. |
| **6** | `<h1>` | This tag represents the heading. |
| **7** | `<p></p>` | This tag represents a paragraph. |

To learn HTML, you will need to study various tags and understand how they behave while formatting a textual document. Learning HTML is simple as users have to learn the usage of different tags in order to format the text or images to make a beautiful webpage.

---

## 4. HTML Document Structure
A typical HTML document will have the following structure:

```html
<html>
    <head>
        Document header related tags
    </head>
    <body>
        Document body related tags
    </body>
</html>
```

### The `<!DOCTYPE>` Declaration
The `<!DOCTYPE>` declaration tag is used by the web browser to understand the version of the HTML used in the document. Current version of HTML is **5** and it makes use of the following declaration:

```html
<!DOCTYPE html>
```

There are many other declaration types which can be used in HTML document depending on what version of HTML is being used.

---

## 5. Heading Tags
Any document starts with a heading. You can use different sizes for your headings. HTML also has six levels of headings, which use the elements `<h1>`, `<h2>`, `<h3>`, `<h4>`, `<h5>`, and `<h6>`. While displaying any heading, browser adds one line before and one line after that heading.

### Example
```html
<!DOCTYPE html>
<html>
<head>
    <title>Heading Example</title>
</head>
<body>
    <h1>This is heading 1</h1>
    <h2>This is heading 2</h2>
    <h3>This is heading 3</h3>
    <h4>This is heading 4</h4>
    <h5>This is heading 5</h5>
    <h6>This is heading 6</h6>
</body>
</html>
```

---

## 6. Paragraph Tag
The `<p>` tag offers a way to structure your text into different paragraphs. Each paragraph of text should go in between an opening `<p>` and a closing `</p>` tag as shown below in the example:

### Example
```html
<!DOCTYPE html>
<html>
<head>
    <title>Paragraph Example</title>
</head>
<body>
    <p>Here is a first paragraph of text.</p>
    <p>Here is a second paragraph of text.</p>
    <p>Here is a third paragraph of text.</p>
</body>
</html>
```

---

## 7. Lab Tasks (Verbatim)
1. **Task 1**: Create a webpage that prints your name to the screen.
2. **Task 2**: Create a webpage that prints the numbers `1 - 10` to the screen.
3. **Task 3**: Create a webpage and set its title to `"This is a webpage"`.
4. **Task 4**: Create a webpage that prints the message to the screen, and set the title of the page to the current date.
""",
        "quizzes": [
            {
                "question": "What does the abbreviation HTML stand for?",
                "options": [
                    "Hypertext Markup Language",
                    "High-Tech Modern Language",
                    "Hyper Transfer Module Layout",
                    "Home Tool Markup Link"
                ],
                "correctAnswer": "Hypertext Markup Language",
                "explanation": "HTML stands for Hypertext Markup Language. Hypertext refers to clickable links between pages, and Markup refers to tagging text with structural formatting."
            },
            {
                "question": "Which declaration informs the web browser that the document is written in modern HTML5?",
                "options": [
                    "<!DOCTYPE html>",
                    "<doctype html5>",
                    "<?xml version='1.0'?>",
                    "<html version='5.0'>"
                ],
                "correctAnswer": "<!DOCTYPE html>",
                "explanation": "In HTML5, the standard doctype declaration is simply <!DOCTYPE html>, which is placed at the very top of the document."
            },
            {
                "question": "How many levels of headings does HTML provide natively?",
                "options": [
                    "6 levels (<h1> to <h6>)",
                    "3 levels (<h1> to <h3>)",
                    "8 levels (<h1> to <h8>)",
                    "10 levels (<h1> to <h10>)"
                ],
                "correctAnswer": "6 levels (<h1> to <h6>)",
                "explanation": "HTML defines six heading levels, ranging from <h1> (the largest, top-level heading) down to <h6> (the smallest subheading)."
            }
        ],
        "flashcards": [
            {
                "question": "What is the purpose of the <title> tag in an HTML document?",
                "answer": "It specifies the title of the webpage, which appears in the browser's title bar or tab, and is placed inside the <head> element."
            },
            {
                "question": "What does W3C recommend regarding HTML tag case starting from HTML 4?",
                "answer": "The World Wide Web Consortium (W3C) recommends writing all HTML tags and attributes in lowercase."
            },
            {
                "question": "What automatic spacing does a web browser add around HTML heading tags?",
                "answer": "The browser automatically adds one empty line of vertical margin before and after every heading element."
            },
            {
                "question": "Which HTML element encloses all visible contents of a webpage displayed in the browser window?",
                "answer": "The <body> element."
            }
        ]
    },

    # -------------------------------------------------------------------------
    # LAB 9: HTML CONTINUED
    # -------------------------------------------------------------------------
    {
        "order": 9,
        "title": "Lab 9: HTML Continued  -  Attributes, Text Formatting & Hyperlinks",
        "codeSnippet": """<!DOCTYPE html>
<html>
<head>
    <title>HTML Formatting and Hyperlinks</title>
</head>
<body bgcolor="green">
    <p align="center" id="html">This para explains what is <b>HTML</b></p>
    <p align="left" id="css">The following word uses <i>italicized</i>, <u>underlined</u>, and <strike>strikethrough</strike> typeface.</p>
    <p>Polynomial: 2x<sup>3</sup> + 5x<sup>2</sup> + 3x + 9 = 0</p>
    <p>Logarithm: log<sub>10</sub>(x + 2Y)</p>
    <p>I want to drink <del>cola</del> <ins>wine</ins></p>
    <p>Comparing <big>big</big> and <small>small</small> text with <tt>monospaced</tt> font.</p>
    <a href="contact_us.html">CONTACT</a> | <a href="http://www.yahoo.com/">ABOUT</a>
</body>
</html>""",
        "content": """# Lab 9: HTML Continued  -  Attributes, Formatting & Hyperlinks

![University Header](assets/images/university/itc/lab0_hamdard_logo.png)

## Course & Lab Information
- **Course Title**: Introduction to Computing & ITC Lab
- **Course Code**: CS - 111
- **Program**: BSCS / Engineering
- **Department**: Department of Computing, Hamdard Institute of Engineering & Technology
- **Dated**: _______________

---

## 1. Objective
Learn to create web page using HTML attributes, typographical styling tags, and hyperlinks.

---

## 2. Theory: HTML Attributes
An **attribute** is used to define the characteristics of an HTML element and is placed inside the element's opening tag. All attributes are made up of two parts:
1. **Name**: The property you want to set. For example, the paragraph `<p>` element carries an attribute whose name is `align`, which indicates the alignment of the paragraph on the page.
2. **Value**: What you want the value of the property to be set, always placed within quotation marks. Common values for `align` include `left`, `center`, and `right`.

> Attribute names and attribute values are case-insensitive. However, the World Wide Web Consortium (W3C) recommends lowercase attributes/attribute values in their HTML 4 recommendation.

### Example: Paragraph Alignment
```html
<!DOCTYPE html>
<html>
<head>
    <title>write anything you want</title>
</head>
<body>
    <p align="left">This is left aligned</p>
    <p align="center">This is center aligned</p>
    <p align="right">This is right aligned</p>
</body>
</html>
```

---

## 3. Core Attributes
The four core attributes that can be used on the majority of HTML elements are:
1. `id`
2. `title`
3. `class`
4. `style`

### The `id` Attribute
The `id` attribute of an HTML tag uniquely identifies any element within an HTML page. There are two primary reasons to use an `id`:
- If an element carries an `id` as a unique identifier, it is possible to identify just that element and its content.
- If you have two elements of the same name within a webpage (or style sheet), you can use the `id` attribute to distinguish between them.

```html
<p id="html">This para explains what is HTML</p>
<p id="css">This para explains what is Cascading Style Sheet</p>
```

### The `bgcolor` Attribute
Places a background color behind an element, such as `<body>`. It can take three types of values:
- Color names (e.g., `"green"`, `"red"`)
- Hexadecimal color codes (e.g., `"#00FF00"`)
- RGB values (e.g., `(0,255,0)`)

```html
<body bgcolor="green">This para explains what is HTML</body>
```

---

## 4. Text Formatting Tags
HTML provides a comprehensive set of typographical tags to alter text appearance:

### Bold Text: `<b>`
Displays text in bold typeface:
```html
<b>The following word uses a bold typeface</b>
```

### Italic Text: `<i>`
Displays text in italicized typeface:
```html
<p>The following word uses an <i>italicized</i> typeface.</p>
```

### Underlined Text: `<u>`
Displays text with an underline:
```html
<p>The following word uses an <u>underlined</u> typeface.</p>
```

### Strike Text: `<strike>`
Displays text with a strikethrough (a horizontal line drawn through the center):
```html
<p>The following word uses a <strike>strikethrough</strike> typeface.</p>
```

### Monospaced Font: `<tt>`
Renders text in teletype (monospaced) font where each letter has equal width (unlike variable-width fonts where 'm' is wider than 'i'):
```html
<p>The following word uses a <tt>monospaced</tt> typeface.</p>
```

### Superscript Text: `<sup>`
Displays characters half a character's height above surrounding text:
```html
<p>The following word uses a <sup>superscript</sup> typeface.</p>
<p>2x<sup>3</sup> + 5x<sup>2</sup> + 3x + 9 = 0</p>
```

### Subscript Text: `<sub>`
Displays characters half a character's height beneath surrounding text:
```html
<p>The following word uses a <sub>subscript</sub> typeface.</p>
<p>Following is general formulae: log<sub>10</sub>(x+2Y)</p>
```

### Inserted & Deleted Text: `<ins>` and `<del>`
`<ins>` marks inserted text, and `<del>` marks deleted text:
```html
<p>I want to drink <del>cola</del><ins>wine</ins></p>
```

### Larger Text & Smaller Text: `<big>` and `<small>`
- `<big>`: Displays text one font size larger than surrounding text.
- `<small>`: Displays text one font size smaller than surrounding text.
```html
<p>The following word uses a <big>big</big> typeface.</p>
<p>The following word uses a <small>small</small> typeface.</p>
```

---

## 5. Hyper Text Links: `<a>`
The hyper text of a document uses the `<a>...</a>` anchor element. You can link your page to another local HTML page or an external website using the `href` attribute:

```html
<!DOCTYPE html>
<html>
<head>
    <title>Div Tag Example</title>
</head>
<body>
    <a href="contact_us.html">CONTACT</a> |
    <a href="http://www.yahoo.com/">ABOUT</a>
</body>
</html>
```

---

## 6. Lab Tasks (Verbatim)
1. **Task 1**: Create a webpage that displays a table of contents page of **Chapter 1 - 4**.
2. **Task 2**: Create hyper link on each chapter that refers to separate web page for each chapter.
3. **Task 3**: Include link on each chapter to go back to main page.
4. **Task 4**: In each chapter use all tags and attributes studied in this lab.
""",
        "quizzes": [
            {
                "question": "Which two parts make up every HTML attribute?",
                "options": [
                    "A name and a value (name=\"value\")",
                    "A tag and a closing bracket",
                    "A class and an ID",
                    "A source and a destination"
                ],
                "correctAnswer": "A name and a value (name=\"value\")",
                "explanation": "All HTML attributes consist of a name (the property being configured) and a value (the assigned setting inside quotes)."
            },
            {
                "question": "Which HTML tag is used to write mathematical powers like x² in superscript?",
                "options": [
                    "<sup>",
                    "<sub>",
                    "<power>",
                    "<up>"
                ],
                "correctAnswer": "<sup>",
                "explanation": "The <sup> tag renders superscript text positioned half a character's height above the standard baseline."
            },
            {
                "question": "How does a monospaced font (<tt>) differ from standard variable-width fonts?",
                "options": [
                    "Every letter in a monospaced font has the exact same horizontal width",
                    "Monospaced fonts are always italicized and bold",
                    "Letters are drawn with double pixel borders",
                    "It only displays numerical digits"
                ],
                "correctAnswer": "Every letter in a monospaced font has the exact same horizontal width",
                "explanation": "In a monospaced font, all characters (including narrow letters like 'i' and wide letters like 'm') occupy identical horizontal spacing."
            }
        ],
        "flashcards": [
            {
                "question": "What are the four core attributes usable across most HTML elements?",
                "answer": "id, title, class, and style."
            },
            {
                "question": "What is the difference between <del> and <ins> tags?",
                "answer": "<del> displays text as deleted (with a strikethrough), while <ins> displays text as inserted (underlined)."
            },
            {
                "question": "What tag is used to create hyperlinks in HTML?",
                "answer": "The anchor tag: <a href=\"URL\">Link Text</a>."
            },
            {
                "question": "What are three valid formats for values assigned to the bgcolor attribute?",
                "answer": "Color names ('green'), hexadecimal codes ('#00FF00'), and RGB values ('(0,255,0)')."
            }
        ]
    },

    # -------------------------------------------------------------------------
    # LAB 10: HTML CONTINUED (ADVANCED)
    # -------------------------------------------------------------------------
    {
        "order": 10,
        "title": "Lab 10: HTML Continued (Advanced)  -  Grouping, Images, Tables, Lists & Forms",
        "codeSnippet": """<!DOCTYPE html>
<html>
<head>
    <title>Educational Consultancy Portal</title>
</head>
<body>
    <!-- Header Section -->
    <div style="background-color:#eee; padding:10px;">
        <h1>Global Education Consultancy</h1>
        <a href="#feedback">Skip to Feedback Form</a>
    </div>

    <!-- Course Table -->
    <h2>Available Programs & Fees</h2>
    <table border="1" cellpadding="5" cellspacing="5">
        <tr>
            <th>Program Name</th>
            <th>Duration</th>
            <th>Tuition Fee</th>
        </tr>
        <tr>
            <td>Computer Science (BSCS)</td>
            <td>4 Years</td>
            <td>$5000 / year</td>
        </tr>
        <tr>
            <td>Software Engineering</td>
            <td>4 Years</td>
            <td>$5200 / year</td>
        </tr>
    </table>

    <!-- Services List -->
    <h2>Services Offered</h2>
    <ul type="square">
        <li>University Admissions Guidance</li>
        <li>Visa Documentation & Filing</li>
        <li>IELTS / TOEFL Preparation</li>
    </ul>

    <!-- Order / Consultation Form -->
    <h2 id="feedback">Book Consultation</h2>
    <form action="process.php" method="POST" enctype="multipart/form-data">
        First name: <input type="text" name="first_name"/><br/><br/>
        User ID: <input type="text" name="user_id"/><br/><br/>
        Password: <input type="password" name="password"/><br/><br/>
        
        Subjects of Interest:<br/>
        <input type="checkbox" name="maths" value="on"> Mathematics
        <input type="checkbox" name="cs" value="on" checked> Computer Science<br/><br/>
        
        Degree Level:<br/>
        <input type="radio" name="level" value="undergrad" checked> Undergraduate
        <input type="radio" name="level" value="grad"> Postgraduate<br/><br/>
        
        Country Destination:<br/>
        <select name="country">
            <option value="UK" selected>United Kingdom</option>
            <option value="USA">United States</option>
            <option value="Canada">Canada</option>
        </select><br/><br/>
        
        Statement of Purpose:<br/>
        <textarea rows="5" cols="40" name="sop">Enter details...</textarea><br/><br/>
        
        Upload Academic Transcript:<br/>
        <input type="file" name="transcript" accept="application/pdf,image/*"/><br/><br/>
        
        <input type="hidden" name="portal_version" value="1.0"/>
        <input type="submit" name="submit" value="Submit Application"/>
        <input type="reset" name="reset" value="Reset Form"/>
    </form>
</body>
</html>""",
        "content": """# Lab 10: HTML Continued (Advanced)  -  Grouping, Images, Tables, Lists & Forms

![University Header](assets/images/university/itc/lab0_hamdard_logo.png)

## Course & Lab Information
- **Course Title**: Introduction to Computing & ITC Lab
- **Course Code**: CS - 111
- **Program**: BSCS / Engineering
- **Department**: Department of Computing, Hamdard Institute of Engineering & Technology
- **Dated**: _______________

---

## 1. Objective
Learn to create professional web pages using grouping elements, embedded images, tables, lists, and interactive HTML forms.

---

## 2. Grouping Elements: `<div>` and `<span>`
The `<div>` and `<span>` elements allow you to group together several elements to create sections or subsections of a page:
- **`<div>` (Block-level grouping)**: Used to group block-level content, such as grouping all footnotes or creating major document layout sections. You can attach CSS style rules to an entire `<div>`.
- **`<span>` (Inline grouping)**: Used to group inline elements, such as words or short phrases within a sentence.

```html
<!DOCTYPE html>
<html>
<head>
    <title>Span Tag Example</title>
</head>
<body>
    <p>This is the example of <span style="color:green">span tag</span>
    and the <span style="color:red">div tag</span> alongwith CSS</p>
</body>
</html>
```

---

## 3. HTML Comments
A **comment** is a piece of code which is ignored by any web browser. Adding comments into HTML code indicates sections of a document and helps developers understand code structure:

```html
<!-- This is an HTML comment and will be completely ignored by the browser -->
```

---

## 4. HTML Images: `<img>`
Images beautify and clarify complex concepts on webpages. The `<img>` tag is an **empty tag** (it contains only attributes and has no closing tag):

```html
<img src="Image URL" alt="Alternate Text" width="150" height="100" border="3" align="right"/>
```

### Image Attributes
- **`src`**: Mandatory image file path or URL (case-sensitive). Supports PNG, JPEG, and GIF formats.
- **`alt`**: Mandatory alternative text displayed if the image fails to load.
- **`width` & `height`**: Specified in pixels or percentage.
- **`border`**: Border thickness in pixels (`0` means no border).
- **`align`**: Positions image to `left`, `center`, or `right`.

---

## 5. Hyperlinks: Advanced Navigation
The `<a>` tag specifies hyperlinks with destination URL specified in `href`:

```html
<a href="https://www.tutorialspoint.com" target="_self">Tutorials Point</a>
```

### The `target` Attribute
Specifies where the linked document opens:

| Sr. No | Option | Description |
|:---:|:---|:---|
| **1** | `_blank` | Opens the linked document in a new window or tab. |
| **2** | `_self` | Opens the linked document in the same frame (default). |
| **3** | `_parent` | Opens the linked document in the parent frame. |
| **4** | `_top` | Opens the linked document in the full body of the window. |
| **5** | `Targetframe` | Opens the linked document in a named target frame. |

### Linking to a Page Section
Link to internal bookmarks within a long page:
```html
<!-- Target section -->
<h1>HTML Text Links <a name="top"></a></h1>

<!-- Hyperlink jumping to section -->
<a href="#top">Go to the Top</a>
```

### Image Hyperlinks
Wrap an `<img>` tag inside an anchor `<a>` tag to create clickable graphical buttons:
```html
<a href="https://www.tutorialspoint.com" target="_self">
    <img src="/images/logo.png" alt="Tutorials Point" border="0"/>
</a>
```

---

## 6. HTML Tables: `<table>`, `<tr>`, `<td>`, `<th>`
HTML tables arrange data (text, images, links) into structured rows and columns:
- `<table>`: Root table container.
- `<tr>`: Defines a table row.
- `<td>`: Regular data cell (left-aligned by default).
- `<th>`: Header cell (bold and centered by default).
- **`cellpadding`**: Spacing between cell borders and cell content.
- **`cellspacing`**: Spacing between adjacent table cells.

```html
<table border="1" cellpadding="5" cellspacing="5">
    <tr>
        <th>Name</th>
        <th>Salary</th>
    </tr>
    <tr>
        <td>Ramesh Raman</td>
        <td>5000</td>
    </tr>
    <tr>
        <td>Shabbir Hussein</td>
        <td>7000</td>
    </tr>
</table>
```

---

## 7. HTML Lists
HTML provides three list varieties:
1. **Unordered Lists (`<ul>`)**: Plain bulleted items (`<li>`).
   - `type="disc"` (default filled circle)
   - `type="circle"` (empty hollow circle)
   - `type="square"` (filled square)
2. **Ordered Lists (`<ol>`)**: Sequenced numbered items (`<li>`).
   - `type="1"`: Default Arabic numerals (1, 2, 3...)
   - `type="I"`: Uppercase Roman numerals (I, II, III...)
   - `type="i"`: Lowercase Roman numerals (i, ii, iii...)
   - `type="A"`: Uppercase English letters (A, B, C...)
   - `type="a"`: Lowercase English letters (a, b, c...)
3. **Definition Lists (`<dl>`)**: Dictionary-style terms (`<dt>`) and descriptions (`<dd>`).

---

## 8. HTML Forms & Form Controls
Forms collect user data and transmit it to backend server scripts (PHP, ASP, CGI):

```html
<form action="Script URL" method="GET|POST" enctype="application/x-www-form-urlencoded">
    <!-- Form controls -->
</form>
```

### Form Attributes
- **`action`**: Backend script URL processing submitted data.
- **`method`**: Transmission protocol (`GET` appends to URL query string; `POST` transmits securely inside HTTP request body).
- **`enctype`**: Data encoding format (`application/x-www-form-urlencoded` for text; `multipart/form-data` for binary file uploads).

### Comprehensive Form Controls
1. **Single-line Text Input**: `<input type="text" name="first_name" size="20" maxlength="50"/>`
2. **Password Input**: `<input type="password" name="password"/>` (masks characters on screen).
3. **Multi-line Text Area**: `<textarea rows="5" cols="40" name="description">Default text</textarea>`
4. **Checkbox**: `<input type="checkbox" name="maths" value="on" checked> Maths` (permits multiple selections).
5. **Radio Button**: `<input type="radio" name="subject" value="maths"> Maths` (permits only one selection per group name).
6. **Select Box (Dropdown)**:
   ```html
   <select name="dropdown">
       <option value="Maths" selected>Maths</option>
       <option value="Physics">Physics</option>
   </select>
   ```
7. **File Upload Box**: `<input type="file" name="fileupload" accept="image/*"/>`
8. **Buttons**:
   - Submit: `<input type="submit" name="submit" value="Submit"/>`
   - Reset: `<input type="reset" name="reset" value="Reset"/>`
   - Custom Script Button: `<input type="button" name="ok" value="OK"/>`
   - Image Button: `<input type="image" src="btn.png"/>`
9. **Hidden Form Field**: `<input type="hidden" name="pagename" value="10"/>` (persists state without UI display).

---

## 9. Lab Tasks (Verbatim)
1. **Task 1**: Create a webportal for a company providing some consultancy services in education.
2. **Task 2**: It includes many pages, having text, tables, images and an order form.
""",
        "quizzes": [
            {
                "question": "Which target attribute value forces a hyperlink to open inside a brand new browser tab or window?",
                "options": [
                    "_blank",
                    "_self",
                    "_parent",
                    "_top"
                ],
                "correctAnswer": "_blank",
                "explanation": "Setting target='_blank' instructs the browser to open the linked target document in a new tab or window."
            },
            {
                "question": "What is the key difference between cellpadding and cellspacing in HTML tables?",
                "options": [
                    "Cellpadding controls distance inside the cell border, while cellspacing controls distance between adjacent cells",
                    "Cellpadding adds borders, while cellspacing colors text",
                    "Cellpadding is for rows, while cellspacing is for columns",
                    "They are identical synonyms in HTML5"
                ],
                "correctAnswer": "Cellpadding controls distance inside the cell border, while cellspacing controls distance between adjacent cells",
                "explanation": "Cellpadding adjusts whitespace between the cell boundary and its internal content; cellspacing sets the gap between neighboring cells."
            },
            {
                "question": "Which form enctype must be specified when submitting binary file uploads via <input type='file'>?",
                "options": [
                    "multipart/form-data",
                    "application/x-www-form-urlencoded",
                    "text/plain",
                    "binary/octet-stream"
                ],
                "correctAnswer": "multipart/form-data",
                "explanation": "When uploading files through HTML forms, enctype='multipart/form-data' is required so data is partitioned into mime parts without character encoding distortion."
            }
        ],
        "flashcards": [
            {
                "question": "What is the structural difference between <div> and <span>?",
                "answer": "<div> is a block-level container creating section divisions, whereas <span> is an inline container styling text snippets within sentences."
            },
            {
                "question": "What is an HTML empty tag?",
                "answer": "A tag that carries only attributes and has no closing tag (e.g., <img>, <br>, <hr>, <input>)."
            },
            {
                "question": "What are the allowed type values for an ordered list (<ol>)?",
                "answer": "'1' (default digits), 'I' (uppercase Roman), 'i' (lowercase Roman), 'A' (uppercase letters), and 'a' (lowercase letters)."
            },
            {
                "question": "Why are hidden form controls (<input type='hidden'>) used?",
                "answer": "They pass persistent application data (e.g. user session IDs, page numbers) to the server without displaying anything on the screen."
            }
        ]
    },

    # -------------------------------------------------------------------------
    # LAB 11: INTRODUCTION TO MATLAB
    # -------------------------------------------------------------------------
    {
        "order": 11,
        "title": "Lab 11: Introduction to MATLAB  -  Workspace, Vector Operations, M-Files & Debugging",
        "codeSnippet": """% MATLAB Numerical Computation & Matrix Algebra
clc;
clear;

% Calculator calculations
x = 1 + 2 * 3; % x = 7
ans_mult = 4 * x; % ans = 28

% Vectors
v = [1 4 7 10 13]; % Row vector
w = [1; 4; 7; 10; 13]; % Column vector

% 3x3 System of Linear Equations
% 1x + 2y + 3z = 1
% 4x + 5y + 6z = 1
% 7x + 8y + 0z = 1
A = [1 2 3; 4 5 6; 7 8 0];
B = [1; 1; 1];

% Determinant and Matrix Inversion
det_A = det(A);
c = inv(A);
X = c * B;

disp('Determinant:');
disp(det_A);
disp('Solution Vector X:');
disp(X);""",
        "content": """# Lab 11: Introduction to MATLAB

![University Header](assets/images/university/itc/lab0_hamdard_logo.png)

## Course & Lab Information
- **Course Title**: Introduction to Computing & ITC Lab
- **Course Code**: CS - 111
- **Program**: BSCS / Engineering
- **Department**: Department of Computing, Hamdard Institute of Engineering & Technology
- **Dated**: _______________

---

## 1. Objective
To familiarize students with the MATLAB interactive mathematical computing environment, command line operations, vector/matrix generation, M-File script authoring, and debugging techniques.

---

## 2. Introduction to MATLAB
The name **MATLAB** stands for **MATrix LABoratory**. MATLAB was written originally to provide easy access to matrix software developed by the **LINPACK** (linear system package) and **EISPACK** (Eigen system package) projects.

MATLAB is a high-performance language for technical computing. It integrates computation, visualization, and programming environment. Furthermore, MATLAB is a modern programming language environment: it has sophisticated data structures, contains built-in editing and debugging tools, and supports object-oriented programming. These factors make MATLAB an excellent tool for teaching and research.

MATLAB has many advantages compared to conventional computer languages (e.g., C, FORTRAN) for solving technical problems. MATLAB is an interactive system whose basic data element is an array that does not require dimensioning. The software package has been commercially available since **1984** and is now considered as a standard tool at most universities and industries worldwide.

---

## 3. Basic Features & Minimum Session
A minimum MATLAB session teaches the first operational steps:
1. How to log on
2. Invoke MATLAB
3. Do a few simple calculations
4. How to quit MATLAB

### Starting MATLAB & The Desktop Interface
Double-click on the MATLAB shortcut icon on your Windows desktop. When you start MATLAB, a special window called the **MATLAB desktop** appears. The desktop contains major tools:
- **The Command Window**
- **The Command History**
- **The Workspace**
- **The Current Directory**
- **The Help Browser**
- **The Start Button**

![The graphical interface to the MATLAB workspace](assets/images/university/itc/lab10_matlab_desktop.png)

![MATLAB Command Output](assets/images/university/itc/lab10_matlab_command_output.png)

### The Command Window Prompt
In the Command Window, you are greeted with a prompt:
- `>>`: Full commercial version
- `EDU>`: Educational version

---

## 4. Using MATLAB as a Calculator
Type any expression at the prompt to evaluate it immediately:

```matlab
>> 1 + 2 * 3
ans = 7
```

If you do not specify an output variable, MATLAB uses a default variable **`ans`** (short for *answer*) to store calculation results. 

### Variable Assignment & Reassignment
Assign values using the assignment operator (`=`):
```matlab
>> x = 1 + 2 * 3
x = 7

>> 4 * x
ans = 28.0000
```

### Semicolon (`;`) for Output Suppression
Suppress the display of intermediate results by placing a semicolon at the end of a command:
```matlab
>> t = 5;
>> t = t + 1
t = 6
```

### Error Handling
MATLAB provides immediate syntax diagnostics:
```matlab
>> x = 10;
>> 5x
??? 5x
       |
Error: Unexpected MATLAB expression.
```

### Operator Precedence & Parentheses
Parentheses override default operator evaluation order:
```matlab
>> (1 + 2) * 3
ans = 9

>> 1 + 2 * 3
ans = 7
```

### Multiple Statements per Line
Separate statements on a single line using commas (`,`) to print outputs, or semicolons (`;`) to suppress them:
```matlab
>> a = 7; b = cos(a), c = cosh(a)
b = 0.6570
c = 48.3170
```

### Miscellaneous Utility Commands
- **`clc`**: Clears the Command Window text.
- **`ctrl-c`**: Aborts a running computation.
- **`...` (ellipsis)**: Continues a long command onto the next line.
- **`who` / `whos`**: Lists active variables in the workspace with data types and byte allocations.

---

## 5. Matrix & Vector Generation
Matrices are fundamental to MATLAB. An array of dimension $1 \times n$ is a **row vector**, and an array of dimension $m \times 1$ is a **column vector**.

### Row Vector
Enclose elements in square brackets separated by spaces or commas:
```matlab
>> v = [1 4 7 10 13]
v =
     1     4     7    10    13
```

### Column Vector
Separate elements with semicolons (`;`):
```matlab
>> w = [1; 4; 7; 10; 13]
w =
     1
     4
     7
    10
    13
```

### $3 \times 3$ Matrix Generation
```matlab
>> A = [1 2 3; 4 5 6; 7 8 9]
A =
     1     2     3
     4     5     6
     7     8     9
```

---

## 6. M-File Scripts
A script file is an external file containing a sequence of MATLAB statements with the `.m` extension (often called **M-files**):
- **Scripts**: Execute command batches directly within the active workspace.
- **Functions**: Accept input parameters, declare isolated local scopes, and return outputs.

### Linear Equations Example
Consider the system:
$$x + 2y + 3z = 1$$
$$3x + 3y + 4z = 1$$
$$2x + 3y + 3z = 2$$

---

## 7. Debugging M-Files
Debugging isolates and fixes errors in programs:
- **Syntax errors**: Missing parentheses, misspelled keywords.
- **Runtime errors**: Semantic failures producing incorrect numerical outputs.

### Debugging Workflow
1. **Preparing for debugging**: Open file, save changes, ensure file is on the MATLAB search path.
2. **Setting breakpoints**: Pauses execution at specific lines.
   - *Standard breakpoint*: Stops at a specified line.
   - *Conditional breakpoint*: Stops only if a logical condition evaluates to true.
   - *Error breakpoint*: Pauses when a warning, error, NaN, or Inf occurs.
3. **Running with breakpoints**: The prompt changes to **`K>>`** indicating debug mode. The execution pause is highlighted by a green arrow.
4. **Stepping through code & Examining values**: Use Datatips (hovering over variables) and evaluate stack variables.
5. **Ending debugging**: Select *Exit Debug Mode* from the Debug menu.

---

## 8. Lab Tasks (Verbatim)
1. **Task 1**: Calculate the value of the expression:
   $$y = e^{-a} \sin(x) + 10 y^{1/2}$$
   for $a = 5, x = 2$ and $y = 8$.

2. **Task 2**: Consider the following system of linear equations:
   $$1x + 2y + 3z = 1$$
   $$4x + 5y + 6z = 1$$
   $$7x + 8y + 0z = 1$$
   Find out the following and add output:
   - `det(A)`
   - `c = inv(A) = A^-1`
   - `X = c * B`
""",
        "quizzes": [
            {
                "question": "What is the historical origin of the name MATLAB?",
                "options": [
                    "MATrix LABoratory",
                    "Mathematical Tables Library",
                    "Matrix Algorithm Batch",
                    "Modern Applied Technology Lab"
                ],
                "correctAnswer": "MATrix LABoratory",
                "explanation": "MATLAB stands for MATrix LABoratory, originally built to provide access to LINPACK and EISPACK matrix libraries."
            },
            {
                "question": "What is the effect of placing a semicolon (;) at the end of a MATLAB command?",
                "options": [
                    "It suppresses the screen display of the computed result",
                    "It terminates and exits the MATLAB program",
                    "It comments out the preceding code",
                    "It converts the output into a floating-point number"
                ],
                "correctAnswer": "It suppresses the screen display of the computed result",
                "explanation": "In MATLAB, terminating a statement with a semicolon executes the command while suppressing console printout."
            },
            {
                "question": "How does the MATLAB prompt change when entering debug mode at an active breakpoint?",
                "options": [
                    "K>>",
                    "DEBUG>>",
                    "??>>",
                    "STOP>>"
                ],
                "correctAnswer": "K>>",
                "explanation": "When MATLAB halts execution at a breakpoint, the Command Window prompt changes from >> to K>> to indicate debug mode."
            }
        ],
        "flashcards": [
            {
                "question": "What default variable does MATLAB assign when a calculation output is not named?",
                "answer": "ans (short for answer)."
            },
            {
                "question": "How are row vectors distinguished from column vectors in MATLAB syntax?",
                "answer": "Row vector elements are separated by spaces or commas ([1 2 3]), while column vector elements are separated by semicolons ([1; 2; 3])."
            },
            {
                "question": "What is the difference between MATLAB commands clc and clear?",
                "answer": "clc clears the Command Window screen, whereas clear deletes all variables from the memory workspace."
            },
            {
                "question": "What are the three types of breakpoints in MATLAB?",
                "answer": "Standard breakpoints, conditional breakpoints, and error breakpoints."
            }
        ]
    },

    # -------------------------------------------------------------------------
    # LAB 12: PROGRAMMING IN C++ (IDE & BASIC STRUCTURE)
    # -------------------------------------------------------------------------
    {
        "order": 12,
        "title": "Lab 12: Programming in C++  -  C-Free IDE, Program Anatomy & Console Output",
        "codeSnippet": """#include <iostream.h>

int main(void)
{
    // String printing with insertion operator
    cout << "Welcome" << " To " << "Hamdard University" << endl;

    // Numerical expressions
    cout << "Sqr(5) = " << 5 * 5 << endl
         << " and sum of 19 + 10 is: "
         << 19 + 10 << endl;

    return 0;
}""",
        "content": """# Lab 12: Programming in C++ (IDE and Basic Program Structure)

![University Header](assets/images/university/itc/lab0_hamdard_logo.png)

## Course & Lab Information
- **Course Title**: Introduction to Computing & ITC Lab
- **Course Code**: CS - 111
- **Program**: BSCS / Engineering
- **Department**: Department of Computing, Hamdard Institute of Engineering & Technology
- **Dated**: _______________

---

## 1. Objective
To study the features of the Integrated Development Environment (IDE) for C++ language and study the basic building blocks and structures of a C++ program.

---

## 2. Theory: IDE Basics
C++ language features an **Integrated Development Environment (IDE)** as the programmer’s platform. It is a screen with windows and pull-down menus. Code of the program, error messages, and other information are displayed in separate windows. Programmers use menu selections or key combinations to revoke all the operations necessary for program development. Debugging capabilities are also built into the IDE.

### General Overview of IDE Components
- **Run**: Compiles, links, and runs the program.
- **Edit Window**: Space for writing the program.
- **Functions**: Functions used in the program.
- **Tabs**: Different tabs for different source files.
- **New**: Opens a new edit window.
- **Open**: Opens a previously saved program.
- **Line with the error**: Highlights syntax failures.
- **Save**: Saves the program.
- **Build Status**: Shows the status of the compilation and linking process.
- **Error**: Describes the error along with the line number.

![C-Free IDE Interface](assets/images/university/itc/lab12_cfree_ide.png)
![C-Free Launch Screen](assets/images/university/itc/lab12_cfree_launch.png)
![C-Free Editor Window](assets/images/university/itc/lab12_cfree_editor_window.png)
![C-Free Output Window](assets/images/university/itc/lab12_cfree_output_window.png)

---

## 3. Invoking and Operating the IDE
1. **Invoking the IDE**: Double-click on the C-Free icon at the desktop or select it from the Start menu. Click on the *New* icon or select it from the File menu.
2. **Compilation & Execution**: Press **`F5`** to compile and run your program. If your source file contains no errors, an output console window pops up displaying results.
3. **Using Menus**: Press the **`ALT`** function key to activate the menu bar. Navigate using cursor arrow keys.
4. **Writing Code**: Press `[Enter]` to create new lines. Delete characters with `[Del]`. Delete an entire line by selecting it and pressing `[Del]` or via the **`CTRL+Y`** shortcut.
5. **Saving**: Press **`CTRL+S`** or select *File -> Save*. Always add the **`.cpp`** file extension.
6. **Error Correction**: Errors are reported in the Build window at the bottom with line numbers and diagnostic messages.
7. **Exiting the IDE**: Close edit tabs using `[Alt][X]` or exit C-Free using **`[Alt][F4]`**.

---

## 4. Structure of a C++ Program
C++ programs are constructed from fundamental syntactic building blocks:

### Function Definition: `main()`
All C++ programs are divided into units called **functions**. Every C++ program consists of one or more functions. Execution starts at `main()`:

```cpp
#include <iostream.h>
main ()
{
    cout << "This is a program" << endl;
}
```

The `main` function is the entry point to which control is passed from the Operating System when the program is invoked.

### Delimiters: `{ }`
The braces after the function definition signal the beginning and end of the function body. Opening brace `{` indicates the start of a code block; closing brace `}` terminates the block. Braces also delimit loops and decision statements.

### Statement Terminator: `;`
Statements in C++ are terminated with a semicolon `;`. The semicolon terminates the statement, not the carriage return. C++ ignores whitespace (spaces, tabs, carriage returns).

### Program Indentation
Indentation aligns code blocks and matching braces, significantly improving readability and maintainability.

---

## 5. Console Output: The `cout` Statement
The `cout` statement prints information to the console screen. It is followed by the **insertion operator (`<<`)**:

```cpp
cout << "This is a program" << endl;
```

> **Case Sensitivity**: C++ is strictly case-sensitive: `COUT` and `cout` are not the same!

### Syntax
```cpp
cout << e1;
cout << e1 << e2 << e3 << ... << en;
```

### Printing Strings
```cpp
#include <iostream.h>
main ()
{
    cout << "Welcome"
         << " To "
         << "Hamdard University";
}
```

### Printing Numbers and Expressions
Numeric expressions are computed dynamically and substituted with their evaluation:
```cpp
#include <iostream.h>
int main (void)
{
    cout << "Sqr(5) = " << 5 * 5 << endl
         << " and sum of 19 + 10 is: "
         << 19 + 10 << endl;
}
```

---

## 6. Lab Tasks (Verbatim)

### Task 1
Write a program which prints your bio data.

### Task 2
Write a program that prints the table of 8.

**Sample Output:**
```
8 x 1 = 8
8 x 2 = 16
8 x 3 = 24
8 x 4 = 32
8 x 5 = 40
8 x 6 = 48
8 x 7 = 56
8 x 8 = 64
8 x 9 = 72
8 x 10 = 80
```

### Task 3
Write a program which prints the following shape on the display screen:
```
*
**
***
****
```

### Task 4
Write a program which prints the GPA of your five courses.

**Sample Output:**
| Courses | GPA |
|:---|:---:|
| Calculus: | 3.5 |
| Physics: | 2.5 |
| Basic Electronics: | 2.0 |
| Introduction to Computing | 3.9 |
| Islamic Studies | 3.0 |
""",
        "quizzes": [
            {
                "question": "Which function serves as the mandatory entry point where C++ program execution begins?",
                "options": [
                    "main()",
                    "start()",
                    "init()",
                    "cout()"
                ],
                "correctAnswer": "main()",
                "explanation": "In standard C++, the operating system transfers control to the main() function upon execution."
            },
            {
                "question": "What keyboard shortcut compiles and runs a C++ program in the C-Free IDE?",
                "options": [
                    "F5",
                    "F9",
                    "Ctrl+R",
                    "Alt+X"
                ],
                "correctAnswer": "F5",
                "explanation": "In C-Free IDE, pressing the F5 function key triggers compilation, linking, and execution."
            },
            {
                "question": "What is the role of the << operator when used with cout in C++?",
                "options": [
                    "Insertion operator (streams data into standard output)",
                    "Extraction operator (takes input from keyboard)",
                    "Bitwise left-shift comparison",
                    "Statement terminator"
                ],
                "correctAnswer": "Insertion operator (streams data into standard output)",
                "explanation": "The << operator is the insertion (stream output) operator that sends data operands into the cout output stream."
            }
        ],
        "flashcards": [
            {
                "question": "What character is used as the mandatory statement terminator in C++?",
                "answer": "The semicolon (;)."
            },
            {
                "question": "What is the purpose of the endl manipulator in a cout statement?",
                "answer": "It inserts a newline character and flushes the console output stream."
            },
            {
                "question": "What shortcut key combination deletes an entire line of code in the C-Free editor?",
                "answer": "CTRL + Y."
            },
            {
                "question": "What file extension must be given to C++ source code files?",
                "answer": ".cpp"
            }
        ]
    },

    # -------------------------------------------------------------------------
    # LAB 13: PROGRAMMING IN C++ (VARIABLES, DATA TYPES & I/O)
    # -------------------------------------------------------------------------
    {
        "order": 13,
        "title": "Lab 13: Programming in C++  -  Variables, Data Types, cin Input & Decision Control",
        "codeSnippet": """#include <iostream.h>

int main(void)
{
    int age;
    cout << "Enter your age: ";
    cin >> age;

    if (age <= 0)
    {
        cout << "Invalid age" << endl;
    }
    else
    {
        cout << "Age in days: " << age * 365 << endl;
        cout << "Welcome to Hamdard University" << endl;
    }

    return 0;
}""",
        "content": """# Lab 13: Variables, Data Types and I/O Functions

![University Header](assets/images/university/itc/lab0_hamdard_logo.png)

## Course & Lab Information
- **Course Title**: Introduction to Computing & ITC Lab
- **Course Code**: CS - 111
- **Program**: BSCS / Engineering
- **Department**: Department of Computing, Hamdard Institute of Engineering & Technology
- **Dated**: _______________

---

## 1. Objective
- Learn to write programs declaring different variables and data types.
- Learn statements for providing input and displaying output.

---

## 2. Theory: Variables
A **variable** is a named memory location that can hold various values. All variables must be declared before they can be used. A variable’s declaration tells the C compiler what type of variable is being used, giving identity and allocating memory.

### Basic Data Types of C/C++ Language
C supports four basic primitive data types:

| Data Type | Description | Keyword | Storage & Range |
|:---|:---|:---:|:---|
| **Character** | Character data | `char` | 1 byte (holds single symbol e.g., `'A'`, `'0'`, `'&'`) |
| **Integer** | Signed whole number | `int` | 2 or 4 bytes (holds -32,768 to 32,767 in 16-bit systems) |
| **Float** | Floating point number | `float` | Fractional signed values, large magnitude |
| **Void** | Valueless | `void` | Represents empty/valueless operations |

*Additional fundamental C++ types include `double` (double-precision floating point) and `bool` (boolean true/false).*

### Variable Declaration & Value Assignment
```cpp
// Declaration: Type var-name;
int a, b, c;

// Assignment: Variable name = value;
X = 1000;
```

---

## 3. Example Programs & Outputs

### Program 1: Variable Declaration and Assignment
```cpp
#include<iostream.h>
int main (void)
{
    int number;
    number = 1000;
    cout << "The value is " << number << endl;
}
```
**Output:**
```
The value is 1000
```

### Program 2: Multi-Type Variable Usage
```cpp
#include<iostream.h>
int main (void)
{
    int event = 5;
    char heat = 'c';
    float time = 27.25;
    cout << "The winning time in heat " << heat << " of event was "
         << event << " is " << time << endl;
}
```
**Output:**
```
The winning time in heat c of event 5 is 27.25.
```

---

## 4. Input Statement: `cin`
The `cin` statement allows the user to enter data from the keyboard (numbers or single characters). It consists of the keyword `cin` followed by the **extraction operator (`>>`)**, the destination variable name, and a semicolon:

```cpp
cin >> VariableName;
```

### Program: Age in Days Calculator
```cpp
#include <iostream.h> // default compiler selected
int main (void)
{
    int age;
    cout << "Enter your age: ";
    cin >> age; // age variable created earlier
    cout << "Age in days: " << age * 365 << endl;
}
```

---

## 5. Decision Making: The `if` Statement
Decisions to execute or bypass statements are made using `if (expression)`. If the conditional expression evaluates to true, the succeeding statement or block enclosed in `{ ... }` executes:

```cpp
#include <iostream.h>
int main (void)
{
    int age;
    cout << "Enter your age: ";
    cin >> age;
    if (age <= 0)
        cout << "Invalid age" << endl;
}
```

---

## 6. Control Structures: The `if-else` Construct
When alternative paths are required, `if-else` executes the `if` block when true and the `else` block when false:

```cpp
#include <iostream.h>
int main (void)
{
    int age;
    cout << "Enter your age: ";
    cin >> age;
    if (age <= 0)
        cout << "Invalid age" << endl;
    else
        cout << "Welcome to Hamdard University" << endl;
}
```

> **Indentation Rule**: For clarity and making a program easy to understand, each `else` should be indented the same amount as its matching `if`.

---

## 7. Lab Tasks (Verbatim)

### Task 1
Write a program that inputs three numbers and finds the greatest number among these numbers.

**Sample Output:**
```
Enter First Number: 2
Enter Second Number: 3
Enter Third Number: 5
The greatest number is 5
```

### Task 2
Write a program that swaps the value of two variables using a third variable.

**Sample Output:**
```
Variable1: 5
Variable2: 9
After swapping
Variable1: 9
Variable2: 5
```

### Task 3
Write a program that checks whether the entered year is a leap year or not.

### Task 4
Write a program that checks whether the entered number is positive or negative.
""",
        "quizzes": [
            {
                "question": "What is the extraction operator symbol used with the cin input statement in C++?",
                "options": [
                    ">> (extraction operator)",
                    "<< (insertion operator)",
                    "== (relational equals)",
                    "-> (member pointer)"
                ],
                "correctAnswer": ">> (extraction operator)",
                "explanation": "In C++, the stream extraction operator >> reads input from standard input (cin) and stores it into a variable."
            },
            {
                "question": "How much memory does a standard char primitive variable occupy in C++?",
                "options": [
                    "1 byte",
                    "2 bytes",
                    "4 bytes",
                    "8 bytes"
                ],
                "correctAnswer": "1 byte",
                "explanation": "A char variable in C++ stores a single character and requires exactly 1 byte (8 bits) of memory."
            },
            {
                "question": "What happens if the condition in an if statement evaluates to false, and no else branch exists?",
                "options": [
                    "Execution bypasses the if block and proceeds to the next line",
                    "The program crashes with a segmentation fault",
                    "The compiler generates a syntax error",
                    "The program resets back to main()"
                ],
                "correctAnswer": "Execution bypasses the if block and proceeds to the next line",
                "explanation": "If an if statement evaluates to false and there is no else clause, the enclosed block is skipped entirely and program control advances."
            }
        ],
        "flashcards": [
            {
                "question": "What is a variable in computer programming?",
                "answer": "A named location in memory used to store and manipulate data values during program execution."
            },
            {
                "question": "What numeric range can a signed 16-bit integer hold?",
                "answer": "-32,768 to 32,767."
            },
            {
                "question": "How are character literals enclosed in C++?",
                "answer": "Character constants are enclosed within single quotation marks (e.g., 'A', 'c')."
            },
            {
                "question": "What logic determines whether an if or an else block executes?",
                "answer": "The condition expression: if true, the if-block executes; if false, the else-block executes."
            }
        ]
    },

    # -------------------------------------------------------------------------
    # LAB 14: PROGRAMMING IN C++ (ARITHMETIC & LOGIC OPERATIONS)
    # -------------------------------------------------------------------------
    {
        "order": 14,
        "title": "Lab 14: Programming in C++  -  Arithmetic, Relational & Logical Operators",
        "codeSnippet": """#include <iostream.h>

int main()
{
    int a = 13, b = 6;
    cout << "The Modulus of a,b is :: " << a % b << endl;
    cout << "The Sum of a,b is :: " << a + b << endl;

    // Unary increment
    int c = a++;
    cout << "Value of a++ is: " << c << endl;
    cout << "Value of a is: " << a << endl;

    // Relational and Logical Operators
    if (a > b && b != 0)
    {
        cout << "Condition is true: a > b and b is non-zero" << endl;
    }

    return 0;
}""",
        "content": """# Lab 14: Arithmetic and Logic Operations

![University Header](assets/images/university/itc/lab0_hamdard_logo.png)

## Course & Lab Information
- **Course Title**: Introduction to Computing & ITC Lab
- **Course Code**: CS - 111
- **Program**: BSCS / Engineering
- **Department**: Department of Computing, Hamdard Institute of Engineering & Technology
- **Dated**: _______________

---

## 1. Objective
Learn to write programs using different arithmetic, relational, and logical operators in C++.

---

## 2. Arithmetic Operators
Arithmetic operators perform basic mathematical calculations: addition, subtraction, multiplication, division, and modulus.

| Operator | Action | Description |
|:---:|:---|:---|
| **`+`** | Addition | Adds two operands |
| **`-`** | Subtraction | Subtracts second operand from the first |
| **`*`** | Multiplication | Multiplies both operands |
| **`/`** | Division | Divides numerator by denominator |
| **`%`** | Modulus | Returns remainder after integer division |

### Sample Program: Binary Arithmetic
```cpp
#include <iostream.h>
int main( )
{
    int x = 13;
    int y = 6;
    int a = x % y;
    int b = x + y;
    cout << "The Modulus of x,y is ::" << a << '\n' ;
    cout << "The Sum of x,y is ::" << b << '\n' ;
    return 0;
}
```
**Program Output:**
```
The Modulus of x,y is :: 1
The Sum of x,y is :: 19
```

---

## 3. Unary Arithmetic Operators
Unary operators take only **one operand**. Plus (`+`) and minus (`-`) serve as increment and decrement operators:
- **`++` (Increment operator)**: Increases integer value by one (`x++` is identical to `x = x + 1`).
- **`--` (Decrement operator)**: Decreases integer value by one (`x--` is identical to `x = x - 1`).

### Pre-increment vs. Post-increment
- **Post-increment (`a++`)**: The original value of `a` is assigned/evaluated first, and then incremented.
- **Pre-increment (`++a`)**: The value of `a` is incremented first, and then assigned/evaluated.

```cpp
#include <iostream.h>
main()
{
    int a = 21;
    int c;

    // Value of a will not be increased before assignment.
    c = a++;
    cout << "Value of a++ is :" << c << endl;

    // After expression value of a is increased
    cout << "Value of a is :" << a << endl;

    // Value of a will be increased before assignment.
    c = ++a;
    cout << "Value of ++a is  :" << c << endl;

    return 0;
}
```
**Program Output:**
```
Value of a++ is :21
Value of a is :22
Value of ++a is  :23
```

---

## 4. Assignment Operator (`=`)
Assigns a value to a variable. The assignment operation **always takes place from right to left**:
```cpp
x = 5; // Assigns integer 5 to variable x
```

### Sample Program
```cpp
#include <iostream.h>
int main ()
{
    int a, b;         // a:?,  b:?
    a = 10;           // a:10, b:?
    b = 4;            // a:10, b:4
    a = b;            // a:4,  b:4
    b = 7;            // a:4,  b:7

    cout << "a:";
    cout << a;
    cout << " b:";
    cout << b;
}
```
**Program Output:**
```
a:4 b:7
```

---

## 5. Relational Operators
Relational operators compare two operands and evaluate to boolean true or false:

| Operator | Description | Example |
|:---:|:---|:---|
| **`==`** | Checks if the values of two operands are equal or not | `(A == B)` |
| **`!=`** | Checks if the values of two operands are not equal | `(A != B)` |
| **`>`** | Checks if the value of left operand is greater than right | `(A > B)` |
| **`<`** | Checks if the value of left operand is less than right | `(A < B)` |
| **`>=`** | Checks if the value of left operand is greater than or equal to right | `(A >= B)` |
| **`<=`** | Checks if the value of left operand is less than or equal to right | `(A <= B)` |

### Sample Program: Relational Comparisons
```cpp
#include <iostream.h>
main()
{
    int a = 21;
    int b = 10;
    int c;

    if( a == b ) {
        cout << "a is equal to b" << endl;
    } else {
        cout << "a is not equal to b" << endl;
    }

    if ( a < b ) {
        cout << "a is less than b" << endl;
    } else {
        cout << "a is not less than b" << endl;
    }

    if ( a > b ) {
        cout << "a is greater than b" << endl;
    } else {
        cout << "a is not greater than b" << endl;
    }

    return 0;
}
```
**Program Output:**
```
a is not equal to b
a is not less than b
a is greater than b
```

---

## 6. Logical Operators
Logical operators combine or invert conditional statements:

| Operator | Name | Description | Example |
|:---:|:---|:---|:---|
| **`&&`** | Logical AND | If both operands are non-zero (true), condition becomes true | `(A && B)` |
| **`||`** | Logical OR | If any of the two operands is non-zero (true), condition becomes true | `(A || B)` |
| **`!`** | Logical NOT | Reverses the logical state of its operand (true becomes false) | `!(A && B)` |

### Sample Program: Logical Evaluations
```cpp
#include <iostream.h>
main()
{
    int a = 5;
    int b = 20;
    int c;

    if ( a && b ) {
        cout << "Line 1 - Condition is true" << endl;
    }

    if ( a || b ) {
        cout << "Line 2 - Condition is true" << endl;
    }

    /* Let's change the values of a and b */
    a = 0;
    b = 10;

    if ( a && b ) {
        cout << "Line 3 - Condition is true" << endl;
    } else {
        cout << "Line 4 - Condition is not true" << endl;
    }

    if ( !(a && b) ) {
        cout << "Line 5 - Condition is true" << endl;
    }

    return 0;
}
```
**Program Output:**
```
Line 1 - Condition is true
Line 2 - Condition is true
Line 4 - Condition is not true
Line 5 - Condition is true
```

---

## 7. Lab Tasks (Verbatim)

### Task 1
Write a program that prints the area and the perimeter of the rectangle:
- **Area of rectangle**: $L \times B$
- **Perimeter of rectangle**: $2(L + B)$

**Sample Output:**
```
Enter length of the rectangle: 6
Enter breadth of rectangle: 9
Area of a rectangle is 54
```

### Task 2
Write a program that checks whether the entered alphabet is a vowel or not.

### Task 3
Write a program that checks whether the number entered as input is odd or even.

### Task 4
Write a program that takes two numbers as input and then calculate and print the sum, difference, product and quotients of these two numbers.

**Sample Output:**
```
Enter first number: 6
Enter second number: 2
Sum: 8
Difference: 4
Product: 12
Quotient: 3
```
""",
        "quizzes": [
            {
                "question": "What is the result of 13 % 6 in C++?",
                "options": [
                    "1 (remainder of integer division 13 / 6)",
                    "2 (quotient)",
                    "0",
                    "7"
                ],
                "correctAnswer": "1 (remainder of integer division 13 / 6)",
                "explanation": "The modulus operator % calculates the integer remainder: 13 divided by 6 is 2 with a remainder of 1."
            },
            {
                "question": "If int a = 21, what is the value of c after executing c = a++;?",
                "options": [
                    "21 (post-increment assigns first, then increments a to 22)",
                    "22",
                    "20",
                    "Undefined"
                ],
                "correctAnswer": "21 (post-increment assigns first, then increments a to 22)",
                "explanation": "With post-increment (a++), the current value 21 is assigned to c before a is incremented to 22."
            },
            {
                "question": "Which logical operator evaluates to true if either one of the operands is true?",
                "options": [
                    "|| (Logical OR)",
                    "&& (Logical AND)",
                    "! (Logical NOT)",
                    "== (Equality)"
                ],
                "correctAnswer": "|| (Logical OR)",
                "explanation": "The logical OR operator || returns true if at least one of its conditions evaluates to true."
            }
        ],
        "flashcards": [
            {
                "question": "In which direction does variable assignment always execute in C++?",
                "answer": "From right to left (the right-hand expression is evaluated and stored into the left-hand variable)."
            },
            {
                "question": "What is the difference between pre-increment (++a) and post-increment (a++)?",
                "answer": "Pre-increment increases the variable before its value is used in the expression; post-increment uses the original value before increasing."
            },
            {
                "question": "What mathematical operator returns the remainder of integer division?",
                "answer": "The modulus operator (%)."
            },
            {
                "question": "What does the logical NOT operator (!) do?",
                "answer": "It inverts the boolean state of its operand, turning true into false and false into true."
            }
        ]
    }
]
