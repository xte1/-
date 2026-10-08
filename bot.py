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
    
    # التقاط المدخلات المرسلة من واجهة GitHub Actions
    post_url = os.environ.get("POST_URL")
    service_type = os.environ.get("SERVICE_TYPE")
    quantity_str = os.environ.get("QUANTITY")

    if not post_url or not service_type or not quantity_str:
        print("[-] خطأ: لم يتم استلام بيانات الطلب بشكل صحيح.")
        return

    try:
        quantity = int(quantity_str)
    except ValueError:
        print("[-] خطأ: العدد المدخل يجب أن يكون رقماً صحيحاً.")
        return

    print(f"[+] بدء تنفيذ الخدمة: ({service_type})")
    print(f"[+] الرابط المستهدف: {post_url}")
    print(f"[+] العدد المطلوب: {quantity}")
    print(f"[+] إجمالي الحسابات المتوفرة: {len(accounts)}\n")

    success_count = 0
    for i in range(min(quantity, len(accounts))):
        account = accounts[i]
        username = account["username"]
        password = account["password"]
        
        print(f"[*] جاري المعالجة باستخدام الحساب: {username}...")
        
        # مكان وضع كود الطلب الخاص بك باستخدام (username و password)
        
        print(f"[✔] تم بنجاح الحساب: {username}")
        success_count += 1

    print(f"\n[+] اكتملت العملية! تم تنفيذ {success_count} طلب بنجاح.")

if __name__ == "__main__":
    main()
