Aplicación:

[Abrir el proyecto uso de perceptrones para la clasificación de flores - dataset iris](https://perceptron-clasificador-iris.herokuapp.com/)

# Instalación de Streamlit

Mediante el uso de [streamlit](https://streamlit.io/) podemos hacer visibles el uso de nuestros modelos de IA para cualquier usuario.

```
    pip install streamlit
```

y en el entorno de env que previamente has creado, ejecutar

```
    streamlit run main.py
```

dentro del fichero main, nuestro 'hello world' sería:

```
    import streamlit as st

    st.write("Hello world!")
```

esto levantará un servidor

![](up_streamlit.jpg)

y ya tendrás tus scripts de python con IA corriendo en la web, con una interfaz transparente al usuario. Ahora queda la parte más dificil, enlazar nuestro repositorio git con los códigos fuentes a heroku y hacer deploy automático en cada cambio.

# Conexión de git con heroku

[https://devcenter.heroku.com/articles/git]()

[https://devcenter.heroku.com/articles/getting-started-with-python]()

## Subiendo nuestro app Stramlit

Actualiza los cambios en el repositorio y heroku lo detecta automáticamente, pero para ello es importante que esté activado el "Automatically deploys from master", luego en "activity" podrás ver el curso del build y cuando indique la ruta de la nueva app querrá decir que ha terminado.

### nota

He tenido un problema con el fichero del dataset, que es general a todos los fichero que se tengan que acceder desde Heroku y es que no admite las rutas relativas, por ello con este trozo de código se soluciona:

```
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#Donde se tenga que apuntar la ruta
ruta = os.path.join(BASE_DIR, 'nombre_fichero')

```

### Content License

Creative Commons ![](./88x311.png)

This web page, all content with proyects and source code, is licensed under Creative Commons: Attribution-NonCommercial-NoDerivatives 4.0 International (CC BY-NC-ND 4.0) [More info](https://creativecommons.org/licenses/by-nc-nd/4.0/)

Esta página web y todo su contenido, incluido proyectos y código fuente, está licenciado bajo una licencia de Creative Commons: Attribution-NonCommercial-NoDerivatives 4.0 International (CC BY-NC-ND 4.0) [Más info](https://creativecommons.org/licenses/by-nc-nd/4.0/deed.es)
