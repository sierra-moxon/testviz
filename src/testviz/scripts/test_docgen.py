from linkml.generators.docgen import DocGenerator
from pathlib import Path

yaml_path = Path("src/testviz/schema/testviz.yaml")
print(yaml_path)

gen = DocGenerator(
    yaml_path,
    directory="docs",
    template_directory="src/doc-templates",
    use_slot_uris=True,
    hierarchical_class_view=True
)
print(gen.serialize())

