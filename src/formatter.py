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

def generate_html(keyword: str, results: Dict[str, Any]) -> str:
    """
    Tạo báo cáo HTML kết hợp PAA và Top 10 urls.
    """
    html = [
        f"<!DOCTYPE html>",
        f"<html>",
        f"<head>",
        f"<meta charset='utf-8'>",
        f"<title>Báo Cáo SEO: {keyword}</title>",
        f"<style>",
        f"body {{ font-family: Arial, sans-serif; line-height: 1.6; padding: 20px; color: #333; }}",
        f"table {{ width: 100%; border-collapse: collapse; margin-top: 20px; }}",
        f"th, td {{ border: 1px solid #ddd; padding: 8px; text-align: left; vertical-align: top; }}",
        f"th {{ background-color: #f2f2f2; }}",
        f"a {{ color: #1a0dab; text-decoration: none; }}",
        f"a:hover {{ text-decoration: underline; }}",
        f".content {{ max-height: 200px; overflow-y: auto; display: block; }}",
        f"</style>",
        f"</head>",
        f"<body>",
        f"<h1>BÁO CÁO SEO: <code>{keyword}</code></h1>"
    ]
    
    if not results.get("success"):
        html.append(f"<p style='color: red;'>❌ Lỗi truy xuất Google Search: {results.get('error')}</p>")
        html.append("</body></html>")
        return "\n".join(html)
        
    html.append("<h2>❓ MỌI NGƯỜI CŨNG HỎI (People Also Ask)</h2>")
    paa_list = results.get("paa", [])
    if paa_list:
        html.append("<ul>")
        for question in paa_list:
            html.append(f"<li>{question}</li>")
        html.append("</ul>")
    else:
        html.append("<p><em>(Không tìm thấy mục PAA nào cho từ khóa này)</em></p>")
        
    html.append("<h2>🏆 TOP 10 KẾT QUẢ TÌM KIẾM (Nội dung bóc tách)</h2>")
    
    top_10 = results.get("top_10", [])
    if not top_10:
        html.append("<p><em>(Không tìm thấy kết quả URL tự nhiên nào)</em></p>")
        html.append("</body></html>")
        return "\n".join(html)
        
    html.append("<table>")
    html.append("<tr><th>TOP</th><th>Tiêu đề</th><th>URL</th><th>NỘI DUNG BÓC TÁCH (Sạch)</th></tr>")
    
    for item in top_10:
        pos = item.get("position", "-")
        title = item.get("title", "")
        url = item.get("link", "")
        content = item.get("extracted_content", "").replace("\n", "<br>")
        if not content:
            content = "[Trống]"
            
        html.append(f"<tr>")
        html.append(f"<td>{pos}</td>")
        html.append(f"<td><strong>{title}</strong></td>")
        html.append(f"<td><a href='{url}' target='_blank'>Link</a></td>")
        html.append(f"<td><div class='content'>{content}</div></td>")
        html.append(f"</tr>")

    html.append("</table>")
    html.append("</body></html>")
    
    return "\n".join(html)
