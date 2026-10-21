"""
Membuat ulang model-data.js dari folder model/.
Jalankan dari folder utama proyek:  python tools/buat-model-data.py
Dipakai kalau Anda melatih ulang model di Teachable Machine:
ganti 3 file di folder model/, lalu jalankan skrip ini.
"""
import base64
import json

with open("model/model.json", encoding="utf-8") as f:
    model = json.load(f)
with open("model/metadata.json", encoding="utf-8") as f:
    meta = json.load(f)
with open("model/weights.bin", "rb") as f:
    weights = base64.b64encode(f.read()).decode()

with open("model-data.js", "w", encoding="utf-8") as out:
    out.write("// File ini dibuat otomatis oleh tools/buat-model-data.py. Jangan diubah.\n")
    out.write("window.MODEL_DATA = {\n")
    out.write("  metadata: " + json.dumps(meta) + ",\n")
    out.write("  modelJson: " + json.dumps(model, separators=(",", ":")) + ",\n")
    out.write('  weightsBase64: "' + weights + '"\n};\n')

print("Selesai: model-data.js dibuat.")
