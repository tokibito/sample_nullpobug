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
