import os
import shutil

#กำหนดโฟลเดอร์เป้าหมายที่เราต้องการจัดระเบียบ (เช่น โฟลเดอร์ Downloads)
target_dir = "./test_folder" #ลองสร้างโฟลเดอร์จำลองชื่อนี้ดูก่อนได้ครับ

#กำหนดหมวดหมู่ตามนามสกุลไฟล์
folders = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx"],
    "Code": [".py", ".html", ".css", ".js", ".cs"]
}

def organize_files():
    if not os.path.exists(target_dir):
        print(f"ไม่พบโฟลเดอร์ {target_dir} สร้างโฟลเดอร์ทดสอบก่อน")
        return

    for filename in os.listdir(target_dir):
        file_path = os.path.join(target_dir, filename)
        
        #ข้ามถ้าเป็นโฟลเดอร์
        if os.path.isdir(file_path):
            continue
            
        #เช็คนามสกุลไฟล์
        file_ext = os.path.splitext(filename)[1].lower()
        
        moved = False
        for folder_name, exts in folders.items():
            if file_ext in exts:
                dest_folder = os.path.join(target_dir, folder_name)
                os.makedirs(dest_folder, exist_ok=True)
                
                # ย้ายไฟล์ไปยังโฟลเดอร์หมวดหมู่
                shutil.move(file_path, os.path.join(dest_folder, filename))
                print(f"ย้ายไฟล์: {filename} -> ไปที่หมวด {folder_name}")
                moved = True
                break
                
        if not moved:
            print(f"ข้ามไฟล์ประเภทอื่น: {filename}")

if __name__ == "__main__":
    organize_files()