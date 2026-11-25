# Bảng chi phí · Nhiệm vụ A và B

Số tính bằng `src/lab13.py`. Mọi con số tính từ cột `_simulated` ghi nhãn `simulated`. Mỗi câu trả lời không quá ba dòng, có ít nhất một con số.

## A1 · Ba phép thử đáp án biết trước

| Phép thử (p = 0,8) | Kết quả của nhóm |
| --- | --- |
| Số lần chạy trung bình, tối đa 2 lần | 1,20 |
| Số lần chạy trung bình, chạy đến khi đúng | 1,25 |
| Hệ số chi phí mỗi việc thành công, tối đa 3 lần | 1,25 |

**Tính tay** với xác suất thành công mỗi lần chạy p = 0,8, xác suất thất bại là 1 − p = 0,2:

1. **Tối đa 2 lần:** luôn chạy lần đầu; chỉ chạy lần hai nếu lần đầu thất bại. Số lần chạy trung bình = 1 + 0,2 = **1,20 lần**.
2. **Chạy đến khi đúng:** số lần chạy trung bình = 1 / p = 1 / 0,8 = **1,25 lần**.
3. **Chi phí mỗi việc thành công, tối đa 3 lần:**
   - Số lần chạy trung bình = 1 + 0,2 + 0,2^2 = **1,24 lần**.
   - Tỉ lệ thành công = 1 − 0,2^3 = **0,992**.
   - Hệ số chi phí = 1,24 / 0,992 = **1,25 lần chi phí của một lần chạy**.

## A2 · Mô hình chi phí từ trace

| Khoản | Số tiền (đ) | Nguồn | Nhãn |
| --- | ---: | --- | --- |
| Token | 245.585 | `logix_runs.csv` | tính từ trace |
| Tool | 84.000 | `logix_runs.csv` | tính từ trace |
| Trong đó, phần của lần chạy thứ 2 và 3 | 93.804 | attempt lớn hơn 1 | tính từ trace; đã nằm trong token và tool |
| Xem lại | 1.780.000 | 890 phút × 2.000 đ | simulated |
| Làm lại | 2.264.000 | 1.132 phút × 2.000 đ | simulated |
| Tổng chi phí | 4.373.585 | tổng bốn khoản | simulated |
| Số việc thành công | 978 | `ket_qua` | |
| Chi phí mỗi việc thành công | 4.472 | 4.373.585 / 978 | simulated |
| Hoá đơn token và tool chia cho số yêu cầu | 274,7 | 329.585 / 1.200 | tính từ trace |

- Chi phí mỗi việc thành công gấp khoảng 16,3 lần hoá đơn token và tool chia số yêu cầu (simulated).
- Làm lại lớn nhất: 2.264.000 / 4.373.585 = 51,8% tổng chi phí (simulated).

## A3 · Tách theo loại yêu cầu

| Loại | Số yêu cầu | Tỉ lệ thành công | Số lần chạy mỗi yêu cầu | Chi phí mỗi việc thành công | So với 12.000 đ |
| --- | ---: | ---: | ---: | ---: | ---: |
| noi_dia | 824 | 95,0% | 1,11 | 2.696 đ (simulated) | 0,22× (simulated) |
| hang_nang | 158 | 74,1% | 1,47 | 8.221 đ (simulated) | 0,69× (simulated) |
| quoc_te | 150 | 27,3% | 2,32 | 22.515 đ (simulated) | 1,88× (simulated) |
| doi_tac | 68 | 54,4% | 1,88 | 10.215 đ (simulated) | 0,85× (simulated) |

- `quoc_te` có chi phí 22.515 đ/việc thành công, bằng 1,88× mức nhân viên tự làm (simulated); tỷ lệ thành công 27,3%. Tỷ lệ lần chạy `ok` giảm từ 30,0% ở lần 1 xuống 11,4% và 2,2% ở lần 2 và 3; chạy lại tạo rất ít thành công bổ sung và tốn thêm chi phí.

Các tỷ số trong bảng so chi phí mỗi việc thành công với 12.000 đ/việc, chưa phải chi phí cả hệ thống. Tính thêm nhân viên xử lý 222 yêu cầu không thành công: (4.373.585 + 222 × 12.000) / 1.200 = 5.865 đ/yêu cầu, bằng 0,49× mức 12.000 đ (simulated; chưa cộng chi phí cố định).

## A4 · Chi phí cố định (phạm vi noi_dia + hang_nang)

| Khối lượng | Việc thành công mỗi tháng | Chi phí cố định mỗi việc | Chi phí mỗi việc thành công + cố định | So với 12.000 đ |
| --- | ---: | ---: | ---: | ---: |
| 45.000 yêu cầu/tháng | 33.750 | 1.185 đ | 4.599 đ (simulated) | 0,38× (simulated) |
| Một nửa khối lượng: 22.500 yêu cầu/tháng | 16.875 | 2.370 đ | 5.784 đ (simulated) | 0,48× (simulated) |

- Chưa đổi kết luận ở cả hai mức: 4.599 đ và 5.784 đ/việc thành công đều thấp hơn 12.000 đ (simulated). Với giả định giữ tỷ lệ trong mẫu, 45.000 × 900 / 1.200 = 33.750 việc thành công/tháng; chi phí cố định = 40.000.000 / 33.750 = 1.185 đ/việc.

## B1 · Đổi từng yếu tố

Chi phí gốc: **4.472 đ/việc thành công (simulated)**. Các kết quả và tỉ lệ thay đổi trong bảng đều là **simulated**.

| Kịch bản | Cách tính | Chi phí mỗi việc thành công | Thay đổi (%) |
| --- | --- | ---: | ---: |
| Giá token gấp đôi | 52 đ và 260 đ cho 1.000 token; giá tool giữ nguyên | 4.723 đ | +5,6% |
| Giá token giảm một nửa | 13 đ và 65 đ | 4.346 đ | −2,8% |
| Tỉ lệ xem lại gấp đôi | Tiền xem lại × 2 | 6.292 đ | +40,7% |
| Tỉ lệ xem lại giảm một nửa | Tiền xem lại ÷ 2 | 3.562 đ | −20,3% |
| Số ca làm lại gấp đôi | Tiền làm lại × 2 | 6.787 đ | +51,8% |
| Số ca làm lại giảm một nửa | Tiền làm lại ÷ 2 | 3.315 đ | −25,9% |
| Lương nhân viên tăng 25% | 2.500 đ mỗi phút | 5.506 đ | +23,1% |
| Chỉ cho chạy tối đa 2 lần | Bỏ lần chạy có attempt > 2; yêu cầu có so_lan_chay > 2 coi là chuyen_nhan_vien | 4.237 đ | −5,2% |
| Chỉ cho chạy 1 lần | Như trên với giới hạn 1 | 4.111 đ | −8,1% |

## B2 · Đổi một cặp và xếp hạng

- Giá token gấp đôi cùng lúc tỉ lệ xem lại gấp đôi: **6.543 đ/việc thành công, tăng 46,3%** (simulated). Tác động bằng tổng hai mức tăng riêng: 5,6% + 40,7% = 46,3%.
- Ba yếu tố ảnh hưởng mạnh nhất: **1. Số ca làm lại: +51,8% · 2. Tỉ lệ xem lại: +40,7% · 3. Lương nhân viên: +23,1%** (simulated).

## B3 · Giới hạn chạy lại có thật sự rẻ hơn

| Giới hạn | Tổng chi phí trợ lý | Số yêu cầu không thành công | Chi phí cả hệ thống | Chi phí mỗi việc thành công |
| --- | ---: | ---: | ---: | ---: |
| 1 lần | 3.621.781 đ (simulated) | 319 | 7.449.781 đ (simulated) | 4.111 đ (simulated) |
| 2 lần | 4.093.220 đ (simulated) | 234 | 6.901.220 đ (simulated) | 4.237 đ (simulated) |
| 3 lần | 4.373.585 đ (simulated) | 222 | 7.037.585 đ (simulated) | 4.472 đ (simulated) |

- Giới hạn **2 lần** rẻ nhất cho công ty: **6.901.220 đ** (simulated). Không trùng: giới hạn **1 lần** có chi phí mỗi việc thành công thấp nhất, **4.111 đ** (simulated), nhưng chuyển thêm 85 yêu cầu không thành công cho nhân viên so với 2 lần.

## B4 · Nếu phải xem lại tất cả

- Với 9 phút làm lại/ca, chi phí là **11.743 đ/việc thành công**, bằng **0,98×** 12.000 đ (simulated). Với thời gian làm lại trung bình khoảng 15,3 phút từ dữ liệu giả lập, chi phí là **12.415 đ**, bằng **1,03×** (simulated).
- Pilot cần đo xem có thể giảm tỉ lệ và thời gian xem lại một cách an toàn không. Ngưỡng hòa vốn cho mỗi lần xem lại khoảng **5,12 phút** với 9 phút làm lại, hoặc **4,80 phút** với mức trung bình giả lập khoảng 15,3 phút/ca (simulated).
