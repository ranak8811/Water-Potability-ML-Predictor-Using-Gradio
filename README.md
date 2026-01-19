# Water Potability Predictor

This project is a web application that predicts the potability of water based on several chemical and physical properties. The application is built using Gradio and uses a pre-trained Random Forest model.

---

## 🌐 Live Site URL:

[Water Potability Predictor Live on Hugging Face](https://huggingface.co/spaces/ranak8811/Water-Potability-Predictor)

---

## 🚀 Features

- Predicts water potability based on 9 input features.
- User-friendly interface built with Gradio.
- Includes example values for quick testing.
- Provides a clear "Potable" or "Not Potable" result.

## 📖 Dataset

The model was trained on the "Water Potability" dataset, which contains water quality metrics for 3276 different water bodies.

### Dataset Columns:

1.  **pH value:** An important parameter in evaluating the acid–base balance of water.
2.  **Hardness:** Mainly caused by calcium and magnesium salts.
3.  **Solids (Total dissolved solids - TDS):** The total concentration of dissolved substances in water.
4.  **Chloramines:** A disinfectant used in public water systems.
5.  **Sulfate:** A naturally occurring substance found in minerals, soil, and rocks.
6.  **Conductivity:** The ability of water to conduct an electric current.
7.  **Organic Carbon:** The total amount of carbon in organic compounds in pure water.
8.  **Trihalomethanes (THMs):** Chemicals that may be found in water treated with chlorine.
9.  **Turbidity:** The measure of the cloudiness or haziness of water.
10. **Potability:** Indicates if water is safe for human consumption (1 = Potable, 0 = Not Potable).

## 🛠️ Installation

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/ranak8811/Water-Potability-ML-Predictor-Using-Gradio.git
    cd Water-Potability-ML-Predictor-Using-Gradio
    ```

2.  **Create a virtual environment:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3.  **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## 🏃‍♀️ Usage

To run the application, execute the following command:

```bash
python app.py
```

Then, open your web browser and navigate to the URL provided by Gradio (usually `http://127.0.0.1:7860`).

## 🖼️ Screenshot

![Screenshot of the application](/assets/gradio.png)

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
