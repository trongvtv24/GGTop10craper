import os
import requests

def search_google(keyword: str) -> dict:
    """
    Search Google using SerpApi and extract Organic Results + People Also Ask.
    """
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
        
        # Lấy Top 10 URLs tự nhiên
        organic_results = data.get("organic_results", [])
        top_10 = []
        for res in organic_results[:10]:
            top_10.append({
                "position": res.get("position"),
                "title": res.get("title"),
                "link": res.get("link"),
                "snippet": res.get("snippet", "")
            })
            
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
