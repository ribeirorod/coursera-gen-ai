# PEFT (Parameter Efficient Fine Tuning)

Fine-tuning large language models requires significant memory to store the model parameters and other components required during the training process. Even if your computer can hold the model weights, which are now on the order of hundreds of gigabytes for the largest models, you must also be able to allocate memory for optimizer states, gradients, forward activations, and temporary memory throughout the training process.

## Full Fine-Tuning vs PEFT

In contrast to full fine-tuning where every model weight is updated during supervised learning, parameter efficient fine tuning methods only update a small subset of parameters. Some techniques freeze most of the model weights and focus on fine-tuning a subset of existing model parameters, for example, particular layers or components. 

With PEFT, most if not all of the LLM weights are kept frozen. This makes the memory requirements for training much more manageable. In fact, PEFT can often be performed on a single GPU. And because the original LLM is only slightly modified or left unchanged, PEFT is less prone to the catastrophic forgetting problems of full fine-tuning.

## Advantages of PEFT

With parameter efficient fine-tuning, you train only a small number of weights, which results in a much smaller footprint overall. The new parameters are combined with the original LLM weights for inference. The PEFT weights are trained for each task and can be easily swapped out for inference, allowing efficient adaptation of the original model to multiple tasks.

## Methods of PEFT

There are several methods you can use for parameter efficient fine-tuning, each with trade-offs on parameter efficiency, memory efficiency, training speed, model quality, and inference costs. Let's take a look at the three main classes of PEFT methods.

1. **Selective methods**: These fine-tune only a subset of the original LLM parameters. You have the option to train only certain components of the model or specific layers, or even individual parameter types.

2. **Reparameterization methods**: These also work with the original LLM parameters, but reduce the number of parameters to train by creating new low rank transformations of the original network weights. A commonly used technique of this type is LoRA.

3. **Additive methods**: These carry out fine-tuning by keeping all of the original LLM weights frozen and introducing new trainable components. Here there are two main approaches: Adapter methods add new trainable layers to the architecture of the model; Soft prompt methods keep the model architecture fixed and focus on manipulating the input to achieve better performance.

# Low Rank Adaptation (LoRA)

LoRA is a strategy that reduces the number of parameters to be trained during fine-tuning by freezing all of the original model parameters and then injecting a pair of rank decomposition matrices alongside the original weights.

## Working of LoRA

The dimensions of the smaller matrices are set so that their product is a matrix with the same dimensions as the weights they're modifying. You then keep the original weights of the LLM frozen and train the smaller matrices using the same supervised learning process you saw earlier this week.

For inference, the two low-rank matrices are multiplied together to create a matrix with the same dimensions as the frozen weights. You then add this to the original weights and replace them in the model with these updated values. 

## Advantages of LoRA

Because this model has the same number of parameters as the original, there is little to no impact on inference latency. Researchers have found that applying LoRA to just the self-attention layers of the model is often enough to fine-tune for a task and achieve performance gains. However, in principle, you can also use LoRA on other components like the feed-forward layers.

By updating the weights of these new low-rank matrices instead of the original weights, you'll be training fewer parameters and hence, reducing memory requirements significantly. 

## Practical Example

Let's look at a practical example using the transformer architecture described in the Attention is All You Need paper. The paper specifies that the transformer weights have dimensions of 512 by 64. This means that each weights matrix has 32,768 trainable parameters.

If you use LoRA as a fine-tuning method with the rank equal to eight, you will instead train two small rank decomposition matrices whose small dimension is eight. This means that Matrix A will have dimensions of 8 by 64, resulting in 512 total parameters. Matrix B will have dimensions of 512 by 8, or 4,096 trainable parameters. By updating the weights of these new low-rank matrices instead of the original weights, you'll be training 4,608 parameters instead of 32,768 - an 86% reduction.

## Efficiency in Multiple Task Training

Since the rank-decomposition matrices are small, you can fine-tune a different set for each task and then switch them out at inference time by updating the weights. The memory required to store these LoRA matrices is very small. So in principle, you can use LoRA to train for many tasks, switch out the weights when you need to use them, and avoid having to store multiple full-size versions of the LLM.

## Model Performance

LoRA fine-tuned models have shown comparable performance to fully fine-tuned models while reducing the number of trainable parameters significantly. This makes it a viable option for those who want to minimize computational resources while maintaining high model performance. 

Choosing the rank of the LoRA matrices is an active area of research. Optimizing the choice of rank is an ongoing area of research and best practices may evolve as more practitioners make use of LoRA.

# PEFT techniques: Soft Prompts

# Soft Prompts

Soft prompts is a parameter efficient fine tuning method. In this process, additional trainable tokens are added to your prompt and the supervised learning process determines their optimal values. These set of trainable tokens are called soft prompts and they get prepended to the embedding vectors that represent your input text.

## Differences from Prompt Engineering

While prompt engineering involves modifying the language of your prompt to get the desired completion, prompt tuning involves adding trainable tokens to your prompt. This makes it different and often more efficient than prompt engineering, which can require significant manual effort.

## Working of Soft Prompts

The soft prompt vectors have the same length as the embedding vectors of the language tokens. Including between 20 and 100 virtual tokens can be sufficient for good performance. These virtual tokens can take on any value within the continuous multidimensional embedding space. Through supervised learning, the model learns the values for these virtual tokens that maximize performance for a given task.

In contrast with full fine tuning where the weights of the large language model are updated during supervised learning, in prompt tuning, the weights of the large language model are frozen and the underlying model does not get updated. Instead, the embedding vectors of the soft prompt gets updated over time to optimize the model's completion of the prompt.

## Advantages of Soft Prompts

Prompt tuning is a very parameter efficient strategy because only a few parameters are being trained. You can train a different set of soft prompts for each task and then easily swap them out at inference time. Soft prompts are very small on disk, so this kind of fine tuning is extremely efficient and flexible.

## Performance of Soft Prompts

Prompt tuning doesn't perform as well as full fine tuning for smaller LLMs. However, as the model size increases, so does the performance of prompt tuning. Once models have around 10 billion parameters, prompt tuning can be as effective as full fine tuning and offers a significant boost in performance over prompt engineering alone.

## Interpretability of Soft Prompts

One potential issue to consider is the interpretability of learned virtual tokens. Since they can take any value within the continuous embedding vector space, the trained tokens don't correspond to any known token, word, or phrase in the vocabulary of the LLM. However, an analysis of the nearest neighbor tokens to the soft prompt location shows that they form tight semantic clusters, indicating that the prompts are learning word like representations.

In conclusion, both LoRA and Prompt Tuning enable you to fine tune models with the potential for improved performance on your tasks while using much less compute than full fine tuning methods. These methods are heavily used in practice due to their efficiency and comparable performance to full fine tuning for many tasks and datasets.