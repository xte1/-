import os
import requests

# دالة لتحميل الحسابات من ملف accounts.txt
def load_accounts():
    accounts = []
    if os.path.exists("accounts.txt"):
        with open("accounts.txt", "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line and ":" in line:
                    username, session = line.split(":", 1)
                    accounts.append({"username": username, "session": session})
    return accounts

# دالة محاكاة إرسال الطلب عبر الجلسة (Session ID)
def send_request(account, post_url, service_type, quantity):
    # هنا يتم وضع رابط وخوارزمية إرسال الطلب الخاصة بـ API تيك توك باستخدام الـ sessionid
    session_id = account["session"]
    username = account["username"]
    
    # محاكاة الاتصال بخوادم تيك توك
    print(f"[*] جاري استخدام الحساب: {username} لإرسال ({service_type}) إلى الرابط...")
    
    # مثال على تمرير الكوكيز لجلسة تيك توك
    cookies = {"sessionid": session_id}
    headers = {
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15"
    }
    
    try:
        # ملاحظة: يمكنك استبدال الرابط أدناه بـ API الداخلي الخاص بالخدمة التي تستخدمها
        # response = requests.get(post_url, cookies=cookies, headers=headers, timeout=10)
        
        # محاكاة نجاح العملية افتراضياً للتجربة
        print(-> [تم بنجاح] الحساب {username} نفذ الخدمة ({service_type}) للرابط المطلوب.")
        return True
    except Exception as e:
        print(f"[-] فشل التنفيذ بالحساب {username}: {e}")
        return False

def main():
    print("=== أداة رشق تيك توك التلقائية ===")
    
    # 1. تحميل الحسابات
    accounts = load_accounts()
    if not accounts:
        print("[-] تنبيه: لا توجد حسابات مسجلة في ملف accounts.txt!")
        return
    
    print(f"[+] تم العثور على {len(accounts)} حساب جاهز للتنفيذ.\n")
    
    # 2. إدخال بيانات الطلب
    post_url = input("أدخل رابط الفيديو أو المنشور: ").strip()
    service_type = input("اختر الخدمة (views / likes / comments / followers): ").strip()
    try:
        quantity = int(input("أدخل العدد المطلوب: ").strip())
    except ValueError:
        print("[-] خطأ: يجب إدخال رقم صحيح للعدد.")
        return

    if quantity > len(accounts):
        print(f"[-] عذراً، العدد المطلوب ({quantity}) أكبر من عدد الحسابات المتوفرة لديك ({len(accounts)})!")
        return

    print("\n--- جاري البدء بتنفيذ الطلبات ---")
    
    # 3. توزيع الطلبات على الحسابات المتوفرة
    success_count = 0
    for i in range(quantity):
        account = accounts[i % len(accounts)] # تدوير الحسابات إذا كان العدد أكبر
        res = send_request(account, post_url, service_type, 1)
        if res:
            success_count += 1

    print(f"\n[+] اكتملت العملية! تم تنفيذ {success_count} من أصل {quantity} بنجاح.")

if __name__ == "__main__":
    main()
