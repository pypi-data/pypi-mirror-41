import requests


class Document:
    """an Invoice object contains image or pdf data of an invoice and is
    typically passed to :py:class:`~las.client.Client` for scanning.
    Supported file formats are jpeg, png, gif, bmp and pdf.

    :param str url: An http or https url pointing to an invoice image or pdf.
    :param str filename: A path to a local invoice image or pdf file.
    :param typing.BinaryIO fp: A file-like python object
    :param bytes content: Binary invoice image or pdf data.

    """
    def __init__(self, url=None, filename=None, fp=None, content=None):
        if not fp and not url and not filename and not content:
            raise Exception('fp, url, filename or content must be provided')

        if url:
            self.content = requests.get(url).content
        elif filename:
            with open(filename, 'rb') as fp:
                self.content = fp.read()
        elif fp:
            self.content = fp.read()
        else:
            self.content = content
