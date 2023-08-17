
# Pre-training large language models

### Generative AI Project Life Cycle
   - After defining your use case, the next step is to select a model.
   - You can either use an existing model or train your own from scratch.
   - Open-source models are available for use via hubs curated by developers like Hugging Face and PyTorch.

### Model Selection
   - Model cards in these hubs provide details about best use cases, training methods, and limitations for each model.
   - The choice of model depends on the task at hand.
  
### Training Large Language Models (LLMs)
   - LLMs learn from vast amounts of unstructured textual data during the pre-training phase.
   - Pre-training involves updating model weights to minimize the loss of the training objective.
   - Data quality curation is crucial; often only 1-3% of tokens are used for pre-training.

### Variations of Transformer Models
   - Three variants exist: Encoder-only (Autoencoding), Decoder-only (Autoregressive), and Sequence-to-sequence models (Encoder-Decoder)
   - Each variant is trained on a different objective and is suited to different tasks.
   - Autoencoding models, pre trained with mass languague models (MLM), are suitable for sentence classification tasks and token-level tasks (BERT & RoBERTa).
   - Autoregressive models, pre-trained with causal language modeling (CLM), are often used for text generation (GPT & BLOOM).
   - Sequence-to-sequence models are used for translation, summarization, and question-answering tasks (T5 & BART).

### Challenges of Training Large Models
   - Although larger models are more capable, they are also more difficult and expensive to train.
   - Continuously training larger models may be infeasible due to these challenges.

# Computational Challenges

### Memory Constraints in Training LLMs
   - LLMs require enormous memory due to their size and the complexity of their parameters.
   - Additional components that use GPU memory during training include optimizer states, gradients, activations, and temporary variables.
   - Training a one billion parameter model at 32-bit full precision requires approximately 80 gigabytes of GPU RAM, which exceeds the capacity of most hardware.

### Quantization as a Solution
   - Quantization reduces memory requirements by decreasing the precision from 32-bit floating point numbers to 16-bit or 8-bit numbers.
   - The corresponding data types are FP32 for 32-bit full position, FP16 or Bfloat16 for 16-bit half precision, and int8 eight-bit integers.

### Different Quantization Formats
   - FP32: Represents a wide range of numbers, used by default for model weights, activations, and other parameters.
   - FP16: Reduces the range and precision of numbers, resulting in lower memory usage.
   - BFLOAT16: A hybrid between FP16 and FP32, it maintains the dynamic range of FP32 but reduces memory footprint by half.
   - INT8: Further reduces the precision and range of numbers, leading to significant memory savings but a dramatic loss of precision.

### Impact of Quantization
   - Quantization can significantly reduce the memory consumption required to store model parameters.
   - It also enables the training of large models on a single GPU.
   - However, for models exceeding a few billion parameters, distributed computing techniques across multiple GPUs become necessary.

### Distributed Computing Techniques
   - As models scale beyond a few billion parameters, it becomes impossible to train them on a single GPU.
   - Training across multiple GPUs could require access to hundreds of GPUs, making it very expensive.
   - An additional training process called fine-tuning also requires storing all training parameters in memory.

# Multi-GPU compute strategies

### Model Replication DDP 
   - Distributed Data Parallel (DDP) is a popular implementation of this technique in PyTorch.
   - DDP copies the model onto each GPU and sends batches of data to each of the GPUs in parallel, allowing for faster training.
   - However, DDP requires that the model weights and all additional parameters fit onto a single GPU.

### Model Sharding FSDP
   - Fully Sharded Data Parallel (FSDP) is an implementation of this technique in PyTorch.
   - FSDP is based on ZeRO (Zero Redundancy Optimizer), a technique proposed by Microsoft researchers to optimize memory by distributing model states across GPUs without data overlap.
   - ZeRO offers three optimization stages: ZeRO Stage 1 shards the optimizer states, ZeRO Stage 2 shards the gradients, and ZeRO Stage 3 shards all components including the model parameters.

### Comparison between DDP and FSDP
   - While DDP requires a full model copy on each GPU, leading to redundant memory consumption, FSDP eliminates this redundancy by sharding the model parameters, gradients, and optimizer states across GPUs.
   - FSDP also allows for models that are too big to fit on a single chip to be worked with.

### Performance of FSDP
   - FSDP performance is comparable to DDP for models up to 2.28 billion parameters.
   - For larger models, DDP runs into out-of-memory errors while FSDP can handle them easily.
   - As the model size increases and is distributed across more GPUs, the increase in communication volume starts to impact performance.

### Conclusion
   - FSDP can be used for both small and large models and allows seamless scaling of model training across multiple GPUs.
   - Researchers are exploring ways to achieve better performance with smaller models due to the expense and technical complexity of training models across GPUs.

# Scaling laws and compute-optimal models

### Compute Budget
   - A unit of compute that quantifies the required resources is defined as a petaFLOP per second day.
   - This measure is approximately equivalent to eight NVIDIA V100 GPUs operating at full efficiency for one full day.
   - Larger models require more compute resources to train and generally also require more data to achieve good performance.

### Trade-offs in Model Training
   - Researchers have explored the trade-offs between training dataset size, model size, and compute budget.
   - There are well-defined relationships between these three scaling choices, which can be approximated by a power-law relationship.

### Impact of Training Dataset Size and Model Size on Performance
   - As the volume of training data increases, the performance of the model continues to improve.
   - As the model increases in size, the test loss decreases indicating better performance.

### Finding the Optimal Balance
   - A detailed study was carried out to find the optimal number of parameters and volume of training data for a given compute budget.
   - The resulting compute-optimal model was named Chinchilla.
   - The Chinchilla paper suggests that many large language models may actually be over-parameterized and under-trained.

### Chinchilla Optimal Model
   - The optimal training dataset size for a given model is about 20 times larger than the number of parameters in the model.
   - The compute-optimal Chinchilla model outperforms non-compute-optimal models such as GPT-3 on a large range of downstream evaluation tasks.
   
### Future Trends
   - Teams have recently started to develop smaller models that achieved similar, if not better results than larger models that were trained in a non-optimal way.
   - Expect to see a deviation from the "bigger is always better" trend as more teams or developers start to optimize their model design.


# Domain Adaptation

   - Certain domains like law and medicine use specific terminology not commonly found in everyday language.
   - Existing Large Language Models (LLMs) may struggle with such terms due to their rarity in training texts.
   - Pretraining your model from scratch can result in better models for highly specialized domains like law, medicine, finance, or science.

### BloombergGPT: A Domain-Specific LLM
   - This model, announced in 2023 by Bloomberg, is an example of an LLM pretrained for a specific domain, finance.
   - The researchers combined both finance data and general-purpose text data to pretrain a model that achieves best-in-class results on financial benchmarks while also maintaining competitive performance on general-purpose LLM benchmarks.

### Adherence to Chinchilla Scaling Laws
   - The researchers used the Chinchilla scaling laws as guidance and made trade-offs where necessary.
   - In terms of model size, BloombergGPT roughly follows the Chinchilla approach for the given compute budget.
   - However, the actual number of tokens used to pretrain BloombergGPT was below the recommended Chinchilla value due to the limited availability of financial domain data.

## Conclusion

 - In this module, you learned about:

- Common use cases for LLMs such as essay writing, dialogue summarization, and translation.
- Detailed presentation of the transformer architecture that powers these models.
- Parameters you can use at inference time to influence the model's output.
- An introduction to a generative AI project lifecycle.
- The initial training phase called pretraining and computational challenges associated with it.
- Discussion of scaling laws discovered for LLMs and how they can be used to design compute-optimal models.

# BloombergGPT: A Domain-Specific Large Language Model

BloombergGPT, developed by Bloomberg, is a large Decoder-only language model. It was pretrained using an extensive financial dataset that included news articles, reports, and market data. This comprehensive training helped the model to understand finance better and generate finance-related natural language text.

### Training Guided by Chinchilla Scaling Laws

During the training of BloombergGPT, the authors used the Chinchilla Scaling Laws to guide them in determining the number of parameters in the model and the volume of training data (measured in tokens). The Chinchilla recommendations are represented by the lines labeled as Chinchilla-1, Chinchilla-2, and Chinchilla-3 in the graph. As can be observed, BloombergGPT aligns closely with these recommendations.

The Chinchilla Scaling Laws suggested a configuration for the team's available training compute budget of 50 billion parameters and 1.4 trillion tokens. However, gathering 1.4 trillion tokens of training data in the finance domain proved to be a significant challenge.

### Real-world Constraints and Trade-offs

Due to the difficulty in acquiring sufficient financial domain data, the team could only construct a dataset containing 700 billion tokens, which is less than the compute-optimal value recommended by the Chinchilla Scaling Laws. Moreover, due to early stopping, the training process terminated after processing just 569 billion tokens.

This example of the BloombergGPT project highlights the practical challenges that may force developers to make trade-offs against compute-optimal model and training configurations when pretraining a model for increased domain-specificity.