/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './templates/**/*.html',
    './apps/**/*.html',
  ],
  theme: {
    extend: {
      colors: {
        bg: '#07080A',
        surface: '#101216',
        border: 'rgba(255,255,255,0.08)',
        text: '#EDEEF0',
        muted: '#8A8F98',
        accent: '#7DB8FF',
      },
      fontFamily: {
        heading: ['"Archivo"', 'sans-serif'],
        body: ['"Hanken Grotesk"', 'sans-serif'],
      },
      fontSize: {
        '8xl': ['96px', { lineHeight: '1' }],
      },
      letterSpacing: {
        tighter: '-0.04em',
        tight: '-0.02em',
      }
    },
  },
  plugins: [],
}
