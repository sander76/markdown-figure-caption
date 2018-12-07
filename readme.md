# Markdown Image caption.

Inspired by the probably un-maintained package [mdx_figcap](ttps://github.com/mkszk/mdx_figcap)

## Usage:

Make sure you have [markdown](https://pypi.org/project/Markdown/) installed. 

Define an image with caption in your markdown.

```markdown
![alttext](http://example.com/image.png "caption")
```

This will be converted to:

```html

<span class="img_container center" style="display: block;">
    <img alt="test" src="http://example.com/image.png" style="display:block; margin-left: auto; margin-right: auto;" title="caption" />
    <span class="img_caption" style="display: block; text-align: center;">caption</span>
</span>

<figure>
    <img alt="alttext" src="http://example.com/image.png" title="caption" />
    <figcaption>caption</figcaption>
</figure>
```

Why no figure tag implementation ?

The figure tag is a block level element. The image element is an inline element. This difference breaks the attribute extension.
So `![alttext](http://example.com/image.png "caption"){: .center}` would not work if a figure was used.

## Installation

```bash
pip install markdown-image-caption
```

add the plugin to your markdown

```python
import markdown

parser = markdown.Markdown(extensions=["markdown_image_caption.plugin"])
```