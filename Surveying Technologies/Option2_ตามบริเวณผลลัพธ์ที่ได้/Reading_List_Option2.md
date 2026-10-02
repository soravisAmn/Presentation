# Reading List: ทางเลือก 2 (แบ่งตามบริเวณที่สำรวจ)

รายการสิ่งที่ต้องไปหาข้อมูลสำหรับสไลด์ `Survey_Technology_Outline_Option2.pptx` ในโฟลเดอร์นี้ แหล่งที่บันทึกแล้วอยู่ใน `Research_Sources.xlsx` (ชีต Sources, รหัส S###)

ทางเลือกนี้ต่างจากทางเลือก 1 ตรงที่ **หน่วยของตารางคือ "ชนิดเครื่องมือ + ตัวอย่างผลิตภัณฑ์"** ดังนั้นงานค้นหลักคือ datasheet และราคา ไม่ใช่บทความทบทวนเทคโนโลยีอย่างเดียว

## สัญลักษณ์

- ✅ เปิดอ่านจริงแล้ว (บันทึกใน Excel)
- 📖 หนังสือ *Elementary Surveying* (เลขหน้าเป็นเลขที่พิมพ์; เขียนราว 2011)
- 🔑 ไม่มีลิงก์ที่ยืนยันได้ ให้ใช้คำค้น (ผมไม่เดาลิงก์)
- ⚠ มาจากความรู้ทั่วไปของผม ยังไม่ได้ตรวจ

## ข้อควรระวังเรื่องรายชื่อผลิตภัณฑ์ในสไลด์

ชื่อยี่ห้อ/รุ่นทั้งหมดในตารางเป็น ⚠ **รายการที่ผมเลือกจากความรู้ทั่วไป ยังไม่ได้เปิดเว็บผู้ผลิต** เลือกเฉพาะรายที่ข้อมูลสาธารณะหาง่าย ก่อนใช้จริงให้ทำตามนี้

1. ยืนยันว่ารุ่นนั้นยังจำหน่ายอยู่ และชื่อรุ่นสะกดถูก (ค้น `site:<โดเมนผู้ผลิต> <ชนิดเครื่องมือ> datasheet` หรือ `specifications`)
2. ใส่ความแม่นยำเป็น "ค่าที่ผู้ผลิตระบุ" พร้อมเงื่อนไขการวัด (ระยะ วิธีวัด)
3. ราคา: ผู้ผลิตส่วนใหญ่ไม่ประกาศ ให้ใช้ ราคากลางภาครัฐ 🔑 ค้นด้วยชื่อครุภัณฑ์ภาษาไทย เช่น `ราคากลาง กล้องสำรวจประมวลผลรวม`, `ราคากลาง เครื่องรับสัญญาณดาวเทียม GNSS`, `ราคากลาง เครื่องสแกนเลเซอร์ 3 มิติ`, `ราคากลาง อากาศยานไร้คนขับ สำรวจ`, `ราคากลาง เครื่องหยั่งน้ำลึก` (ระบบจัดซื้อจัดจ้างภาครัฐ ⚠ ผมยังไม่ได้ทดลองค้น) ถ้าไม่พบ ให้เว้นว่างและใช้ระดับสัมพัทธ์
4. ค่าความแม่นยำที่ไม่ใช่ของผู้ผลิต: หา 1 บทความทดสอบอิสระต่อชนิดเครื่องมือ

คำค้นรูปแบบกลาง (ปรับชื่อชนิดและยี่ห้อ)
```
"<ชนิดเครื่องมือ>" accuracy test OR evaluation OR comparison -questionnaire
site:<ผู้ผลิต>.com "<รุ่น>" specifications
```

---

## บทที่ 0: ตำแหน่งอ้างอิง

| รายการ | มีแล้ว | ต้องหา |
|---|---|---|
| ขอบเขตและผลลัพธ์ | ✅ S043, S044, S045 | — |
| ชนิดเครื่องมือและหลักการ | 📖 บทที่ 13 GNSS (p.331), 8 Total Station (p.191), 4 Leveling (p.73) | — |
| ตัวอย่างผลิตภัณฑ์ (ตรวจ) | — | ⚠ GNSS: Trimble, Leica Geosystems, Topcon, CHC Navigation, Emlid · Total station: Leica Geosystems, Trimble, Topcon, Sokkia, South · กล้องระดับ: Leica, Trimble, Topcon, Sokkia |
| บริการแก้ค่า | — | เครือข่ายสถานี CORS ของไทย (หน่วยงานเจ้าของ เงื่อนไขการใช้ ค่าบริการ) 🔑 `เครือข่าย CORS กรมที่ดิน OR กรมแผนที่ทหาร ค่าบริการ` |
| ความแม่นยำ | ✅ S006 (PPP-RTK review) | บทความเทียบ static / RTK / network RTK |

คำค้น
```
"network RTK" OR "PPP-RTK" accuracy review GNSS positioning
"survey-grade GNSS receiver" accuracy test low-cost comparison
```

## บทที่ 1: ภูมิประเทศและสิ่งปลูกสร้างเหนือผิวดิน (เฉพาะที่ / แนวยาว / พื้นที่กว้าง)

| รายการ | มีแล้ว | ต้องหา |
|---|---|---|
| ขอบเขตและผลลัพธ์ | ✅ S042, S044, S045 | — |
| ชนิดเครื่องมือและหลักการ | 📖 บทที่ 17 Mapping Surveys (p.467), 23 Construction Surveys (p.685), 27 Photogrammetry (p.799) · ✅ S008 (UAV photogrammetry/LiDAR review) · ✅ S014 (LiDAR SLAM survey) | หลักการ mobile mapping (📖 §1.3 หน้า 7 ✅ มี scanner+GNSS+IMU+กล้อง) |
| ตัวอย่างผลิตภัณฑ์ (ตรวจ) | — | ⚠ TLS: Leica (RTC360), Trimble (X7), FARO (Focus), RIEGL (VZ) · MLS: Leica (Pegasus), Trimble (MX), RIEGL (VMX), Topcon · SLAM พกพา: GeoSLAM, Leica (BLK2GO) · UAV: DJI, Wingtra, AgEagle (eBee), Quantum Systems · UAV LiDAR: DJI (Zenmuse L2), RIEGL, YellowScan · อากาศยานมีคนขับ: Leica, RIEGL, Teledyne Optech, Vexcel · ดาวเทียม: Airbus (Pléiades), Maxar (WorldView), Planet, ESA (Sentinel-2) |
| เกณฑ์ตามขนาดพื้นที่ | ✅ S045 (ground ใช้พื้นที่เล็ก, photogrammetry ใช้พื้นที่กว้าง ราว 2011) | แหล่งใหม่กว่าที่ระบุว่าขนาดพื้นที่ใดเหมาะกับวิธีใด (🔑 `UAV photogrammetry vs terrestrial survey area size cost comparison`) |
| รอยต่อบก–น้ำ | — | ⚠ ทั้งสไลด์ยังไม่มีแหล่ง: 🔑 `topo-bathymetric lidar riverbank OR shallow water survey review`, 🔑 `UAV bathymetry shallow river turbidity limitation` |
| มาตรฐานความแม่นยำ | — | ⚠ ASPRS Positional Accuracy Standards for Digital Geospatial Data (ตรวจฉบับล่าสุด), USGS 3DEP lidar base specification 🔑 |
| Trend | ✅ S001 (ISPRS) | งานทบทวน UAV LiDAR, mobile mapping, deep learning กับ point cloud |

คำค้น
```
"UAV photogrammetry" accuracy review "ground control points"
"UAV LiDAR" accuracy "digital terrain model" vegetation review
"terrestrial laser scanning" OR "mobile mapping" accuracy review
"handheld mobile laser scanning" SLAM accuracy evaluation
"airborne laser scanning" cost per km2
```

## บทที่ 2: ท้องน้ำ

| รายการ | มีแล้ว | ต้องหา |
|---|---|---|
| ขอบเขตและผลลัพธ์ | ✅ S046, S048 | — |
| ชนิดเครื่องมือและหลักการ | 📖 §17.13 (p.493) ใช้ sounding pole และ depth sounder (หนังสือไม่มี multibeam) | หลักการ echo sounding, multibeam, side-scan, ADCP (บทความหรือคู่มือ IHO C-13 บทอื่น 🔑) |
| ตัวอย่างผลิตภัณฑ์ (ตรวจ) | — | ⚠ SBES: Teledyne Odom, CEE Hydrosystems, Ohmex · MBES: Teledyne RESON, Kongsberg, R2Sonic, Norbit · Side-scan: EdgeTech, Klein · ADCP: Teledyne RDI, SonTek · POS: Applanix, Kongsberg · USV: Seafloor Systems |
| มาตรฐานความแม่นยำ | — | IHO S-44 ฉบับล่าสุด (ตัวเลข order ต้องอ่านจากตัวมาตรฐาน; หน้า listing ระบุ Ed. 6.2.0 ต.ค. 2024 ⚠ ยังไม่ได้เปิดตัวมาตรฐาน) |
| งานแม่น้ำ/อ่างเก็บน้ำ | ✅ S046 (ความจุอ่างเก็บน้ำ ขุดลอก) | ตัวอย่างงานสำรวจหน้าตัดลำน้ำ/ท้องน้ำของกรมชลประทาน หรือกรมเจ้าท่า 🔑 `สำรวจหน้าตัดลำน้ำ เครื่องหยั่งน้ำลึก มาตรฐาน` |
| Trend | — | งานทบทวน USV, multibeam บนเรือเล็ก, bathymetry จากดาวเทียม ⚠ |

คำค้น
```
"multibeam echosounder" OR "single beam" river OR reservoir survey accuracy
"unmanned surface vessel" hydrographic survey review
"ADCP" river bathymetry discharge accuracy
IHO S-44 "Standards for Hydrographic Surveys" order 1a OR "Exclusive Order"
```

## บทที่ 3: ใต้ผิวดิน (ลองรวมภาพตัดชั้นดินก่อน)

| รายการ | มีแล้ว | ต้องหา |
|---|---|---|
| ขอบเขตและผลลัพธ์ | ✅ S044 (mine surveys รวม geophysical), S049, S050 | ตัดสินว่าจะรวมภาพตัดชั้นดิน (ERT, seismic) หรือไม่ (เกี่ยวกับตลิ่ง/เสถียรภาพ แต่ใกล้งานธรณีเทคนิค) |
| ชนิดเครื่องมือและหลักการ | ✅ S050 (GPR, electromagnetic locating, vacuum excavation) | หลักการ ERT/seismic จากแหล่งที่เป็นตำรา/บทความทบทวน |
| ตัวอย่างผลิตภัณฑ์ (ตรวจ) | — | ⚠ GPR: GSSI, Guideline Geo (MALÅ), Screening Eagle, IDS GeoRadar · locator: Radiodetection, Vivax-Metrotech, Leica · ERT: Iris Instruments, Guideline Geo (ABEM), Advanced Geosciences · Seismic: Geometrics |
| ความแม่นยำ | ✅ S049 (GPR along-pipe < 0.10 m; เป็นผลงานวิจัย ไม่ใช่ค่ากลางของเครื่อง) | ASCE 38 quality levels 🔑 (⚠ ตรวจฉบับ) |
| Trend | — | งานทบทวน GPR + deep learning, utility mapping |

คำค้น
```
"ground penetrating radar" utility mapping accuracy review
"subsurface utility engineering" "quality level" ASCE 38
"electrical resistivity tomography" embankment OR levee OR riverbank investigation
"seismic refraction" OR "MASW" levee investigation review
```

## บทที่ 4: ติดตามการเปลี่ยนแปลง (บทแยก)

| รายการ | มีแล้ว | ต้องหา |
|---|---|---|
| ขอบเขตและผลลัพธ์ | ✅ S041, S047 (§1.13 หน้า 19-20) | ตัวอย่างตลิ่ง/คันดิน/การกัดเซาะ (ยังไม่มีแหล่ง) |
| ชนิดเครื่องมือและหลักการ | ✅ S011 (InSAR review) · ✅ S002 (FIG C6 WG 6.1-6.4) | หลักการ ground-based radar interferometry, GNSS ต่อเนื่อง |
| ตัวอย่างผลิตภัณฑ์ (ตรวจ) | — | ⚠ Robotic TS monitoring: Leica (GeoMoS), Trimble (4D Control), Topcon · GNSS: Leica, Trimble, Septentrio · InSAR: ESA (Sentinel-1), JAXA (ALOS-2), Airbus (TerraSAR-X) · GB-radar: IDS GeoRadar (IBIS), MetaSensing · geotechnical: Geokon, Slope Indicator |
| Trend | ✅ S002 | 🔎 FIG WG 6.1 Deformation Monitoring and Analysis (หา publications), digital twin เพื่อ monitoring |

คำค้น
```
"deformation monitoring" dam OR embankment geomatics review
"riverbank erosion" monitoring UAV OR LiDAR review
"InSAR" "ground subsidence" OR dam OR levee monitoring review
"structural health monitoring" GNSS OR "robotic total station" review
```

## บทที่ 5: จัดการและวิเคราะห์ข้อมูลเชิงพื้นที่ (บทปิดท้าย)

| รายการ | มีแล้ว | ต้องหา |
|---|---|---|
| ทั้งบท | ✅ S030-S039 (ดูรายละเอียดใน `Reading_List_Option1.md` หน้าที่ 6) | ราคา ArcGIS Pro ในไทย 🔑 `Esri Thailand ArcGIS Pro price`; PostGIS 🔑; ต้นทุนคลาวด์ 🔑; เทียบประสิทธิภาพ 🔑 |

---

## สิ่งที่ยังไม่ตัดสินใจ (จากการคุย)

- ขอบเขตใต้ผิวดิน (ภาพตัดชั้นดินรวมหรือไม่)
- เกณฑ์การเลือกใช้ (สไลด์ที่ 4 ของแต่ละบท) ยังเป็นโครงร่าง
- บท 0 จะย่อเหลือ 1 สไลด์หรือไม่ (ตอนนี้ครบ 5 หัวข้อ)
