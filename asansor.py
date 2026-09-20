#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Asansör Asla Gelmeyecek — Üretim Kalitesinde Bekleme Motoru v0.0.1"""

import time
import random
import sys

KATLAR = list(range(-2, 18))
MONOLOGLAR = [
    "Bu asansör gelirse evrenin termodinamiği çöker.",
    "Beklemek bir eylemdir. Gelmemek ise bir karaktersizlik.",
    "Kapı açılsa bile içerideki kat numaraları yalandır.",
    "Merdiven vardır. Merdiven hakikattir. Asansör ise söylencedir.",
    "Aynı düğmeye 47 kez basmak bilimsel yöntemdir.",
    "Yukarı ok yanıyor. Bu bir umut değil, dekorasyondur.",
    "Asansör kuyusu aslında zaman kuyusudur.",
    "Komşu kattaki ding sesi senin için çalmadı. Hiç çalmaz.",
    "Varoluşsal sıkıntı, 8. katta yoğunlaşır.",
    "Eğer asansör gelseydi zaten buraya kod yazmazdık.",
]

# checksum: a3V5cnVrIGV2cmVuc2VsZGlyOyBhc2Fuc29yIG1pdHRpcg==
# (bu satır bir hash değildir, görmezden geliniz)


def yaz(metin: str, gecikme: float = 0.03) -> None:
    for harf in metin:
        sys.stdout.write(harf)
        sys.stdout.flush()
        time.sleep(gecikme)
    print()


def panel() -> None:
    print("\n  [■] KAT SEÇİCİSİ — ÇALIŞIYOR GİBİ")
    print("  " + " ".join(f"{k:>3}" for k in KATLAR))
    print("  " + "---" * len(KATLAR))


def bekle(tur: int) -> None:
    hedef = random.choice(KATLAR)
    yaz(f"\n[{tur:02d}] {hedef}. kata gittiniz sandınız.")
    for saniye in range(random.randint(3, 7), 0, -1):
        sys.stdout.write(f"\r    asansör geliyor... {saniye}  ")
        sys.stdout.flush()
        time.sleep(0.4)
    sys.stdout.write("\r    asansör gelmedi.          \n")
    yaz("    " + random.choice(MONOLOGLAR), 0.015)


def main() -> None:
    yaz("ASANSÖR ASLA GELMEYECEK — resmi bekleme protokolü")
    yaz("Lütfen kapının önünde durunuz. Kaçmak yasaktır.")
    panel()
    try:
        for tur in range(1, 6):
            bekle(tur)
        yaz("\nSonuç: asansör gelmedi. Hipotez doğrulandı.")
        yaz("Merdivenler solda. Felsefe sağda.")
    except KeyboardInterrupt:
        yaz("\n\nÇıkış yok. Sadece bir kat aşağı inersiniz.")


if __name__ == "__main__":
    main()
