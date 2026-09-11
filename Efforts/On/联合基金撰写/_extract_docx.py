# -*- coding: utf-8 -*-
"""Extract text (incl. tables, comments, tracked changes) from docx to UTF-8 txt."""
import zipfile
from xml.etree import ElementTree as ET

W = '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'


def para_text(p):
    parts = []
    for node in p.iter():
        tag = node.tag
        if tag == W + 't':
            parts.append(node.text or '')
        elif tag == W + 'tab':
            parts.append('\t')
        elif tag == W + 'br':
            parts.append('\n')
        elif tag == W + 'delText':  # deleted text in tracked changes
            parts.append('[DEL:' + (node.text or '') + ']')
    return ''.join(parts)


def walk_body(body, lines):
    for child in body:
        tag = child.tag
        if tag == W + 'p':
            lines.append(para_text(child))
        elif tag == W + 'tbl':
            for row in child.iter(W + 'tr'):
                cells = []
                for tc in row.iter(W + 'tc'):
                    cell = ' '.join(para_text(p) for p in tc.iter(W + 'p'))
                    cells.append(cell.strip())
                lines.append('｜'.join(cells))


def extract(path, out):
    z = zipfile.ZipFile(path)
    lines = []
    root = ET.fromstring(z.read('word/document.xml'))
    body = root.find(W + 'body')
    walk_body(body, lines)
    if 'word/comments.xml' in z.namelist():
        croot = ET.fromstring(z.read('word/comments.xml'))
        lines.append('')
        lines.append('===== 批注 COMMENTS =====')
        for c in croot.iter(W + 'comment'):
            author = c.get(W + 'author', '')
            lines.append('[批注 by %s] %s' % (author, para_text(c)))
    text = '\n'.join(lines)
    with open(out, 'w', encoding='utf-8') as f:
        f.write(text)
    print(out.encode('unicode_escape').decode()[:80], 'paras:', len(lines))


base = r'D:\hyper_ly\05_Personal\05_Obsidian\Ideaverse Lite 1.5\Ideaverse Lite 1.5\Efforts\On\联合基金撰写'
extract(base + r'\专题六.docx', base + r'\_终稿提取.txt')
extract(base + r'\研究内容_批注.docx', base + r'\_批注提取.txt')
