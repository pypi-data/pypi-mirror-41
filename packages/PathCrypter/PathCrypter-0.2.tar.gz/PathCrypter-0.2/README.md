# Path Encoder
## Description
This application allows encryting files and folder (names) using AES.

### Installation
The config generator can be installed directly through PIP from this repo:

```
pip install -e "git+https://wwwin-github.cisco.com/AS-Community/Cable.git#subdirectory=Configuration and Provisioning/ConfigGenerator&egg=ConfigGenerator"
```
 

## Usage
Using the tool requires execution of **"config_generator &lt;options&gt;"**.The following options are supported:
* **-h:** Show the help message
* **-t:** The JINJA2 template file to use
* **-o:** The output file
* **-d:** Data input URL. The scheme in the URL specifies the parser to use. The rest of the URL is the reference to the actual data. This option can be specified multiple times. The following data formats are currently supported:
  * **xml:** Any XML file. The root tag in the file will be used as name to reference the data in the JINJA2 template.
  * **xlsx:** An Excel 2010+ file. The name of the file will be used as name to reference the data in the JINJA2 template (spaces are replaced by underscores).

## Templating
This paragraph describes how to get access to the input data. The complete JINJA2 templating documentation is available from the [JINJA2 documentation site](http://jinja.pocoo.org/docs/2.9/templates/ "JINJA2 templating documentation").

### XML
Assume an XML file with the following content:
```xml
<cablevideo>
    <linecard>
        <slot>1</slot>
    </linecard>
    <linecard>
        <slot>2</slot>
    </linecard>
    <linecard>
        <slot>3</slot>
    </linecard>
</cablevideo>
```
When executing the tool, the data in this file will be mapped to a PYTHON data-structure with the same hierarchy. This means that the 3 linecard sections will be available in a list named **cablevideo.linecard**. This list can be used in various JINJA2 constructs like loops. Each of the slot values is than available as **cablevideo.linecard[i].slot**, with i being the index in the linecard list.

### Excel 2010+ xlsx
The XLSX data is available in the JINJA2 template with a name corresponding to the file basename, without the extension and spaces replaced by underscores (e.g. "test data.xlsx" would be named "test_data"). The data-object supports the following properties:
* **active_worksheet:** Name of the active worksheet. By default the first worksheet in the file is the active one.
* **worksheets:** List of all worksheets in the workbook. This list can be used in loops etc.

Data in the file can only be read, not changed. The value of cells is available using the following functions:
* **cell(&lt;cell-ref&gt;):** This returns the value of the cell as a string
* **cell(&lt;cell-ref&gt;, &lt;row_offset&gt;, &lt;col_offset&gt;):** This returns the value of the cell &glt;row_offset&gt; rows below and &lt;col_offset&gt; columns to the right of the cell specified by &lt;cell-ref&gt;. Example: cell('A1', 2, 3) will return the value of cell 'D3'.
* **cell_as_int(&lt;cell-ref&gt;):** Same as the function cell, but the value is returned as int.
* **cell_as_int(&lt;cell-ref&gt;, &lt;row_offset&gt;, &lt;col_offset&gt;):** Same as the function cell (with 3 parameters), but the value is returned as int.
* **cell_as_float(&lt;cell-ref&gt;):** Same as the function cell, but the value is returned as float.
* **cell_as_float(&lt;cell-ref&gt;, &lt;row_offset&gt;, &lt;col_offset&gt;):** Same as the function cell (with 3 parameters), but the value is returned as float.
* **worksheet(&lt;sheet&gt;):** This function allows changing the active worksheet. The sheet can be specified as an integer (sheet index, zero based) or string (case-sensitive sheet name). Calling this function is to be done using the syntax below (mind the dashes, since these will prevent unwanted spaces and newlines being rendered):
```jinja2
 {{- xlsx_data.worksheet(s) -}}
 ```

> **Note:** All cell references in the cell functions mentioned earlier are on the *active* worksheet. Hence you should be mindful of always setting the correct worksheet before calling a cell function.
