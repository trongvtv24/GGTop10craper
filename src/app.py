import sys
import os
import argparse
from serp import search_google
from extractor import extract_content
from formatter import generate_markdown

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
    print(f"✅ Đã tải được {len(top_10)} bài viết và {len(results.get('paa', []))} câu hỏi PAA.")
    
    # Bắt đầu bóc tách nội dung
    for index, item in enumerate(top_10):
        url = item.get("link")
        print(f"[{index + 1}/{len(top_10)}] Đang hút nội dung: {url}")
        content = extract_content(url, max_length=args.max_length)
        item["extracted_content"] = content
        
    print(f"📝 Đang sinh báo cáo Markdown...")
    report_md = generate_markdown(args.keyword, results)
    
    # Lưu file .md
    os.makedirs("outputs", exist_ok=True)
    safe_keyword = str(args.keyword).replace(" ", "_").lower()
    file_path = f"outputs/seo_{safe_keyword}.md"
    
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(report_md)
        
    print(f"✅ Báo cáo đã được lưu tại: {file_path}")
    
    # In thẳng ra stdout cho AWF bắt context
    print("\n--- BÁO CÁO START ---\n")
    print(report_md)
    print("\n--- BÁO CÁO END ---\n")

if __name__ == "__main__":
    main()
