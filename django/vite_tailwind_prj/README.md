## frontendプロジェクト作成

```
npm create vite@latest frontend -- --template vanilla-ts
cd frontend
npm install
```

## 不要なファイルを削除

```
rm public/vite.svg
rm src/counter.ts src/style.css src/typescript.svg
```

## vite.config.ts

```
import { defineConfig } from 'vite'

export default defineConfig({
  base: '/static/',  // 静的ファイルのprefix
  plugins: [],
  build: {
    rollupOptions: {
      output: {
        entryFileNames: `assets/[name].js`,
        chunkFileNames: `assets/[name].js`,
        assetFileNames: `assets/[name].[ext]`
      }
    }
  }
})
```

## サーバー起動せずwatchによる継続ビルド用に書き換え

package.jsonでdevコマンドを以下に変更

```
vite build --watch --sourcemap --mode development
```

dist/assetsにビルド結果が出るので、シンボリックリンクでDjangoプロジェクトルートにassetsをリンク

## sassとtailwindとdaisyui

npm install --save-dev tailwindcss daisyui sass postcss postcss-import autoprefixer

## main.ts

```
import './style.scss'
```

## style.scss

```
@tailwind base;
@tailwind components;
@tailwind utilities;
```

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
    "../myproject/templates/*.html",
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
