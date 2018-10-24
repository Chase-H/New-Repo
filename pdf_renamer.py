from StringIO import StringIO
import pyPdf
import os
import re

# a function here
def getPDFContent(path):
        content = ""
            num_pages = 10
                p = file(path, "rb")
                    pdf = pyPdf.PdfFileReader(p)
                        for i in range(0, num_pages):
                                    content += pdf.getPage(i).extractText() + "\n"
                                            content = " ".join(content.replace(u"\xa0", " ").strip().split())     
                                                p.close()
                                                    return content  

                                                # name of the source PDF file
                                                PDF_name = 'awsdfadsf '

                                                # picking texts from the PDF file
                                                pdfContent = StringIO(getPDFContent(r"c:\Users\chase.hudson\Desktop\Email Project" + PDF_name + ".pdf").encode("ascii", "ignore"))
                                                for line in pdfContent:
                                                        aaa = line.find(r'\d{9}')

                                                            final_name = str(aaa)

                                                            print(final_name)

                                                            f = open(r"c:\Users\chase.hudson\Desktop\Email Project" + PDF_name + ".pdf")
                                                            f.close()

                                                            os.rename(r"c:\Users\chase.hudson\Desktop\Email Project" + PDF_name + ".pdf", "C:\\" + final_name + ".pdf")


