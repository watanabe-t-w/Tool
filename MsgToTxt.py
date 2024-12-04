
# pyinstaller --onefile --exclude-module numpy --exclude-module pandas C:\Users\watanabe-t\github\python\Msgファイルをtext形式に\MsgTotxt.py
# pyinstaller <MsgTotxt.py> --onefile --exclude-module numpy --exclude-module pandas
import tkinter as tk
from tkinter import filedialog, messagebox
import aspose.email as ae  #Python Outlook API

# tkinterを使ってファイル選択ダイアログを開く
def select_file():
    root = tk.Tk()
    root.withdraw()  # メインウィンドウは表示しない
    file_path = filedialog.askopenfilename(filetypes=[("Outlook Message Files", "*.msg")])
    return file_path

# 保存場所を指定するダイアログ
def select_save_location():
    root = tk.Tk()
    root.withdraw()  # メインウィンドウは表示しない
    save_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
    return save_path

# メッセージボックスを表示
def show_message(title, message, message_type="info"):
    root = tk.Tk()
    root.withdraw()  # メインウィンドウは表示しない
    if message_type == "info":
        messagebox.showinfo(title, message)
    elif message_type == "error":
        messagebox.showerror(title, message)
    elif message_type == "warning":
        messagebox.showwarning(title, message)

# ファイルを選択
msg_file = select_file()

if msg_file:
    try:
        # msgファイルを読み込む
        message = ae.MailMessage.load(msg_file)

        # メッセージの本文を取得
        message_text = message.body

        # 保存場所を選択
        txt_output_path = select_save_location()

        if txt_output_path:
            # テキストファイルとして保存
            with open(txt_output_path, 'w', encoding='utf-8') as f:
                f.write(message_text)

            # 保存完了メッセージ（メッセージボックス）
            show_message("成功", f"ファイルが正常に保存されました: {txt_output_path}", "info")
        else:
            show_message("警告", "保存先が選択されませんでした。", "warning")
    except Exception as e:
        show_message("エラー", f"msgファイルの処理中にエラーが発生しました: {e}", "error")
else:
    show_message("警告", "ファイルが選択されませんでした。", "warning")
