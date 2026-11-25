# Team

## Thông tin nhóm

- Tên nhóm: BuaDi
- Lớp: L3B
- Repo nhóm: `K5-L3B-DAY13-BuaDi-LaunchEconomics`
- URL repo, nhánh nộp, commit chốt: `https://github.com/LongNhat2kruoi/K5-L3B-DAY13-BuaDi-LaunchEconomics`, `lesylongnhat`, cập nhật sau commit cuối

## Thành viên

| STT | Họ tên | MSSV | Email | GitHub | Vai trò |
| --: | ------ | ---- | ----- | ------ | ------- |
|   1 | Vương Trường Giang | 2A202603834 | 26ai.giangvt@vinuni.edu.vn       |   vtgiang213      | Người kiểm số |
|   2 | Hoàng Quang Đạt | 2A202603808 | hoangquangdat182005@gmail.com | HoangQuangDat | Người gắn nhãn 1 |
|   3 | Lê Sỹ Long Nhật | 2A202603881 | lenhat07112005@gmail.com | LongNhat2kruoi | Người gắn nhãn 2, kiêm giữ hồ sơ |
|   4 | Vương Quang Thắng | 2A202603855 | 26ai.thangvq@vinuni.edu.vn | vuongquangthang | Người viết code |

Bốn vai của lab:

- **Người viết code:** viết và chạy `src/lab13.py`.
- **Người kiểm số:** tính tay một con số để đối chiếu, điền bảng.
- **Người gắn nhãn 1:** đọc đề, theo dõi điều kiện "Xong khi"; gắn nhãn 20 ca độc lập ở CP3.
- **Người gắn nhãn 2, kiêm giữ hồ sơ:** điền `report/team/ho_so_launch_v0.md` từ đầu buổi; gắn nhãn 20 ca độc lập ở CP3.

Đổi người viết code sau giờ giải lao, để ít nhất hai người trong nhóm tự tay tính được chi phí.

## Cá nhân

Mỗi thành viên đồng thời tạo một báo cáo riêng trong `report/` theo dạng:

```text
report/team/MSSV_HoTen.md
```

Ví dụ: `report/team/20241234_NguyenVanAn.md`.

Sao chép mục dưới đây cho từng thành viên.

## VuongTruongGiang-2A202603834

### Phần việc phụ trách

- Người kiểm số cho CP1 và CP2.

### Đóng góp cụ thể

- Phối hợp hoàn thiện bảng chi phí A1–A4 và bảng độ nhạy B1–B4; đối chiếu kết quả với đầu ra do người viết code cung cấp, sử dụng Codex hỗ trợ tính toán và trình bày.

### Bằng chứng

- `report/team/bang_chi_phi.md`; commit CP1 `5b4c000`; phép tính A1 với p = 0,8 và tối đa 2 lần cho kết quả 1,20 lần chạy trung bình.

## HoangQuangDat-2A202603808

### Phần việc phụ trách

- Người gắn nhãn 1; theo dõi điều kiện hoàn thành CP3.

### Đóng góp cụ thể

- Gắn nhãn độc lập 20 ca lỗi theo nguyên nhân gốc; đối chiếu năm loại lỗi và hỗ trợ chọn ca khắc phục.

### Bằng chứng

- `report/team/bang_loi.md`; báo cáo cá nhân `report/team/2A202603808_HoangQuangDat.md`.

## LeSyLongNhat

### Phần việc phụ trách

- Người gắn nhãn 2, kiêm giữ hồ sơ launch v0.

### Đóng góp cụ thể

- Gắn nhãn độc lập 20 ca lỗi; điền `ho_so_launch_v0.md`, cập nhật các mục chỉ số, pilot và rủi ro theo số liệu đã chạy.

### Bằng chứng

- `report/team/bang_loi.md`, `report/team/ho_so_launch_v0.md`, branch `lesylongnhat`.


## VuongQuangThang-2A202603855

### Phần việc phụ trách

- Người viết code (`src/lab13.py`), phụ trách tính toán toàn bộ số liệu cho nhiệm vụ A (CP1), B (CP2), D1 (CP4) và E1 (CP5), sau đó chuyển giao chạy kiểm thử chéo trên máy thành viên khác[cite: 5, 6].

### Đóng góp cụ thể

- Viết 3 hàm kiểm thử A1 đạt `1.20 · 1.25 · 1.25`, xây dựng hàm `mo_hinh` tính chi phí mỗi việc thành công, tách theo 4 loại yêu cầu (A3) và cộng chi phí cố định 40 triệu đ/tháng (A4)[cite: 1, 15].
- Lập trình chạy 9 kịch bản độ nhạy (B1), cặp biến đồng thời (B2), chi phí cả hệ thống theo giới hạn lượt chạy (B3) và kịch bản xem lại 100% (B4)[cite: 1, 15].
- Tính 5 câu cỡ mẫu pilot D1, tỉ lệ mở lại trong 7 ngày nền và 3 chỉ số tính thử E1 trên 1.200 yêu cầu[cite: 1, 15].

### Bằng chứng

- File `src/lab13.py` chạy sạch từ đầu đến cuối trên môi trường Python `.venv` và xuất toàn bộ bảng số liệu khớp 100% với đáp án chuẩn; báo cáo chi tiết tại `report/team/2A202603855_VuongQuangThang.md`[cite: 5, 15].
- branch : `vuongquangthang`
