import os
import re
import xml.etree.ElementTree
from typing import List

from doxybook.markdown import Md, MdDocument, MdCode, MdCodeBlock, MdBold, MdItalic, MdLink, MdHeader, MdList, MdParagraph, MdRenderer, MdLine, MdTable, MdTableRow, MdTableCell, Text, Br
from doxybook.node import Node
from doxybook.kind import Kind
from doxybook.cache import Cache
from doxybook.config import config
from doxybook.generators.paragraph import generate_paragraph, convert_xml_para

def generate_file(index_path: str, output_path: str, node: Node, cache: Cache) -> dict:
    output_file = os.path.join(output_path, node.refid + '_source.md')
    print('Generating ' + output_file)
    document = MdDocument()

    # Add title
    title = node.name + ' File Reference'
    document.append(MdHeader(1, [Text(title)]))

    # Load XML
    xml_root = xml.etree.ElementTree.parse(os.path.join(index_path, node.refid + '.xml')).getroot()
    if xml_root is None:
        IndexError('Root xml not found!')
    compounddef = xml_root.find('compounddef')
    if compounddef is None:
        IndexError('compounddef not found in xml!')  

    document.append(MdParagraph([MdBold([MdLink([Text('Go to the documentation of this file.')], node.refid + '.md')])]))  

    location = compounddef.find('location')
    if location is not None:
        document.append(MdParagraph([Text('Source: '), MdCode([Text(location.get('file'))])]))

    programlisting = compounddef.find('programlisting')
    if programlisting is None:
        return

    document.append(MdParagraph(convert_xml_para(compounddef, cache)))

    if not config.noindex:
        document.set_keywords([node.name, 'file'])
    document.set_title(title)

    # Save
    with open(output_file, 'w') as f:
        document.render(MdRenderer(f))