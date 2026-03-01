# Research SEO (AWF Global Skill)

🔥 **Một công cụ cào dữ liệu Google chuẩn SEO, sạch rác HTML, tiết kiệm API Tokens dành riêng cho hệ sinh thái Antigravity Workflow Framework (AWF)**.

Dự án này tích hợp thẳng luồng nghiên cứu từ khóa (Lấy Top 10 đối thủ + Các câu hỏi người dùng thường hỏi) vào khung chat AI của bạn! 

## ✨ Tính năng nổi bật
1. **Lấy "People Also Ask":** Nắm bắt ngay insight của người dùng cực nhanh.
2. **Cào Top 10 URL Organic:** Bóc tách nội dung HTML bằng `Trafilatura`, gọt giũa hoàn toàn Menu, Footer, Ads, Sidebar để ép vào 1 file Markdown. Rất thân thiện khi dùng LLM để phân tích ngược lại.
3. **Thân thiện với AI (Markdown-first):** Xuất báo cáo dạng `.md` 5 cột giúp theo dõi dễ dàng hoặc đưa cho LLM tóm tắt chiến lược Content.
4. **Chống chịu lỗi cao:** Tự động skip các trang dùng SPA (chặn tải nội dung) hoặc timeout để không treo toàn quá trình.

## ⚙️ Hướng dẫn Cài đặt nhanh

### Yêu cầu
- Máy đã cài đặt Python 3.10+
- Hệ thống Antigravity hoạt động ở `~/.gemini/antigravity`
- Có tài khoản và API Key tại [SerpApi](https://serpapi.com/)

### Cài đặt (1-Click)
Khởi chạy file `install.ps1` (trên Windows) để công cụ tự động sao chép các workflows và script vào đúng thư mục hệ thống:

```bash
.\install.ps1
```

*(Hoặc cài thủ công: chép thư mục code vào `skills/research-seo-skill` và file workflow vào thư mục `global_workflows/`)*

### Cấu hình API Key
Mở file `configs/.env` hoặc khai báo biến môi trường biến sau:
```env
SERPAPI_KEY=your_api_key_here
```

## 🚀 Cách sử dụng

Chỉ cần mở cửa sổ chat AI với Antigravity ở bất kì dự án nào, gõ:
```text
/Research SEO "từ khóa bạn muốn"
```

AI sẽ tự động nạp skill, chạy script ngầm, và nhả kết quả phân tích chiến lược vào luồng chat cho bạn!

## 🧩 Tech Stack
- **Python:** `google-search-results`, `trafilatura`, `beautifulsoup4`, `tqdm`.
- **Integration:** Antigravity Workflow (`.md` schemas).

---
*Dành cho SEOers & Content Creators yêu thích tốc độ - Design by AWF*
