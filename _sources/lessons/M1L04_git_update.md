# Utilizando git

## Actualizar repositorio del curso

Para actualizar el repositorio del curso (típicamente cada clase) debes abrir una terminal que tenga `git` en el `PATH`, que para usuarios de Windows podría ser _Git Bash_ o _Anaconda Prompt_ (si es que se configuró así). Luego ejecutar el siguiente comando en la carpeta del repositorio `mat281_2020S2`:

```bash
git pull
```

En caso que la ejecución anterior arroje algún error ejecuta lo siguiente:

```bash
git reset --hard
git pull
```

```{danger}
Perderás todos los cambios que hayas hecho en el repositorio del curso, no olvides respaldar tus desarrollos en tu portafolio.
```

Copia y pega el laboratorio/tarea/etc. actualizado del repositorio `mat281_2020` en tu repositorio `mat281_portfolio` en el directorio correspondiente. Por ejemplo, la cuarta clase del módulo tiene asociado el laboratorio `mat281_2020S2/labs/lab01.ipynb`, luego de hacer `pull` debes copiar este archivo en tu repositorio en el directorio `mat281_portfolio/labs/lab01.ipynb`. 

Ejecuta Jupyter Lab en tu directorio favorito, de preferencia uno que tenga acceso a ambos repositorios. Luego abre el laboratorio de tu repositorio, por ejemplo `mat281_portfolio/labs/lab01.ipynb` y comienza a desarrollar.

Al finalizar es importante que subas los cambios a tu repositorio en GitHub (recuerda que hasta el momento esos cambios solo están reflejados en tu computador personal). En la carpeta de tu portafolio ejecuta lo siguiente en una terminal con acceso a `git`:

```bash
git config user.name "{YOUR_NAME}"
git config user.email "{YOUR_GITHUB_ACCOUNT_EMAIL}"
```

donde debes reemplazar por tu nombre personal y tu correo electrónico (asociado a tu cuenta de GitHub). Esto configura el autor de los cambios.

El siguiente paso es seleccionar los cambios a subir, típicamente deberás agregar el archivo notebook del entregable y en caso de ser necesario otros archivos que sean necesarios para el correcto desarrollo, ya sea conjuntos de datos, scripts, imágenes, etc. Siguiente con el mismo ejemplo, debería ser algo así:

```bash
git add labs/M1L04_lab.ipynb
```

Ahora es necesario firmar estos cambios, con el siguiente comando:

```bash
git commit -m "{ANY DESCRIPTIVE MESSAGE}"
```

donde se recomienda agregar un mensaje descriptivo del cambio en cuestión, por ejemplo: _"Se agrega desarrollo del laboratorio 01 correspondiente a la clase M1L04"_.

Finalmente, es necesario subir estos cambios a GitHub:

```bash
git push origin master
```

Verifica que los cambios se hayan actualizado en tu cuenta de GitHub y además verifica que tu entregable funciona correctamente con Binder.

```{warning}
Repositorios en donde Binder no ejecute correctamente se calificarán con nota cero.
```

Para cumplir con las formalidades debes enviar un correo antes del plazo establecido (o si no se aplicará la sanción correspondiente) a `alonso.ogueda@usm.cl` que contenga el link al commit de tu entregable (al que puedes acceder directamente desde tu repositorio). Tu link debe lucir similar a este [`https://github.com/aoguedao/mat281_portfolio_template/commit/7081d2fb63e55a391f712aef942f35c60e8b7a2b`](https://github.com/aoguedao/mat281_portfolio_template/commit/7081d2fb63e55a391f712aef942f35c60e8b7a2b). Nota que el commit está asociado a una hora específica, por lo que para caso de plazos se utilizará la fecha del correo electrónico pero se revisará el desarrollo al commit enviado (por lo que es posible determinar si el entregable ha sido modificado después de enviar el correo).