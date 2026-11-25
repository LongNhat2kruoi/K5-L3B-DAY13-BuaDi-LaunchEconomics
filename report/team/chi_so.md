# Đặc tả chỉ số, event và rủi ro kinh tế · Nhiệm vụ E1, E2

## E1 · Đặc tả chỉ số

| Loại | Chỉ số | Công thức | Tính thử trên 1.200 yêu cầu |
| --- | --- | --- | --- |
| Chính (kết quả) | % yêu cầu đóng trong 24 giờ và không mở lại trong 7 ngày | `dong_trong_24h` bằng 1 và `mo_lai_trong_7_ngay` bằng 0, chia tổng số yêu cầu | 82,83% (994/1.200) trong đợt chạy thử |
| Dùng | Tỉ lệ bỏ qua gợi ý | `quyet_dinh_xem_lai` là `sua` hoặc `bo`, chia số yêu cầu được xem lại | 27,12% (48/177) trong đợt chạy thử |
| An toàn | Tỉ lệ lỗi lọt đến khách | `mo_lai_trong_7_ngay` bằng 1, chia tổng số yêu cầu | 4,25% (51/1.200) trong đợt chạy thử |
| Dùng | Tỉ lệ yêu cầu được xem lại | `duoc_xem_lai` bằng 1, chia tổng số yêu cầu | Không cần tính thêm; dùng `duoc_xem_lai` để theo dõi |
| An toàn | Tỉ lệ hoàn sai qua kiểm tra mẫu | `audit_sample_checked` có `so_tien_dung` khác `so_tien_da_hoan`, chia số mẫu kiểm tra | Không cần tính từ hai CSV; cần event kiểm toán |

Viết "chỉ số trong đợt chạy thử là …", không viết "trợ lý đã nâng chỉ số": đợt chạy thử không có nhóm đối chứng.

## Danh sách event

Ít nhất sáu event, mỗi event có `trace_id` để nối với trace của agent.

| Event | Ai tạo | Thuộc tính chính | Thời điểm |
| --- | --- | --- | --- |
| refund_request_created | App khách | `request_id`, `loai`, `so_tien`, `arm`, `trace_id` | Khi khách gửi yêu cầu |
| agent_run_completed | Agent | `attempt`, `tokens_in/out`, `tool_calls`, `status`, `trace_id` | Sau mỗi lần chạy, kể cả lỗi |
| agent_suggestion_shown | Giao diện nhân viên | `staff_id`, `so_tien_de_xuat`, `trace_id` | Khi gợi ý hiển thị |
| staff_review_decision | Nhân viên | `giu/sua/bo`, `phut_xem_lai`, `trace_id` | Khi nhân viên gửi/sửa/bỏ |
| refund_ledger_write | Dịch vụ sổ cái | `idempotency_key`, `so_tien`, `ket_qua`, `trace_id` | Khi ghi sổ cái |
| ticket_closed | Hệ thống ticket | `closed_at`, `trace_id` | Khi đóng yêu cầu |
| ticket_reopened | Khách | `reopened_at`, `reason`, `trace_id` | Khi yêu cầu mở lại |
| audit_sample_checked | Nhân viên kiểm toán | `so_tien_dung`, `so_tien_da_hoan`, `checked_at`, `trace_id` | Khi hoàn tất kiểm tra mẫu |

**Kiểm tra chéo:** với mỗi chỉ số ở bảng E1, ghi event dùng để tính. Chỉ số nào không tính được từ danh sách event thì chưa đo được.

- Chỉ số chính dùng `ticket_closed` kết hợp `ticket_reopened` và `refund_request_created`; tỷ lệ bỏ qua dùng `staff_review_decision` trên số yêu cầu được xem lại; tỷ lệ được xem lại dùng `staff_review_decision` và `refund_request_created`; tỷ lệ mở lại dùng `ticket_reopened` và `refund_request_created`; kiểm toán dùng `audit_sample_checked`. Tính mở lại và chỉ số chính trên yêu cầu đã đủ 7 ngày theo dõi. Mọi event có `trace_id` để nối với yêu cầu; nhóm đối chứng cũng cần ID liên kết dù không có lượt chạy agent.

## E2 · Rủi ro kinh tế

Ít nhất hai dòng, số lấy từ bảng độ nhạy (`bang_chi_phi.md`).

| Rủi ro | Tác động đã tính | Dấu hiệu theo dõi | Hành động | Người phụ trách |
| --- | --- | --- | --- | --- |
| Số ca làm lại tăng gấp đôi | +51,8%, lên 6.787 đ/việc thành công (simulated) | Tỉ lệ làm lại theo tuần > 7%; đợt chạy thử trong phạm vi là 4,9% (simulated) | Thu hẹp về `noi_dia`, rà 20 trace làm lại | PM trợ lý hoàn phí |
| Phải xem lại 100% kéo dài | 11.743 đ = 0,98x; với 15,3 phút/ca là 12.415 đ = 1,03x (simulated) | Tỉ lệ yêu cầu được xem lại > 50% ở cuối bước rollout 0,25 | Giảm xem lại theo bậc khi tỷ lệ sửa + bỏ < 15% | Trưởng nhóm CSKH |
| Khối lượng thấp hơn dự kiến | Chi phí cố định thêm 1.185 đ/việc ở 45.000 yêu cầu/tháng, 2.370 đ nếu còn một nửa (simulated) | Số việc thành công/tuần < 50% kế hoạch | Không mở rộng pilot, xem lại chi phí cố định | PM trợ lý hoàn phí |
