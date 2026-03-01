import os
import json
import requests
import subprocess
import sys

# Extract session cookie from the provided JSON
cookie_json = """{"url":"https://github.com","cookies":[{"domain":".github.com","expirationDate":1797952735.715934,"hostOnly":false,"httpOnly":false,"name":"_octo","path":"/","sameSite":"lax","secure":true,"session":false,"storeId":"0","value":"GH1.1.808846544.1766416735"},{"domain":".github.com","hostOnly":false,"httpOnly":false,"name":"cpu_bucket","path":"/","sameSite":"lax","secure":true,"session":true,"storeId":"0","value":"xlg"},{"domain":".github.com","hostOnly":false,"httpOnly":false,"name":"preferred_color_mode","path":"/","sameSite":"lax","secure":true,"session":true,"storeId":"0","value":"light"},{"domain":".github.com","hostOnly":false,"httpOnly":false,"name":"tz","path":"/","sameSite":"lax","secure":true,"session":true,"storeId":"0","value":"Asia%2FBangkok"},{"domain":"github.com","expirationDate":1803746278.66945,"hostOnly":true,"httpOnly":true,"name":"_device_id","path":"/","sameSite":"lax","secure":true,"session":false,"storeId":"0","value":"cd0db4701c377da2e0893c59cbbe3e04"},{"domain":"github.com","expirationDate":1775578613.578176,"hostOnly":true,"httpOnly":true,"name":"saved_user_sessions","path":"/","sameSite":"lax","secure":true,"session":false,"storeId":"0","value":"246411265%3AuemJdoU5EtIIrSJfU0WXTEbmGRw4obBnDsQU2tGeZxx9rx5r"},{"domain":"github.com","expirationDate":1773419878.669559,"hostOnly":true,"httpOnly":true,"name":"user_session","path":"/","sameSite":"lax","secure":true,"session":false,"storeId":"0","value":"uemJdoU5EtIIrSJfU0WXTEbmGRw4obBnDsQU2tGeZxx9rx5r"},{"domain":"github.com","expirationDate":1773419878.669612,"hostOnly":true,"httpOnly":true,"name":"__Host-user_session_same_site","path":"/","sameSite":"strict","secure":true,"session":false,"storeId":"0","value":"uemJdoU5EtIIrSJfU0WXTEbmGRw4obBnDsQU2tGeZxx9rx5r"},{"domain":"github.com","hostOnly":true,"httpOnly":true,"name":"tz","path":"/","sameSite":"lax","secure":true,"session":true,"storeId":"0","value":"Asia%2FBangkok"},{"domain":".github.com","hostOnly":false,"httpOnly":false,"name":"color_mode","path":"/","sameSite":"lax","secure":true,"session":true,"storeId":"0","value":"%7B%22color_mode%22%3A%22auto%22%2C%22light_theme%22%3A%7B%22name%22%3A%22light%22%2C%22color_mode%22%3A%22light%22%7D%2C%22dark_theme%22%3A%7B%22name%22%3A%22dark%22%2C%22color_mode%22%3A%22dark%22%7D%7D"},{"domain":".github.com","expirationDate":1799338613.578446,"hostOnly":false,"httpOnly":true,"name":"logged_in","path":"/","sameSite":"lax","secure":true,"session":false,"storeId":"0","value":"yes"},{"domain":".github.com","expirationDate":1801915861.469047,"hostOnly":false,"httpOnly":true,"name":"dotcom_user","path":"/","sameSite":"lax","secure":true,"session":false,"storeId":"0","value":"trongvtv24"},{"domain":"github.com","hostOnly":true,"httpOnly":true,"name":"last_write_ms","path":"/","sameSite":"lax","secure":true,"session":true,"storeId":"0","value":"1772380125795"},{"domain":"github.com","hostOnly":true,"httpOnly":true,"name":"_gh_sess","path":"/","sameSite":"lax","secure":true,"session":true,"storeId":"0","value":"%2Fgy3dH9FbUpMLp%2BQQYbTrH5nNCzSYFf%2BzN%2Fzr4X5PpjgJ8JcRZwu4bFA3Bc0C8i9pyTzNbN4%2FDzDaV7l5HqGaSws0RlNlbvNGQXQtixdbni76FPs%2Bct%2BTNPWdVuM9pXYdfkz31lB5ohvy34rWzJj%2B2viokgRrSl13vIHGCE6K2L5lK%2B%2Fh5h29pHsO7QsuadypEcP533lTU70CdkzYhI1LLFnTecW29u%2F103JfVkKR0OhUmrseGAru28aC%2Bgqaovd0mxzamXsZhiloX3wJxCHo0hRcFCmTBefosR%2BE%2FNs8Cxfmr7eYptgwagWEbWwZXF7ipEY3hY03aQhpDd0qsmCevFGBkgcpV5HALuj0Lrj07qP3bziuAdP4ivMa4p5XSh%2F8m9H4Ag8PTtyVF2qXqUMdYJvhTyxxFsLysmMuNh0Wk9HZO60J33gQRfv9hrTp7hWebAbkPMaQhPSTQf8l6HVNsi3BQ%2BSAJN343LCN73YFdcJeofHPJQhBtVzAumu%2BfSTHNsgLtDmIChqz2lyXCYUYh7HQYlDQ4bq34x4%2BGzmaEE01I8bfTyVT4zZA1GO772Sz3by0s1vTtI%2BOGraAcbHfc5lYRzT2vgG0fZi8Kh2c7br3DyaFO28W2kyTXGAgvK%2BYgKTuahKFFQbnYmQGRjc2j29Zgn0mTOD9KP970Z1Im3ZCoMbQeKykiTqLrDyYjfZ8lUfr6RC2wSfJmxcAvi9boyGUbs%3D--%2FHoAzI0ME4wIM94Y--Vys%2F2xXLpULBw2hxAZZhDA%3D%3D"}]}"""
data = json.loads(cookie_json)
cookie_str = "; ".join([f"{c['name']}={c['value']}" for c in data["cookies"]])

headers = {
    "Cookie": cookie_str,
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
    "Accept": "application/json",
    "Content-Type": "application/json"
}

# 1. Fetch the authenticity_token from new repo page
import re
res = requests.get("https://github.com/new", headers=headers)
match = re.search(r'<input type="hidden" name="authenticity_token" value="(.*?)"', res.text)
if not match:
    print("Failed to find authenticity_token. The cookie might be invalid or expired.")
    sys.exit(1)

auth_token = match.group(1)

# 2. Create the repository
payload = {
    "authenticity_token": auth_token,
    "repository[name]": "GGTop10craper",
    "repository[description]": "Antigravity Global Skill: SEO Research tool using SerpApi and Trafilatura to extract clean organic Google search results.",
    "repository[visibility]": "public",
    "commit": "Create repository"
}

create_res = requests.post("https://github.com/repositories", headers=headers, data=payload)
if create_res.status_code in [200, 302] or "GGTop10craper" in create_res.url:
    print("✅ Repository created successfully!")
else:
    print("❌ Failed to create repository.")
    print("Status:", create_res.status_code)
    sys.exit(1)
