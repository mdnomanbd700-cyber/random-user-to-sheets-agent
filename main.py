import requests
import gspread
from google.auth.transport.requests import Request
from google.oauth2.service_account import Credentials
from datetime import datetime
import json

# Google Sheets Configuration
GOOGLE_SHEET_ID = "1WER4pfynXJkju55d8sMpi4_FteF76TaIQkefCoNvSJk"
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

# Random User API Configuration
RANDOM_USER_API = "https://randomuser.me/api/?results=50"

def authenticate_google_sheets():
    """Authenticate with Google Sheets API using credentials file"""
    try:
        creds = Credentials.from_service_account_file(
            'credentials.json', scopes=SCOPES)
        return gspread.authorize(creds)
    except FileNotFoundError:
        print("❌ Error: credentials.json not found!")
        print("Please follow the setup instructions in README.md")
        return None

def fetch_random_users(count=50):
    """Fetch random user data from randomuser.me API"""
    try:
        url = f"https://randomuser.me/api/?results={count}"
        print(f"🔄 Fetching {count} random users from {url}...")
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        
        data = response.json()
        users = data.get('results', [])
        print(f"✅ Successfully fetched {len(users)} users")
        return users
    
    except requests.exceptions.RequestException as e:
        print(f"❌ Error fetching data: {e}")
        return []

def extract_user_data(users):
    """Extract relevant user data from API response"""
    extracted_data = []
    
    for user in users:
        try:
            data = {
                'First Name': user.get('name', {}).get('first', ''),
                'Last Name': user.get('name', {}).get('last', ''),
                'Email': user.get('email', ''),
                'Phone': user.get('phone', ''),
                'Gender': user.get('gender', ''),
                'Nationality': user.get('nat', ''),
                'Username': user.get('login', {}).get('username', ''),
                'City': user.get('location', {}).get('city', ''),
                'State': user.get('location', {}).get('state', ''),
                'Country': user.get('location', {}).get('country', ''),
                'Age': user.get('dob', {}).get('age', ''),
                'Profile Picture': user.get('picture', {}).get('large', ''),
                'Fetched At': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            }
            extracted_data.append(data)
        except Exception as e:
            print(f"⚠️  Warning: Error extracting user data: {e}")
            continue
    
    return extracted_data

def append_to_google_sheets(client, data):
    """Append user data to Google Sheets"""
    try:
        # Open the spreadsheet
        sheet = client.open_by_key(GOOGLE_SHEET_ID)
        worksheet = sheet.worksheet("Sheet1")
        
        # Get existing headers
        headers = worksheet.row_values(1)
        
        # If no headers exist, add them
        if not headers:
            headers = list(data[0].keys()) if data else []
            worksheet.append_row(headers)
            print(f"📝 Added headers: {headers}")
        
        # Prepare rows for insertion
        rows = []
        for user in data:
            row = [user.get(header, '') for header in headers]
            rows.append(row)
        
        # Append rows to sheet
        if rows:
            worksheet.append_rows(rows)
            print(f"✅ Successfully appended {len(rows)} rows to Google Sheets")
        else:
            print("⚠️  No data to append")
        
        return True
    
    except gspread.exceptions.APIError as e:
        print(f"❌ Google Sheets API Error: {e}")
        return False
    except Exception as e:
        print(f"❌ Error appending to Google Sheets: {e}")
        return False

def main():
    """Main execution function"""
    print("=" * 60)
    print("🚀 Random User to Google Sheets Agent")
    print("=" * 60)
    
    # Step 1: Authenticate with Google Sheets
    print("\n1️⃣  Authenticating with Google Sheets...")
    client = authenticate_google_sheets()
    if not client:
        return False
    print("✅ Authentication successful!")
    
    # Step 2: Fetch random users from API
    print("\n2️⃣  Fetching random users from randomuser.me...")
    users = fetch_random_users(count=50)
    if not users:
        print("❌ Failed to fetch users")
        return False
    
    # Step 3: Extract relevant data
    print("\n3️⃣  Extracting user data...")
    extracted_data = extract_user_data(users)
    print(f"✅ Extracted data from {len(extracted_data)} users")
    
    # Step 4: Append to Google Sheets
    print("\n4️⃣  Uploading to Google Sheets...")
    success = append_to_google_sheets(client, extracted_data)
    
    if success:
        print("\n" + "=" * 60)
        print("✅ SUCCESS! All users have been exported to Google Sheets")
        print(f"📊 Google Sheet: https://docs.google.com/spreadsheets/d/{GOOGLE_SHEET_ID}")
        print("=" * 60)
        return True
    else:
        print("\n❌ Failed to export data")
        return False

if __name__ == "__main__":
    main()
