from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)
@app.route("/index", methods=["GET"])

def construir_df():
    MERCURE_NEG = "MERCURE 1. Muy decepcionado. Tenía una reserva con mucha ilusión y sufrí un accidente que me impidió viajar."
    NOVOTEL_NEG = "NOVOTEL 1. Esta iba a ser la peor estancia de hotel de mis vacaciones de verano. Me he alojado"
    SOFITEL_NEG = "SOFITEL 1. La primera noche, noté una fuga de agua del piso de arriba en el inodoro y la zona del lavabo."
    SLS_NEG = "SLS 1. Cancelaron mi vuelo y nos mandaron a este Hotel..."
    MERCURE_POS = "MERCURE 1. Lo recomiendo. Encantada..."
    NOVOTEL_POS = "NOVOTEL 1. Excelente hotel recomendable..."
    SOFITEL_POS = "SOFITEL 1. Durante mi estancia el hotel siempre estuvo impecable..."
    SLS_POS = "SLS 1. Experiencia inolvidable en el SLS Barcelona."

    df = pd.DataFrame(
        data={
            "RESEÑAS NEGATIVAS": [MERCURE_NEG, NOVOTEL_NEG, SOFITEL_NEG, SLS_NEG],
            "RESEÑAS POSITIVAS": [MERCURE_POS, NOVOTEL_POS, SOFITEL_POS, SLS_POS],
        },
        index=["MERCURE", "NOVOTEL", "SOFITEL", "SLS"],
    )
    return df



def index():
    df = construir_df()
    tabla_html = df.to_html(classes="table table-striped", escape=False)
    return render_template("index.html", tabla=tabla_html)

if __name__ == "__main__":
    app.run(debug=True)
