# Instalación

## Git

* Windows: Descargar el instalador en la [página oficial](https://git-scm.com/download/win) y ejecutarlo. Recomiendo agregar al `PATH` para acceder de cualquier terminal.
* Linux: En algunas distribuciones se encuentra instalado por defecto, en caso contrario sigue las instrucciones de este [link](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) pues depende de la distribución.

Para validar si tu instalación fue correcta, debes ejecutar en la terminal:
 ```
 git --version
 ```
 Usuarios de Windows que no agregaron Git al `PATH` tendrán que utilizar la terminal _Git Bash_.


## GitHub

* Utilizando tu correo institucional puedes registrarte a través de [GitHub Student Developer Pack](https://education.github.com/pack), con el cual puedes acceder a repositorios privados, entre otras cosas. En caso contrario, puedes crear una cuenta directamente en el [sitio oficial](https://github.com/).
* Para crear tu portafolio personal, ingresa a [este](https://github.com/aoguedao/mat281_portfolio_template) repositorio, haz click en *__Use this template__* y asigna el nombre `mat281_portfolio` y en modo público.


## Conda

* Seguir la instalación regular de desde la [documentación oficial](https://docs.conda.io/projects/conda/en/latest/user-guide/install/) según tu sistema operativo.
* Instalar **Miniconda**
    - Windows: En su menú de inicio tendrán dos nuevos programas **Anaconda Prompt** y **Anaconda Powershell Prompt**, pueden ocupar cualquiera. Personalmente prefiero Powershell.
    - Linux: En la instalación se recomienda agregar `conda` al `PATH`. Si cada vez que inicias una terminal vez el texto `(base)` al comienzo, debes ejecutar `conda config --set auto_activate_base false` y luego cada vez que quieras utilizar conda debes ejecutar `conda activate`.


## Entorno de trabajo

* Clonar el repositorio oficial del curso: 
```
git clone https://github.com/aoguedao/mat281_2020S2.git
```
en alguna carpeta que estimes conveniente.
* Clonar tu portafolio personal:
```
git clone https://github.com/{GH_USERNAME}/mat281_portfolio.git
```
donde `{GH_USERNAME}` es tu nombre de usuario en GitHub.
* Para crear el entorno virtual ejecuta el siguiente comando
```
conda env create -f environment.yml --yes
```
en la carpeta `mat281_portfolio/binder`. Según tu sistema operativo debes utilizar Anaconda Prompt o activar conda en tu terminal.
* Verifica que tu ambiente virtual se instaló con `conda env list`, deberías ver dos ambientes virtuales, `base`(default) y `mat281`.
* Activa tu ambiente virtual con `conda activate mat281`.
* Ejecuta `jupyter lab` en la terminal y en tu navegador de internet accede a `http://localhost:8888/lab` (o sigue el link de la terminal).
* Abre el archivo `mat281_portfolio/labs/test_installation.ipynb` y verifica que todas las celdas se ejecuten sin errores.
* Felicitaciones, tienes todo lo necesario para triunfar en este curso!

## Próximos pasos

Con tal de facilitar la entrega y revisión de laboratorios, tareas y proyectos, los estudiantes deben subir estos entregables en los plazos establecidos en su portafolio personal. En este [link](https://github.com/aoguedao/mat281_portfolio_template/blob/master/setup.md) encontrarás más detalles del flujo típico de una clase (también lo puedes encontrar en `mat281_portfolio/setup.md`).