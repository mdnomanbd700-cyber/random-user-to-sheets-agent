# 🚀 Random User to Google Sheets Agent

এই এজেন্ট **randomuser.me API** থেকে র্যান্ডম ইউজার ডেটা ফেচ করে আপনার **Google Sheets-এ স্বয়ংক্রিয়ভাবে রপ্তানি করে**।

## ✨ ফিচার

✅ **randomuser.me API থেকে ডেটা ফেচ করা**  
✅ **Google Sheets-এ সরাসরি ডেটা আপলোড করা**  
✅ **স্বয়ংক্রিয় হেডার ম্যানেজমেন্ট**  
✅ **ত্রুটি হ্যান্ডলিং এবং লগিং**  
✅ **কাস্টমাইজযোগ্য ইউজার কাউন্ট**

## 📊 এক্সট্র্যাক্টেড ডেটা

এজেন্ট নিম্নলিখিত তথ্য সংগ্রহ করে:

| ফিল্ড | বিবরণ |
|--------|---------|
| First Name | প্রথম নাম |
| Last Name | শেষ নাম |
| Email | ইমেইল ঠিকানা |
| Phone | ফোন নম্বর |
| Gender | লিঙ্গ |
| Nationality | জাতীয়তা |
| Username | ইউজারনেম |
| City | শহর |
| Country | দেশ |
| Age | বয়স |
| Fetched At | ডেটা সংগ্রহের সময় |

## 🔧 সেটআপ গাইড

### ১. প্রয়োজনীয় বিষয়গুলি

- Python 3.8+
- Google Sheets API অ্যাক্সেস
- Service Account Credentials

### २. ইনস্টলেশন

```bash
# রেপোজিটরি ক্লোন করুন
git clone https://github.com/mdnomanbd700-cyber/random-user-to-sheets-agent.git
cd random-user-to-sheets-agent

# ডিপেন্ডেন্সি ইনস্টল করুন
pip install -r requirements.txt
```

### ३. Google Sheets API সেটআপ

#### ধাপ 1: Google Cloud Console এ যান
1. [Google Cloud Console](https://console.cloud.google.com/) খুলুন
2. একটি নতুন প্রজেক্ট তৈরি করুন
3. "Google Sheets API" সার্চ করুন এবং এনেবল করুন

#### ধাপ 2: Service Account তৈরি করুন
1. **APIs & Services** → **Credentials** এ যান
2. **Create Credentials** → **Service Account** ক্লিক করুন
3. বিস্তারিত তথ্য পূরণ করুন এবং সেভ করুন

#### ধাপ 3: Private Key ডাউনলোড করুন
1. তৈরি করা Service Account ক্লিক করুন
2. **Keys** ট্যাব এ যান
3. **Add Key** → **Create new key** → **JSON** নির্বাচন করুন
4. ডাউনলোড করা ফাইলটি `credentials.json` নাম দিয়ে প্রজেক্ট ফোল্ডারে রাখুন

#### ধাপ 4: Google Sheet শেয়ার করুন
আপনার Google Sheet কে Service Account ইমেইলের সাথে শেয়ার করুন

## 🚀 ব্যবহার

### সাধারণ ব্যবহার

```bash
python main.py
```

## 🛠️ ফাইলের বর্ণনা

- **main.py** - মৌলিক এজেন্ট স্ক্রিপ্ট
- **advanced_agent.py** - OOP ডিজাইন সহ উন্নত সংস্করণ
- **requirements.txt** - Python ডিপেন্ডেন্সি

## 📝 লাইসেন্স

MIT License

---

**তৈরি করেছে:** GitHub Copilot  
**তারিখ:** 2026-09-06
