"""
Image Caption Extension for Python-Markdown
==================================
Converts \![alttext](http://example.com/image.png "caption")
to the image with a caption.
Its syntax is same as embedding images.
License: [BSD](http://www.opensource.org/licenses/bsd-license.php)
"""


from markdown.extensions import Extension
from markdown.inlinepatterns import IMAGE_LINK_RE
from markdown.util import etree
from markdown.inlinepatterns import ImageInlineProcessor


class FigureCaptionExtension(Extension):
    def extendMarkdown(self, md):
        # append to inline patterns
        md.inlinePatterns["image_link"] = FigureCaptionPattern(
            IMAGE_LINK_RE, md
        )


class FigureCaptionPattern(ImageInlineProcessor):
    def handleMatch(self, m, data):
        image, start, index = super().handleMatch(m, data)
        if image is None:
            return image, start, index
        title = image.get("title")
        if title:
            image.set(
                "style",
                "display:block; margin-left: auto; margin-right: auto;",
            )

            container = etree.Element(
                "span",
                attrib={"style": "display: block;", "class": "img_container"},
            )

            container.append(image)
            etree.SubElement(
                container,
                "span",
                attrib={
                    "class": "img_caption",
                    "style": "display: block; text-align: center;",
                },
            ).text = title
            return container, start, index
        else:
            return image, start, index


def makeExtension(*args, **kwargs):
    return FigureCaptionExtension(*args, **kwargs)
