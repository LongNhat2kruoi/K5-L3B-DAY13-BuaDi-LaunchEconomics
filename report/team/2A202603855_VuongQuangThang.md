## 2. Phần việc phụ trách

- Thiết lập môi trường Python (`.venv`) và hoàn thiện toàn bộ mã nguồn tính toán trong `src/lab13.py` cho các nhiệm vụ A (CP1), B (CP2), D1 (CP4) và tính thử chỉ số E1 (CP5)[cite: 1, 2].
- Xuất bộ số liệu chuẩn xác để bàn giao cho Người kiểm số điền `report/team/bang_chi_phi.md` và Người giữ hồ sơ tổng hợp `report/team/pilot_plan.yaml`, `report/team/chi_so.md`, `report/team/ho_so_launch_v0.md`[cite: 1, 6].
- Chuyển giao mã nguồn cho thành viên khác trong nhóm chạy kiểm thử chéo trên máy thứ hai và tham gia giải trình số liệu tại phiên duyệt chéo Gate 2a[cite: 5, 6].

## 3. Đóng góp cụ thể

- **Nhiệm vụ A (CP1):** Hoàn thiện 3 hàm kiểm thử A1 (`so_lan_chay_ky_vong`, `ti_le_thanh_cong`, `he_so_chi_phi_moi_viec_thanh_cong`) đạt chuẩn `1.20 · 1.25 · 1.25`; xây dựng hàm `mo_hinh` tính đầy đủ chi phí token, tool, xem lại (`simulated`), làm lại (`simulated`), tách chi phí theo 4 loại yêu cầu (`noi_dia`, `hang_nang`, `quoc_te`, `doi_tac`) và cộng chi phí cố định 40 triệu đ/tháng cho phạm vi `noi_dia` + `hang_nang`.
- **Nhiệm vụ B (CP2):** Lập trình chạy 9 kịch bản phân tích độ nhạy (B1), kịch bản biến thiên đồng thời cặp yếu tố token ×2 & xem lại ×2 (B2), tính tổng chi phí cả hệ thống theo giới hạn 1–3 lần chạy (B3) và mô phỏng kịch bản xem lại 100% kèm ngưỡng hòa vốn (B4).
- **Nhiệm vụ D (CP4):** Viết hàm tính 5 bài toán cỡ mẫu D1 (theo yêu cầu, theo nhân viên, theo depot, và mức chênh 6 điểm phần trăm) cùng power thực tế khi mức tăng thật đạt 5 điểm (`0.64`), đồng thời tính tỉ lệ mở lại trong 7 ngày hiện tại (`4.25%` toàn mẫu, `3.97%` phạm vi pilot) để làm căn cứ đặt luật dừng an toàn.
- **Nhiệm vụ E (CP5):** Bổ sung đoạn code tính thử 3 chỉ số trên 1.200 yêu cầu cho mục E1 (`82.83%` chỉ số chính, `27.12%` tỉ lệ bỏ qua gợi ý, `4.25%` lỗi lọt đến khách)[cite: 15].

## 4. Bằng chứng

- **File mã nguồn:** `src/lab13.py` (commit: `[Điền mã commit sau khi git push]`).
- **Kết quả chạy thực tế từ terminal (`cd src && python lab13.py`):**

```text
=== NHIỆM VỤ A1 · BA PHÉP THỬ ĐÁP ÁN BIẾT TRƯỚC ===
Ba phép thử đáp án biết trước: ĐẠT
- p=0.8, tối đa 2 lần: 1.20
- p=0.8, chạy đến khi đúng: 1.25
- p=0.8, hệ số chi phí (tối đa 3 lần): 1.25

=== NHIỆM VỤ A2 · MÔ HÌNH CHI PHÍ TỪ TRACE ===
Token (mọi lần chạy)                    245,585 [đo từ trace]
Tool (5,600 lần gọi)                     84,000 [đo từ trace]
Trong đó, lần chạy thứ 2 và 3            93,804 [đo từ trace]
Xem lại (890 phút)                    1,780,000 [simulated]
Làm lại (1,132 phút)                  2,264,000 [simulated]
Tổng chi phí                          4,373,585 [có phần simulated]
Số việc thành công                          978 
Chi phí mỗi việc thành công               4,472 [simulated]
Hoá đơn token + tool / yêu cầu            274.7 [đo từ trace]
Hệ số gấp hoá đơn token+tool/yêu cầu: 16.3 lần [simulated]
Khoản lớn nhất: Làm lại [simulated] (51.8%); tổng giờ nhân viên: 92.5% [simulated]
Chi phí cả hệ thống/yêu cầu (cộng 222 ca không thành công × 12,000 đ): 5,865 đ/yêu cầu = 0.49× của 12,000 đ [simulated]

=== NHIỆM VỤ A3 · TÁCH THEO LOẠI YÊU CẦU ===
Loại           Số YC   Thành công  Lần chạy/YC    CPS [sim]  So 12.000đ
noi_dia          824        95.0%         1.11       2,696đ       0.22×
hang_nang        158        74.1%         1.47       8,221đ       0.69×
quoc_te          150        27.3%         2.32      22,515đ       1.88×
doi_tac           68        54.4%         1.88      10,215đ       0.85×

=== NHIỆM VỤ A4 · CHI PHÍ CỐ ĐỊNH (PHẠM VI noi_dia + hang_nang) ===
45.000 yêu cầu/tháng         | TC/tháng:  33,750 | Cố định/việc:  1,185 đ | CPS + cố định:  4,599 đ (0.38×) [simulated]
Một nửa (22.500 yc/tháng)    | TC/tháng:  16,875 | Cố định/việc:  2,370 đ | CPS + cố định:  5,784 đ (0.48×) [simulated]

=== NHIỆM VỤ B1 · ĐỔI TỪNG YẾU TỐ (SO VỚI GỐC A2) ===
Gốc (A2)                           4,472 đ        [simulated]
Giá token gấp đôi                  4,723 đ   +5.6% [simulated]
Giá token giảm một nửa             4,346 đ   -2.8% [simulated]
Tỉ lệ xem lại gấp đôi              6,292 đ  +40.7% [simulated]
Tỉ lệ xem lại giảm một nửa         3,562 đ  -20.3% [simulated]
Số ca làm lại gấp đôi              6,787 đ  +51.8% [simulated]
Số ca làm lại giảm một nửa         3,315 đ  -25.9% [simulated]
Lương nhân viên tăng 25%           5,506 đ  +23.1% [simulated]
Chỉ cho chạy tối đa 2 lần          4,237 đ   -5.2% [simulated]
Chỉ cho chạy 1 lần                 4,111 đ   -8.1% [simulated]

=== NHIỆM VỤ B2 · ĐỔI ĐỒNG THỜI & XẾP HẠNG ===
Token ×2 + Xem lại ×2: 6,543 đ (+46.3%) [simulated]
Xếp hạng 3 yếu tố tác động mạnh nhất: 1. Số ca làm lại (+51.8%) · 2. Tỉ lệ xem lại (+40.7%) · 3. Lương nhân viên (+23.1%)

=== NHIỆM VỤ B3 · CHI PHÍ CẢ HỆ THỐNG THEO GIỚI HẠN CHẠY LẠI ===
Giới hạn    Tổng trợ lý [sim]   Không TC  Cả hệ thống [sim]    CPS [sim]
1 lần              3,621,781đ        319         7,449,781đ       4,111đ
2 lần              4,093,220đ        234         6,901,220đ       4,237đ
3 lần              4,373,585đ        222         7,037,585đ       4,472đ

=== NHIỆM VỤ B4 · XEM LẠI 100% (PHẠM VI noi_dia + hang_nang) ===
Số ca xem lại 100% (có >=1 lần ok): 948 | Số ca làm lại: 48 | Thành công: 900
TH1 (9 phút/ca làm lại): Tổng = 10,568,513 đ | CPS = 11,743 đ (0.98×) | Hoà vốn xem lại <= 5.12 phút [simulated]
TH2 (15.3 phút/ca làm lại thực tế): Tổng = 11,173,054 đ | CPS = 12,415 đ (1.03×) | Hoà vốn xem lại <= 4.80 phút [simulated]

=== NHIỆM VỤ D1 · CỠ MẪU PILOT (baseline=0.70, alpha=0.05, power=0.80, ICC=0.02) ===
a) Chia theo yêu cầu (mục tiêu +5 điểm): 1,251 yêu cầu/nhóm
b) Theo nhân viên, m=75: DE = 2.48 -> 3,103 yêu cầu/nhóm (42 NV/nhóm, tổng 84 > 40: không đủ người)
c) 20 nhân viên/nhóm: hiệu dụng tối đa c/ICC = 1,000 (< 1,251: không đạt)
d) 6 depot/nhóm: hiệu dụng tối đa c/ICC = 300
e) Mức chênh +6 điểm (859/nhóm), 20 NV/nhóm: m >= 299 yêu cầu/người (DE = 6.96)
Power thực tế khi n=859 nếu mức tăng thật chỉ +5 điểm: 0.64 (64.2%)
Tỉ lệ mo_lai_trong_7_ngay == 1 toàn bộ 1.200 yc: 4.25% (51/1200)
Tỉ lệ mo_lai_trong_7_ngay == 1 phạm vi noi_dia + hang_nang: 3.97% (39/982)

=== NHIỆM VỤ E1 · BA CHỈ SỐ TÍNH THỬ TRÊN 1.200 YÊU CẦU ===
Chính (% đóng <=24h và không mở lại 7 ngày): 82.83% (994/1200)
Dùng (tỉ lệ sua + bo trên số được xem lại):   27.12% (48/177)
An toàn (% mở lại trong 7 ngày):             4.25% (51/1200)
```

## 5. Công cụ AI đã dùng

- **Công cụ sử dụng:** Gemini
- **Mục đích sử dụng:** Rà soát quy tắc đọc dữ liệu (`keep_default_na=False`), tối ưu cấu trúc hàm `mo_hinh` để tái sử dụng cho nhiều kịch bản độ nhạy, và định dạng bảng kết quả xuất ra terminal.
- **Cách tự kiểm tra kết quả:**
  - Chạy kiểm thử chốt chặn A1 và xác nhận đạt chính xác `1.20`, `1.25`, `1.25` trước khi tính trên dữ liệu trace.
  - Kiểm tra tính đối xứng tuyến tính ở bảng độ nhạy B1 (mức giảm khi giảm một nửa tham số bằng đúng một nửa mức tăng khi nhân đôi tham số).
  - Đối chiếu chéo toàn bộ số liệu đầu ra với con số tính tay của Người kiểm số và bảng đối chiếu trong tài liệu hướng dẫn, đảm bảo khớp 100% (nằm trong giới hạn sai số cho phép <= 2%).

## 6. Tự đánh giá

- Hoàn thành đúng tiến độ toàn bộ phần lập trình và tính toán số liệu từ CP1 đến E1, giúp nhóm có đủ dữ liệu sớm để thảo luận thiết kế pilot (CP4) và hoàn thiện hồ sơ duyệt chéo Gate 2a (CP5).
- Nắm vững bản chất kinh tế của chi phí mỗi việc thành công (tử số tính cả lần chạy lỗi và giờ công nhân viên xem lại/làm lại; mẫu số chỉ đếm yêu cầu thành công) cũng như giới hạn trần cỡ mẫu khi chia nhóm pilot theo cụm.