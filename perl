<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>郵便番号検索結果</title>
    <script>
        // AJAXで住所を取得
        function fetchAddress() {
            // 郵便番号を取得 (数字以外の文字を削除)
            var zipcode = document.getElementById("zipcode").value.replace(/[^0-9]/g, '');

            if (zipcode.match(/^\d{7}$/)) {
                var xhr = new XMLHttpRequest();
                xhr.open("GET", "/cgi-bin/zipcode.pl?zipcode=" + zipcode, true);
                xhr.onreadystatechange = function() {
                    if (xhr.readyState == 4) {
                        if (xhr.status == 200) {
                            try {
                                if (xhr.responseText) {
                                    // レスポンスをログに表示して確認
                                    // console.log("レスポンス:", xhr.responseText);

                                    // BOMを取り除くための処理
                                    var responseText = xhr.responseText.trim().replace(/^\uFEFF/, '');  // BOMの取り除き

                                    // JSON形式でレスポンスをパース
                                    var response = JSON.parse(responseText);
                                    if (response.address) {
                                        document.getElementById("address").value = response.address;
                                    } else {
                                        document.getElementById("address").value = "住所が見つかりませんでした";
                                    }
                                } else {
                                    // console.error("空のレスポンスを受信しました");
                                    document.getElementById("address").value = "エラーが発生しました";
                                }
                            } catch (e) {
                                // console.error("JSONパースエラー:", e);
                                document.getElementById("address").value = "エラーが発生しました";
                            }
                        } else {
                            // console.error("HTTPエラー:", xhr.status);
                            document.getElementById("address").value = "通信エラーが発生しました";
                        }
                    }
                };                
                xhr.send();
            } else {
                alert("郵便番号の形式が正しくありません。");
            }
        }
    </script>
</head>
<body>
    <h2>郵便番号検索</h2>

    <!-- 郵便番号入力フォーム -->
    <form onsubmit="event.preventDefault(); fetchAddress();">
        <label for="zipcode">郵便番号 (XXXXXXX):</label>
        <input type="text" id="zipcode" name="zipcode" maxlength="7" required>
        <input type="submit" value="検索">
    </form>

    <h3>検索結果</h3>
    <h4>住所:</h4>
    <input type="text" id="address" readonly>

</body>
</html>
