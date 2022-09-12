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
