from langchain_community.llms import Ollama


def get_hf_llm(
    model_name: str = "llama3.2:3b",
    **kwargs
):
    llm = Ollama(
        model=model_name,
        base_url="http://localhost:11434",
        **kwargs
    )

    return llm