def listado_aves(aves):
    listado = ''
    for ave in aves:
        listado += f'''
            <div class="col-3">
                <div class="card" style="width: 18rem; margin-bottom: 2rem;">
                    <img src="{ave['images']['main']}" class="card-img-top" alt="{['name']}"style="display: inline-block; width: 18rem; height: 18rem;"></img>
                    <div class="card-body">
                        <li class="list-group-item"><h2 style="font-size: 20px;">Nombre español: {ave['name']['spanish']}</h2></li>
                        <li class="list-group-item"><h2 style="font-size: 20px;">Nombre inglés: {ave['name']['english']}</h2></li>
                    </div>
                </div>
            </div>
            '''
    return listado


def cuerpo_html(listado):
    html_template =f'''
    <!DOCTYPE html>
    <html lang="es">
    <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Aves de Chile</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
    </head>
    <body class="bg-info">
        <h1 class='text-center text-light' style='padding-top: 3rem; padding-bottom: 3rem; '>Aves de Chile</h1>
        <div class="container">
            <div style="width: 100%; text-align: center;">
                <div class="row">
                    {listado}
                </div>
            </div>
        </div>
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" crossorigin="anonymous"></script>
    </body>
    </html>
    '''
    return html_template