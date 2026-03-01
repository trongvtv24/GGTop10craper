import os
import requests
from dotenv import load_dotenv

def search_google(keyword: str, blacklist: list = None) -> dict:
    """
    Search Google using SerpApi and extract Organic Results + People Also Ask.
    Skips domains in the blacklist.
    """
    if blacklist is None:
        blacklist = ["shopee.vn", "facebook.com", "lazada.vn"]
    env_path = os.path.join(os.path.dirname(__file__), "..", "configs", ".env")
    load_dotenv(env_path)
    api_key = os.environ.get("SERPAPI_KEY")
    if not api_key:
        raise ValueError("Lỗi: Không tìm thấy SERPAPI_KEY trong biến môi trường.")

    params = {
        "engine": "google",
        "q": keyword,
        "hl": "vi",
        "gl": "vn",
        "api_key": api_key
    }

    try:
        response = requests.get("https://serpapi.com/search", params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
        
        # Lấy Top 10 URLs tự nhiên sau khi lọc blacklist
        organic_results = data.get("organic_results", [])
        top_10 = []
        for res in organic_results:
            link = res.get("link", "").lower()
            
            # Kiểm tra xem link có chứa domain bị cấm không
            if any(domain in link for domain in blacklist):
                continue
                
            top_10.append({
                "position": res.get("position"),
                "title": res.get("title"),
                "link": res.get("link"),
                "snippet": res.get("snippet", "")
            })
            
            # Đủ 10 bài thì dừng
            if len(top_10) == 10:
                break
            
        # Lấy People also ask
        paa = []
        for question in data.get("related_questions", []):
            paa.append(question.get("question"))
            
        return {
            "success": True,
            "top_10": top_10,
            "paa": paa
        }
    except Exception as e:
        return {
            "success": False,
            "error": str(e)
        }
