The growing use of artificial intelligence has sparked major security concerns about code produced by large language models (LLMs). 

This paper examines weaknesses in LLM-generated code, focusing on the Llama 3 model. While these systems can speed up software development, our initial tests uncovered serious vulnerabilities (such as SQL injection, cross-site scripting , and buffer overflows) appearing across multiple programming languages. 

To address this, we fine-tuned Llama 3 with examples of secure coding practices and then built a simple "insecure code detector" with the goal of spotting those specific issues. 

Findings show that fine-tuning lowered the frequency of some vulnerabilities but did not remove them entirely. The detector, however, was effective at catching remaining problems, especially when used alongside the fine-tuned model. 

Overall, the study shows the need for stronger fine-tuning and more effective vulnerability detection, and calls for continued work on integrating security measures directly into LLMs to better protect AI-generated code.
