import pandas as pd
import numpy as np
import gradio as gr

housing = pd.read_csv("housing.csv")

def predict_price(
    longitude,
    latitude,
    housing_median_age,
    total_rooms,
    total_bedrooms,
    population,
    households,
    median_income
):

    # fake prediction formula
    price = (
        median_income*50000 +
        housing_median_age*2000 +
        total_rooms*10 +
        households*50
    )

    result = f"Predicted Median House Value: ${price:,.0f}"

    return result


demo = gr.Interface(
    fn=predict_price,
    inputs=[
        gr.Slider(-125, -114, value=-118, label="Longitude"),
        gr.Slider(32, 42, value=34, label="Latitude"),
        gr.Slider(1, 52, value=20, label="Housing Median Age"),
        gr.Slider(2, 40000, value=2000, label="Total Rooms"),
        gr.Slider(1, 10000, value=400, label="Total Bedrooms"),
        gr.Slider(1, 40000, value=1000, label="Population"),
        gr.Slider(1, 10000, value=500, label="Households"),
        gr.Slider(0, 15, value=3, label="Median Income")
    ],

    outputs=gr.Textbox(label="Predicted House Value"),

    title="Housing Price Prediction App",
    description="Enter housing features to predict median house value"
)

demo.launch()
