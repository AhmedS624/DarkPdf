this is a program to turn pdf files to dark mode

put the pdf file in the pdf folder copy it's name (with the extention) then run
the app.py
>it will ask for the name of the pdf file then
>A name of a folder (somthing like dark would do the trick) it is also the
name of the new Dark pdf file to be generated so be carful not to overwrite somthing in the pdf folder

and voila you have a dark pdf waiting for you in the pdf folder

then it will ask you for a folder name this name will be the name of the finished
pdf file (just type somthing like 'dark' for example 

!!!IMPORTANT

pased on the pdf you are working with you may need to change the filter file in
functions just comment and uncomment to switch methods


for_potato_laptop

IMPORTANT TIP
    when using app.py on a multi part pdf make sure the folder you name are numbered
          because part2 will overwrite part1 if you name them both 'dark' do something
                     ||  
          like this \||/
                     \/
    for example: name of pdf in pdf folder: part1.pdf
                 name of folder: dark1
    and so on

I made this program on a potato laptop (1 GB RAM) so it can't take a 200 page pdf file
in on go so I made 2 tools to help with that

split pdf.py

    this tool splits one big pdf into a multible parts based on how you divide it
    first it asks for the name of the file then a number to split by
    for example: if the big pdf has 200 pages and you enter 50 in the result folder
                you will find 4 pdf each one has 50 pages
    if it has 210 the result will be 4 pdfs with 50 pages and 1 with 10 (5 parts in total)
merge pdf.py

    after you take the parts from the results folder into Darkpdf/pdf folder then use app.py on
    all of them one by one you will need to merge them into a one big file
    here is where this tool comes in
    1- you put the finished files in the Darkpdfs folder(the one in the same folder that has the mergepdf.py and the splitpdf.py)
    2- run the merge pdf.py tool
    3- enter every file name in order
    4- press enter again when finished
    5- congrats you are finished the file is named merged.pdf
