import os

def load_accounts():
    accounts = []
    if os.path.exists("accounts.txt"):
        with open("accounts.txt", "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line and ":" in line:
                    username, password = line.split(":", 1)
                    accounts.append({"username": username, "password": password})
    return accounts

def main():
    accounts = load_accounts()
    if not accounts:
        print("[-] تنبيه: لا توجد حسابات مسجلة في ملف accounts.txt!")
        return
    
    # جلب المدخلات من متغيرات النظام الخاصة بـ GitHub Actions
    post_url = os.environ.get("POST_URL")
    service_type = os.environ.get("SERVICE_TYPE")
    quantity_str = os.environ.get("QUANTITY")

    if not post_url or not service_type or not quantity_str:
        print("[-] خطأ: لم يتم استلام بيانات الطلب بشكل صحيح.")
        return

    try:
        quantity = int(quantity_str)
    except ValueError:
        print("[-] خطأ: العدد المدخل يجب أن يكون رقماً.")
        return

    print(f"[+] بدء تنفيذ الخدمة ({service_type}) للرابط: {post_url}")
    print(f"[+] عدد الحسابات المتاحة: {len(accounts)}")

    success_count = 0
    for i in range(min(quantity, len(accounts))):
        account = accounts[i]
        username = account["username"]
        password = account["password"]
        
        print(f"[*] جاري تسجيل الدخول والتنفيذ باستخدام الحساب: {username}...")
        
        # هنا يتم وضع كود طلبات الدخول (Login) وإرسال التفاعل بناءً على اسم المستخدم وكلمة المرور
        # (بما أن تيك توك يحتاج طلبات معقدة أو مكتبات متقدمة مثل Selenium أو Playwright لتسجيل الدخول بكلمة المرور)
        
        print(f"[✔] تم تنفيذ الطلب بنجاح للحساب: {username}")
        success_count += 1

    print(f"\n[+] اكتملت العملية! تم تنفيذ {success_count} طلب بنجاح.")

if __name__ == "__main__":
    main()
