# Reading List — Option 3 (วัตถุประสงค์ → หลักการ → เทคโนโลยี → เครื่องมือ)

สถานะแหล่งอ้างอิง: รหัส S อยู่ใน `Research_Sources.xlsx` (S001–S056) ข้อที่ไม่มีรหัส = ยังไม่มีแหล่ง ต้องหา

## บทนำ: ภาพรวมงานสำรวจ (1 สไลด์, ~5 นาที)
- มีแล้ว: FIG 11 หน้าที่ (Elementary Surveying §1.2 หน้า 2) [S041]; §1.6 หน้า 11-12 [S044]; FIG/ISPRS commissions [S051]
- ต้องหา: ไม่มี (การแบ่ง 6 หน้าที่เป็นการสังเคราะห์ของผู้นำเสนอ รายละเอียดดู Option 1)

## ข้อมูลที่ต้องหาทุกหัวข้อ (ใช้ซ้ำทุกบท)
1. นิยามหลักการวัด 1-2 บรรทัดต่อหลักการ จากตำรา/มาตรฐาน (ตอนนี้เป็นร่างจากความรู้ทั่วไป)
2. ชนิดเครื่องมือ/เทคโนโลยีต่อหลักการ จาก review paper ไม่เกิน 5 ปี
3. ตัวอย่างผลิตภัณฑ์: ตรวจชื่อยี่ห้อ/รุ่นกับ datasheet ผู้ผลิต (ทำไปแล้ว: ไม่มี)
4. ความแม่นยำตามที่ผู้ผลิตระบุ (ใส่เฉพาะค่าจาก datasheet)
5. ข้อจำกัดด้านสภาพแวดล้อม + เวลาประมวลผล
6. ต้นทุนสัมพัทธ์เป็นบาท: ราคากลางหน่วยงานรัฐ (e-GP) หรือใบเสนอราคา; ถ้าไม่พบ ใส่ search key
7. Research trend ล่าสุด (review paper ปี 2021+)

## บท 1 การกำหนดตำแหน่งอ้างอิง
- มีแล้ว: §1.4, §1.6, §17.2 [S043-S045]; PPP-RTK review [S006]
- ต้องหา: หลักการ GNSS/traverse/leveling จากหนังสือบท 13, 8, 4 (ยังไม่ลงรหัส); สถานี CORS ของไทย (ผู้ให้บริการ/หน่วยงาน); ความแม่นยำ static vs RTK vs PPP จาก datasheet
- Search key: `"PPP-RTK" OR "network RTK" review GNSS positioning`

## บท 2.1 ผิวดินและวัตถุบนบก
- มีแล้ว: §1.3 [S042], §1.6 [S044], §17.2 [S045]; UAV review [S008]; LiDAR SLAM [S014]
- ต้องหา: เกณฑ์ขนาดพื้นที่ (เฉพาะที่/แนวยาว/กว้าง) จากแหล่งที่ไม่ใช่ตำราปี 2011; ความแม่นยำ UAV photogrammetry เทียบ LiDAR; แหล่งของแถว topo-bathymetric LiDAR ในตาราง 2.2 (ข้อจำกัดความขุ่น) — ตัดสไลด์รอยต่อบก–น้ำแล้ว
- Search key: `"topo-bathymetric" OR "topobathymetric" LiDAR review`; `"UAV photogrammetry" accuracy review "ground control points"`

## บท 2.2 ใต้น้ำ
- มีแล้ว: §17.13 [S046]; IHO Manual ch.1 [S048]
- ต้องหา: **หลักการ echo sounding / multibeam / side-scan / ADCP** (IHO S-44 ฉบับปัจจุบัน, ตำรา hydrography); ปริมาณงานวัดหน้าตัดลำน้ำที่เกี่ยวกับงานตลิ่ง
- Search key: `"multibeam echosounder" OR "unmanned surface vessel" hydrographic survey review`

## บท 2.3 ใต้ผิวดิน
- มีแล้ว: GPR [S049, S050 แหล่งรอง]; §1.6 หน้า 12 [S044]
- ต้องหา: **หลักการ ERT และ seismic** (ตำราธรณีฟิสิกส์วิศวกรรม); ตัดสินใจว่าจะรวม ERT/seismic หรือจำกัดที่สาธารณูปโภค
- Search key: `"electrical resistivity tomography" OR "seismic refraction" engineering geophysics review`

## บท 3 การติดตามการเปลี่ยนแปลง
- มีแล้ว: FIG หน้าที่ [S041]; §1.13 [S047]; InSAR review [S011]
- ต้องหา: **ตัวอย่างงานตลิ่ง/คันกั้นน้ำ** (การกัดเซาะ การทรุดตัว); หลักการ robotic TS monitoring; เกณฑ์เลือกระหว่าง InSAR กับการวัดภาคพื้น
- Search key: `"riverbank erosion" monitoring UAV OR LiDAR OR InSAR`; `"deformation monitoring" "robotic total station" review`

## บท 4 การจัดการและวิเคราะห์ข้อมูลเชิงพื้นที่
- มีแล้ว: §1.8, §28.4.2, §28.9 [S030-S032]; QGIS [S033]; ราคา ArcGIS Pro (USD รัฐอินเดียนา) [S035]; cloud-native [S037]; GeoAI [S038]; digital twin [S039]
- ต้องหา: ราคาไทย (ArcGIS ตัวแทนในไทย / ราคากลาง); เนื้อหาแถว GeoAI ในตาราง; อัตราแปลงสกุลเงินที่ใช้จริง (ตอนนี้สมมติ 33 บาท/USD)
