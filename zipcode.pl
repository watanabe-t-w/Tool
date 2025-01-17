#!/usr/bin/perl
use strict;
use warnings;
use utf8;
use LWP::UserAgent;
use JSON;
use CGI qw(:standard);
use Encode;

# 標準出力のエンコーディングをUTF-8に設定
binmode STDOUT, ':encoding(UTF-8)';

# CGIオブジェクトを作成
my $q = CGI->new;

# HTMLヘッダーを出力（JSONとして、UTF-8エンコーディングを指定）
print $q->header('application/json; charset=UTF-8');

# 郵便番号をフォームから取得
my $zipcode = $q->param('zipcode');
my $address = "";

# レスポンスを構造化する
my %response = ();

# 郵便番号が入力されている場合、APIを呼び出す
if ($zipcode) {
    # 郵便番号の形式をチェック
    if ($zipcode =~ /^\d{7}$/) {
        my $url = "https://zipcloud.ibsnet.co.jp/api/search?zipcode=$zipcode";  # zipcloudのURL

        # HTTPリクエストを送信
        my $ua = LWP::UserAgent->new;
        my $response_api = $ua->get($url);

        # レスポンスが成功した場合
        if ($response_api->is_success) {
            my $json_data = $response_api->decoded_content(charset => 'utf-8');
            
            # デコード処理
            my $decoded_json;
            eval {
                $decoded_json = from_json($json_data);  # JSON形式でデコード
            };
            if ($@) {
                # デコードエラーがあった場合
                $address = "エラーが発生しました（デコードエラー）。";
            } else {
                # 住所情報を取得
                if ($decoded_json->{status} == 200 && @{$decoded_json->{results}} > 0) {
                    # 住所を組み立てる
                    my $address1 = $decoded_json->{results}[0]{address1};  # 都道府県
                    my $address2 = $decoded_json->{results}[0]{address2};  # 市区町村
                    my $address3 = $decoded_json->{results}[0]{address3};  # 番地

                    # 住所がある場合にセット
                    $address = "$address1$address2$address3";
                } else {
                    $address = "住所が見つかりませんでした。";
                }
            }
        } else {
            $address = "APIへの接続に失敗しました: " . $response_api->status_line;
        }
    } else {
        $address = "郵便番号が無効です。正しい形式で入力してください。";
    }
} else {
    $address = "郵便番号が入力されていません。";
}

# JSONレスポンスを返す（UTF-8エンコード）
$response{address} = $address;
print to_json(\%response);  # JSONとしてレスポンスを返す
