/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./shortener/templates/**/*.html",
  ],
  theme: {
    extend: {
      fontFamily: {
        sans: ["Space Grotesk", "sans-serif"],
        mono: ["JetBrains Mono", "monospace"],
      },
      colors: {
        black: "#0A0A0A",
        lime: "#C6FF00",
      },
    },
  },
  plugins: [],
}
