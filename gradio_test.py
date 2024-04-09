import gradio as gr
from transformers import pipeline

generator = pipeline('text-generation', model='gpt2')

def generate_text(input_text):
    generated_text = generator(input_text, max_length=50)
    return generated_text[0]['generated_text']

iface = gr.Interface(fn=generate_text, 
                     inputs=gr.inputs.Textbox(lines=2, placeholder="Does AI live up to it's hype?"), 
                     outputs='text')

iface.launch()