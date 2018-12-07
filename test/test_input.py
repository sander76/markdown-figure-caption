import markdown
import pytest

from markdown_image_caption.plugin import FigureCaptionExtension
import markdown.extensions.attr_list

input1 = "![test](imgs/img.png)"
output1 = '<p><img alt="test" src="imgs/img.png" /></p>'

input2 = '![test](imgs/img.png "figure caption")'
output2 = '<p><span class="img_container" style="display: block;"><img alt="test" src="imgs/img.png" style="display:block; margin-left: auto; margin-right: auto;" title="figure caption" /><span class="img_caption" style="display: block; text-align: center;">figure caption</span></span></p>'

input3 = "no image here"
output3 = "<p>no image here</p>"

input4 = "![test](imgs/img.png){: .center}"
output4 = '<p><img alt="test" class="center" src="imgs/img.png" /></p>'

input5 = '![test](imgs/img.png "figure caption"){: .center}'
output5 = '<p><span class="img_container center" style="display: block;"><img alt="test" src="imgs/img.png" style="display:block; margin-left: auto; margin-right: auto;" title="figure caption" /><span class="img_caption" style="display: block; text-align: center;">figure caption</span></span></p>'


@pytest.fixture
def parser():
    return markdown.Markdown(
        extensions=[FigureCaptionExtension(), "markdown.extensions.attr_list"]
    )


def test_image(parser):
    txt = parser.convert(input1)
    print(txt)
    assert txt == output1


def test_figure(parser):
    txt = parser.convert(input2)
    print(txt)

    assert txt == output2


def test_no_image(parser):
    txt = parser.convert(input3)
    assert txt == output3


def test_image_with_attr_list(parser):
    txt = parser.convert(input4)
    print(txt)
    assert txt == output4


def test_figure_with_attr_list(parser):
    txt = parser.convert(input5)
    print(txt)
    assert txt == output5
