import json
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT / "data"
MANIFEST_PATH = DATA_DIR / "manifest.json"
OUTPUT_PATH = DATA_DIR / "offline-data.js"


def main():
    manifest = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
    if not isinstance(manifest.get("tools"), list):
        raise ValueError("Manifest must contain a tools list")

    tool_data = {}
    for tool in manifest["tools"]:
        tool_path = ROOT / tool["file"]
        data = json.loads(tool_path.read_text(encoding="utf-8"))
        if data.get("id") != tool["id"]:
            raise ValueError("Tool id mismatch in {}".format(tool_path))
        tool_data[tool["id"]] = data

    bundle = {"manifest": manifest, "toolData": tool_data}
    serialized = json.dumps(bundle, ensure_ascii=True, separators=(",", ":"))
    serialized = serialized.replace("<", "\\u003c")
    OUTPUT_PATH.write_text(
        "window.AIMasterclassOfflineData = {};\n".format(serialized),
        encoding="utf-8",
    )
    print("Generated {}".format(OUTPUT_PATH.relative_to(ROOT)))


if __name__ == "__main__":
    main()
