import os
from django.db import models
from Docentes.models import CustomUser
from django.contrib.auth.models import User

class Reporte(models.Model):
  CICLOS = (
    ('2019-A', '2019-A'),
    ('2019-B', '2019-B'),
    ('2020-A', '2020-A'),
    ('2020-B', '2020-B'),
    ('2021-A', '2021-A'),
    ('2021-B', '2021-B'),
    ('2022-A', '2022-A'),
    ('2022-B', '2022-B'),
    ('2023-A', '2023-A'),
    ('2023-B', '2023-B'),
    ('2024-A', '2024-A'),
    ('2024-B', '2024-B'),
    ('2025-A', '2025-A'),
    ('2025-B', '2025-B'),
  )

  CURSOS = (
    ('Algoritmos Bioinspirados', 'Algoritmos Bioinspirados'),
    ('Analisis de Algoritmos', 'Analisis de Algoritmos'),
    ('Aprendizaje Automatico', 'Aprendizaje Automatico'),
    ('Almacenes e indicadores', 'Almacenes e indicadores'),
    ('Bases de Datos I', 'Bases de Datos I'),
    ('Bases de Datos II', 'Bases de Datos II'),
    ('Compiladores', 'Compiladores'),
    ('Criptografia', 'Criptografia'),
    ('Continuidad y Gestion de Incidentes', 'Continuidad y Gestion de Incidentes'),
    ('Computacion y modelacion', 'Computacion y modelacion'),
    ('Desarrollo de Aplicaciones Moviles', 'Desarrollo de Aplicaciones Moviles'),
    ('Desarrollo Dinamico', 'Desarrollo Dinamico'),
    ('Desarrollo Dinamico Multiplataforma', 'Desarrollo Dinamico Multiplataforma'),
    ('Desarrollo Dinamico para Web', 'Desarrollo Dinamico para Web'),
    ('Desarrollo de competencias digitales', 'Desarrollo de competencias digitales'),
    ('Desarrollo de Videojuegos', 'Desarrollo de Videojuegos'),
    ('Diseno Digital de la Informacion', 'Diseno Digital de la Informacion'),
    ('Estudio de Casos de Calidad del Software', 'Estudio de Casos de Calidad del Software'),
    ('Estructuras de Datos I', 'Estructuras de Datos I'),
    ('Experiencia de Usuario', 'Experiencia de Usuario'),
    ('Fundamentos de la Cs. Computacional', 'Fundamentos de la Cs. Computacional'),
    ('Fundamentos del Diseno', 'Fundamentos del Diseno'),
    ('Gestión de Proyectos de Software', 'Gestión de Proyectos de Software'),
    ('Graficos, Interfaces y Usabilidad', 'Graficos, Interfaces y Usabilidad'),
    ('Gestion y diseno Digital de la Informacion', 'Gestion y diseno Digital de la Informacion'),
    ('Herramientas computacionales', 'Herramientas computacionales'),
    ('Ingenieria del Software', 'Ingenieria del Software'),
    ('Innovacion, Vigilancia y Desarrollo Tecnologico', 'Innovacion, Vigilancia y Desarrollo Tecnologico'),
    ('Metodologias de Desarrollo agil', 'Metodologias de Desarrollo agil'),
    ('Metologías de Analisis y Diseno de Sistemas', 'Metologías de Analisis y Diseno de Sistemas'),
    ('Mineria de Datos', 'Mineria de Datos'),
    ('Modelado y Animacion Digital', 'Modelado y Animacion Digital'),
    ('Programacion Estructurada', 'Programacion Estructurada'),
    ('Programacion Logica y Funcional', 'Programacion Logica y Funcional'),
    ('Programacion Orientada a Eventos y UML', 'Programacion Orientada a Eventos y UML'),
    ('Programacion Orientada a Objetos', 'Programacion Orientada a Objetos'),
    ('Programacion Web', 'Programacion Web'),
    ('Proyecto Integrador de Desarrollo de Software', 'Proyecto Integrador de Desarrollo de Software'),
    ('Pruebas de Software', 'Pruebas de Software'),
    ('Programacion de Servicios en la Web', 'Programacion de Servicios en la Web'),
    ('Programacion Paralela', 'Programacion Paralela'),
    ('Procesamiento Masivo de Datos', 'Procesamiento Masivo de Datos'),
    ('Redes Neuronales Profundas', 'Redes Neuronales Profundas'),
    ('Sistemas de Control de Versiones', 'Sistemas de Control de Versiones'),
    ('Sistemas Inteligentes', 'Sistemas Inteligentes'),
    ('Sistemas para la Toma de Decisiones', 'Sistemas para la Toma de Decisiones'),
    ('Software para Manejo de Imagenes', 'Software para Manejo de Imagenes'),
    ('Sistemas de Informacion Geografica', 'Sistemas de Informacion Geografica'),
    ('Topicos de Calidad', 'Topicos de Calidad'),
    ('Topicos de Ingeniería de Software', 'Topicos de Ingeniería de Software'),
    ('Teoria de la Computacion', 'Teoria de la Computacion'),
    ('Topicos de Ingenieria de Datos', 'Topicos de Ingenieria de Datos'),
    ('Topicos de Videojuegos', 'Topicos de Videojuegos'),
    ('Tecnologías de la Informacion (Ciencias Forenses)', 'Tecnologías de la Informacion (Ciencias Forenses)'),
    ('Tecnologías de la Informacion (Contaduria)', 'Tecnologías de la Informacion (Contaduria)'),
    ('Tecnologías en Gestion de la Informacion', 'Tecnologías en Gestion de la Informacion'),
    ('Teledeteccion Satelital y Modelacion', 'Teledeteccion Satelital y Modelacion'),
  )

  ACADEMY = (
    ('Ingenieria de Software', 'Ingenieria de Software'),
    ('Programación Avanzada', 'Programación Avanzada'),
    ('Gestión de Datos', 'Gestión de Datos'),
    ('Gestión de Tecnologias de Información', 'Gestión de Tecnologias de Información'),
  )

  EVIDENCIAS = (
    ('Actividades', 'Actividades'),
    ('Examen', 'Examen'),
    ('Lista de Asisntencia', 'Lista de Asisntencia'),
    ('Proyecto', 'Proyecto'),
  )

  TURNOS = (
    ('Matutino', 'Matutino'),
    ('Vespertino', 'Vespertino'),
  )

  titulo = models.CharField('Nombre del Reporte', max_length=120)
  academia = models.CharField(max_length=50, choices=ACADEMY)
  curso = models.CharField(max_length=100, choices=CURSOS)
  ciclo = models.CharField(max_length=10, choices=CICLOS)
  evidencia = models.CharField(max_length=25, choices=EVIDENCIAS)
  turno = models.CharField(max_length=25, choices=TURNOS)
  archivo = models.FileField(upload_to='static/files', blank=True, null=True)
  fecha = models.DateField('Fecha de creación', auto_now_add=True)
  descripcion = models.TextField('Descripción', blank=True, null=True)
  docentes = models.ForeignKey(CustomUser, blank=True, null=True, on_delete=models.CASCADE)

  def __str__(self):
    return self.titulo + ' por ' + self.docentes.username
