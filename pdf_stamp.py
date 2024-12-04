 # -*- coding: utf-8 -*-
from pdfrw import PdfReader
from pdfrw.buildxobj import pagexobj
from pdfrw.toreportlab import makerl
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import portrait, landscape, A3, A4, A5, A6, B3, B4, B5, B6
from reportlab.lib.utils import ImageReader
from reportlab.lib.units import mm
from reportlab.lib.colors import HexColor

from datetime import datetime

# def make_pdf():
# file_in  = './sample.pdf'
# file_out = './sample_out.pdf'
# stamp_file = './stamp_ok.png'
file_in  = r'C:\Users\watanabe-t\Documents\パックミズタニ\sample.pdf'
file_out = r'C:\Users\watanabe-t\Documents\パックミズタニ\sample_out.pdf'
stamp_file = r'C:\Users\watanabe-t\Documents\パックミズタニ\stamp_ok.png'
# file_in  = r'C:\Users\watanabe-t\OneDrive - 株式会社ケーエスアイ\ドキュメント - Test\pdf\sample.pdf'
# file_out = r'C:\Users\watanabe-t\OneDrive - 株式会社ケーエスアイ\ドキュメント - Test\pdf\sample_out.pdf'
# stamp_file = r'C:\Users\watanabe-t\OneDrive - 株式会社ケーエスアイ\ドキュメント - Test\pdf\stamp_ok.png'

# 元のPDFを読み込み
pages = PdfReader(file_in, decompress=False).pages

# キャンバスのセット
cc = canvas.Canvas(file_out, pagesize=portrait(A4))

# ページ取得
pp = pagexobj(pages[0])
cc.doForm(makerl(cc, pp))
img = ImageReader(stamp_file)

cc.drawImage(img, 120, 50, 300, 200, preserveAspectRatio=True,mask='auto')

# 四角形を描画する
# cc.rect(50, 50, 300, 200)
# 線の太さと色を設定する
# cc.setLineWidth(2)
# cc.setStrokeColorRGB(0, 0, 0)  # 黒色
# 描画を実行する
# cc.showPage()

# 文字
cc.setFillColor(HexColor('#FF0000')) # RRGGBB で指定
# 日付の取得とフォーマット
today = datetime.today().strftime('%Y-%m-%d')
cc.drawString(x=20.00*mm, y=24*mm, text=today)
# cc.drawCentredString(x=42.00*mm, y=34*mm, text=today)
# cc.drawRightString(x=44.00*mm, y=44*mm,text=today)

cc.showPage()  #改ページ
cc.save()
