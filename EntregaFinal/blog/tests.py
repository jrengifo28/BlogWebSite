from django.test import TestCase
from blog.models import Pagina

# Create your tests here.


class ViewtestCase(TestCase):

    def test_crear_pagina(self):
        Pagina.objects.create(titulo="Test0", subtitulo="Prueba",
                              cuerpo="Este es el test de prueba", autor="Automata", fecha="2022-11-07")
        all_paginas = Pagina.objects.all()
        print(all_paginas)

        # Creamos un test para probar que se creó una página nueva
        assert len(all_paginas) == 1

    def test_crear_3paginas(self):
        Pagina.objects.create(titulo="Test1", subtitulo="Prueba1",
                              cuerpo="Este es el test de prueba1", autor="Automata1", fecha="2022-11-07")
        Pagina.objects.create(titulo="Test2", subtitulo="Prueba2",
                              cuerpo="Este es el test de prueba2", autor="Automata2", fecha="2022-11-06")
        Pagina.objects.create(titulo="Test3", subtitulo="Prueba3",
                              cuerpo="Este es el test de prueba3", autor="Automata3", fecha="2022-11-05")
        all_paginas = Pagina.objects.all()

        # Creamos un test para probar que se crearon las 3 páginas nuevas
        assert len(all_paginas) == 3

    def test_verificar_atributos(self):
        Pagina.objects.create(titulo="Test1", subtitulo="Prueba1",
                              cuerpo="Este es el test de prueba1", autor="Automata1", fecha="2022-11-07")
        Pagina.objects.create(titulo="Test2", subtitulo="Prueba2",
                              cuerpo="Este es el test de prueba2", autor="Automata2", fecha="2022-11-06")
        Pagina.objects.create(titulo="Test3", subtitulo="Prueba3",
                              cuerpo="Este es el test de prueba3", autor="Automata3", fecha="2022-11-05")
        all_paginas = Pagina.objects.all()

        # Creamos un test para probar que las páginas se hayan creado con los atributos correctos
        assert all_paginas[0].titulo == "Test1"
        assert all_paginas[1].subtitulo == "Prueba2"
        assert all_paginas[2].cuerpo == "Este es el test de prueba3"
