import gradio as gr
import numpy as np
import pandas as pd
import pickle

with open('water_potability_rf_model.pkl', 'rb') as f:
    model = pickle.load(f)

def predict(ph,Hardness,Solids,Chloramines,
            Sulfate,Conductivity,
            Organic_carbon,Trihalomethanes,
            Turbidity):

    input_df = pd.DataFrame(
            [[
                ph,Hardness,Solids,Chloramines,
                Sulfate,Conductivity,
                Organic_carbon,Trihalomethanes,
                Turbidity
            ]],
            columns=[
                'ph','Hardness','Solids','Chloramines',
                'Sulfate','Conductivity',
                'Organic_carbon','Trihalomethanes',
                'Turbidity'
            ]
        )

    prediction = model.predict(input_df)[0]

    if prediction == 1:
        return gr.Textbox(value="Potable", label="Result")
    else:
        return gr.Textbox(value="Not Potable", label="Result")


inputs = [
    gr.Number(label='ph', value=7.0),
    gr.Number(label='Hardness', value=196.0),
    gr.Number(label='Solids', value=22014.0),
    gr.Number(label='Chloramines', value=7.0),
    gr.Number(label='Sulfate', value=333.0),
    gr.Number(label='Conductivity', value=426.0),
    gr.Number(label='Organic_carbon', value=14.0),
    gr.Number(label='Trihalomethanes', value=66.0),
    gr.Number(label='Turbidity', value=4.0)
]

with gr.Blocks(theme=gr.themes.Soft()) as app:
    gr.Markdown(
        """
        # 💧 Water Potability Predictor
        This app predicts whether water is potable (safe to drink) based on 9 chemical and physical properties.
        """
    )
    with gr.Row():
        with gr.Column():
            gr.Markdown("## Input Features")
            for input_component in inputs:
                input_component.render()
        with gr.Column():
            gr.Markdown("## Prediction")
            output_text = gr.Textbox(label="Result")
    
    predict_button = gr.Button("Predict")
    predict_button.click(
        fn=predict,
        inputs=inputs,
        outputs=output_text
    )

    gr.Examples(
        examples=[
            [7.0, 196.0, 22014.0, 7.0, 333.0, 426.0, 14.0, 66.0, 4.0],
            [3.7, 129.4, 18630.0, 6.6, 312.1, 398.4, 13.6, 66.4, 4.2],
            [9.1, 199.0, 20325.4, 7.5, 345.0, 450.0, 12.0, 70.0, 3.5]
        ],
        inputs=inputs,
        outputs=output_text,
        fn=predict,
        cache_examples=True
    )


app.launch()
