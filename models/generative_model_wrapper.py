import vertexai
from vertexai.generative_models import GenerativeModel

class GenerativeModelWrapper:
    def __init__(self, system_instruction, model_id='gemini-1.5-flash'):
        self.model_id = model_id
        self.system_instruction = system_instruction
        self.model = GenerativeModel(model_id)

    def generate_content(self, contents, generation_config=None):
        response = self.model.generate_content(
            contents=contents,
            generation_config=generation_config
        )
        return response.text
