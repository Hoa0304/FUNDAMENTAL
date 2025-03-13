import pandas as pd
from deep_translator import GoogleTranslator

df = pd.read_csv("VN_housing_dataset.csv")
def translate(text):
    print(f"Translating: {text}")
    return GoogleTranslator(source="vi", target="en").translate(text) if isinstance(text, str) else text

df_translated = df.applymap(translate)

df_translated.to_csv("dataset.csv", index= False)
