# Prompting and prompt engineering

In the process of working with language models, there are several important terms and concepts. 

1. **Prompt**: The text that is fed into the model.
2. **Inference**: The act of generating text.
3. **Completion**: The output text from the model.
4. **Context Window**: The full amount of text or memory available for the prompt.

Sometimes, the model doesn't produce the desired outcome on the first try. In such cases, multiple prompt revisions is required to chieve the desired result. This process is known as **prompt engineering**.

One effective strategy in prompt engineering is to include examples of the task inside the prompt. This method, known as **in-context learning**, helps the model understand the task better.

I've also explored different types of inference:

1. **Zero-shot Inference**: Including the input data within the prompt without any examples.
2. **One-shot Inference**: Providing a single example in the prompt.
3. **Few-shot Inference**: Providing multiple examples in the prompt.

While larger models are good at zero-shot inference, smaller models often benefit more from one-shot or few-shot inference. However, there's a limit to the amount of in-context learning that can be passed into the model due to the context window constraint. *If a model isn't performing well even after including several examples, it might be time to consider **fine-tuning** the model.*

The scale of the model plays a significant role in its performance. Larger models with more parameters capture a better understanding of language and are surprisingly good at zero-shot inference. In contrast, smaller models are generally only good at tasks similar to those they were trained on.

Finally, once a suitable model is selected, there are several configuration settings to experiment with in order to influence the structure and style of the completions the model generates.

# Generative configuration | at inference time

**Configuration Parameters**: These are distinct from training parameters and are invoked at inference time to control aspects like the maximum number of tokens in the completion and the creativity of the output.

1. **Max New Tokens**: This parameter limits the number of tokens that the model will generate. It's essentially a cap on the number of times the model will go through the selection process. 

2. **Greedy Decoding**: By default, most large language models operate with greedy decoding, always choosing the word with the highest probability. However, this method can lead to repeated words or sequences.

3. **Random Sampling**: To introduce variability and avoid repetition, random sampling can be used. The model chooses an output word at random using the probability distribution to weight the selection.

4. **Top K and Top P Sampling**: These techniques limit the random sampling and increase the chance that the output will make sense. With top k, the model is restricted to choose from only the k tokens with the highest probability. With top p, the model is limited to predictions whose combined probabilities do not exceed p.

5. **Temperature**: This parameter influences the shape of the probability distribution for the next token. A higher temperature results in higher randomness and a lower temperature results in lower randomness.

After exploring these concepts, one gains a deeper understanding of how to get the best possible performance out of these models using prompt engineering and by experimenting with different inference configuration parameters. Finally, prepared to start thinking about the steps required to develop and launch a language model-powered application.