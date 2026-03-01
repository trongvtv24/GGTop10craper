import sys
import os
import argparse
from serp import search_google
from extractor import extract_content
from formatter import generate_markdown, generate_html

def main():
    parser = argparse.ArgumentParser(description="Research SEO CLI Tool")
    parser.add_argument("keyword", help="Từ khóa SEO cần cào")
    parser.add_argument("--max-length", type=int, default=5000, help="Độ dài tối đa mỗi bài viết xuất ra")
    
    args = parser.parse_args()
    
    print(f"🔄 Đang tìm kiếm Google cho từ khóa: '{args.keyword}'...")
    results = search_google(args.keyword)
    
    if not results.get("success"):
        print(f"❌ Lỗi: {results.get('error')}")
        sys.exit(1)
        
    top_10 = results.get("top_10", [])
    
    # Optional logic to display a friendly message regarding skipped URLs if the organic_results were originally larger
    print(f"✅ Đã tải được {len(top_10)} bài viết (đã lọc bỏ Shopee, Facebook, Lazada, WebSoSanh, ThiTruongSi) và {len(results.get('paa', []))} câu hỏi PAA.")
    
    # Bắt đầu bóc tách nội dung
    for index, item in enumerate(top_10):
        url = item.get("link")
        print(f"[{index + 1}/{len(top_10)}] Đang hút nội dung: {url}")
        content = extract_content(url, max_length=args.max_length)
        item["extracted_content"] = content
        
    print(f"📝 Đang sinh báo cáo Markdown và HTML...")
    report_md = generate_markdown(args.keyword, results)
    report_html = generate_html(args.keyword, results)
    
    # Lấy đường dẫn Desktop của user
    desktop_dir = os.path.join(os.path.expanduser("~"), "Desktop")
    safe_keyword = str(args.keyword).replace(" ", "_").lower()
    
    file_path_md = os.path.join(desktop_dir, f"seo_{safe_keyword}.md")
    file_path_html = os.path.join(desktop_dir, f"seo_{safe_keyword}.html")
    
    # Lưu file .md
    with open(file_path_md, "w", encoding="utf-8") as f:
        f.write(report_md)
        
    # Lưu file .html
    with open(file_path_html, "w", encoding="utf-8") as f:
        f.write(report_html)
        
    print(f"✅ Báo cáo đã được lưu tại Desktop:\n   - {file_path_md}\n   - {file_path_html}")
    
    # In thẳng ra stdout cho AWF bắt context
    print("\n--- BÁO CÁO START ---\n")
    print(report_md)
    print("\n--- BÁO CÁO END ---\n")

if __name__ == "__main__":
    main()
