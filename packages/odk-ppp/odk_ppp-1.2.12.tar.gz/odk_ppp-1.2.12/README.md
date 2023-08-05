# PPP
## About
PPP is a project with the purpose of helping people convert XlsForm Excel files into more human-readable, printable formats, commonly called "paper questionnaires". Officially, PPP stands for "Pretty PDF Printer", but other formats are supported. The project consists of...

- A [web application](https://github.com/pma-2020/ppp)
- A [command line tool](https://github.com/pma-2020/ppp-web)

Both tools are open source and free to install. You can also use it online with no installation necessary, at http://ppp.pma2020.org.

#### Samples
- Source Excel file: [demo.xlsx](docs/demo.xlsx)
- Converted to PDF: [demo.pdf](docs/demo.pdf)
- Converted to DOC: [demo.doc](docs/demo.doc)
- Manually saved as DOCX from DOC: [demo.docx](docs/demo.docx)
- Converted to HTML: [demo.html](docs/demo.html)

**Example Screenshot**

![demo.png](docs/demo.png)

## Documentation for end users
### CLI
#### Positional Arguments
| Argument | Description |
|:---------|:------------|
| xlsxfile |  Path to source XLSForm. |

#### Options
| Short Flag | Long Flag | Description |
|:-----------|:----------|:------------|
| -h | --help           | Show this help message and exit.
| -d | --debug          | Turns on debug mode. Currently only works for 'html' format. Only feature of debug mode currently is that it prints a stringified JSON representation of survey to the JavaScript console.
| -H | --highlight      | Turns on highlighting of various portions of survey components. Useful to assess positioning.
| -o | --outpath | Path to write output. If this argument is not supplied, then STDOUT is used. Option Usage: `-o OUPATH`.
| -l | --language | Language to write the paper version in. If not specified, the 'default_language' in the 'settings' worksheet is used. If that is not specified and more than one language is in the XLSForm, the language that comes first alphabetically will be used. Option usage: `-l LANGUAGE`.
| -f | --format | File format. HTML and DOC are supported formats. PDF is not supported, but one can easily convert a PPP .doc file into PDF via the use of *wkhtmltopdf* (https://wkhtmltopdf.org/). If this flag is not supplied, output is html by default. Option usage: `-f {html,doc}`.
| -i | --input-replacement | Adding this option will toggle replacement of visible choice options in input fields. Instead of the normal choice options, whatever has been placed in the 'ppp_input' field of the XlsForm will be used. This is normally to hide sensitive information.
| -e | --exclusion       | Adding this option will toggle exclusion of certain survey form components from the rendered form. This can be used to remove ODK-specific implementation elements from the form which are only useful for developers, and can also be used to wholly remove sensitive information without any replacement.
| -r | --hr-relevant     | Adding this option will toggle display of human readable 'relevant' text, rather than the syntax-heavy codified logic of the original XlsForm.
| -c | --hr-constraint   | Adding this option will toggle display of human readable 'constraint' text, rather than the syntax- heavy codified logic of the original XlsForm.
| -C | --no-constraint   | Adding this option will toggle removal of all constraints from the rendered form.
| -t | --text-replacements | Adding this option will toggle text replacements as shown in the 'text_replacements' worksheet of the XlsForm. The most common function of text replacement is to render more human readable variable names, but can also be used to remove sensitive information, or add brevity / clarity where needed.
| -p  | --preset | Select from a preset of bundled options. The 'developer' preset renders a form that is the most similar to the original XlsForm. The 'internal' preset is more human readable but is not stripped of sensitive information. The 'public' option is like the 'internal' option, only with sensitive information removed. Option usage: `-p {public,internal,developer,standard}`.

#### Example Usage
> `python3 -m  ppp myXlsForm.xlsx`
> *Prints HTML converted XlsForm with default settings to the console*

> `python3 -m  ppp myXlsForm.xlsx -l Français -f doc -p standard > myXlsForm.doc`
> *Converts an ODK Excel file to a MS Word-readable .doc file (is really HTML under the hood), with the preset of "standard", and the language set to French*

> `python3 -m ppp myXlsForm1.xlsx myXlsForm2.xlsx -l Luganda Lusoga English -f doc pdf -p standard detailed`
> *Saves a document for every combination of forms and options passed, in this case **2** input files \* **3** languages \* **2** file formats \* **2** detail formats, or **24** output files*

## Documentation for developers
### Installing and building locally
- Clone: `git clone <url>`
- Install dependencies: `cd ppp && pip3 install -r requirements.txt`
- Test to make sure everything's ok: `make test`
