# Reading List: ทางเลือก 1 (แบ่งตามหน้าที่ของงานสำรวจ)

รายการสิ่งที่ต้องไปหาข้อมูลเพิ่มสำหรับสไลด์ `Survey_Technology_Outline_v3.pptx` ในโฟลเดอร์นี้ แยกตามหน้าที่ 6 ข้อ แหล่งที่บันทึกแล้วอยู่ใน `Research_Sources.xlsx` (ชีต Sources, รหัส S###)

## สัญลักษณ์

- ✅ เปิดอ่านจริงแล้ว (บันทึกใน Excel)
- 📖 หนังสือ *Elementary Surveying* (ไฟล์ในโฟลเดอร์หลัก; เลขหน้าเป็นเลขที่พิมพ์ในหนังสือ; หนังสือเขียนราว 2011 ไม่มี UAV, SLAM, InSAR, multibeam)
- 🔑 ไม่มีลิงก์ที่ยืนยันได้ ให้ใช้คำค้น (ผมไม่เดาลิงก์)
- ⚠ มาจากความรู้ทั่วไปของผม ยังไม่ได้ตรวจ ต้องตรวจก่อนใช้

## หลักการค้นที่ใช้ร่วมกันทุกหน้าที่

- คำว่า "survey" ชนกับแบบสอบถาม ให้ผูกกับคำของวงการเสมอ เช่น `geomatics`, `land surveying`, `geodesy`, `photogrammetry`, `LiDAR`, `hydrographic`
- ค่าความแม่นยำที่เป็นตัวเลข: ใช้ 2 ชั้น คือ (1) บทความทบทวน/ทดสอบอิสระ (2) datasheet ผู้ผลิต โดยในตารางต้องระบุว่าเป็น "ค่าที่ผู้ผลิตระบุ"
- ต้นทุนเป็นบาท: ลองค้น 🔑 ราคากลางในระบบจัดซื้อจัดจ้างภาครัฐ (e-GP) ด้วยชื่อครุภัณฑ์ภาษาไทย เช่น `ราคากลาง กล้องสำรวจประมวลผลรวม`, `ราคากลาง เครื่องรับสัญญาณดาวเทียม GNSS`, `ราคากลาง อากาศยานไร้คนขับ สำรวจ` ⚠ (วิธีนี้ผมยังไม่ได้ทดลอง)
- ใช้ `Research_Sources.xlsx` ผ่านสกิล `research-source-tracker` ทุกครั้งที่ให้ผมค้นต่อ

---

## หน้าที่ 1: การกำหนดตำแหน่งอ้างอิง

| รายการ | มีแล้ว | ต้องหา |
|---|---|---|
| วัตถุประสงค์ | ✅ S043, S044, S045 | — |
| หลักการที่ใช้ | 📖 บทที่ 13 GNSS (p.331), 19 Control Surveys (p.529), 20 State Plane (p.589) | ✍ สรุปหลักการ: การวัดระยะจากดาวเทียม, การวัดแบบ static/kinematic, การวัดมุม-ระยะ, ผลต่างระดับ |
| เทคโนโลยีต่อหลักการ | 📖 บทที่ 14 Static (p.367), 15 Kinematic/RTK (p.399, 413) | ภาพรวมบริการ CORS/network RTK ของไทย 🔑 `เครือข่าย CORS กรมที่ดิน OR กรมแผนที่ทหาร` |
| ตารางเปรียบเทียบ | — | แถวที่แข่งกัน: static GNSS / RTK / network RTK / PPP-RTK (และ traverse ด้วย total station, leveling สำหรับแนวดิ่ง); ต้องหา: ความแม่นยำ (บทความทบทวน), ข้อจำกัด (สภาพแวดล้อม/เวลาสังเกต), ต้นทุน |
| Trend | ✅ S006 (PPP-RTK review, Li et al. 2022) | 🔎 TU Delft PPP-RTK, 🔎 FIG Commission 5 work plan 2023-2026 (เปิดอ่านจริงก่อนอ้าง) |

คำค้น
```
"PPP-RTK" OR "network RTK" review GNSS positioning
"multi-GNSS" "multi-frequency" precise positioning review
"static GNSS" OR "RTK" accuracy comparison "survey-grade" -questionnaire
"height reference frame" OR "ITRF" geodesy site:fig.net
```

## หน้าที่ 2: การวัดรายละเอียดและการถ่ายแนว

| รายการ | มีแล้ว | ต้องหา |
|---|---|---|
| วัตถุประสงค์ | ✅ S044, S045 | — |
| หลักการที่ใช้ | 📖 บทที่ 4 Leveling (p.73), 6 Distance Measurement (p.131), 8 Total Station Instruments (p.191), 17 Mapping Surveys (p.467), 23 Construction Surveys (p.685) | การวัดระยะแบบอิเล็กทรอนิกส์ (EDM), การวัดมุมดิจิทัล, การ setting-out |
| เทคโนโลยีต่อหลักการ | ✅ S042 (laser scanning, หน้า 7) | total station แบบ robotic/reflectorless, GNSS RTK, กล้องระดับดิจิทัล, SLAM scanner พกพา |
| ตารางเปรียบเทียบ | — | แถว: total station / GNSS RTK / TLS ระยะใกล้ / SLAM พกพา; ความแม่นยำ ข้อจำกัด (ทัศนวิสัย สัญญาณ) ต้นทุน |
| Trend | 🔎 FIG Commission 6 | งานทบทวน: robotic total station, SLAM, BIM-based setting-out |

คำค้น
```
"robotic total station" OR "reflectorless" accuracy review
"construction layout" OR "setting out" "total station" "GNSS" comparison
"handheld mobile laser scanning" OR "SLAM" accuracy survey review
"BIM" "setting out" construction survey review
```

## หน้าที่ 3: การเก็บข้อมูลพื้นผิวและวัตถุในพื้นที่กว้าง

| รายการ | มีแล้ว | ต้องหา |
|---|---|---|
| วัตถุประสงค์ | ✅ S042, S044, S045 | — |
| หลักการที่ใช้ | 📖 บทที่ 27 Photogrammetry (p.799) | การวางภาพ (image orientation), การวัดระยะด้วยเลเซอร์ + GNSS/IMU, เซนเซอร์สเปกตรัม/ความร้อน/ไมโครเวฟ (ISPRS I-III) |
| เทคโนโลยีต่อหลักการ | ✅ S008 (UAV photogrammetry/LiDAR review, Kovanic et al. 2023) · ✅ S014 (LiDAR SLAM survey, arXiv) | LiDAR ทางอากาศแบบมีคนขับ, ภาพถ่ายดาวเทียม (ความละเอียด ราคาต่อ กม.²) |
| ตารางเปรียบเทียบ | — | แถว: UAV photogrammetry / UAV LiDAR / LiDAR ทางอากาศ / TLS / ภาพดาวเทียม; ความแม่นยำจาก S008 + การทดสอบอิสระ; ข้อจำกัด (พืชพรรณ แสง ความลึกน้ำ เวลาประมวลผล); ต้นทุนต่อพื้นที่ |
| Trend | ✅ S001 (ISPRS commissions) | งานทบทวน: point cloud + deep learning, UAV LiDAR, 3D Gaussian splatting/NeRF ⚠ (ตรวจว่าเกี่ยวกับงานสำรวจหรือไม่) |

คำค้น
```
"UAV photogrammetry" accuracy review "ground control points"
"UAV LiDAR" accuracy "digital terrain model" vegetation review
"airborne laser scanning" cost per km2 mapping
"terrestrial laser scanning" OR "mobile mapping" review
"deep learning" "point cloud" classification survey review
```

## หน้าที่ 4: การสำรวจใต้น้ำและใต้ผิวดิน

| รายการ | มีแล้ว | ต้องหา |
|---|---|---|
| วัตถุประสงค์ | ✅ S046, S048, S049, S050 | ตัดสินขอบเขตใต้ผิวดิน (สาธารณูปโภคอย่างเดียว หรือรวมธรณีฟิสิกส์) |
| หลักการที่ใช้ | 📖 §17.13 (p.493) | หลักการ echo sounding/multibeam, ADCP, GPR, ERT (ต้องหาบทความหรือมาตรฐาน) |
| เทคโนโลยีต่อหลักการ | — | single-beam, multibeam, side-scan, ADCP, USV; GPR, EM locator |
| ตารางเปรียบเทียบ | ✅ S049 (GPR < 0.10 m ตามผลงานวิจัย) | ความแม่นยำตามมาตรฐาน IHO S-44 (ตรวจฉบับล่าสุด ⚠ หน้า listing ระบุ Ed. 6.2.0 ต.ค. 2024 แต่ยังไม่ได้เปิดตัวมาตรฐาน), ASCE 38 quality levels 🔑 |
| Trend | — | งานทบทวน: USV hydrographic survey, topo-bathymetric LiDAR, utility mapping + GPR/AI |

คำค้น
```
"multibeam echosounder" OR "unmanned surface vessel" hydrographic survey review
IHO S-44 "Standards for Hydrographic Surveys" "Exclusive Order" OR "Order 1a"
"ADCP" bathymetry river survey accuracy
"ground penetrating radar" "utility" mapping accuracy review
"ASCE 38" "quality level" subsurface utility engineering
```

## หน้าที่ 5: การติดตามการเปลี่ยนแปลง

| รายการ | มีแล้ว | ต้องหา |
|---|---|---|
| วัตถุประสงค์ | ✅ S041, S047 (§1.13 Future Challenges หน้า 19-20) | **ตัวอย่างตลิ่ง/คันดิน/การกัดเซาะ ยังไม่มีแหล่ง** |
| หลักการที่ใช้ | ✅ S011 (InSAR hydropower review, Aswathi et al. 2022) | หลักการ deformation monitoring (วัดซ้ำ, ระบบอ้างอิงเสถียร, การวิเคราะห์ทางสถิติ) 📖 บทที่ 16 Adjustments by Least Squares (p.421) |
| เทคโนโลยีต่อหลักการ | — | robotic total station + prism, GNSS ต่อเนื่อง, TLS/UAV วัดซ้ำ, InSAR, ground-based radar |
| ตารางเปรียบเทียบ | — | แถว: robotic total station / GNSS ต่อเนื่อง / วัดซ้ำด้วย UAV-TLS / InSAR; ความแม่นยำระดับ มม.-ซม. ของแต่ละวิธี ต้องหาจากบทความทบทวน |
| Trend | ✅ S002 (FIG C6 + WG 6.1-6.4) | 🔎 FIG WG 6.1 Deformation Monitoring and Analysis (หน้าเว็บไม่มีรายละเอียด; หา publications/proceedings), งานทบทวน digital twin เพื่อ monitoring |

คำค้น
```
"deformation monitoring" geodetic OR geomatics review dam OR embankment
"riverbank erosion" monitoring UAV OR LiDAR OR "terrestrial laser scanning" review
InSAR "ground subsidence" OR "dam" monitoring review
"structural health monitoring" "GNSS" OR "robotic total station" review
site:fig.net "deformation" working group 6.1
```

## หน้าที่ 6: การจัดการและวิเคราะห์ข้อมูลเชิงพื้นที่

| รายการ | มีแล้ว | ต้องหา |
|---|---|---|
| วัตถุประสงค์ + หลักการ | ✅ S030, S031, S032 | — |
| เทคโนโลยี/ตาราง | ✅ S033 (QGIS), S034, S035 (ราคา ArcGIS Pro รัฐอินเดียนา), S036, S037 | ราคา ArcGIS Pro ในไทย 🔑 `Esri Thailand ArcGIS Pro price`; PostGIS 🔑 `PostGIS spatial database`; ต้นทุนคลาวด์ 🔑 `cloud object storage price per TB month`; เทียบประสิทธิภาพ 🔑 `QGIS ArcGIS Pro benchmark large dataset performance` |
| Trend | ✅ S038, S039 (อ่านเฉพาะบทคัดย่อ) | 🔎 S040 (arXiv 2412.11643: เห็นแค่ชื่อ), งานทบทวน GeoAI/cloud-native |

คำค้น
```
"GeoAI" review "geo-foundation model"
"cloud-native geospatial" COG OR GeoParquet OR STAC review
"spatial data infrastructure" review site:fig.net OR site:isprs.org
```

---

## สิ่งที่ยังไม่ตัดสินใจ (จากการคุย)

- ขอบเขตใต้ผิวดินในหน้าที่ 4
- ทำเมทริกซ์เทคโนโลยี × หน้าที่ (สไลด์ 34) ต่อหรือไม่
