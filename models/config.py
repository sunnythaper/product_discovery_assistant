from pydantic import BaseModel, FilePath


class Config(BaseModel):
    llm_model: str = 'llama3'
    print_stream: bool = True
    prompts_dir: FilePath = 'prompts'
    prompts_extension: str = 'md'
