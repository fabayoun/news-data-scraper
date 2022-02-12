import docx
from docx import Document
from docx.shared import Pt
from docx.oxml import OxmlElement
from docx.enum.dml import MSO_THEME_COLOR_INDEX
from docx.opc import constants


def add_hyperlink(paragraph: Document, text: str, url: str) -> None:
    """
    Adds text with a hyperlink to the paragraph above function
    :param paragraph: paragraph under which a hyperlink should be added
    :param text: text which will contain the hyperlink
    :param url: hyperlink
    :return: updated text file
    """
    # This gets access to the document.xml.rels file and gets a new relation id value
    part = paragraph.part
    r_id = part.relate_to(url, docx.opc.constants.RELATIONSHIP_TYPE.HYPERLINK, is_external=True)

    # Create the w:hyperlink tag and add needed values
    hyperlink = docx.oxml.shared.OxmlElement('w:hyperlink')
    hyperlink.set(docx.oxml.shared.qn('r:id'), r_id, )

    # Create a w:r element and a new w:rPr element
    new_run = docx.oxml.shared.OxmlElement('w:r')
    r_pr = docx.oxml.shared.OxmlElement('w:rPr')

    # Join all the xml elements together add add the required text to the w:r element
    new_run.append(r_pr)
    new_run.text = text
    hyperlink.append(new_run)

    # Create a new Run object and add the hyperlink into it
    r = paragraph.add_run()
    r._r.append(hyperlink)

    # A workaround for the lack of a hyperlink style (doesn't go purple after using the link)
    # Delete this if using a template that has the hyperlink style in it
    r.font.color.theme_color = MSO_THEME_COLOR_INDEX.HYPERLINK
    r.font.underline = True
    r.font.name = 'Calibri'
    r.font.size = Pt(11)
    return hyperlink