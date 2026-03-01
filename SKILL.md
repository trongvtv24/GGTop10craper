---
name: "Research SEO"
description: "Phân tích và lấy dữ liệu 10 bài viết Top Google tự nhiên (Organic) sạch sẽ kèm danh sách People Also Ask."
---

# Kỹ năng (Skill): Research SEO

Nhóm: Công cụ Tự động hóa / Phân tích Content SEO
Ngôn ngữ: Python 3.12 

## 1. Công dụng
Công cụ này được nạp vào AWF để xử lý lệnh `/Research SEO`. 
Nó sẽ trực tiếp cào 10 trang web đầu tiên trên kết quả Google Search (Bỏ qua Ads) và bóc tách lấy văn bản gốc dạng Markdown siêu sạch thông qua thư viện `Trafilatura`.

## 2. Cách AI Kích hoạt (Trigger)
Khi User nhập mục tiêu là một TỪ KHÓA, AI sử dụng công cụ `run_command` (hoặc bash execution) để chạy tập lệnh Python sau (với đường dẫn là vị trí thư mục hiện tại của Skill này):

```bash
cd ~/.gemini/antigravity/skills/research-seo-skill
python src/app.py "TỪ kHÓA"
```

Lưu ý: Bạn (AI) cần đọc luồng Output (Stdout) in ra từ Terminal. Output sẽ chứa Báo Cáo SEO dạng Markdown. Máy sẽ in báo cáo nằm giữa đoạn:
`--- BÁO CÁO START ---` và `--- BÁO CÁO END ---`.

## 3. Cách AI Xử lý Dữ Liệu Sau Khi Cào
Sau khi Script chạy xong (mất khoảng 10-30s tuỳ tốc độ load 10 trang), bạn (AI) KHÔNG in nguyên văn kết quả tóm tắt này cho User (Vì màn hình chat sẽ rất dài).
Thay vào đó, bạn nạp kết quả đó vào vùng nhớ Ngữ Cảnh (Context), và:
- In cho User xem **1 bảng Outline tóm tắt**.
- Kết luận: "Phân tích điểm yếu của Top 10" và đề xuất "Cấu trúc bài viết (Heading 2, 3) mà User nên viết để có vị trí Top 1".
