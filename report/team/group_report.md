# Báo cáo nhóm

Báo cáo ngắn, tối đa 2 trang. Số liệu chi tiết nằm trong các file hồ sơ; ở đây chỉ dẫn lại con số chính.

## 1. Thông tin nhóm

- Tên nhóm: BuaDi
- Lớp: L3B
- Thành viên: xem `TEAM.md`

## 2. Mục tiêu và cách tiếp cận

Nhóm xây dựng hồ sơ pilot offline cho trợ lý hoàn phí LogiX-VN từ 1.624 trace agent và 1.200 yêu cầu. Các số từ cột `_simulated` được ghi rõ là `simulated`; phạm vi đề xuất được thu hẹp về `noi_dia` và `hang_nang`.

## 3. Giải pháp

Tóm tắt cách nhóm làm từng nhiệm vụ A–E và link tới file hồ sơ tương ứng.

Nhiệm vụ A–B dùng mô hình cộng chi phí token, tool, xem lại và làm lại; `bang_chi_phi.md` lưu các bảng A1–A4 và B1–B4. Nhiệm vụ C dùng hai bộ nhãn 20 ca và bảng khắc phục trong `bang_loi.md`. Nhiệm vụ D chọn chia theo nhân viên trong `pilot_plan.yaml`; nhiệm vụ E nối chỉ số, event và rủi ro trong `chi_so.md` và hồ sơ launch.

## 4. Kết quả

Con số chính (ghi nhãn `simulated` khi cần) và đề xuất cuối của `ho_so_launch_v0.md`. Kết quả duyệt chéo nhóm nhận được từ hội đồng.

Chi phí A2 là 4.472 đ/việc thành công (4.373.585 đ/978 việc, simulated); chi phí cả hệ thống là 5.865 đ/yêu cầu, bằng 0,49× nhân viên tự làm (simulated). `quoc_te` là 22.515 đ/việc, 1,88× baseline và chỉ thành công 27,3%; B3 cho thấy giới hạn 2 lần có chi phí cả hệ thống thấp nhất: 6.901.220 đ (simulated). Chỉ số thử là 82,83% chính, 27,12% dùng và 4,25% an toàn. Đề xuất cuối: Go có điều kiện.

## 5. Khó khăn và cách xử lý

Khó khăn chính là phân biệt chi phí trợ lý với chi phí nhân viên làm thay và không được dùng số tự phát. Nhóm xử lý bằng cách chạy `src/lab13.py`, đối chiếu A1–D1 với hướng dẫn, kiểm tra nhãn `simulated`, YAML và từ cấm trước khi đóng gói.

## 6. Tổng hợp đóng góp

Chi tiết đóng góp của từng thành viên nằm trong `TEAM.md`.

## 7. Hạn chế và hướng cải thiện

Dữ liệu là mẫu giả lập hai tuần, chưa có nhóm đối chứng nên chưa kết luận tác động nhân quả. Pilot phải ghi event có `trace_id`, thay phút giả lập bằng phút đo thật sau tuần 1 và theo dõi power khoảng 0,64 nếu tác động thật chỉ đạt +5 điểm.

## 8. Tài liệu tham khảo

Nguồn chính: `README.md`, `CHECKPOINTS.md`, `RULES.md`, `RUBRIC.md`, `docs/du_lieu_va_cong_thuc.md` và `docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md`.
