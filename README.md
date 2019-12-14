# give-me-the-money
Project PSIT 2019 
.
.
.
แนะนำโปรเจค:โปรเจคนี้ได้มีแนวคิดมาจากปัญหาการเก็บเงินในรุ่น ในตอนที่เพื่อนที่เป็นเหรัญญิกของรุ่นได้ทำการเก็บเงินจะต้อง
มีการทำเอกสาร ซึ่งปัญหาที่พบก็คือเพื่อนจะต้องมานั่งทำเอกสารซึ่งต้องปริ้นออกมาเป็นกระดาษ ซึ่งกระดาษจะมีสูญหาย หรือที่จดไว้นั้นจางไป
เพื่อเป็นการแก้ปัญหาเลยได้ริเริ่มทำโปรเจคนี้ขึ้น
.
.
โปรเจคที่ทำขึ้นใช้ Framework Django เป็นการพัฒนาเว็บ application โดยใช้ภาษา python
ซึ่ง ตัว Framework นั้นจะมีรูปแบบ เป็น directory แบ่งเป็นส่วนต่างๆ ตอนรันสามารถเข้ามาในส่วนของโฟลเดอร์โปรเจค
give-me-the-money/money/ ตอนรันจะเจอไฟล์ที่ชื่อ manage.py สามารถเข้ามา path(ในcmd)นี้ แล้วใช้คำสั่ง
py manage.py runserver ในcmd เริ่มทำงานได้โดย framework นี้จะสร้าง webserver โดยมี application รันอยู่บนเว็บ server

พูดถึงในส่วนของ application (ในที่นี้จะเป็นโฟลเดอร์ mainapp) จะมีโครงสร้างต่างๆแบ่งไว้ในแต่ละไฟล์ดังนี้
-
admin.py - จะเป็นโค้ดในส่วนที่เราจะต้องใช้งานเพื่อลงทะเบียนตัว modelของ database
apps.py - ส่วนนี้ไม่ได้ใช้
forms.py - ใช้ในการทำแบบฟอร์มสำหรับเพิ่มนักศึกษาที่ละคน แก้ไขนักศึกษาในฟีเจอร์ของโปรเจคนี้
models.py - ใช้ในส่วนของการสร้างโครงสร้างของตัว database ที่ใช้ในการเก็บข้อมูล
test.py - ส่วนนี้ไม่ได้ใช้
urls.py - ใช้ในการเก็บ url ของแต่ละหน้า ซึ่งไฟล์นี้จะเชื่อมโยงกับ view.py 
views.py - ไฟล์นี้จะเก็บการทำงานที่เป็นฟังก์ชั่นหลักๆทั้งหมด 
