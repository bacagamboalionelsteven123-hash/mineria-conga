from flask import Flask, send_file

app = Flask(__name__)


@app.route("/")
def inicio():
    return """
<!DOCTYPE html>
<html lang="es">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <title>Minería en Conga - Cajamarca</title>

    <style>

        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            scroll-behavior: smooth;
        }

        body {
            font-family: Arial, sans-serif;
            background-color: #f2f2f2;
            color: #222;
        }

        /* BARRA DE NAVEGACIÓN */

        header {
            background-color: #183b2b;
            color: white;
            padding: 20px;
            text-align: center;
        }

        header h1 {
            font-size: 32px;
            margin-bottom: 15px;
        }

        nav a {
            color: white;
            text-decoration: none;
            margin: 0 15px;
            font-weight: bold;
        }

        nav a:hover {
            text-decoration: underline;
        }

        /* PORTADA */

        .portada {
            min-height: 500px;

            background-image:
                linear-gradient(
                    rgba(0, 0, 0, 0.55),
                    rgba(0, 0, 0, 0.55)
                ),
                url("/conga.png");

            background-size: cover;
            background-position: center;

            display: flex;
            justify-content: center;
            align-items: center;

            text-align: center;
            color: white;
            padding: 40px;
        }

        .portada-contenido {
            max-width: 800px;
        }

        .portada h2 {
            font-size: 50px;
            margin-bottom: 20px;
        }

        .portada p {
            font-size: 22px;
            line-height: 1.6;
        }

        /* SECCIONES */

        section {
            padding: 60px 10%;
        }

        section h2 {
            text-align: center;
            color: #183b2b;
            font-size: 32px;
            margin-bottom: 25px;
        }

        section p {
            font-size: 18px;
            line-height: 1.7;
            text-align: justify;
        }

        /* TARJETAS */

        .tarjetas {
            display: flex;
            gap: 25px;
            justify-content: center;
            flex-wrap: wrap;
            margin-top: 30px;
        }

        .tarjeta {
            background-color: white;
            width: 300px;
            padding: 30px;
            border-radius: 12px;

            box-shadow: 0 4px 12px rgba(0,0,0,0.15);

            text-align: center;
        }

        .tarjeta h3 {
            color: #183b2b;
            margin-bottom: 15px;
            font-size: 22px;
        }

        .tarjeta p {
            text-align: center;
            font-size: 16px;
        }

        /* SOLUCIONES */

        .soluciones {
            background-color: #dfeee5;
        }

        .lista {
            max-width: 800px;
            margin: auto;
        }

        .lista li {
            background-color: white;
            margin: 15px 0;
            padding: 18px;
            border-radius: 8px;
            font-size: 18px;
            box-shadow: 0 2px 6px rgba(0,0,0,0.1);
        }

        /* FUENTES */

        .fuentes {
            background-color: white;
        }

        .fuentes ul {
            max-width: 700px;
            margin: auto;
            line-height: 2;
            font-size: 18px;
        }

        /* PIE DE PÁGINA */

        footer {
            background-color: #183b2b;
            color: white;
            text-align: center;
            padding: 25px;
        }

        /* CELULARES */

        @media (max-width: 700px) {

            header h1 {
                font-size: 24px;
            }

            nav a {
                display: block;
                margin: 10px;
            }

            .portada h2 {
                font-size: 35px;
            }

            .portada p {
                font-size: 18px;
            }

            section {
                padding: 40px 6%;
            }

        }

    </style>
</head>


<body>

    <!-- ENCABEZADO -->

    <header>

        <h1>CONGA - CAJAMARCA</h1>

        <nav>
            <a href="#inicio">Inicio</a>
            <a href="#problema">Problema</a>
            <a href="#impactos">Impactos</a>
            <a href="#soluciones">Soluciones</a>
            <a href="#fuentes">Fuentes</a>
        </nav>

    </header>


    <!-- PORTADA -->

    <div class="portada" id="inicio">

        <div class="portada-contenido">

            <h2>Minería y ambiente en Conga</h2>

            <p>
                Información sobre la actividad minera,
                sus posibles impactos ambientales y la
                importancia de la protección de los recursos naturales.
            </p>

        </div>

    </div>


    <!-- PROBLEMA -->

    <section id="problema">

        <h2>La problemática</h2>

        <p>
            La actividad minera puede generar cambios importantes
            en el territorio. Cuando una actividad minera se realiza
            fuera de las normas y autorizaciones correspondientes,
            puede generar riesgos para el ambiente y las comunidades.
        </p>

        <br>

        <p>
            En Cajamarca, el agua, los ecosistemas altoandinos y las
            actividades de las poblaciones locales son elementos
            importantes dentro del debate sobre el uso de los recursos
            naturales.
        </p>

    </section>


    <!-- IMPACTOS -->

    <section id="impactos">

        <h2>Posibles impactos</h2>

        <div class="tarjetas">

            <div class="tarjeta">

                <h3>💧 Agua</h3>

                <p>
                    Las actividades mineras pueden afectar la calidad
                    y disponibilidad del agua si no se aplican medidas
                    adecuadas de prevención y control.
                </p>

            </div>


            <div class="tarjeta">

                <h3>🌱 Medio ambiente</h3>

                <p>
                    La modificación del suelo y del paisaje puede
                    afectar ecosistemas y especies que dependen
                    de estos espacios.
                </p>

            </div>


            <div class="tarjeta">

                <h3>👥 Sociedad</h3>

                <p>
                    Los cambios en el territorio pueden relacionarse
                    con actividades económicas, sociales y culturales
                    de las poblaciones cercanas.
                </p>

            </div>

        </div>

    </section>


    <!-- SOLUCIONES -->

    <section id="soluciones" class="soluciones">

        <h2>Medidas de prevención y control</h2>

        <div class="lista">

            <ul>

                <li>
                    🔎 Fortalecer la fiscalización y supervisión
                    de las actividades mineras.
                </li>

                <li>
                    💧 Proteger las fuentes y ecosistemas
                    relacionados con el agua.
                </li>

                <li>
                    🌳 Promover la recuperación de áreas afectadas.
                </li>

                <li>
                    📚 Informar a la población sobre los impactos
                    ambientales y las normas existentes.
                </li>

                <li>
                    🤝 Promover el diálogo y la participación
                    de las comunidades.
                </li>

            </ul>

        </div>

    </section>


    <!-- FUENTES -->

    <section id="fuentes" class="fuentes">

        <h2>Fuentes de información</h2>

        <ul>

            <li>Ministerio del Ambiente (MINAM)</li>

            <li>Ministerio de Energía y Minas (MINEM)</li>

            <li>Organismo de Evaluación y Fiscalización Ambiental (OEFA)</li>

            <li>Autoridad Nacional del Agua (ANA)</li>

        </ul>

    </section>


    <!-- PIE DE PÁGINA -->

    <footer>

        <p>
            Página educativa sobre minería y ambiente en Conga, Cajamarca.
        </p>

        <p>
            Proyecto realizado con Python y Flask.
        </p>

    </footer>


</body>

</html>
"""


# RUTA PARA MOSTRAR LA IMAGEN

@app.route("/conga.png")
def imagen():
    return send_file("conga.png")


# INICIAR LA PÁGINA

if __name__ == "__main__":
    app.run()