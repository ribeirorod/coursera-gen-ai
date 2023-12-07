# Import necessary libraries
from datasets import load_dataset
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer, GenerationConfig

# Dialogue Summarization with T5

def load_data_and_model(huggingface_dataset_name, model_name):
    """
    Load the dataset and model.
    """
    dataset = load_dataset(huggingface_dataset_name)
    model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
    tokenizer = AutoTokenizer.from_pretrained(model_name, use_fast=True)
    
    return dataset, model, tokenizer

def summarize_dialogue(dataset, model, tokenizer, example_indices):
    """
    Summarize dialogues from the dataset using the model and tokenizer.
    """
    dash_line = '-'*100
    
    for i, index in enumerate(example_indices):
        dialogue = dataset['test'][index]['dialogue']
        summary = dataset['test'][index]['summary']
        
        # Without prompt engineering
        inputs = tokenizer(dialogue, return_tensors='pt')
        output = tokenizer.decode(
            model.generate(inputs["input_ids"], max_new_tokens=50)[0], 
            skip_special_tokens=True
        )

        print_output(i, dialogue, summary, output, 'WITHOUT PROMPT ENGINEERING')

        # With an instruction prompt
        prompt = f"Summarize the following conversation.\n\n{dialogue}\n\nSummary:"
        inputs = tokenizer(prompt, return_tensors='pt')
        output = tokenizer.decode(
            model.generate(inputs["input_ids"], max_new_tokens=50)[0], 
            skip_special_tokens=True
        )

        print_output(i, prompt, summary, output, 'ZERO SHOT')

        # With a different prompt
        prompt = f"Dialogue:\n\n{dialogue}\n\nWhat was going on?"
        inputs = tokenizer(prompt, return_tensors='pt')
        output = tokenizer.decode(
            model.generate(inputs["input_ids"], max_new_tokens=50)[0], 
            skip_special_tokens=True
        )

        print_output(i, prompt, summary, output, 'ZERO SHOT')

def make_prompt(dataset, example_indices_full, example_index_to_summarize):
    """
    Construct the prompt for one-shot and few-shot inference.
    """
    prompt = ''
    for index in example_indices_full:
        dialogue = dataset['test'][index]['dialogue']
        summary = dataset['test'][index]['summary']
        prompt += f"Dialogue:\n\n{dialogue}\n\nWhat was going on?\n{summary}\n\n"
    
    dialogue = dataset['test'][example_index_to_summarize]['dialogue']
    prompt += f"Dialogue:\n\n{dialogue}\n\nWhat was going on?"

    return prompt

def one_shot_inference(dataset, model, tokenizer, example_indices_full, example_index_to_summarize):
    """
    Perform one-shot inference.
    """
    one_shot_prompt = make_prompt(dataset, example_indices_full, example_index_to_summarize)
    summary = dataset['test'][example_index_to_summarize]['summary']

    inputs = tokenizer(one_shot_prompt, return_tensors='pt')
    output = tokenizer.decode(
        model.generate(inputs["input_ids"], max_new_tokens=50)[0], 
        skip_special_tokens=True
    )

    print_output(None, one_shot_prompt, summary, output, 'ONE SHOT')

def few_shot_inference(dataset, model, tokenizer, example_indices_full, example_index_to_summarize):
    """
    Perform few-shot inference.
    """
    few_shot_prompt = make_prompt(dataset, example_indices_full, example_index_to_summarize)
    summary = dataset['test'][example_index_to_summarize]['summary']

    inputs = tokenizer(few_shot_prompt, return_tensors='pt')
    output = tokenizer.decode(
        model.generate(inputs["input_ids"], max_new_tokens=50)[0], 
        skip_special_tokens=True
    )

    print_output(None, few_shot_prompt, summary, output, 'FEW SHOT')

def print_output(i, dialogue, summary, output, method):
    """
    Print the output in a formatted manner.
    """
    dash_line = '-'*100
    print(dash_line)
    if i is not None:
        print(f'Example {i + 1}')
    print(dash_line)
    print(f'INPUT PROMPT:\n{dialogue}')
    print(dash_line)
    print(f'BASELINE HUMAN SUMMARY:\n{summary}')
    print(dash_line)
    print(f'MODEL GENERATION - {method}:\n{output}\n')

# Load the dataset and model
dataset, model, tokenizer = load_data_and_model("knkarthick/dialogsum", "google/flan-t5-base")

# Summarize dialogues
summarize_dialogue(dataset, model, tokenizer, [40, 200])

# Perform one-shot inference
one_shot_inference(dataset, model, tokenizer, [40], 200)

# Perform few-shot inference
few_shot_inference(dataset, model, tokenizer, [40, 80, 120], 200)
