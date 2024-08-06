from app.db.models import ExampleModel

class ExampleService:
    def __init__(self):
        pass

    def get_all_examples(self):
        return ExampleModel.query.all()

    def get_example_by_id(self, id: int):
        return ExampleModel.query.get(id)

    def create_example(self, name: str, description: str):
        example = ExampleModel(name=name, description=description)
        return example

    def update_example(self, id: int, name: str, description: str):
        example = self.get_example_by_id(id)
        if example:
            example.name = name
            example.description = description
            return example

    def delete_example(self, id: int):
        example = self.get_example_by_id(id)
        if example:
            return example