# Fracta

日本語 | [English](README.en.md)

Fracta は Cerune の安全性チェックや脆弱性を、許可された環境で再現・研究する公式プロジェクトです。

## 目的

- 最小限の `.ceru` サンプルを使い、実行時の挙動を再現する。
- 設計通りの安全な停止と、修正すべき脆弱性を区別する。
- 修正済みの事例を回帰テストに残す。
- 実行経路の差分テストは [Parallax](https://github.com/Cerune-Lang/Parallax) で管理する。

## 初期ケース

`cases/checked_overflow.ceru` は符号付き整数のオーバーフロー検出を確認するサンプルです。安全な停止は、それ自体が脆弱性という意味ではありません。

```sh
cerune check cases/checked_overflow.ceru
cerune run cases/checked_overflow.ceru
cerune run-vm cases/checked_overflow.ceru
```

セキュリティの問題は公開 Issue に投稿せず、[SECURITY.md](SECURITY.md) に沿って非公開で報告してください。参加方法は [CONTRIBUTING.md](CONTRIBUTING.md) を参照。

初期開発中であり、安全性の保証はありません。ライセンスは検討中です。
