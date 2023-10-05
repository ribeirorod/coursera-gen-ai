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

## Low Rank Adaptation (LoRA)
