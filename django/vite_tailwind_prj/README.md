## frontendプロジェクト作成

```
npm create vite@latest frontend -- --template vanilla-ts
cd frontend
npm install

npm run dev -- --host 0.0.0.0

npm run build
```

## サーバー起動せずwatchによる継続ビルド用に書き換え

package.jsonでdevコマンドを以下に変更

```
vite build --watch --sourcemap --mode development
```

dist/assetsにビルド結果が出るので、シンボリックリンクでDjangoプロジェクトルートにassetsをリンク

## sassとtailwindとdaisyui

npm install --save-dev tailwindcss daisyui sass postcss postcss-import autoprefixer

## postcss.config.cjs

```
module.exports = {
  plugins: [
    require('postcss-import'),
    require('tailwindcss'),
    require('autoprefixer')
  ],
}
```

## tailwind.config.cjs

```
module.exports = {
  variants: {
    extend: {
    },
  },
  content: [
    "./*.html",
  ],
  theme: {
    extend: {},
  },
  plugins: [
    require("daisyui"),
  ],
  daisyui: {
  }
}
```
