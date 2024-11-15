import typography from '@tailwindcss/typography';
import type { Config } from 'tailwindcss';

export default {
  content: ['./src/**/*.{html,js,svelte,ts}'],

  theme: {
    extend: {
      colors: {
        Twhite: '#F8F8FF',
        Tblack: '#031602',
        
      },
      fontFamily: {
        iMono: ['Space Mono', 'monospace'],
        iGro: ['Space Grotesk', 'sans-serif'],
      }
    }
  },

  plugins: [typography]
} as Config;
