# Hệ Thống Ôn Tập Trắc Nghiệm Quản Lý Dự Án CNTT (65 Câu Chuẩn Hóa)

[![Live Demo](https://img.shields.io/badge/Live%20Demo-GitHub%20Pages-2ea44f?style=for-the-badge&logo=github)](https://nguyentatmanh.github.io/OnTap-QuanLyDuAnCNTT/)
[![Ngân hàng câu hỏi](https://img.shields.io/badge/Ng%C3%A2n%20h%C3%A0ng-65%20c%C3%A2u%20chu%E1%BA%A9n%20h%C3%B3a-4f46e5?style=for-the-badge)](questions.json)
[![Platform](https://img.shields.io/badge/N%E1%BB%81n%20t%E1%BA%A3ng-Web%20Client%20%2F%20SPA-0284c7?style=for-the-badge)](index.html)

> 🌐 **Trải nghiệm trực tuyến ngay (Live Demo):**  
> **👉 [https://nguyentatmanh.github.io/OnTap-QuanLyDuAnCNTT/](https://nguyentatmanh.github.io/OnTap-QuanLyDuAnCNTT/)**  
> *(Hoạt động trơn tru trên mọi thiết bị: Máy tính bảng, PC, Laptop, Điện thoại. Không cần cài đặt.)*

---

Ứng dụng web ôn tập trắc nghiệm toàn diện cho học phần **Quản lý dự án Công nghệ Thông tin**, được xây dựng theo phong cách **thẻ học lớn toàn màn hình (Quizlet / Flashcard)** với hệ thống âm thanh mô phỏng tự nhiên và khả năng tra cứu, đối chiếu tài liệu gốc đến từng số trang PDF.

---

## ✨ Điểm nổi bật & Tính năng chính

### 1. Giao diện hiện đại & Trải nghiệm thị giác (Modern UI/UX)
* **Phong cách Flashcard tập trung**: Hiển thị câu hỏi dạng thẻ lớn trung tâm với tỷ lệ chữ và khoảng cách tối ưu cho việc tập trung ghi nhớ sâu.
* **Bộ font chữ cao cấp**: Tích hợp font **Plus Jakarta Sans** chuẩn quốc tế kết hợp **JetBrains Mono** cho các nhãn phím tắt, hiển thị sắc nét trên mọi độ phân giải.
* **Hiệu ứng Mesh Gradient & Đổ bóng đa tầng**: Nền canvas kết hợp ánh sáng vệt mờ dịu mắt, hiệu ứng quầng sáng chuột mượt mà khi di chuyển qua các thẻ.
* **Thẻ phương án xúc giác (Tactile Keycap)**: Nút bấm A, B, C, D dạng phím cơ nổi khối kèm gợi ý phím tắt `[A]`, `[B]`, `[C]`, `[D]`.
* **Chuyển đổi giao diện linh hoạt**:
  * Chế độ **Sáng (Light)** / **Tối (Midnight Dark)** dịu mắt khi học đêm.
  * Tùy chọn **Bo mềm (Soft Radius)** hoặc **Góc phẳng (Sharp Radius)** theo sở thích.

### 2. Hệ thống âm thanh tự nhiên (Acoustic Web Audio API)
* **Hoạt động 100% Offline**: Không dùng file âm thanh bên ngoài, được tổng hợp thời gian thực bằng Web Audio API của trình duyệt.
* **Âm gõ phím (Tactile Wood Pop / Switch Click)**: Tiếng gõ phím cơ thanh nhẹ, êm ái, tạo cảm giác xúc giác cơ học thỏa mãn khi click.
* **Âm làm đúng (Marimba & Celesta Chime)**: Hợp âm Major 9th thăng hoa tươi vui, tạo cảm giác tưởng thưởng dopamine tích cực.
* **Âm làm sai (Muted Low-pass Wood Tone)**: Tiếng gỗ trầm nhẹ nhàng qua bộ lọc thông thấp, tạo cảm giác nhắc nhở khích lệ thay vì tiếng còi buzzer chói tai.
* **Âm chuyển câu (Silky Page Swoosh)**: Tiếng lướt trang sách lụa êm ái.

### 3. Đối chiếu nguồn tài liệu chuẩn xác đến từng trang PDF (Deep-Linking)
* Mọi câu hỏi đều có phần **Căn cứ trích dẫn từ tài liệu & Slide bài giảng**:
  * **Slide bài giảng môn học** (`tai-lieu/slides.pdf`): Đối chiếu chính xác theo từng số slide.
  * **Giáo trình Software Engineering (Roger Pressman 5th Ed)** (`tai-lieu/pressman.pdf`): Đối chiếu theo mục và số trang sách.
  * **Scrum Guide 2017 & 2020**: Trích dẫn quy chuẩn Scrum quốc tế.
  * **OMG UML 2.5.1 Specification**: Chuẩn hóa khái niệm mô hình hóa phần mềm.
* **Trình xem trực tiếp trong app**: Bấm **"📖 Xem trực tiếp trang trong PDF"** để mở modal xem trước ngay tại vị trí trang sách mà không làm gián đoạn bài học.
* **Điều hướng tab mới**: Nút **"↗ Mở tab mới"** tự động nhảy đến đúng trang PDF qua hash `#page=X`.

### 4. Hai chế độ hiển thị & Hai chế độ làm bài
* **Chế độ hiển thị đáp án**:
  * `✓ Hiện ngay`: Chọn xong lập tức hiện đúng/sai, âm thanh phản hồi và mở lời giải thích chi tiết.
  * `📋 Nộp mới hiện`: Chỉ lưu lựa chọn, cho phép cân nhắc và đổi phương án; chỉ hiển thị lời giải khi bấm nộp hoặc bấm chấm điểm riêng từng câu.
* **Chế độ học tập**:
  * `⚡ Luyện tập (Practice)`: Tự do duyệt 65 câu, xem giải thích, làm đi làm lại câu sai.
  * `⏱ Thi thử (Exam)`: Tùy chọn 10, 20, 30 hoặc toàn bộ câu hỏi, xáo trộn thứ tự, đồng hồ đếm ngược (15 - 60 phút) và bảng kết quả chấm điểm thang 10.

### 5. Ngăn kéo ma trận 65 câu hỏi (Drawer Matrix ☰ 1/65)
* Nhấn nút `☰ 1 / 65` ở góc trên bên phải để trượt ra ma trận toàn bộ 65 câu hỏi.
* Mã màu trực quan:
  * 🟢 **Xanh lá**: Đã làm đúng.
  * 🔴 **Đỏ**: Cần ôn lại (làm sai).
  * 🟡 **Vàng**: Câu có điều kiện / đọc ghi chú.
  * 🔵 **Xanh dương**: Đã chọn đáp án.
* **Lọc ôn tập có trọng tâm**: Lọc nhanh *Toàn bộ câu hỏi*, *Câu làm sai*, *Câu đã đánh dấu (Star)*, *Câu có điều kiện lập luận*.

### 6. Phím tắt thao tác nhanh (Keyboard Shortcuts)
| Phím | Chức năng |
| :--- | :--- |
| `1`, `2`, `3`, `4` hoặc `A`, `B`, `C`, `D` | Chọn phương án tương ứng |
| `←` (Mũi tên trái) | Quay lại câu trước |
| `→` (Mũi tên phải) | Chuyển sang câu tiếp theo |
| `F` | Đánh dấu sao / Lưu câu hỏi quan trọng |
| `R` | Làm lại câu hỏi hiện tại |
| `M` | Bật / Tắt nhanh âm thanh |

---

## 📁 Cấu trúc thư mục dự án

```text
Quản lý dự án CNTT/
├── index.html          # Ứng dụng web ôn tập Single-Page Application (HTML + CSS + JS)
├── questions.json      # Ngân hàng 65 câu hỏi trắc nghiệm chuẩn hóa (Dữ liệu gốc)
├── sync_questions.py   # Script Python tự động validate và đồng bộ JSON vào index.html
├── tai-lieu/           # Thư mục tài liệu tham khảo hỗ trợ nhảy trang PDF
│   ├── slides.pdf      # Slide bài giảng Quản lý dự án CNTT (83 slide)
│   └── pressman.pdf    # Giáo trình Software Engineering - Roger Pressman 5e (888 trang)
└── README.md           # Tài liệu hướng dẫn sử dụng dự án
```

---

## 🚀 Hướng dẫn khởi chạy & Sử dụng

### Cách 1: Truy cập trực tuyến qua GitHub Pages (Khuyên dùng - Nhanh nhất & Đầy đủ nhất)
* 👉 **Truy cập ngay:** [https://nguyentatmanh.github.io/OnTap-QuanLyDuAnCNTT/](https://nguyentatmanh.github.io/OnTap-QuanLyDuAnCNTT/)
* Hoạt động 100% trên trình duyệt (máy tính, máy tính bảng, điện thoại).
* Hỗ trợ đầy đủ âm thanh Web Audio và xem trước tài liệu PDF nhúng ngay trong app mà không gặp trở ngại chính sách bảo mật CORS / iframe nội bộ của một số trình duyệt.

### Cách 2: Mở trực tiếp file cục bộ (Offline)
* Tải repository về máy hoặc giải nén file mã nguồn.
* Nhấp đúp chuột trực tiếp vào file **`index.html`** để mở trên Google Chrome, Microsoft Edge, Firefox hoặc trình duyệt bất kỳ.
* Ứng dụng chạy hoàn toàn phía client (offline), không yêu cầu kết nối mạng hay cài đặt môi trường.

### Cách 3: Chạy qua Local HTTP Server (Khuyên dùng khi chạy local muốn xem PDF nhúng)
Một số trình duyệt hạn chế nạp `iframe` nội bộ khi mở qua giao thức `file:///`. Để tính năng mở xem PDF trực tiếp trong modal hoạt động trơn tru nhất khi phát triển ở local:
1. Mở terminal tại thư mục dự án:
   ```bash
   python -m http.server 8000
   ```
2. Mở trình duyệt và truy cập:
   ```text
   http://localhost:8000
   ```

---

## 🛠 Quản lý & Đồng bộ ngân hàng câu hỏi

Tất cả nội dung câu hỏi, phương án, đáp án, giải thích và liên kết PDF được lưu trữ có cấu trúc trong file **`questions.json`**.

Nếu bạn chỉnh sửa hoặc bổ sung câu hỏi trong `questions.json`:
1. Chạy lệnh đồng bộ bằng Python:
   ```bash
   python sync_questions.py
   ```
2. Kịch bản sẽ:
   * Kiểm tra tính toàn vẹn (validate cấu trúc, tính hợp lệ của từng câu).
   * Tự động nhúng trực tiếp ngân hàng câu hỏi mới vào thẻ `<script id="question-bank">` trong `index.html`.

---

## 📊 Thống kê nội dung ngân hàng câu hỏi

* **Tổng số câu hỏi**: 65 câu trắc nghiệm được biên soạn và chuẩn hóa.
* **Phân bổ theo chuyên đề**:
  * **Quản lý dự án CNTT (SPM)**: 44 câu (WBS, Gantt, CPM, PERT, COCOMO, FP, LOC, quản lý rủi ro, phân bổ nỗ lực 40-20-40, v.v.).
  * **Mô hình Scrum & Agile**: 15 câu (Scrum events, Scrum artifacts, vai trò Scrum Team, Sprint Goal, Sprint Retrospective, v.v.).
  * **Mô hình hóa phần mềm (UML)**: 6 câu (Use Case, Class Diagram, Association, Sequence, v.v.).
* **Trạng thái đối chiếu**:
  * `supported`: Đáp án chuẩn mực có đối chiếu trực tiếp từ giáo trình và slide.
  * `conditional`: Đáp án đề xuất kèm ghi chú điều kiện lập luận (phân tích các trường hợp câu hỏi câu từ chưa chặt chẽ theo thuật ngữ gốc).
  * `missing`: Câu hỏi thiếu dữ kiện hoặc chưa đủ cơ sở chốt duy nhất, có phân tích loại suy chi tiết.

---

## 📄 Bản quyền & Tài liệu tham khảo
* Tài liệu trích dẫn thuộc bản quyền của các tác giả và tổ chức tương ứng:
  * Roger S. Pressman — *Software Engineering: A Practitioner's Approach (5th Edition)*.
  * Ken Schwaber & Jeff Sutherland — *The Scrum Guide (2017, 2020)*.
  * Object Management Group (OMG) — *Unified Modeling Language (UML) Specification 2.5.1*.

---

## 🔗 Liên kết & Thông tin triển khai
* 🌐 **Ứng dụng trực tuyến (GitHub Pages)**: [https://nguyentatmanh.github.io/OnTap-QuanLyDuAnCNTT/](https://nguyentatmanh.github.io/OnTap-QuanLyDuAnCNTT/)
* 💻 **Mã nguồn dự án (GitHub Repository)**: [https://github.com/nguyentatmanh/OnTap-QuanLyDuAnCNTT](https://github.com/nguyentatmanh/OnTap-QuanLyDuAnCNTT)

