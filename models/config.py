from pydantic import BaseModel, FilePath


class Config(BaseModel):
    llm_model: str = 'llama3'
    print_stream: bool = False
    prompts_dir: FilePath = 'prompts'
    prompts_extension: str = 'md'
    reports_dir: FilePath = 'reports'
    reports_extension: str = 'md'
    surveys_dir: FilePath = 'surveys'
    surveys_extension: str = 'md'
