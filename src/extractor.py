import requests
import trafilatura
from bs4 import BeautifulSoup
import logging
from typing import Dict, Any

# Cấu hình logging để tránh in lỗi rác ra màn hình của LLM
logging.getLogger("trafilatura").setLevel(logging.ERROR)

def extract_content(url: str, max_length: int = 5000) -> str:
    """
    Tải HTML và trích xuất nội dung chính (Markdown) không có rác (ads, footer...).
    """
    try:
        # 1. Fetch HTML với header giả lập ngắn gọn
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
        }
        res = requests.get(url, headers=headers, timeout=12)
        res.raise_for_status()
        html_content = res.text

        # 2. Extract bằng Trafilatura (Ưu tiên số 1 vì nó xuất Markdown chuẩn)
        extracted = trafilatura.extract(
            html_content,
            include_links=True,
            include_images=False,
            include_formatting=True
        )

        if extracted:
            return _truncate(extracted, max_length)

        # 3. Fallback: Nếu Trafilatura thất bại, thử nghiệm bằng BS4 lấy các thẻ <p>
        soup = BeautifulSoup(html_content, 'html.parser')
        paragraphs = soup.find_all('p')
        text_blocks = [p.get_text(separator=' ', strip=True) for p in paragraphs if p.get_text(strip=True)]
        
        if text_blocks:
            fallback_text = "\n\n".join(text_blocks)
            return _truncate(fallback_text, max_length)
            
        return "[LỖI LẤY NỘI DUNG] Không tìm thấy nội dung văn bản chính."

    except requests.exceptions.Timeout:
        return "[BỎ QUA] Tải trang quá lâu (Timeout > 12s)."
    except requests.exceptions.RequestException:
        return "[BỊ CHẶN] Trang web từ chối truy cập hoặc có bảo vệ Anti-Bot mạnh."
    except Exception as e:
        return f"[LỖI XỬ LÝ] {str(e)}"

def _truncate(text: str, limit: int) -> str:
    if len(text) > limit:
        return text[:limit] + f"\n\n...(Nội dung bị cắt bớt do vượt quá {limit} ký tự)..."
    return text
