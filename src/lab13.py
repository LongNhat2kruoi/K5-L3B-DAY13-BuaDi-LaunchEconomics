"""Lab 13 · Định giá agent và lập kế hoạch pilot (Gate 2a) — bài làm của nhóm (file nộp).
Chạy trong thư mục src/: python3 lab13.py   (cần pandas; Nhiệm vụ D cần thêm statsmodels)
Không cần khoá API. Điền các chỗ ghi VIẾT Ở ĐÂY (đánh dấu TODO CP1…CP4). Dữ liệu trong hai file CSV là giả lập.
Bản gốc chưa sửa nằm ở lab13_starter.py.
"""
import math
from statistics import NormalDist

import pandas as pd
from statsmodels.stats.power import NormalIndPower
from statsmodels.stats.proportion import proportion_effectsize

# Bảng giá GIẢ ĐỊNH của lab (không phải giá thật của nhà cung cấp nào)
GIA_VAO = 26        # đồng cho 1.000 token đầu vào
GIA_RA = 130        # đồng cho 1.000 token đầu ra
GIA_TOOL = 15       # đồng cho 1 lần gọi tool
LUONG_PHUT = 2000   # đồng cho 1 phút của nhân viên (đã gồm bảo hiểm, văn phòng)
BASELINE = 12000    # đồng cho 1 yêu cầu khi nhân viên tự làm (6 phút)
CHI_PHI_CO_DINH_THANG = 40_000_000  # đồng/tháng


# ---------- Nhiệm vụ A1 · Kinh tế của việc chạy lại ----------
def so_lan_chay_ky_vong(p, k=None):
    """Số lần chạy trung bình cho 1 yêu cầu khi mỗi lần đúng với xác suất p.
    k = số lần chạy tối đa; k=None nghĩa là chạy lại đến khi đúng."""
    return 1 / p if k is None else (1 - (1 - p) ** k) / p


def ti_le_thanh_cong(p, k=None):
    """Xác suất yêu cầu thành công sau tối đa k lần chạy."""
    return 1.0 if k is None else 1 - (1 - p) ** k


def he_so_chi_phi_moi_viec_thanh_cong(p, k=None):
    """Chi phí mỗi việc thành công, tính bằng bội số của giá một lần chạy."""
    return so_lan_chay_ky_vong(p, k) / ti_le_thanh_cong(p, k)


def kiem_tra_dap_an_biet_truoc():
    """Ba phép thử bắt buộc đạt 100% trước khi tính trên dữ liệu."""
    assert abs(so_lan_chay_ky_vong(0.8, 2) - 1.20) < 1e-9, 'p=0,8, tối đa 2 lần → 1,20 lần chạy'
    assert abs(so_lan_chay_ky_vong(0.8) - 1.25) < 1e-9, 'p=0,8, chạy đến khi đúng → 1,25 lần chạy'
    assert abs(he_so_chi_phi_moi_viec_thanh_cong(0.8, 3) - 1.25) < 1e-9, 'p=0,8, tối đa 3 lần → 1,25 lần giá một lần chạy'
    print('Ba phép thử đáp án biết trước: ĐẠT')
    print(f'  - p=0.8, tối đa 2 lần: {so_lan_chay_ky_vong(0.8, 2):.2f}')
    print(f'  - p=0.8, chạy đến khi đúng: {so_lan_chay_ky_vong(0.8):.2f}')
    print(f'  - p=0.8, hệ số chi phí (tối đa 3 lần): {he_so_chi_phi_moi_viec_thanh_cong(0.8, 3):.2f}')


# ---------- Nhiệm vụ A2 · Mô hình chi phí từ trace ----------
def mo_hinh(runs, reqs, gia_vao=26, gia_ra=130, gia_tool=15, luong_phut=2000,
            he_so_xem_lai=1.0, he_so_lam_lai=1.0, max_lan_chay=None):
    """Trả về dict gồm: token, tool, chay_lai, xem_lai, lam_lai, tong, thanh_cong, cps, hoa_don_moi_yc.
    - token, tool: cộng trên MỌI lần chạy trong runs, kể cả lần lỗi.
    - xem_lai, lam_lai: số phút (cột *_simulated) × luong_phut. Đây là số GIẢ LẬP, phải ghi nhãn simulated khi báo cáo.
    - thanh_cong: số yêu cầu có ket_qua == 'thanh_cong'.
    - max_lan_chay: nếu khác None, lọc attempt <= max_lan_chay và coi các ca vượt ngưỡng là chuyen_nhan_vien (0 phút simulated).
    """
    reqs = reqs.copy()
    runs = runs[runs['request_id'].isin(reqs['request_id'])]
    if max_lan_chay is not None:
        runs = runs[runs['attempt'] <= max_lan_chay]
        vuot = reqs['so_lan_chay'] > max_lan_chay
        reqs.loc[vuot, 'ket_qua'] = 'chuyen_nhan_vien'
        reqs.loc[vuot, ['phut_xem_lai_simulated', 'phut_lam_lai_simulated']] = 0

    tien_token = runs['tokens_in'] / 1000 * gia_vao + runs['tokens_out'] / 1000 * gia_ra
    tien_tool = runs['tool_calls'] * gia_tool
    xem_lai = reqs['phut_xem_lai_simulated'].sum() * luong_phut * he_so_xem_lai
    lam_lai = reqs['phut_lam_lai_simulated'].sum() * luong_phut * he_so_lam_lai
    tong = tien_token.sum() + tien_tool.sum() + xem_lai + lam_lai
    thanh_cong = int((reqs['ket_qua'] == 'thanh_cong').sum())
    return dict(
        token=tien_token.sum(),
        tool=tien_tool.sum(),
        chay_lai=(tien_token + tien_tool)[runs['attempt'] > 1].sum(),
        xem_lai=xem_lai,
        lam_lai=lam_lai,
        tong=tong,
        thanh_cong=thanh_cong,
        cps=tong / thanh_cong,
        hoa_don_moi_yc=(tien_token.sum() + tien_tool.sum()) / len(reqs),
    )


def co_mau(p1, p2, alpha=0.05, power=0.8):
    """Cỡ mẫu mỗi nhóm khi so sánh hai tỉ lệ độc lập."""
    za = NormalDist().inv_cdf(1 - alpha / 2)
    zb = NormalDist().inv_cdf(power)
    pb = (p1 + p2) / 2
    return math.ceil(
        (za * math.sqrt(2 * pb * (1 - pb)) + zb * math.sqrt(p1 * (1 - p1) + p2 * (1 - p2))) ** 2
        / (p2 - p1) ** 2
    )


def in_nhiem_vu_a(runs, reqs):
    """Chạy và in toàn bộ kết quả Nhiệm vụ A (A1–A4)."""
    print('\n=== NHIỆM VỤ A1 · BA PHÉP THỬ ĐÁP ÁN BIẾT TRƯỚC ===')
    kiem_tra_dap_an_biet_truoc()

    print('\n=== NHIỆM VỤ A2 · MÔ HÌNH CHI PHÍ TỪ TRACE ===')
    kq = mo_hinh(runs, reqs)
    tong_tool_calls = int(runs['tool_calls'].sum())
    phut_xem_lai = int(reqs['phut_xem_lai_simulated'].sum())
    phut_lam_lai = int(reqs['phut_lam_lai_simulated'].sum())

    dong_a2 = [
        ('Token (mọi lần chạy)', kq['token'], 'đo từ trace'),
        (f'Tool ({tong_tool_calls:,} lần gọi)', kq['tool'], 'đo từ trace'),
        ('Trong đó, lần chạy thứ 2 và 3', kq['chay_lai'], 'đo từ trace'),
        (f'Xem lại ({phut_xem_lai:,} phút)', kq['xem_lai'], 'simulated'),
        (f'Làm lại ({phut_lam_lai:,} phút)', kq['lam_lai'], 'simulated'),
        ('Tổng chi phí', kq['tong'], 'có phần simulated'),
        ('Số việc thành công', kq['thanh_cong'], ''),
        ('Chi phí mỗi việc thành công', kq['cps'], 'simulated'),
        ('Hoá đơn token + tool / yêu cầu', kq['hoa_don_moi_yc'], 'đo từ trace'),
    ]
    for ten, gia_tri, nhan in dong_a2:
        fmt = f'{gia_tri:>12,.1f}' if ten.startswith('Hoá đơn') else f'{gia_tri:>12,.0f}'
        nhan_str = f'[{nhan}]' if nhan else ''
        print(f'{ten:34s} {fmt} {nhan_str}')

    he_so_gap = kq['cps'] / kq['hoa_don_moi_yc']
    khoan = {'Token': kq['token'], 'Tool': kq['tool'], 'Xem lại [simulated]': kq['xem_lai'], 'Làm lại [simulated]': kq['lam_lai']}
    khoan_lon_nhat = max(khoan, key=khoan.get)
    ti_trong_lon_nhat = khoan[khoan_lon_nhat] / kq['tong'] * 100
    ti_trong_gio_nv = (kq['xem_lai'] + kq['lam_lai']) / kq['tong'] * 100

    khong_thanh_cong = len(reqs) - kq['thanh_cong']
    he_thong_moi_yc = (kq['tong'] + khong_thanh_cong * BASELINE) / len(reqs)
    print(f'Hệ số gấp hoá đơn token+tool/yêu cầu: {he_so_gap:.1f} lần [simulated]')
    print(f'Khoản lớn nhất: {khoan_lon_nhat} ({ti_trong_lon_nhat:.1f}%); tổng giờ nhân viên: {ti_trong_gio_nv:.1f}% [simulated]')
    print(f'Chi phí cả hệ thống/yêu cầu (cộng {khong_thanh_cong} ca không thành công × {BASELINE:,} đ): '
          f'{he_thong_moi_yc:,.0f} đ/yêu cầu = {he_thong_moi_yc / BASELINE:.2f}× của {BASELINE:,} đ [simulated]')

    print('\n=== NHIỆM VỤ A3 · TÁCH THEO LOẠI YÊU CẦU ===')
    print(f"{'Loại':12s} {'Số YC':>7s} {'Thành công':>12s} {'Lần chạy/YC':>12s} {'CPS [sim]':>12s} {'So 12.000đ':>11s}")
    for loai in ['noi_dia', 'hang_nang', 'quoc_te', 'doi_tac']:
        sub = reqs[reqs['loai'] == loai]
        r = mo_hinh(runs, sub)
        tl_tc = r['thanh_cong'] / len(sub) * 100
        lan_chay_tb = sub['so_lan_chay'].mean()
        print(f"{loai:12s} {len(sub):7d} {tl_tc:11.1f}% {lan_chay_tb:12.2f} {r['cps']:11,.0f}đ {r['cps'] / BASELINE:10.2f}×")

    runs_loai = runs.merge(reqs[['request_id', 'loai']], on='request_id')
    runs_loai['is_ok'] = (runs_loai['status'] == 'ok').astype(float)
    pivot_ok = runs_loai.pivot_table(index='loai', columns='attempt', values='is_ok', aggfunc='mean')
    print('\nTỉ lệ status == "ok" theo loại và lần thử (attempt):')
    print((pivot_ok * 100).round(1).to_string(float_format=lambda x: f'{x:.1f}%'))

    print('\n=== NHIỆM VỤ A4 · CHI PHÍ CỐ ĐỊNH (PHẠM VI noi_dia + hang_nang) ===')
    reqs_pilot = reqs[reqs['loai'].isin(['noi_dia', 'hang_nang'])]
    kq_pilot = mo_hinh(runs, reqs_pilot)
    ti_le_tc_pham_vi = kq_pilot['thanh_cong'] / len(reqs)
    for ten_kl, khoi_luong in [('45.000 yêu cầu/tháng', 45000), ('Một nửa (22.500 yc/tháng)', 22500)]:
        tc_thang = khoi_luong * ti_le_tc_pham_vi
        co_dinh_moi_viec = CHI_PHI_CO_DINH_THANG / tc_thang
        tong_cps = kq_pilot['cps'] + co_dinh_moi_viec
        print(f'{ten_kl:28s} | TC/tháng: {tc_thang:7,.0f} | Cố định/việc: {co_dinh_moi_viec:6,.0f} đ '
              f'| CPS + cố định: {tong_cps:6,.0f} đ ({tong_cps / BASELINE:.2f}×) [simulated]')

    return kq, kq_pilot, reqs_pilot


def in_nhiem_vu_b(runs, reqs, kq_goc, kq_pilot, reqs_pilot):
    """Chạy và in toàn bộ kết quả Nhiệm vụ B (B1–B4)."""
    print('\n=== NHIỆM VỤ B1 · ĐỔI TỪNG YẾU TỐ (SO VỚI GỐC A2) ===')
    kich_ban = {
        'Giá token gấp đôi': dict(gia_vao=52, gia_ra=260),
        'Giá token giảm một nửa': dict(gia_vao=13, gia_ra=65),
        'Tỉ lệ xem lại gấp đôi': dict(he_so_xem_lai=2.0),
        'Tỉ lệ xem lại giảm một nửa': dict(he_so_xem_lai=0.5),
        'Số ca làm lại gấp đôi': dict(he_so_lam_lai=2.0),
        'Số ca làm lại giảm một nửa': dict(he_so_lam_lai=0.5),
        'Lương nhân viên tăng 25%': dict(luong_phut=2500),
        'Chỉ cho chạy tối đa 2 lần': dict(max_lan_chay=2),
        'Chỉ cho chạy 1 lần': dict(max_lan_chay=1),
    }
    goc = kq_goc['cps']
    print(f"{'Gốc (A2)':30s} {goc:9,.0f} đ        [simulated]")
    for ten, kw in kich_ban.items():
        cps = mo_hinh(runs, reqs, **kw)['cps']
        pct = (cps / goc - 1) * 100
        print(f'{ten:30s} {cps:9,.0f} đ {pct:+6.1f}% [simulated]')

    print('\n=== NHIỆM VỤ B2 · ĐỔI ĐỒNG THỜI & XẾP HẠNG ===')
    cps_kep = mo_hinh(runs, reqs, gia_vao=52, gia_ra=260, he_so_xem_lai=2.0)['cps']
    print(f'Token ×2 + Xem lại ×2: {cps_kep:,.0f} đ ({(cps_kep / goc - 1) * 100:+.1f}%) [simulated]')
    print('Xếp hạng 3 yếu tố tác động mạnh nhất: 1. Số ca làm lại (+51.8%) · 2. Tỉ lệ xem lại (+40.7%) · 3. Lương nhân viên (+23.1%)')

    print('\n=== NHIỆM VỤ B3 · CHI PHÍ CẢ HỆ THỐNG THEO GIỚI HẠN CHẠY LẠI ===')
    print(f"{'Giới hạn':10s} {'Tổng trợ lý [sim]':>18s} {'Không TC':>10s} {'Cả hệ thống [sim]':>18s} {'CPS [sim]':>12s}")
    for gioi_han in [1, 2, 3]:
        r = mo_hinh(runs, reqs, max_lan_chay=gioi_han)
        khong_tc = len(reqs) - r['thanh_cong']
        he_thong = r['tong'] + khong_tc * BASELINE
        print(f"{f'{gioi_han} lần':10s} {r['tong']:17,.0f}đ {khong_tc:10d} {he_thong:17,.0f}đ {r['cps']:11,.0f}đ")

    print('\n=== NHIỆM VỤ B4 · XEM LẠI 100% (PHẠM VI noi_dia + hang_nang) ===')
    runs_pilot = runs[runs['request_id'].isin(reqs_pilot['request_id'])]
    ok_ids = runs_pilot.loc[runs_pilot['status'] == 'ok', 'request_id'].unique()
    so_ca_xem_lai = int(reqs_pilot['request_id'].isin(ok_ids).sum())
    so_ca_lam_lai = int((reqs_pilot['ket_qua'] == 'lam_lai').sum())
    tien_xem_lai_100 = so_ca_xem_lai * 5 * LUONG_PHUT
    tien_token_tool_pilot = kq_pilot['token'] + kq_pilot['tool']
    tc_pilot = kq_pilot['thanh_cong']

    # Trường hợp 1: giả định 9 phút/ca làm lại
    tien_lam_lai_9 = so_ca_lam_lai * 9 * LUONG_PHUT
    tong_9 = tien_xem_lai_100 + tien_lam_lai_9 + tien_token_tool_pilot
    cps_9 = tong_9 / tc_pilot
    hoa_von_9 = (BASELINE * tc_pilot - tien_lam_lai_9 - tien_token_tool_pilot) / (so_ca_xem_lai * LUONG_PHUT)

    # Trường hợp 2: trung bình thực tế phut_lam_lai_simulated trên các ca lam_lai
    lam_lai_tb_toan_bo = reqs.loc[reqs['ket_qua'] == 'lam_lai', 'phut_lam_lai_simulated'].mean()
    tien_lam_lai_thuc = so_ca_lam_lai * lam_lai_tb_toan_bo * LUONG_PHUT
    tong_thuc = tien_xem_lai_100 + tien_lam_lai_thuc + tien_token_tool_pilot
    cps_thuc = tong_thuc / tc_pilot
    hoa_von_thuc = (BASELINE * tc_pilot - tien_lam_lai_thuc - tien_token_tool_pilot) / (so_ca_xem_lai * LUONG_PHUT)

    print(f'Số ca xem lại 100% (có >=1 lần ok): {so_ca_xem_lai} | Số ca làm lại: {so_ca_lam_lai} | Thành công: {tc_pilot}')
    print(f'TH1 (9 phút/ca làm lại): Tổng = {tong_9:,.0f} đ | CPS = {cps_9:,.0f} đ ({cps_9 / BASELINE:.2f}×) | '
          f'Hoà vốn xem lại <= {hoa_von_9:.2f} phút [simulated]')
    print(f'TH2 ({lam_lai_tb_toan_bo:.1f} phút/ca làm lại thực tế): Tổng = {tong_thuc:,.0f} đ | CPS = {cps_thuc:,.0f} đ ({cps_thuc / BASELINE:.2f}×) | '
          f'Hoà vốn xem lại <= {hoa_von_thuc:.2f} phút [simulated]')


def in_nhiem_vu_d_va_e1(reqs, reqs_pilot):
    """Chạy và in toàn bộ kết quả Nhiệm vụ D (D1 & tỉ lệ lỗi nền) và E1."""
    print('\n=== NHIỆM VỤ D1 · CỠ MẪU PILOT (baseline=0.70, alpha=0.05, power=0.80, ICC=0.02) ===')
    icc = 0.02
    n_a = co_mau(0.70, 0.75)
    de_b = 1 + (75 - 1) * icc
    n_b = math.ceil(n_a * de_b)
    so_nv_b = math.ceil(n_b / 75)
    max_c = int(20 / icc)
    max_d = int(6 / icc)

    n_e = co_mau(0.70, 0.76)
    m_e = math.ceil(n_e * (1 - icc) / (20 - n_e * icc))
    de_e = 1 + (m_e - 1) * icc

    es_5pt = proportion_effectsize(0.75, 0.70)
    power_thuc_te = NormalIndPower().power(effect_size=es_5pt, nobs1=n_e, alpha=0.05, ratio=1.0)

    print(f'a) Chia theo yêu cầu (mục tiêu +5 điểm): {n_a:,} yêu cầu/nhóm')
    print(f'b) Theo nhân viên, m=75: DE = {de_b:.2f} -> {n_b:,} yêu cầu/nhóm ({so_nv_b} NV/nhóm, tổng {so_nv_b * 2} > 40: không đủ người)')
    print(f'c) 20 nhân viên/nhóm: hiệu dụng tối đa c/ICC = {max_c:,} (< {n_a:,}: không đạt)')
    print(f'd) 6 depot/nhóm: hiệu dụng tối đa c/ICC = {max_d:,}')
    print(f'e) Mức chênh +6 điểm ({n_e}/nhóm), 20 NV/nhóm: m >= {m_e} yêu cầu/người (DE = {de_e:.2f})')
    print(f'Power thực tế khi n={n_e} nếu mức tăng thật chỉ +5 điểm: {power_thuc_te:.2f} ({power_thuc_te * 100:.1f}%)')

    mo_lai_all = reqs['mo_lai_trong_7_ngay'].mean()
    mo_lai_pilot = reqs_pilot['mo_lai_trong_7_ngay'].mean()
    print(f"Tỉ lệ mo_lai_trong_7_ngay == 1 toàn bộ 1.200 yc: {mo_lai_all * 100:.2f}% ({int(reqs['mo_lai_trong_7_ngay'].sum())}/{len(reqs)})")
    print(f"Tỉ lệ mo_lai_trong_7_ngay == 1 phạm vi noi_dia + hang_nang: {mo_lai_pilot * 100:.2f}% ({int(reqs_pilot['mo_lai_trong_7_ngay'].sum())}/{len(reqs_pilot)})")

    print('\n=== NHIỆM VỤ E1 · BA CHỈ SỐ TÍNH THỬ TRÊN 1.200 YÊU CẦU ===')
    chinh_mask = (reqs['dong_trong_24h'] == 1) & (reqs['mo_lai_trong_7_ngay'] == 0)
    chinh = chinh_mask.mean()

    xem = reqs[reqs['duoc_xem_lai'] == 1]
    bo_qua_mask = xem['quyet_dinh_xem_lai'].isin(['sua', 'bo'])
    bo_qua = bo_qua_mask.mean()

    an_toan_mask = reqs['mo_lai_trong_7_ngay'] == 1
    an_toan = an_toan_mask.mean()

    print(f'Chính (% đóng <=24h và không mở lại 7 ngày): {chinh * 100:.2f}% ({int(chinh_mask.sum())}/{len(reqs)})')
    print(f'Dùng (tỉ lệ sua + bo trên số được xem lại):   {bo_qua * 100:.2f}% ({int(bo_qua_mask.sum())}/{len(xem)})')
    print(f'An toàn (% mở lại trong 7 ngày):             {an_toan * 100:.2f}% ({int(an_toan_mask.sum())}/{len(reqs)})')


if __name__ == '__main__':
    runs = pd.read_csv('logix_runs.csv')
    reqs = pd.read_csv('logix_requests.csv', keep_default_na=False)
    kq_goc, kq_pilot, reqs_pilot = in_nhiem_vu_a(runs, reqs)
    in_nhiem_vu_b(runs, reqs, kq_goc, kq_pilot, reqs_pilot)
    in_nhiem_vu_d_va_e1(reqs, reqs_pilot)
