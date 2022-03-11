# CSV-to-JSON
Cvs2Json, una clase de Python para convertir text o CSV (con valores de coma separados) a JSON (Notacion de Objeto JavaScript) formato para modelo DJANGO
<h3>Introduccion</H3>
<p>
  Este es mi primer programa. Este es una clase de modulo que ayuda a convertir txt o CSV a formato JSON por
  <a href="https://docs.djangoproject.com/en/3.1/topics/db/models/">modelo Django</a> El cual necesita tre propiedades: <b>“pk”</b>, <b>“model”</b> y <b>“fields”</b>. Ver
  <a href="https://docs.djangoproject.com/en/3.1/topics/serialization/#serialization-formats-json"> serializacion de formatos</a> mas informacion de DJANGO.
</p>
<p>
  En vez de usar <code>strip()</code> y <code>split()</code> funciones como los tutoriales de https://www.geeksforgeeks.org/convert-text-file-to-json-in-python/ y https://github.com/jcamier/csv-json-django/blob/master/convertir_csv_a_json.py. Yo use la construccion de Python y <a href="https://docs.python.org/3/library/csv.html"> libreria csv<a>. Esto es mas facil, conveniente y poderoso. Esto fue creado para leer y escribir datos tabulados en formato CSV el cual fue generado por Microsoft Excel.
</p>
<p>
  Yo krabeeputh y cuenta https://github.com/krabeeputh desarrolle este programa para brindar soporte al lenguage Tailandes con codigo (UNICODE) utf8 asi que espero esto pueda brindar soporte a cualquier lenguate tambien.
</p>


<h3>¿Como usarlo?</h3>
<p>
  1. Importa el modulo<br>
  2. Configura algunas variables
</p>
<ul>
  <li>El archivo CSV a ser convertido</li>
  <li>El archivo de salida JSON</li>
  <li>App y nombre de Modelo</li>
  <li>Los espacios de la Lista en tu modelo</li>
</ul>
<p>
  3. Crea el objeto a usar<br>
  ver mas detalles en el archivo test.py
</p>

<h3>Entrada & Salida</h3>
<p> Tendre 2 archivos</p>
<ul>
  <li>countries.csv, Este es el archivo fuente que se va a convertir a formato JSON. Tu puedes usarlo para testeo en el programa.</li>
  <li>countries.json, Este es el archivo que se auto genera de class. Esta es mi archivo de salida JSON. Tu puedes correr mi programa para el mismo formato de salida</li>
</ul>
