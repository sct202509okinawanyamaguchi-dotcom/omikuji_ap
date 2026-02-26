# マクドナルド・メニュー診断（おみくじ）アプリ
「今の時間帯」と「気分」を選択するだけで、最適なマクドナルドメニューを提案するWebアプリケーションです。

## プレビューURL
https://omikuji-ap.onrender.com/

## 機能
- 条件分岐診断: 「朝マック/レギュラー」×「甘味あり/なし」の4カテゴリによるフィルタリング。
- レスポンシブデザイン: モバイル端末での閲覧を想定し、長い商品名（例：プチパンケーキハッピーセット）も1行で収まるよう動的なフォント・レイアウト調整を実装。
- ブランドカラー最適化: 公式をイメージした赤・黄・白の配色による直感的なインターフェース。

##　使用技術
- 言語	Python 3.x
- フレームワーク	Flet (Flutter-based)
- インフラ / ホスティング	Render (Static Site)
- CI/CD / ソース管理	GitHub

## 工夫した点
- UI/UXの最適化:Fletのno_wrapプロパティやコンテナ幅の動的計算を活用。マルチデバイスにおいて、商品名が不自然に改行されない視認性を確保しました。
- 実運用に即したロジック:単なるランダム抽出ではなく、実際の店舗運用（朝・昼の入れ替わり）に基づいた時間軸の条件分岐を実装しています。
- デプロイ自動化:Renderのビルド設定を最適化（Root Directory: omikuji_ap）し、GitHubへのPushと連動した自動デプロイ環境を構築済みです。

## 実行方法
### リポジトリのクローン
git clone [Your-Repository-URL]
cd omikuji_ap

### 依存ライブラリのインストール
pip install flet

### アプリの起動
flet run main.py

## スクリーンショット
<img width="560" height="772" alt="スクリーンショット 2026-02-26 16 52 58" src="https://github.com/user-attachments/assets/eac5132c-926c-4ca4-ae2e-a1c1d380f450" />
<img width="391" height="570" alt="スクリーンショット 2026-02-26 16 53 06" src="https://github.com/user-attachments/assets/88bdd6bb-53e7-4c7a-8698-417cc0beba68" />
