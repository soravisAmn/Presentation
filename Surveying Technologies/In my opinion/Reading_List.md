# Reading List: เทคโนโลยีสำหรับงานสำรวจวิศวกรรม (แผนที่วงการ + 6 ด้าน)

รายการสำหรับไปหาอ่านเอง แยกตามด้านและหัวข้อ (วัตถุประสงค์ / หลักการคิด / เทคโนโลยี / trend) แหล่งที่มาทั้งหมดบันทึกใน `Research_Sources.xlsx` (ชีต Sources, อ้างด้วยรหัส S###)

## อ่านก่อน: "6 ด้าน" คืออะไร

6 ด้านนี้เป็น **การจัดกลุ่มเพื่อการนำเสนอที่ผมทำขึ้นเอง ไม่ใช่มาตรฐานที่ใครประกาศ** ในสไลด์ควรเขียนว่าเป็นการจัดกลุ่มของผู้นำเสนอ แล้วอ้างอิงกรอบที่มีอยู่จริงมาเทียบ:

| ด้านในสไลด์ | เทียบกับ FIG (10 Commissions) | เทียบกับ ISPRS (Technical Commissions) |
|---|---|---|
| 1 Positioning & Geodetic Control | Commission 5 Positioning and Measurement | (ไม่เห็นหัวข้อนี้ตรง ๆ ในขอบเขต commission ที่เปิดอ่าน) |
| 2 Terrestrial & Optical Surveying | Commission 5, Commission 6 Engineering Surveys | I Sensor Systems (บางส่วน) |
| 3 Remote Sensing & Photogrammetry | (ครอบคลุมบางส่วนใน Commission 3, 6) | II Photogrammetry, III Remote Sensing |
| 4 Hydrographic & Subsurface | Commission 4 Hydrography | III (hydrosphere) บางส่วน |
| 5 Data Processing, GIS & Modeling | Commission 3 Spatial Information Management | IV Spatial Information Science |
| 6 Integration, Automation & Emerging Tech | Commission 6 (WG immersive technologies, dynamic monitoring) | I Sensor Systems (mobile mapping), IV (digital twins) |

การเทียบนี้เป็นการตีความของผม ตรวจสอบกับหน้าต้นทางด้านล่างก่อนใช้

## สัญลักษณ์ระดับความน่าเชื่อถือ

- ✅ **เปิดอ่านจริงแล้ว** (อ่านข้อความในหน้านั้นแล้ว)
- 🔎 **เห็นแค่ชื่อ/ข้อความตัวอย่างในผลค้นหา** ยังไม่ได้เปิดอ่าน ต้องเปิดเองก่อนอ้างตัวเลข
- 🔑 **ไม่มีลิงก์ที่ยืนยันได้** ให้ใช้คำค้นแทน (ผมไม่เดาลิงก์)

## ภาคนำ: แผนที่วงการ (Field Map)

สไลด์ภาคนำ 4 หน้า (นิยาม / 3 มุมมองการแบ่ง / FIG และ ISPRS / เทคโนโลยีหลัก) แล้วตามด้วยหน้าเชื่อมไปสู่ 6 ด้าน แหล่งที่เปิดอ่านแล้วทั้งหมด:

| หัวข้อสไลด์ | อ่านอะไร |
|---|---|
| นิยามและขอบเขต | ✅ หนังสือ §1.1-1.2 หน้า 1-4 (surveying = geomatics; นิยาม 11 หน้าที่ของ surveyor ตาม FIG หน้า 2) · ✅ [Geomatics (Wikipedia)](https://en.wikipedia.org/wiki/Geomatics) (แหล่งรอง; นิยาม ISO/TC 211) |
| วงการถูกแบ่งอย่างไร (3 มุมมอง) | ✅ หนังสือ §1.6 หน้า 11-12 (ตามวัตถุประสงค์งาน และตามแพลตฟอร์ม ground/aerial/satellite) · ✅ หนังสือ §1.4 หน้า 9-10 (geodetic vs plane) · ✅ [Surveying (Wikipedia)](https://en.wikipedia.org/wiki/Surveying) (แหล่งรอง; รายการประเภทงานคล้ายกัน) |
| กรอบขององค์กร | ✅ [About FIG: 10 commissions พร้อมขอบเขต](https://fig.net/about/index.asp) · ✅ [ISPRS Commissions](https://www2.isprs.org/commissions/) |
| เทคโนโลยีหลักของวงการ | ✅ หนังสือ §1.3 หน้า 7-8 (เครื่องมือเดิมถูกแทนที่ด้วย total station, GNSS, laser scanning, digital photogrammetry, mobile mapping) · ✅ หนังสือ §1.8 หน้า 14-15 (GIS/LIS) · Trend ล่าสุดดูรายด้านด้านล่าง เพราะหนังสือเขียนราว 2011 |
| จากแผนที่วงการสู่ 6 ด้าน | ใช้ตารางเทียบ FIG/ISPRS ด้านบน และประเด็นที่ 6 ด้านปนเกณฑ์กัน (เทคนิค / แพลตฟอร์ม / สภาพแวดล้อม / ขั้นตอนงาน) จึงมีส่วนซ้อนกัน เช่นด้าน 1 กับ 2 |

**ข้อควรระวัง:** Wikipedia เป็นแหล่งรอง ตัวเลขเช่น "RTK 1 cm ± 1 ppm" ที่ปรากฏในบทความ Surveying ผมยังไม่ได้ตรวจกับแหล่งต้นทาง อย่าใส่สไลด์ก่อนยืนยัน

## แหล่งหลักที่ใช้ได้กับทุกด้าน

| | แหล่ง | ใช้ทำอะไร |
|---|---|---|
| ✅ | [ISPRS Commissions](https://www2.isprs.org/commissions/) (S001) | ดูขอบเขต 5 commissions ปี 2022-2026: I Sensor Systems, II Photogrammetry, III Remote Sensing, IV Spatial Information Science, V Education |
| ✅ | [FIG Commission 6 - Engineering Surveys](https://www.fig.net/organisation/comm/6/index.asp) | ขอบเขตงานสำรวจวิศวกรรม และ WG 6.1-6.4 (deformation monitoring, dynamic structural monitoring, immersive technologies) |
| 🔎 | [FIG Commissions (หน้ารวม)](https://www.fig.net/organisation/comm/index.asp) | รายชื่อ 10 commissions, ควรเปิดตรวจรายชื่อเองอีกรอบ |
| 📖 | หนังสือ *Elementary Surveying* (ไฟล์ในโฟลเดอร์โปรเจกต์) | พื้นฐานและหลักการ ดูบทตามด้านด้านล่าง |

**หมายเหตุเรื่องหนังสือ:** ค้นเต็มเล่มแล้วไม่พบคำว่า multibeam, SLAM, unmanned aerial, InSAR, digital twin (พบ sonar 1 ครั้ง, BIM 1 ครั้ง) ไฟล์ PDF มีวันที่สร้าง 2011 และไม่ระบุ edition ดังนั้น **ด้าน 4 และ 6 ต้องอ่านจากบทความและมาตรฐานแทนหนังสือ** เลขหน้าด้านล่างเป็น *เลขหน้าที่พิมพ์ในหนังสือ* (เลขหน้าในไฟล์ PDF = เลขที่พิมพ์ + 21 สำหรับบทที่ 1 เป็นต้นไป)

---

## ด้านที่ 1: Positioning & Geodetic Control (การหาตำแหน่งและโครงข่ายหมุดหลักฐาน)

| หัวข้อ | อ่านอะไร |
|---|---|
| วัตถุประสงค์ + หลักการคิด | 📖 บทที่ 13 GNSS: Introduction and Principles (p.331), บทที่ 19 Control Surveys and Geodetic Reductions (p.529), บทที่ 20 State Plane Coordinates and Map Projections (p.589) |
| เทคโนโลยี | 📖 บทที่ 14 Static Surveys (p.367), บทที่ 15 Kinematic Surveys (p.399; Real-Time Networks p.412; RTK p.413) |
| Trend | ✅ [Review of PPP-RTK: achievements, challenges, and opportunities](https://satellite-navigation.springeropen.com/articles/10.1186/s43020-022-00089-9) (Li et al., 2022, *Satellite Navigation*) · 🔎 [Recent advances and perspectives in GNSS PPP-RTK (TU Delft)](https://research.tudelft.nl/en/publications/recent-advances-and-perspectives-in-gnss-ppp-rtk/) · 🔎 [FIG Commission 5](https://www.fig.net/organisation/comm/5/) และ [work plan 2023-2026](https://www.fig.net/organisation/comm/5/workplan_23-26.asp) |

**คำค้น**
```
"PPP-RTK" OR "network RTK" review GNSS positioning
"multi-GNSS" "multi-frequency" precise positioning review
"ITRF" OR "height reference frame" geodesy site:fig.net
"low-cost GNSS" receiver survey-grade accuracy
```

## ด้านที่ 2: Terrestrial & Optical Surveying (การสำรวจภาคพื้นดิน)

| หัวข้อ | อ่านอะไร |
|---|---|
| วัตถุประสงค์ + หลักการคิด | 📖 บทที่ 3 Theory of Errors (p.45), บทที่ 4-5 Leveling (p.73, 103), บทที่ 6 Distance Measurement (p.131), บทที่ 7 Angles, Azimuths, Bearings (p.169) |
| เทคโนโลยี | 📖 บทที่ 8 Total Station Instruments (p.191), บทที่ 9-10 Traversing และ Traverse Computations (p.231, 245), บทที่ 23 Construction Surveys (p.685) · เรื่อง laser scanning มีกล่าวถึงในบทที่ 17 (ราว p.500 ค้นเจอแต่ยังไม่ได้อ่านเนื้อหา) |
| Trend | ✅ [FIG Commission 6](https://www.fig.net/organisation/comm/6/index.asp): WG 6.1 deformation monitoring, 6.2 dynamic structural monitoring, 6.3 immersive technologies · 🔎 [FIG Commission 6 work plan 2023-2026](https://www.fig.net/organisation/comm/6/workplan_23-26.asp) |

**คำค้น**
```
"robotic total station" OR "scanning total station" review deformation monitoring
"terrestrial laser scanning" review accuracy engineering surveying
"digital level" OR "automated leveling" engineering geodesy
"engineering geodesy" immersive OR "augmented reality" construction layout
```

## ด้านที่ 3: Remote Sensing & Photogrammetry (การสำรวจระยะไกลและภาพถ่าย)

| หัวข้อ | อ่านอะไร |
|---|---|
| วัตถุประสงค์ + หลักการคิด | 📖 บทที่ 27 Photogrammetry (p.799), บทที่ 17 Mapping Surveys (p.467); กล่าวถึง remote sensing ราว p.831 |
| เทคโนโลยี | ✅ [Review of Photogrammetric and Lidar Applications of UAV](https://www.mdpi.com/2076-3417/13/11/6732) (Kovanic et al., 2023, *Applied Sciences*) · 🔎 [Accuracy of UAV and SfM photogrammetry vs. number/location of GCPs](https://www.mdpi.com/2072-4292/10/10/1606) · 🔎 [Photogrammetry vs LiDAR DSM accuracy, four UAS](https://www.mdpi.com/2072-4292/12/17/2806) |
| Trend (InSAR/monitoring) | ✅ [InSAR as a tool for monitoring hydropower projects: A review](https://www.sciencedirect.com/science/article/pii/S2666759221000809) (Aswathi et al., 2022, *Energy Geoscience*; เน้นเขื่อน ซึ่งเข้ากับสายน้ำของคุณ) · ✅ ขอบเขต [ISPRS Commission II และ III](https://www2.isprs.org/commissions/) (AI/ML, point cloud, temporal data) |

**คำค้น**
```
"UAV photogrammetry" OR "SfM" accuracy review "ground control points"
"airborne LiDAR" OR "UAV LiDAR" review topographic mapping
InSAR OR "Sentinel-1" "ground subsidence" monitoring review
"deep learning" "point cloud" classification review geomatics
```
ยังขาด: บทความ review InSAR ภาพรวม (ไม่เจาะเขื่อน) ลองคำค้นแรกกับ Google Scholar + "Since 2021"

## ด้านที่ 4: Hydrographic & Subsurface Survey (การสำรวจใต้น้ำและใต้ดิน)

| หัวข้อ | อ่านอะไร |
|---|---|
| วัตถุประสงค์ + หลักการคิด | 🔑 หนังสือเล่มนี้ไม่ครอบคลุม (ไม่พบ multibeam) ใช้คำค้นด้านล่างหา textbook/course notes |
| เทคโนโลยี | 🔎 [IHO S-44 Edition 6.1.0 (PDF)](https://iho.int/uploads/user/pubs/standards/s-44/S-44_Edition_6.1.0.pdf) มาตรฐานความแม่นยำงานสำรวจอุทกศาสตร์ (ยังไม่ได้เปิดอ่าน) |
| Trend | ✅ [IHO releases new standards for hydrographic surveys](https://iho.int/en/iho-releases-new-standards-for-hydrographic-surveys): S-44 Edition 6.0.0 (กันยายน 2020) เพิ่มชั้น Exclusive Order (±10 ซม.) และ specification matrix รองรับเทคโนโลยีใหม่เช่น satellite-derived bathymetry · ควรตรวจว่าตอนนี้ edition ล่าสุดคือเท่าไรก่อนอ้าง |

**คำค้น**
```
"multibeam echosounder" hydrographic survey review
"unmanned surface vessel" OR "USV" bathymetric survey review
"satellite-derived bathymetry" review accuracy
"ground penetrating radar" review civil engineering OR utility mapping
FIG Commission 4 hydrography work plan site:fig.net
IHO S-44 "Exclusive Order" "special order" survey order
```
ยังไม่มีลิงก์ที่ยืนยันได้สำหรับ FIG Commission 4 และ GPR ให้ใช้คำค้นข้างต้น

## ด้านที่ 5: Data Processing, GIS & Modeling (การประมวลผลและจัดการข้อมูลเชิงพื้นที่)

| หัวข้อ | อ่านอะไร |
|---|---|
| วัตถุประสงค์ + หลักการคิด | 📖 บทที่ 16 Adjustments by Least Squares (p.421), บทที่ 18 Mapping (p.503), ภาคผนวก E Matrices (p.917) |
| เทคโนโลยี | 📖 บทที่ 28 Introduction to GIS (p.843) · 🔎 [GIS and BIM Integration: A High Level Global Report (Esri)](https://www.esri.com/content/dam/esrisites/en-us/media/ebooks/gis-bim-integration-report.pdf) (รายงานจากผู้ผลิต อ่านในฐานะมุมมองอุตสาหกรรม) |
| Trend | 🔎 [Advances, challenges and prospective research when GIScience meets digital twin](https://www.tandfonline.com/doi/full/10.1080/27525783.2025.2610851) (เปิดตรง ๆ ได้ 403 ลองผ่านห้องสมุด/Google Scholar) · ✅ ขอบเขต [ISPRS Commission IV](https://www2.isprs.org/commissions/) (digital twins, IoT, AI/uncertainty modeling) |

**คำค้น**
```
"BIM GIS integration" OR "digital twin" geospatial review
"cloud-based GIS" OR "cloud GIS" surveying data management
"least squares adjustment" geodetic network review OR tutorial
"digital terrain model" OR "DEM" generation accuracy review
```

## ด้านที่ 6: Integration, Automation & Emerging Tech (การบูรณาการและเทคโนโลยีเกิดใหม่)

| หัวข้อ | อ่านอะไร |
|---|---|
| วัตถุประสงค์ + หลักการคิด | 🔑 หนังสือไม่ครอบคลุม (ไม่พบ SLAM) ใช้ review ด้านล่างและคำค้น "sensor fusion" |
| เทคโนโลยี | ✅ [LiDAR-based SLAM for robotic mapping: state of the art and new frontiers](https://arxiv.org/abs/2311.00276) (Yue, He, Zhang, arXiv) · ✅ ขอบเขต [ISPRS Commission I](https://www2.isprs.org/commissions/) (mobile mapping, LiDAR, calibration) |
| Trend | จากบทคัดย่อของ SLAM survey: แนวโน้มคือ multi-robot collaborative mapping และ multi-source fusion SLAM กับ deep learning · ✅ [FIG Commission 6](https://www.fig.net/organisation/comm/6/index.asp) WG 6.3 immersive technologies |

**คำค้น**
```
"mobile mapping system" review accuracy surveying
"handheld SLAM" OR "SLAM-based" laser scanner survey accuracy comparison
"sensor fusion" GNSS IMU LiDAR positioning review
"autonomous" "surveying" robot OR drone construction site review
```
บทความ SLAM ที่ได้เป็นมุมมองหุ่นยนต์ ไม่ใช่งานสำรวจโดยตรง ควรหา review ของ mobile mapping ที่เป็นงานสำรวจเพิ่ม

---

## ช่องทางค้นหา (สรุปสั้น)

| ที่ | เหมาะกับ | เคล็ดลับ |
|---|---|---|
| Google Scholar | ครอบคลุมกว้าง | ตั้ง "Since 2021" สำหรับ trend; ดู "Cited by" และ "Related articles" |
| ResearchGate | ฉบับเต็มที่ผู้เขียนอัปโหลด | ค้นวลีเป็นคำ แล้วกรองเป็น Publications; ระวังเป็นฉบับ preprint |
| MDPI (Remote Sensing, Sensors, Applied Sciences) | เปิดอ่านฟรี งาน trend ล่าสุด | ใส่ "review" ในคำค้น |
| fig.net / isprs.org / iho.int | ภาพรวมวิชาชีพและมาตรฐาน | ดูหน้า commission/working group และเอกสาร congress |

**ข้อควรระวังคำว่า "survey":** ค้น `survey` เฉย ๆ จะได้งานแบบสอบถามปนมา ให้ใส่ `geomatics`, `land surveying`, `geodesy`, `engineering surveying` หรือชื่อเทคนิค และใช้ `review` แทนคำว่า survey paper

## ให้ Claude ช่วยอ่านต่อ (ใช้ skill `research-source-tracker`)

ตัวอย่างคำสั่ง:
- "อ่านบทที่ 13 ใน Elementary Surveying แล้วสรุปหลักการ GNSS สำหรับสไลด์ด้านที่ 1 ลง Excel ด้วย"
- "เปิด S-44 Edition 6.1.0 ตรวจว่า order แต่ละชั้นกำหนดความแม่นยำเท่าไร พร้อมเลขหน้า"
- "หา review ของ mobile mapping ที่เป็นงานสำรวจโดยตรง 3 ชิ้น พร้อมลิงก์"

ทุกครั้งผลจะถูกต่อท้ายใน `Research_Sources.xlsx` พร้อมระดับความน่าเชื่อถือของแต่ละแหล่ง
