/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./src/**/*.{html,js,ts,jsx,tsx}",  // Adjust this line to match your project's file structure
    "./main.py",  // Include your Python files where Tailwind CSS classes are used
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}

