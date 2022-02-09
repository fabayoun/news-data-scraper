import re
from docx.shared import Pt

###Adds article text to document based on input sentences


def add_article_text(sentences, document):
    ##adds paragraph for text
    p = document.add_paragraph()
    ##if sentences input is "Text", then article was not downloadable and "Text" is entered as template
    if sentences == "Text":
        p_para = p.add_run(sentences)
    ##if article downloadable, then find first 3 sentences and add into paragraph
    else:
        #finds all ". " and turns sentences into list of seperate sentences
        x = re.findall(r'.+', sentences)
        #takes first 3 sentences and merges them
        if len(x) > 3:
            sentences_first_3 = [x[0], x[1], x[2]]
            sentences_merge_first_3 = ". ".join(sentences_first_3)
            #adds sentences to paragraph
            p_para = p.add_run(sentences_merge_first_3)
        else:
            p_para = p.add_run(sentences)
    ##formats paragraph
    p_para.font.name = 'Calibri'
    p_para.font.size = Pt(11)
    p_para.italic = True
    paragraph_format = document.styles['Normal'].paragraph_format
    paragraph_format.space_before = Pt(0)
    paragraph_format.space_after = Pt(0)