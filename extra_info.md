# Implementation changes

- I dropped the AMS and Linear approx ways of FDA because the LoRA adapter is already small but it can be tested for larger adapters although I am hesitant
- The code base is an expansion of Theologitis' FDA-Opt reposatory for the paper FDA-Opt. It uses hugging face's which is the research standard used in various PEFT methods
- While testing various alternations of the FDA with LoRA it seemsed hard to train both matrices at the sametime thus RoLoRA was attemtped. Specifically the single row training category of FL LoRA methods was tried
- The experiments are conducted on the ARIS HPC center
- The EMA and SMA of dual track was introduced because the original FDA assumes asteady convergance while LoRA adapters are more unstable and we need a way to introduce something more robust than what FDA originally did (which was just a simple idea, nothing to sophisticated)
- There was almost completely lack of code (aside from FDA) therefore everything had to be reimplemented based on their theory