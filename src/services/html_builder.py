import os
from repositories.html_repository import html_repository as default_html_repository

class HtmlBuilder:
    def __init__(self, html_repository=default_html_repository):
        self.text = ""
        self.html_repository = html_repository

# generoitu koodi alkaa
    def generate_html(self, node, width=100, height=100, x_offset=0, y_offset=0):
        x_pos = f"left: {x_offset}%; top: {y_offset}%;"
        style = (
            f'position: absolute; {x_pos} '
            f'width: {width}%; '
            f'height: {height}%; '
            f'background-color: {node.color}; '
            f'color: {node.text_color}; '
            f'font-family: {node.font}; '
            f'font-size: {node.font_size}px; '
            'overflow: hidden;'
        )

        html = f'<div style="{style}">'
        if node.text:
            html += f'<div style="position: relative; left: 10px; top: 10px;">{node.text}</div>\n'

        if node.children:
            size_sum = sum(child.size for child in node.children)
            if node.vertical:
                child_y = 0
                for child in node.children:
                    child_height = (child.size / size_sum) * 100
                    html += self.generate_html(child, 100, child_height, 0, child_y)
                    child_y += child_height
            else:
                child_x = 0
                for child in node.children:
                    child_width = (child.size / size_sum) * 100
                    html += self.generate_html(child, child_width, 100, child_x, 0)
                    child_x += child_width
        html += '\n</div>'

        return html

    def html_document(self, root):
        full_html = f"""<!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Tree Visualization</title>
        <style>
            body, html {{ margin: 0; padding: 0; height: 100%; overflow: hidden; }}
            div {{ display: flex; flex-direction: column; align-items: stretch; }}
        </style>
    </head>
    <body>
    {self.generate_html(root, 100, 100)}
    </body>
    </html>"""
        self.create_html_file(full_html)
        return full_html

    def create_html_file(self, html, filename="output.html"):
        with open(filename, 'w') as file:
            file.write(html)
        file_path = os.path.abspath(filename)
        path = self.html_repository.create(file_path)
        return file_path

# generoitu koodi päättyy
