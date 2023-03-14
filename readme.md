## 使用技術

- API: fastAPI
- デプロイ: vercel
  - url: [https://vercel.com/nanahiryu/fast-api-test-speee](https://vercel.com/nanahiryu/fast-api-test-speee)

## 実装

### ビジネスロジック

- シンプルに再帰で実装した

### エラーハンドリング

- クエリパラメータの型判定
  - fastAPI のデフォルトのバリデーションを利用した(status_code: 422)
- メソッドの判定
  - @app.get というデコレータによって判定(status_code: 405)
- クエリパラメータの有無
  - デフォルト値を None にしておき, None か否かでバリデーションを行った(status_code: 400)
- 値の範囲
  - 今回は自然数に対してのみフィボナッチ数列を返す仕様なので, クエリパラメータ i >= 1 を if 文で判定(status_code: 400)
