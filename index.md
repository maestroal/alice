## Alice the AI.
Created to train algorithms and logic in developing AI, and helping someone in practicing their pronunciation in English is the main goal in making this all.

## Installing
Need >=python3.5 and pip 20.0.2(iam use it)
```markdown
pip install alice-ai
```
## Run the ALice AI with python file
```python
import alice-ai

# this is default settings
ENGINE = alice-ai.engine()
ENGINE.start()

# use this for advanced settings
AI_NAME = "Alice" # name robot default, change this with your robot names
MASTER_NAME = "Maestro Alvardo" # change with your name
ENGINE = alice-ai.engine()
ENGINE.start(
  AI_NAME,
  MASTER_NAME
)
```

## Run the Alice AI with console
```bash
# this is for run with default settings
alice --start

# use this for advance settings
alice --startwith --ainame Alice --mastername Maestro

```


## @Developed by Maestro Alvardo
