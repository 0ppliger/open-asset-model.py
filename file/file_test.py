import json
import pytest
from file.file import File
from asset import Asset
from asset import AssetType

def test_file_key():
    want = "file:///var/html/index.html"
    f = File(url=want, name="index.html", type="Document")

    assert f.key == want

def test_file_asset_type():
    assert issubclass(File, Asset)  # Verify proper implementation of the Asset interface

    f = File(url="")
    expected = AssetType.File
    actual = f.asset_type

    assert actual == expected

def test_file_json():
    f = File(
        url="file:///var/html/index.html",
        name="index.html",
        type="Document",
    )
    expected = json.dumps({"url": "file:///var/html/index.html", "name": "index.html", "type": "Document"})
    actual = f.to_json()

    assert actual == expected
