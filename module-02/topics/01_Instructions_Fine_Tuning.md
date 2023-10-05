
# Week2 
This week's course focuses on instruction tuning and fine-tuning of large language models. It discusses how initial pretraining encodes valuable information about the world, but may not enable the model to respond appropriately to prompts or tasks. Instruction fine-tuning helps modify the model's behavior to be more helpful. It is considered a major breakthrough in large language models as it allows a model trained on vast amounts of internet text to follow instructions using a smaller dataset.

However, a challenge lies in avoiding 'catastrophic forgetting', where the model forgets previously learned data during instruction fine-tuning. The course will detail techniques to combat this, including fine-tuning across diverse instruction types.

The discussion also covers two important types of fine-tuning: instruction fine-tuning and application-specific fine-tuning by developers. Application-specific fine-tuning can be compute and memory intensive due to the need to adjust every parameter in the model. Parameter Efficient Fine-Tuning (PEFT) offers a solution by enabling similar performance results with less memory footprint.

The technique of Layer-wise Relevance Propagation (LoRA) is highlighted for its effectiveness and demand. This method allows excellent performance with minimal compute and memory requirements. Developers often begin with prompting and move to fine-tuning with LoRA or other PEFT techniques when higher performance is needed.

Lastly, the cost and size of models are discussed as critical factors, especially for those who are cost-conscious and need control over their data.

# Instruction Fine Tuning

Fine-tuning an LLM with instruction prompts is a useful method to enhance its task execution. However, the one-shot or few-shot inference strategy, which includes one or more examples of what the model should do, has some limitations. It may not always work for smaller models, and it uses valuable space in the context window. 

A solution to these limitations is fine-tuning, a process that trains a base model further. Unlike pre-training, which uses unstructured textual data, fine-tuning is a supervised learning process that uses a dataset of labeled examples to update the weights of the LLM. One particular strategy, known as instruction fine-tuning, is effective at improving a model's performance across various tasks. 

Instruction fine-tuning, where all of the model's weights are updated, is known as full fine-tuning. This process results in a new version of the model with updated weights. However, like pre-training, it requires sufficient memory and compute resources.

**Preparing Training Data for Instruction Fine-Tuning**

To carry out instruction fine-tuning, the first step is to prepare your training data. You can use publicly available datasets or prompt template libraries to create instruction prompt datasets for fine-tuning. Once the instruction dataset is ready, it's divided into training, validation, and test splits.

**Fine-Tuning Process**

During fine-tuning, prompts from the training dataset are passed to the LLM, which generates completions. These are then compared with the responses specified in the training data. The output of an LLM is a probability distribution across tokens, and this distribution can be compared with that of the training label to calculate loss. This calculated loss is then used to update the model weights over several epochs until the model's performance improves.

**Evaluation Steps**

As in standard supervised learning, separate evaluation steps are defined to measure the LLM's performance using the holdout validation dataset. After fine-tuning, a final performance evaluation is performed using the holdout test dataset. 

**Outcome of Fine-Tuning**

The result of the fine-tuning process is an improved version of the base model, often referred to as an instruct model. Nowadays, fine-tuning with instruction prompts is the most common way to fine-tune LLMs.

# Fine-Tuning for Single Task

Large language models (LLMs) are known for their ability to perform various language tasks. However, if your application requires only a single task, you can fine-tune a pre-trained model to improve performance on that specific task. This process can yield good results with relatively few examples (500-1,000), in contrast to the billions of texts used during pre-training.

**Catastrophic Forgetting**

A potential downside to fine-tuning on a single task is catastrophic forgetting. This phenomenon occurs when the full fine-tuning process modifies the weights of the original LLM, leading to excellent performance on the single fine-tuning task but degrading performance on other tasks. 

**Approaches to Avoid Catastrophic Forgetting**

If you need the model to maintain its multitask generalization capabilities, there are ways to avoid catastrophic forgetting:

1. **Multitask Fine-Tuning**: This approach involves fine-tuning on multiple tasks at once. It may require 50-100,000 examples across many tasks and more data and compute resources to train.

2. **Parameter Efficient Fine-Tuning (PEFT)**: Instead of full fine-tuning, PEFT preserves the weights of the original LLM and trains only a small number of task-specific adapter layers and parameters. This technique shows greater robustness to catastrophic forgetting since most of the pre-trained weights remain unchanged.

## Multi-task instruction fine-tuning

Multitask fine-tuning is an elaboration of single task fine-tuning. In this method, the training dataset includes example inputs and outputs for multiple tasks. Training the model on this mixed dataset enhances its performance on all tasks simultaneously, thereby avoiding catastrophic forgetting.

**FLAN Family of Models**

One example of models trained using multitask instruction fine-tuning is the FLAN family of models. FLAN, standing for Fine-tuned Language Net, is a specific set of instructions used to fine-tune different models. Variants like FLAN-T5 or FLAN-PALM are fine-tuned versions of their respective foundation models. For instance, FLAN-T5 has been fine-tuned on 473 datasets across 146 task categories.

**SAMSum Dataset**

One example of a prompt dataset used for summarization tasks in FLAN-T5 is SAMSum. It's a dataset with 16,000 messenger-like conversations with summaries, crafted by linguists to generate a high-quality training dataset for language models. The linguists created conversations similar to those they would write daily, reflecting the proportion of topics of their real-life messenger conversations. Short summaries of those conversations were then generated, including important pieces of information and names of the people in the dialogue.

**Fine-Tuning for Specific Use Cases**

While FLAN-T5 is a great general-purpose model showing good capability in many tasks, you may still find room for improvement on tasks for your specific use case. For instance, if you're building an app to support your customer service team process requests received through a chatbot, you can perform additional fine-tuning of the FLAN-T5 model using a dialogue dataset that closely matches the conversations happening with your bot.

**DialogSum Dataset**

An additional domain-specific summarization dataset called DialogSum can be used to improve FLAN-T5's ability to summarize support chat conversations. This dataset consists of over 13,000 support chat dialogues and summaries. Fine-tuning on this dataset can help the model generate better summaries that include all important details and avoid fabricating information.

**Using Internal Data for Fine-Tuning**

In practice, you'll get the most out of fine-tuning by using your company's own internal data. For example, the support chat conversations from your customer support application. This will help the model learn the specifics of how your company likes to summarize conversations and what is most useful to your customer service colleagues.

### Model evaluation

Evaluating the performance of large language models can be challenging due to their non-deterministic and language-based outputs. However, several metrics have been developed for this purpose.

**ROUGE and BLEU Metrics**

Two widely used evaluation metrics are ROUGE (Recall Oriented Understudy for Gisting Evaluation) and BLEU (Bilingual Evaluation Understudy). ROUGE is primarily used to assess the quality of automatically generated summaries by comparing them to human-generated reference summaries. BLEU is an algorithm designed to evaluate the quality of machine-translated text by comparing it to human-generated translations.

In these metrics, a unigram refers to a single word, a bigram is two words, and an n-gram is a group of n words.

**ROUGE-1 Metric**

The ROUGE-1 metric calculates recall, precision, and F1 score based on the number of words or unigrams that match between the reference and the generated output. These metrics don't consider the ordering of the words and can be deceptive.

**ROUGE-2 and Rouge-L Score**

By considering bigrams or collections of two words at a time from the reference and generated sentence, we can calculate a ROUGE-2 score. This acknowledges the ordering of the words in the sentence in a very simple way. 

Another approach uses the longest common subsequence present in both the generated output and the reference output to calculate the recall, precision, and F1 score. This is known as the Rouge-L score.

However, all of these scores need to be taken in context and are only comparable if they were determined for the same task.

**BLEU Score**

The BLEU score quantifies the quality of a translation by checking how many n-grams in the machine-generated translation match those in the reference translation. The score is calculated using the average precision over multiple n-gram sizes.

### Evaluation Benchmarks

To measure and compare Large Language Models (LLMs) more comprehensively, researchers use pre-existing datasets and associated benchmarks. The selection of the right evaluation dataset is crucial to accurately assess an LLM's performance and understand its true capabilities.

**GLUE and SuperGLUE**

Two such benchmarks are GLUE (General Language Understanding Evaluation) and SuperGLUE. Introduced in 2018, GLUE is a collection of natural language tasks like sentiment analysis and question-answering, encouraging the development of models that can generalize across multiple tasks. SuperGLUE, introduced as a successor to GLUE in 2019, addresses limitations in GLUE and includes tasks such as multi-sentence reasoning and reading comprehension. Both these benchmarks have leaderboards for comparing evaluated models.

**MMLU and BIG-bench**

Two recent benchmarks pushing LLMs further are Massive Multitask Language Understanding (MMLU) and BIG-bench. MMLU is designed specifically for modern LLMs and tests them on elementary mathematics, US history, computer science, law, etc. BIG-bench consists of 204 tasks ranging through linguistics, childhood development, math, common sense reasoning, biology, physics, social bias, software development and more.

**HELM**

The Holistic Evaluation of Language Models (HELM) framework aims to improve model transparency and offer guidance on which models perform well for specific tasks. HELM measures seven metrics across 16 core scenarios, including metrics for fairness, bias, and toxicity, which are increasingly important to assess as LLMs become more capable of human-like language generation. HELM is a living benchmark that continuously evolves with the addition of new scenarios, metrics, and models.

