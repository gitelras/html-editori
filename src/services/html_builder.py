import os
from repositories.html_repository import html_repository as default_html_repository
# generoitu koodi alkaa
class HtmlBuilder:
    """
    Luokka, joka vastaa HTML-dokumentin rakentamisesta ja tallentamisesta.

    Attributes:
        text (str): Sisältää HTML-muotoilua varten väliaikaisesti tallennettua tekstiä.
        html_repository (module): Moduuli, joka tarjoaa metodit HTML-tiedostojen käsittelyyn.
    """

    def __init__(self, html_repository=default_html_repository):
        """
        Alustaa HtmlBuilder-olion attribuutit.

        Args:
            html_repository (module, optional): Moduuli, 
            joka tarjoaa metodit HTML-tiedostojen käsittelyyn.
                Oletuksena käytetään default_html_repositoryä.
        """
        self.text = ""
        self.html_repository = html_repository

    def generate_html(self, node, width=100, height=100, x_offset=0, y_offset=0):
        """
        Generoi HTML-koodin annetulle solmulle ja rekursiivisesti kaikille sen lapsille.

        Args:
            node (Node): Solmu, jolle HTML generoidaan.
            width (int, optional): Solmun leveys prosentteina. Oletus on 100.
            height (int, optional): Solmun korkeus prosentteina. Oletus on 100.
            x_offset (int, optional): Solmun x-akselin siirtymä prosentteina. Oletus on 0.
            y_offset (int, optional): Solmun y-akselin siirtymä prosentteina. Oletus on 0.

        Returns:
            str: Generoitu HTML-merkkijono solmulle ja sen lapsille.
        """
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

    def html_document(self, root, name):
        """
        Luo koko HTML-dokumentin, joka sisältää puun visualisoinnin.

        Args:
            root (Node): Puun juurisolmu, josta dokumentin generointi aloitetaan.
            name: Dokumentin nimi, jonka käyttäjä asettaa.

        Returns:
            str: Valmis HTML-dokumentti merkkijonona.
        """
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
        self.create_html_file(full_html, name)
        return full_html

    def create_html_file(self, html, filename):
        """
        Tallentaa generoidun HTML-dokumentin tiedostoon ja rekisteröi sen html_repositoryn kautta.

        Args:
            html (str): Tallennettava HTML-dokumentti.
            filename (str, optional): Tiedostonimi, johon dokumentti tallennetaan. 

        Returns:
            str: Absoluuttinen polku luotuun tiedostoon.
        """
        filename = f'{filename}'+'.html'
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(html)
        file_path = os.path.abspath(filename)
        path = self.html_repository.create(file_path)
        return file_path
    
    def all_files(self):
        return default_html_repository.get_files()

# generoitu koodi päättyy
