from typing import List, Dict, Any

def generate_markdown(keyword: str, results: Dict[str, Any]) -> str:
    """
    Tạo báo cáo Markdown kết hợp PAA và Top 10 urls.
    """
    md = []
    
    md.append(f"# BÁO CÁO SEO: `{keyword}`\n")
    
    if not results.get("success"):
        md.append(f"❌ Lỗi truy xuất Google Search: {results.get('error')}\n")
        return "\n".join(md)
        
    md.append("## ❓ MỌI NGƯỜI CŨNG HỎI (People Also Ask)")
    paa_list = results.get("paa", [])
    if paa_list:
        for question in paa_list:
            md.append(f"- {question}")
    else:
        md.append("*(Không tìm thấy mục PAA nào cho từ khóa này)*")
        
    md.append("\n## 🏆 TOP 10 KẾT QUẢ TÌM KIẾM (Nội dung bóc tách)")
    
    top_10 = results.get("top_10", [])
    if not top_10:
        md.append("*(Không tìm thấy kết quả URL tự nhiên nào)*")
        return "\n".join(md)
        
    # Tạo Bảng HTML/Markdown
    md.append("| TOP | Tiêu đề | URL | NỘI DUNG BÓC TÁCH (Sạch) |")
    md.append("|---|---|---|---|")
    
    for item in top_10:
        pos = item.get("position", "-")
        title = item.get("title", "").replace("|", "-")
        url = item.get("link", "")
        # Filter markdown table breakers
        content = item.get("extracted_content", "").replace("\n", "<br>").replace("|", "\\|")
        if not content:
            content = "[Trống]"
            
        md.append(f"| {pos} | **{title}** | [Link]({url}) | {content} |")

    return "\n".join(md)
