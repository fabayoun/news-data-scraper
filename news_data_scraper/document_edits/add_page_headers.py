from docx.shared import Pt


def add_cga_heading_author(document):
    """
    Add CGA Heading and Author
    :param document: document object to be edited
    :return: edited document
    """
    document.add_paragraph()

    # Add CGA Heading
    header_cga = document.add_paragraph().add_run("Central Governments Advisory")
    header_cga.font.size = Pt(15)
    header_cga.font.name = 'Calibri'
    header_cga.bold = True

    # Add CGA Author
    author_cga = document.add_paragraph().add_run("By Harry Allport & Rhiannon Evans")
    author_cga.font.size = Pt(11)
    author_cga.font.name = 'Calibri'

    # Add CGA Heading
    document.add_paragraph()


def add_rn_heading(document):
    """
    Add R&N Heading and Author
    :param document: document object to be edited
    :return: edited document
    """
    h_rn_h = document.add_paragraph().add_run("Retail & Networks")
    h_rn_h.font.size = Pt(15)
    h_rn_h.font.name = 'Calibri'
    h_rn_h.bold = True
    document.add_paragraph()
    pass
