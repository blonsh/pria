module.exports = {
  mode: 'jit',
  content: [
    "./templates/**/*.{html,js}",
    "./static/**/*.{html,js}",
    "./core/**/*.{html,js}",
    "./users/**/*.{html,js}",
    "./workcenter/**/*.{html,js}",
  ],
  theme: {
    extend: {
      colors: {
        primary: '#6A0DAD',
        text: '#000000',
      },
      fontFamily: {
        montserrat: ['"Montserrat"', 'sans-serif'],
        'open-sans': ['"Open Sans"', 'sans-serif'],
      },
    },
  },
  plugins: [],
}
