# Báo cáo cá nhân — Lê Sỹ Long Nhật - 2A202603881

## 1. Thông tin thành viên

- Họ tên: Lê Sỹ Long Nhật
- MSSV: 2A202603881
- Email: lenhat07112005@gmail.com
- Vai trong nhóm: Người gắn nhãn 2, kiêm giữ hồ sơ.

## 2. Phần việc phụ trách

- Gắn nhãn độc lập 20 ca lỗi ở CP3 theo năm loại lỗi của Google PAIR.
- Điền và cập nhật `report/team/ho_so_launch_v0.md` từ các kết quả A–D.
- Theo dõi phạm vi pilot, trạng thái bằng chứng, owner, rủi ro kinh tế và đề xuất cuối.

## 3. Đóng góp cụ thể

- Gắn nhãn 20/20 ca theo nguyên nhân gốc: 4 ca Do người dùng, 5 ca Hệ thống, 4 ca Ngữ cảnh, 4 ca Giới hạn hệ thống và 3 ca Ngầm.
- Hoàn thiện bảng đồng thuận 20/20 = 100% và bảng khắc phục 5 ca có event, ngưỡng/tần suất phát hiện và vai trò phụ trách.
- Hoàn thiện hồ sơ launch v0 gồm 7 mục: chi phí 4.472 đ/việc thành công, ba yếu tố nhạy nhất, so sánh 12.000 đ nhân viên tự làm, chỉ số, bảng lỗi, pilot plan và rủi ro kinh tế.
- Đối chiếu hồ sơ với kết quả chạy `src/lab13.py`: 978 việc thành công, chi phí cả hệ thống 5.865 đ/yêu cầu và giới hạn 2 lần chạy có chi phí cả hệ thống thấp nhất 6.901.220 đ.

## 4. Bằng chứng

- `report/team/bang_loi.md`: hai bộ nhãn độc lập, tỷ lệ đồng thuận và bảng khắc phục 5 ca.
- `report/team/ho_so_launch_v0.md`: hồ sơ 7 mục và đề xuất Go có điều kiện.
- `report/team/pilot_plan.yaml` và `report/team/chi_so.md`: kế hoạch pilot, chỉ số, event và rủi ro được dùng để cập nhật hồ sơ.
- Commit liên quan: `01745a9` hoàn thiện hồ sơ ban đầu; `10a4891` hoàn thiện các báo cáo và pilot plan.

## 5. Công cụ AI đã dùng

- Dùng Codex để đọc đề bài, trích xuất 20 ca lỗi từ tài liệu DOCX, đối chiếu số liệu với hướng dẫn và rà soát định dạng các file hồ sơ.
- Cách tự kiểm tra: chạy `python src/lab13.py`, kiểm tra `pilot_plan.yaml` bằng `yaml.safe_load`, kiểm tra không còn dấu hỏi ngoài chú thích, không có từ cấm trong `report/team` và chạy `git diff --check`.

## 6. Tự đánh giá

- Hoàn thành phần gắn nhãn độc lập và giữ hồ sơ theo đúng vai trò; các số liệu dựa trên đầu ra chương trình hoặc tài liệu đối chiếu, các số từ cột `_simulated` đều được ghi nhãn.
- Hạn chế còn lại là phiếu chấm hội đồng chưa có dữ liệu nhóm đối tác để điền kết quả duyệt chéo thực tế.
