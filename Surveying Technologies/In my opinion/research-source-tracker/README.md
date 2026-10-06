# research-source-tracker (วิธีใช้)

Skill นี้ทำให้ Claude ทำ 2 อย่างทุกครั้งที่ค้นข้อมูล อ่าน PDF หรือสรุปเพื่อมาปรึกษากับคุณ

1. อ่าน PDF แบบระบุเลขหน้าได้ถูกต้อง (ค้นคำ → เปิดเฉพาะหน้าที่เกี่ยวข้อง)
2. สรุปลง Excel ชื่อ `Research_Sources.xlsx` ในโฟลเดอร์โปรเจกต์ ประกอบด้วย 3 ชีต
   - **Summary**: สรุปรายหัวข้อ ประเด็นสำคัญ ข้อสงสัย และรหัสแหล่งที่มา
   - **Sources**: ทุกแหล่งที่ใช้ พร้อมลิงก์ หน้า/หัวข้อ ข้อมูลที่นำมาใช้ คำค้น และระดับความน่าเชื่อถือ
   - **Search Log**: คำค้นที่ลอง ค้นที่ไหน ได้อะไรกลับมา

## ระดับความน่าเชื่อถือ (สีในคอลัมน์ Reliability)

| ค่า | ความหมาย |
|---|---|
| Verified - opened (เขียว) | เปิดอ่านจริงแล้ว |
| Snippet only (เหลือง) | เห็นแค่ข้อความตัวอย่างในผลค้นหา ยังไม่ได้เปิดอ่าน |
| From memory - verify (ส้ม) | มาจากความรู้ของ Claude ไม่มีแหล่งเปิดอ่าน ต้องตรวจสอบเองด้วยคำค้นที่ให้ไว้ |
| Unverified (เทา) | อื่นๆ ที่ยังไม่ยืนยัน |

## ไฟล์ในโฟลเดอร์

```
research-source-tracker/
├── SKILL.md                       คำสั่งหลักที่ Claude อ่าน
├── README.md                      ไฟล์นี้ (สำหรับคุณ)
├── scripts/
│   ├── read_pdf.py                อ่าน/ค้น/ดึงหน้า PDF (info, outline, search, extract, render)
│   └── build_sources_xlsx.py      สร้างหรือต่อท้าย Research_Sources.xlsx
├── references/
│   ├── pdf-reading.md             วิธีอ่าน PDF แต่ละแบบ และเรื่องเลขหน้าไม่ตรงกัน
│   ├── source-record-guide.md     อธิบายทุกช่องในตารางแหล่งอ้างอิง
│   └── search-keys.md             วิธีเขียนคำค้นสำหรับ Google Scholar, ResearchGate ฯลฯ
└── assets/
    └── example_input.json         ตัวอย่างข้อมูลที่ใส่เข้า Excel
```

## เปิดใช้งาน

- ใน Claude Code: วางโฟลเดอร์ `research-source-tracker` ไว้ใน `.claude/skills/` ของโปรเจกต์ หรือ `~/.claude/skills/`
- ใน Claude.ai: บีบอัดโฟลเดอร์นี้เป็น .zip แล้วอัปโหลดที่ Settings → Skills (ถ้าองค์กรอนุญาต)

ต้องมี Python กับไลบรารี `pypdf` และ `openpyxl` (แนะนำให้มี `poppler-utils` สำหรับ `pdftotext`, `pdftoppm` ด้วย)
