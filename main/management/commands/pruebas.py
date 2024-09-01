from django.core.management.base import BaseCommand
from main.services import *

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        # crear_curso('SQL01', 'Curso SQL', 1)
        # crear_curso('CRUD01', 'Manejo del CRUD', 1)
        
        # crear_profesor('1-2', 'Profesor SQL', 'BKN', True, 'KRV')
        # crear_profesor('1-3', 'Profesor CRUD', 'Fome', True, 'Admin1')
        
        # crear_estudiante('9-1', 'Jimmy', 'Newtron', '2001-01-01', True, 'Admin1')
        # crear_estudiante('9-2', 'Carl', 'Wheezer', '2001-01-02', True, 'KRV')
        # crear_estudiante('9-3', 'Cindy', 'Vortex', '2001-01-03', True, 'KRV')

        # crear_direccion('Av. Principal', '111', 'barrioAlto', 'Capital', '9-1')
        # crear_direccion('Calle principal', '222', 'barrioPop', 'Capital', '9-2')
        # crear_direccion('La Montaña', '333', 'barrioCampestre', 'Rural', '9-3')

        # agrega_profesor_a_curso('1-1', 'SQL01')
        
        # agrega_cursos_a_estudiante('CRUD01', '9-1')
        # agrega_cursos_a_estudiante('CRUD01', '9-3')

        imprime_estudiante_cursos('9-1')
        imprime_estudiante_cursos('9-2')
        imprime_estudiante_cursos('9-3')
        print('Acción realizada')
        

