from lib.alibaba_lib import Alibaba

if __name__ == '__main__':
    filename = 'image.jpg'  # Target Image file
    cookie = "lid=tb396890842116; ali_apache_track=c_mid=b2b-221424976583240034|c_lid=tb396890842116|c_ms=1;" \
             " cna=iG43G0zReRQCAX2xfC/oOAcc; alicnweb=touch_tb_at%3D1655737083279; " \
             "_m_h5_tk=d4395672f6d95d802fa564694d6619f8_1656076360926; _m_h5_tk_enc=76f6289c2093a04b5397d50de556db67;" \
             " __last_loginid__=tb396890842116; __cn_userid__=2214249765832; last_mid=b2b-221424976583240034;" \
             " __cn_logon_id__=tb396890842116; __cn_logon__=true; aliwwLastRefresh=1656067001214; " \
             "firstRefresh=1656067001386; lastRefresh=1656067001386; xlly_s=1; " \
             "cookie1=VTsQHZqBZ8kMD%2FudypBOZqlsusHk2Pjl61ym6lxVqDw%3D; cookie2=1d734b8fad41e4a0ca2d3242290b0921; " \
             "cookie17=UUpgQhI3CO11PkQAFw%3D%3D; sgcookie=E1002cI2r4SlGzA2W6LEzlzro4MB%2BdT2qIM3VzxVEcP7BP%2BGBVZzV%" \
             "2F68omQtu616jpb8tRRhmWviZEHjXzlosq0HtJxXom6qjpGIGjWPbtuuN7I%3D; hng=GLOBAL%7Czh-CN%7CUSD%7C999; " \
             "t=8cc8e6f1a625b07269660b50b1413908; _tb_token_=3b3e8be335930; sg=626; csg=0602c5d5; unb=2214249765832; " \
             "uc4=nk4=0%40FY4NCuKlmkol8gU%2B1FPDnsUCSgRbHaUWaw%3D%3D&id4=0%40U2gqzcKwCfn%2FUjUo0BNthaqu3aFJ9XX5;" \
             " ali_apache_tracktmp=c_w_signed=Y; EGG_SESS=_u99sqPgsongEkltyDOrbVAuRl2WRLuwbv3BYkn-1k2Bu-h_MbhYI8Q" \
             "IIfxO6YW0whoKSycgW0nL1eMTrezGGImw7AQxdvmYRnmsXRcLr7ITXN_BdbPkt5du9a7X1_QXvNgs3pNhyenAU9SSqUhZwHvhPDdiMj" \
             "iAwz-XEKhRUAra8NmGLaNPttDYEsGOxGWa32C4vZUQurlU5K7qKTGwVHQi1GhWVcfXv7au0rbUNUNBuTDznkrY1RQW9Y2gULPGb-f" \
             "1XJX-0xJ8lyDGh0ytnhnlrOHKccD7Wu4qiSPzF0R0L-TqooGoHsp8CsOCMzh2nah3Lez9nhNgWMB9xKXv_QEdXxAyJ5JYMpcPDNVX" \
             "bM_WrQJJ3NUUP-Vc47FxB-9ObBHGzank6cZ01bVwehCfQAtk5oORAbUaDxlrh1rgvSZBrp2fFNYvJ2wwtroL26ezh2W4NhWgZMOM" \
             "KIJRyHzNYVYErih-WAownV7S-rKF-xamxXYTl5vi-qQ91gjLe9MH6WPubeT980QVmaFUqhTYk-df9rzuRhCCqS5VP56FWJFa-b8d" \
             "x-W0Coq3z-VRZeoYU7mR0cbGDWogUpazEqO6wS6gUQodGFs-Z0pVDhWJviGg45arA6E8JpQBc-MZ7IzKyAb-ZMGSvdm2uV0FSFGA" \
             "qI0Sg1mNxMV2xjJ1MVjIXl_r5BcKT_A_vq9JO9611mcIfPyg2rK25_5rPQ0ZPJfNu5Hs6cnTYq8P9teSTU-lysoZxjEMM5JTghUFm" \
             "14Bmai-t-_zogYnjvFHMWVad0pAwGuzQhvrSrt9obENzk-0DUW-xAnCdqL6-d_WmEZD3zBzGvzWEifHmEcNJPOt9-5B9Y0fkIPSB" \
             "3cQ2Mzzg2aTH95ugpjYY4T3J3BeWRsI0YkIlf3R7uYn6PlbISWQ2BI6nov78BpX1zoxrfdeW4odO-SJAIJtBdDsOZrBBvNpnN6Pp" \
             "yBwbtqNVCyfPFDnuy8G4dHol5a7_X4pVvKLV5kQN-EHtn9aNDXYcB_tjuRdDvGHd8NMXxFWdTG4pS49gY8_nAZEeFKnt-IP90d5j" \
             "3KdMLeVs1Wm5ewsnw8-MyIXCMaq5-viKvLdMBaDblKexJvD2VSK9IYCXPY85hJyuoBCzNvPR24NdCrjJliksdNTM1fHG_aTLeuzP" \
             "QuFqtMyGgbWe7SekkIU9APpnRGqtR3Kq3gwRyPC6omT6XMQ4ya1-LDZ7vGBiLbeqLilDWEcr94a0XkSea06iuy5HqNQp2hBoCtC" \
             "RUvwBO3A_F6S5JfYCu0Jttg8yNmahJ5VH2NguwpjnW2rkCdg5xvOj-vC1Gm9GkAXax1_6eOojrqQg8bjQxj6_9TLsxFJJDrJHeE" \
             "0mNx30DajdX7IIrNKIhLn2F1MYd5yjrt88On2oqQEiqOpXuhq-Y0ZpP8XZDiG1pyuEkjTfk1F2crxdD1JHXkW_4TgbjmOOzSWHzs" \
             "3czYl9XLgW__9YvlfqOBUKgHmLyFkB1gYsqKcYlXJdd8X4rSuiEYXe2KzRrrDlxzTu041l49wGY9aL3fuse3D-o4eCzlN3fNZWU" \
             "0MFiEyURhUoG782bYdGU5sOdUdoELIwPrdw95131KlAZfk3W23IlwwEgYDRsSTu2ZaPien4WpMZjr7XMxHc_CVndzXTybNozgmF" \
             "YskNJRPiMqr__T861YQqKdETmou8gIJW3kkGdBZVP_cH3FPg4BubTsNhJMGUvZnsVD75bcLT7OcWaLxjaKaszhgcgulJEAC--b" \
             "b-P1g1Q6ZdbYuFZDt_dVAnKyi1ga27hBcFiCX10eK4QGJSMT2Px81GrKDX2jnLmEqWzx1HbsbqIELF1E8dV8XXmTT_uf8rAv8i" \
             "NoramPqI5yoEO6KBjlHFEMAjL3VnRqL8X0Jy7Uqkzm2Fr1DB9Qppp7rlG42OnIfZ7p_1T-nna1Z0hbzFGVdC2hILEkDt2jj87W8" \
             "dIsmfEG3J0qP-Acs8yto_QMbwNzWs63p0AugaPJjdUV6IRc6UEMFj9QMUPFTNSVa6cdcDCgjBlPAIJcc5N11tYwX_PFWT6SipB" \
             "Y05x5jOkwz4lXNF1DwQrAq37a5AspjyBBse4yBh_4=; _csrf_token=1656067002628; tfstk=cwaFB3NFiwQFGb35D2gPOh" \
             "rpP7DdZbMohFlqxtJan6YHRfihiWp-sUAr_bRwEDf..; l=eBgLKO8VLkQbw8qAKOfwourza77OSIRxsuPzaNbMiOCPOUCH5f-" \
             "NW6bS4RYMC3MNhs1HR3SVatiMBeYBqIAgba4Q5ykoKvDmn; isg=BJmZt2tuH710HMMsoUPgZIjbqIVzJo3YqD7PZLtOFUA_wr" \
             "lUA3adqAfUxJ60zSUQ"  # Successful Login Cookie
    url = Alibaba(cookie).run(filename)
    print(url)
