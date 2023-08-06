# -*- coding: utf-8 -*-

# Copyright 2019 Mike Fährmann
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 2 as
# published by the Free Software Foundation.

"""Extractors for https://hentaifox.com/"""

from .common import ChapterExtractor, Extractor, Message
from .. import text


class HentaifoxGalleryExtractor(ChapterExtractor):
    """Extractor for image galleries on hentaifox.com"""
    category = "hentaifox"
    subcategory = "gallery"
    filename_fmt = "{category}_{gallery_id}_{page:>03}.{extension}"
    directory_fmt = ["{category}", "{gallery_id} {title}"]
    archive_fmt = "{gallery_id}_{page}"
    pattern = [r"(?:https?://)?(?:www\.)?hentaifox\.com/gallery/(\d+)"]
    test = [("https://hentaifox.com/gallery/56622/", {
        "pattern": r"https://i\d*\.hentaifox\.com/\d+/\d+/\d+\.jpg",
        "count": 24,
        "keyword": "80fc0fb5db9626fffb078dd2e4f9aff4a9348686",
    })]
    root = "https://hentaifox.com"

    def __init__(self, match):
        self.gallery_id = match.group(1)
        url = "{}/gallery/{}".format(self.root, self.gallery_id)
        ChapterExtractor.__init__(self, url)

    def get_metadata(self, page):
        title, pos = text.extract(page, "<h1>", "</h1>")
        data = text.extract_all(page, (
            ("parodies"  , ">Parodies:"  , "</a></span>"),
            ("characters", ">Characters:", "</a></span>"),
            ("tags"      , ">Tags:"      , "</a></span>"),
            ("artist"    , ">Artists:"   , "</a></span>"),
            ("group"     , ">Groups:"    , "</a></span>"),
            ("type"      , ">Category:"  , "</a></span>"),
        ), pos)[0]

        for key, value in data.items():
            data[key] = text.remove_html(value).replace(" , ", ", ")
        data["gallery_id"] = text.parse_int(self.gallery_id)
        data["title"] = text.unescape(title)
        data["language"] = "English"
        data["lang"] = "en"
        return data

    def get_images(self, page):
        return [
            (text.urljoin(self.root, url.replace("t.", ".")), None)
            for url in text.extract_iter(page, 'data-src="', '"')
        ]


class HentaifoxSearchExtractor(Extractor):
    """Extractor for search results and listings on hentaifox.com"""
    category = "hentaifox"
    subcategory = "search"
    pattern = [r"(?:https?://)?(?:www\.)?hentaifox\.com"
               r"(/(?:parody|tag|artist|character|search)/[^/?%#]+)"]
    test = [
        ("https://hentaifox.com/parody/touhou-project/", None),
        ("https://hentaifox.com/tag/full-color/", None),
        ("https://hentaifox.com/character/reimu-hakurei/", None),
        ("https://hentaifox.com/artist/distance/", None),
        ("https://hentaifox.com/search/touhou/", None,),
        ("https://hentaifox.com/tag/full-colour/", {
            "pattern": HentaifoxGalleryExtractor.pattern[0],
            "count": ">= 40",
            "keyword": {
                "url": str,
                "gallery_id": int,
                "thumbnail": r"re:https://i\d*.hentaifox.com/\d+/\d+/thumb\.",
                "title": str,
                "tags": list,
            },
        }),
    ]
    root = "https://hentaifox.com"

    def __init__(self, match):
        Extractor.__init__(self)
        self.path = match.group(1)

    def items(self):
        yield Message.Version, 1
        for gallery in self.galleries():
            yield Message.Queue, gallery["url"], gallery

    def galleries(self):
        url = "{}/{}/".format(self.root, self.path)

        while True:
            page = self.request(url).text
            info, gpos = text.extract(
                page, 'class="galleries_overview">', 'class="clear">')

            for ginfo in text.extract_iter(info, '<div class="item', '</a>'):
                tags , pos = text.extract(ginfo, '', '"')
                url  , pos = text.extract(ginfo, 'href="', '"', pos)
                title, pos = text.extract(ginfo, 'alt="', '"', pos)
                thumb, pos = text.extract(ginfo, 'src="', '"', pos)

                yield {
                    "url": text.urljoin(self.root, url),
                    "gallery_id": text.parse_int(
                        url.strip("/").rpartition("/")[2]),
                    "thumbnail": text.urljoin(self.root, thumb),
                    "title": text.unescape(title),
                    "tags": tags.split(),
                }

            pos = page.find('class="current"', gpos)
            url = text.extract(page, 'href="', '"', pos)[0]
            if pos == -1 or "/pag" not in url:
                return
            url = text.urljoin(self.root, url)
