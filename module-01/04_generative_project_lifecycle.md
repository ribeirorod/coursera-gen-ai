# Generative AI Project Lifecycle

![AI Project Lifecycle](<resources/../resources/generative_ai_lifecycle.png>)


## 1. Define The Scope
The first and most crucial step in any project is defining the scope as accurately and narrowly as possible. The abilities of Language Learning Models (LLMs) depend strongly on their size and architecture. Consider what function the LLM will play in your application.

## 2. Model Selection
After scoping your requirements, decide whether to train your model from scratch or work with an existing base model. In general, starting with an existing model is recommended, but there might be cases where training a model from scratch is necessary.

## 3. Assess Performance & Additional Training
With your chosen model, assess its performance and carry out additional training if needed. Prompt engineering can sometimes be enough to get your model to perform well. However, if the model does not perform as expected, you can try fine-tuning it.

## 4. Fine-Tuning Techniques
In Week 2, you'll learn about supervised learning processes for fine-tuning your model. In Week 3, you'll learn about reinforcement learning with human feedback, which ensures that your model behaves well.

## 5. Evaluation
Evaluation is a critical aspect of all these techniques. You'll explore metrics and benchmarks that can be used to determine how well your model performs or how well aligned it is to your preferences. 

## 6. Deployment
Once the model meets your performance needs and is well-aligned, you can deploy it into your infrastructure and integrate it with your application. An important step at this stage is optimizing your model for deployment.

## 7. Additional Infrastructure
Consider any additional infrastructure that your application will require to work well. There are some fundamental limitations of LLMs that can be difficult to overcome through training alone. Towards the end of this course, you'll learn techniques to overcome these limitations.

Remember, this life cycle is highly iterative and you'll likely revisit stages multiple times to achieve the desired performance.