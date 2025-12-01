# View PDF viewer

The PDF viewer is dock able panel which is located by default on the right side of the IDE.

![IDE_pdf](ide_pdf.png)

The viewer itself contains a tree with the topics and the actual PDF viewer.

The tree topics can be searched by right clicking on the tree. Choose 'Search' and enter a search text.

When a topic has sub topics, the topic is bold.

When you have enabled 'Auto open Processor PDF' in Options, Environment, PDF, the data sheet will be automatically loaded when you change the $REGFILE value.

It can be shown in a new sheet or it can replace the current PDF.

![pdf_open](pdf_open.png) | Open a PDF.  
---|---  
![pdf_copy](pdf_copy.png) | Copy selected text to the clipboard. You can not copy from protected PDF documents.  
![pdf_first](pdf_first.png) | First page.  
![pdf_prev](pdf_prev.png) | Previous page.  
![pdf_page](pdf_page.png) | Current page indicator. You can enter a page number to jump to a different page.  
![pdf_next](pdf_next.png) | Next page.  
![pdf_last](pdf_last.png) | Last page.  
![pdf_find](pdf_find.png) | Find text in PDF.  
![pdf_zoomin](pdf_zoomin.png) | Zoom in.  
![pdf_zoomout](pdf_zoomout.png) | Zoom out.  
![pdf_rotate](pdf_rotate.png) | Rotate page to the left and right.  
![pdf_print](pdf_print.png) | Print page(s).  
  
When you right click in the PDF, a pop up menu with the most common options will appear.

In [Options, Environment, PDF](options_environment.md) you can specify how data sheets must be downloaded.

Data sheets can be downloaded automatic. When the $REGFILE is changed and the PDF is not present, you will be asked if the PDF must be downloaded.

If you choose to download, it will be downloaded from the Atmel website.

![as_download_pdf](as_download_pdf.png)

When you click 'Do not show this message again' , you will not be asked anymore if you want to download the Mega32.PDF. You will be asked to download other PDF documents when they do not exist.

During the download you will see a similar window:

![down_pdf](down_pdf.png)

You can also download all newer PDF's from the Atmel website with the option : [Tools, PDF Update](tools_pdf_update.md)

When PDF's are downloaded with the UpdateWiz, they are downloaded from the MCS Electronics website.