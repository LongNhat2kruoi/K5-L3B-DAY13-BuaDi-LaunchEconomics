# Phiếu chấm hội đồng Gate 2a

Nhóm số n chấm nhóm số n + 1; nhóm cuối chấm nhóm 1. Chấm theo bằng chứng trong hồ sơ, không theo cách trình bày: một đề xuất No-go có lý do bằng số được điểm cao hơn một đề xuất Go bỏ qua con số bất lợi.

- Nhóm chấm (hội đồng): BuaDi (K5-L3B)
- Nhóm được chấm: HelloWorld (K5-L3B)

| Tiêu chí | 0 điểm | 5 điểm | 10 điểm | Điểm | Lý do (có số) |
| --- | --- | --- | --- | ---: | --- |
| Đề xuất khớp bằng chứng | Mâu thuẫn với số của chính nhóm | Khớp nhưng bỏ qua một con số bất lợi | Khớp, nêu cả con số bất lợi và cách xử lý | 5 | Đề xuất Go có điều kiện hợp lý nhưng hồ sơ gốc bỏ qua 2 con số bất lợi: (1) Mục 3 dùng `0,37×` (`4.472 đ` vs `12.000 đ`) mà quên cộng 222 ca chuyển nhân viên (đúng là `5.865 đ = 0,49×`); (2) Mục 6 chọn MDE `+6 điểm` nhưng không nêu rủi ro `power` giảm còn `0,64` nếu tác động thật chỉ đạt `+5 điểm`. |
| Số giả lập và phạm vi | Không nhãn; phạm vi "mọi yêu cầu" | Có nhãn hoặc có thu hẹp phạm vi | Nhãn ở mọi số giả lập; phạm vi thu hẹp có lý do bằng số | 10 | Gắn nhãn `simulated` đầy đủ ở các mục 1, 2, 3, 7; thu hẹp phạm vi về `noi_dia` (`0,22×`) và `hang_nang` (`0,69×`), loại `quoc_te` (`1,88×`) có lý do bằng số rõ ràng. |
| Pilot ra được quyết định | Không đối chứng hoặc thiếu cỡ mẫu | Đủ cỡ mẫu, luật dừng chung chung | Tách được tác động, đủ mẫu, luật dừng có ngưỡng, thời hạn, người có quyền dừng | 10 | Chia cụm ngẫu nhiên theo nhân viên `20 + 20` (đạt ≥ 20 cụm/nhóm), đủ cỡ mẫu `m ≥ 299` cho MDE `+6 điểm`, có đủ 3 luật dừng kèm ngưỡng, thời hạn và vai trò phụ trách. |
| **Tổng** | | | | **25 / 30** | |

**Quyết định của hội đồng:** Go có điều kiện

**Lý do:** Mô hình chi phí và thiết kế chia cụm `20 + 20` nhân viên tách được tác động; tuy nhiên nhóm cần cập nhật lại thời gian gom mẫu bước 0,50 từ 8 ngày lên ≥ 10 ngày (+ 7 ngày theo dõi), áp dụng xem lại phân tầng theo rủi ro (`hang_nang` 100%, `noi_dia` hạ bậc về 20–25%), và bổ sung chữ ký chấp nhận rủi ro `power = 0,64` ở mức `+5 điểm` trước khi mở pilot.

**Một câu hỏi cho đội trình:** Ở Mục 6, nhóm tính chỉ cần `8 ngày` để gom đủ `299 yêu cầu/nhân viên` trong phạm vi `noi_dia + hang_nang` (trong khi 81,8% lưu lượng chỉ cho ~30,7 YC hợp lệ/người/ngày, cần tối thiểu 10 ngày gom mẫu + 7 ngày theo dõi). Con số 8 ngày tính từ đâu, và làm sao giải quyết mâu thuẫn ở Điều kiện 2 khi ép tỉ lệ xem lại `< 50%` ngay từ Ngày 7 trong khi tỉ lệ mở lại nền đã là `3,97%`?

**Câu trả lời của đội trình (ghi lại tại buổi):** Nhóm thừa nhận con số 8 ngày tính trên tổng lưu lượng chưa lọc phạm vi (`299 ÷ 37,5 = 8 ngày`) và điều chỉnh bước 0,50 thành `≥ 10 ngày` gom mẫu + `7 ngày` theo dõi (= 17 ngày, tổng pilot 3–4 tuần khớp ngày `2027-01-05`). Với Điều kiện 2, nhóm dời mốc kiểm tra sang cuối bước `0,25` và áp dụng xem lại phân tầng: giữ xem lại `100%` cho `hang_nang` (chiếm 16,1%, mở lại 10,6% nếu không xem lại) và hạ dần xem lại `noi_dia` (chiếm 83,9%, mở lại nền 3,16%) xuống `20–25%` khi đạt điều kiện an toàn (`sua + bo < 15%`, mở lại không vượt đối chứng `+2 điểm %`, 0 ca hoàn trùng), giúp kéo tỉ lệ xem lại chung về ~37% (< 50%); nếu không đạt sẽ ưu tiên luật an toàn và thu hẹp về chỉ `noi_dia`.