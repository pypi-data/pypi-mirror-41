import typing

import markdown
import yaml


class FullYamlMetadataExtension(markdown.Extension):
    """Extension for parsing YAML metadata part with Python-Markdown."""
    def extendMarkdown(self, md: markdown.Markdown, md_globals: dict):
        md.Meta = None
        md.preprocessors.add(
            'full_yaml_metadata', FullYamlMetadataPreprocessor(md), '_begin')


class FullYamlMetadataPreprocessor(markdown.preprocessors.Preprocessor):
    """Preprocess markdown content with YAML metadata parsing.

    YAML block is delimited by '---' at start and '...' or '---' at end.

    """
    def run(self, lines: list) -> list:
        meta_lines, lines = self.split_by_meta_and_content(lines)

        self.markdown.Meta = yaml.load('\n'.join(meta_lines))
        return lines

    def split_by_meta_and_content(self, lines: list) -> typing.Tuple[list]:
        meta_lines = []
        if lines[0] != '---':
            return meta_lines, lines

        lines.pop(0)
        for line in lines:  # type: str
            if line in ('---', '...'):
                content_starts_at = lines.index(line) + 1
                lines = lines[content_starts_at:]
                break

            meta_lines.append(line)

        return meta_lines, lines


def makeExtension(configs: dict={}):
    return FullYamlMetadataExtension(configs=configs)
