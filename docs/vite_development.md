# Viteの導入手順

## 環境構築

```bash
npm init
npm install create-vite
npx create-vite my-vite-app
```

以下を選択

> ✔ Select a framework: › Vue  
> ✔ Select a variant: › JavaScript

```bash
cd my-vite-app
npm install
npm run dev
```

## エラー対応

### You installed esbuild for another platform than the one you're currently using.

> 現在のプラットフォーム（例: Linux）とは異なるプラットフォーム（例: macOSまたはWindows）向けにesbuildをインストールしたことを示しています。

#### 対処法

プロジェクト内でesbuildを再インストールする

```bash
npm install esbuild
```