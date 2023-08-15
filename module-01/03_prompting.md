# Prompting and prompt engineering

In the process of working with language models, I've learned several important terms and concepts. 

1. **Prompt**: The text that I feed into the model.
2. **Inference**: The act of generating text.
3. **Completion**: The output text from the model.
4. **Context Window**: The full amount of text or memory available for the prompt.

Sometimes, the model doesn't produce the desired outcome on the first try. In such cases, I have to revise my prompt or its language multiple times to get the desired result. This process is known as **prompt engineering**.

One effective strategy in prompt engineering is to include examples of the task inside the prompt. This method, known as **in-context learning**, helps the model understand the task better.

I've also explored different types of inference:

1. **Zero-shot Inference**: Including the input data within the prompt without any examples.
2. **One-shot Inference**: Providing a single example in the prompt.
3. **Few-shot Inference**: Providing multiple examples in the prompt.

While larger models are good at zero-shot inference, smaller models often benefit more from one-shot or few-shot inference. However, there's a limit to the amount of in-context learning that can be passed into the model due to the context window constraint. If a model isn't performing well even after including several examples, it might be time to consider **fine-tuning** the model.

The scale of the model plays a significant role in its performance. Larger models with more parameters capture a better understanding of language and are surprisingly good at zero-shot inference. In contrast, smaller models are generally only good at tasks similar to those they were trained on.

Finally, once I've found a suitable model, there are several configuration settings I can experiment with to influence the structure and style of the completions the model generates.