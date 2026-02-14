---
name: mama-frontend
description: Create distinctive frontend interfaces for MAMA products (landing page, web app, mobile app). Use when building UI components, pages, or sections. Triggers on /mama, /ui, or any MAMA frontend work.
---

# MAMA Frontend Design System

Build production-grade, memorable interfaces following MAMA's brand identity across all platforms. Avoid generic "AI slop" aesthetics.

## Brand Identity

**Vibe:** Playful, warm, consumer-friendly — NOT enterprise AI
**Target:** Gen Z (18-28) with phone anxiety
**Tone:** Retro-futuristic mom energy, approachable and fun

## Design Tokens

### Colors
```css
/* Primary (Rose) */
--rose-400: #FB7185;  /* Brand color */
--rose-300: #FDA4AF;  /* Hover/secondary */
--rose-500: #F43F5E;  /* Border accent */
--rose-600: #E11D48;  /* Active/pressed, 3D shadow */
--rose-50: #FFF1F2;   /* Light backgrounds */
--rose-100: #FFE4E6;  /* Subtle accents */

/* Backgrounds */
--white: #FFFFFF;
--cream: #FEFAF6;     /* Warm hero background */
--gray-50: #FAFAFA;

/* Text */
--zinc-900: #18181B;  /* Headlines */
--zinc-700: #3F3F46;  /* Card text */
--zinc-600: #52525B;  /* Body */
--zinc-400: #A1A1AA;  /* Muted/placeholder */

/* Accent */
--amber-300: #FCD34D; /* Highlights, badges */

/* Extended Palette - Retro-Futuristic Accents */
--aqua-300: #5EEAD4;   /* Info states, Jetsons pairing with rose */
--aqua-400: #2DD4BF;
--mint-300: #86EFAC;   /* Success states, "connected" */
--mint-400: #4ADE80;
--lavender-200: #DDD6FE; /* Premium, processing, Gen Z */
--lavender-300: #C4B5FD;
--peach-200: #FFD3B6;  /* Warning/pending, warm highlights */
--peach-300: #FDBA74;
--sunshine-200: #FEF08A; /* Badges, celebrations */
```

#### Color Application
| State | Primary | Supporting |
|-------|---------|------------|
| Default | rose-400 | zinc-400 |
| Success | mint-300 | mint-400 |
| In Progress | peach-200 | amber-300 |
| Info | aqua-300 | aqua-400 |
| Premium | lavender-200 | lavender-300 |

### Typography

**Fonts loaded in the project:**
- **Righteous** (display/headlines) - loaded via Google Fonts CDN
- **Quicksand** (body/UI) - loaded via next/font

| Element | Font | Desktop | Mobile | Weight | Implementation |
|---------|------|---------|--------|--------|----------------|
| Display | Righteous | 64-72px | 36-40px | 400 | `style={{ fontFamily: "'Righteous', cursive" }}` |
| H1 | Righteous | 48px | 32px | 400 | `style={{ fontFamily: "'Righteous', cursive" }}` |
| H2 | Righteous | 36px | 24-28px | 400 | `style={{ fontFamily: "'Righteous', cursive" }}` |
| H3 | Quicksand | 24px | 20px | 600 | Default or `style={{ fontFamily: "'Quicksand', sans-serif" }}` |
| Body | Quicksand | 16-18px | 14-16px | 400-500 | Default font |
| Button | Quicksand | 16px | 14px | 600-700 | Default font |
| Caption | Quicksand | 14px | 12px | 400 | Default font |

**Important:** Use inline styles for Righteous headlines. Quicksand is the default body font.

### Spacing & Layout
- **Border radius:** `rounded-2xl` (cards, pills), `rounded-full` (buttons, inputs)
- **Spacing scale:** 4, 8, 12, 16, 24, 32, 48, 64, 96
- **Max content width:** 1280px (desktop), full bleed on mobile
- **Safe areas:** Respect mobile notches and home indicators

## Platform-Specific Guidelines

### Web (Landing Page)
- Hero: Full viewport with mascot centered, headline bottom-left, CTA bottom-right
- Background: Warm cream `#FEFAF6` with subtle noise texture
- Sections: Full-width with max-w container
- Animations: Scroll-triggered reveals, floating messages, word pull-up

### Web App
- Navigation: Bottom tab bar (mobile pattern) or sidebar
- Cards: White background with shadow, rose accents
- Forms: Large touch targets (min 44px), clear validation states
- Loading: Skeleton screens with rose-100 shimmer

### Mobile App (React Native / Capacitor)
- Touch targets: Minimum 44x44px
- Bottom navigation: 5 items max, rose-400 active state
- Gestures: Swipe actions, pull-to-refresh
- Safe areas: iOS notch, Android nav bar
- Haptics: Light feedback on key actions

## Buttons & Interactive Elements

### Primary CTA Button (Arcade Style)
The signature MAMA button has a retro 3D arcade feel:

```tsx
<motion.button
  className={cn(
    // Base retro pill shape
    "relative h-12 sm:h-14 px-8 rounded-full",
    "font-bold text-base",
    // Retro thick border
    "border-[3px] border-rose-500",
    // Background gradient
    "bg-gradient-to-b from-rose-400 to-rose-500 text-white",
    // 3D shadow effect (arcade button style)
    "shadow-[0_4px_0_0_#be123c,0_6px_12px_rgba(225,29,72,0.4)]",
    // Transitions
    "transition-all duration-150 ease-out",
    "disabled:opacity-70"
  )}
  style={{ fontFamily: "'Quicksand', sans-serif" }}
  whileHover={{
    scale: 1.05,
    y: -2,
    boxShadow: "0 6px 0 0 #be123c, 0 8px 20px rgba(225,29,72,0.5)",
  }}
  whileTap={{
    scale: 0.98,
    y: 2,
    boxShadow: "0 1px 0 0 #be123c, 0 2px 4px rgba(225,29,72,0.2)",
  }}
  transition={{ type: "spring", stiffness: 500, damping: 20 }}
>
  Button Text
</motion.button>
```

### Simple Buttons (Forms, Secondary)
```tsx
<motion.button
  whileHover={{ scale: 1.02, y: -2 }}
  whileTap={{ scale: 0.98 }}
  transition={{ type: "spring", stiffness: 400, damping: 17 }}
  className="bg-rose-400 text-white rounded-full px-6 py-3 font-semibold hover:bg-rose-300"
  style={{ fontFamily: "'Quicksand', sans-serif" }}
>
  Continue
</motion.button>
```

### Selection Pills/Cards (Use Cases)
From DualCarousel - used for selectable options:

```tsx
<div
  className={cn(
    "relative flex items-center gap-4 px-6 py-4",
    "bg-white/95",
    "rounded-2xl border-2 border-white/60",
    "whitespace-nowrap shrink-0",
    "shadow-lg shadow-rose-900/10 hover:shadow-xl transition-shadow duration-300"
  )}
>
  <Image src={iconPath} alt="" width={32} height={32} className="object-contain" />
  <span
    className="text-zinc-700 font-semibold text-base"
    style={{ fontFamily: "'Quicksand', sans-serif" }}
  >
    {title}
  </span>
</div>
```

### Button Variants Summary

| Variant | Style | Use Case |
|---------|-------|----------|
| Primary (Arcade) | Gradient + 3D shadow | Main CTAs, hero buttons |
| Primary (Simple) | `bg-rose-400 text-white rounded-full` | Form submit, continue |
| Secondary | `border-2 border-rose-400 text-rose-400` | Alternate actions |
| Ghost | `text-rose-400 hover:bg-rose-50` | Tertiary, inline |
| Selection Pill | `bg-white/95 rounded-2xl shadow-lg` | Multi-select options |
| Disabled | `opacity-50 cursor-not-allowed` | Unavailable |

## Animation Patterns

Use Framer Motion (web) or Reanimated (React Native).

| Pattern | Use | Config |
|---------|-----|--------|
| Word Pull Up | Headlines | 0.15s stagger, ease [0.2, 0.65, 0.3, 0.9] |
| Fade + Slide | Section reveals | 0.6s, ease-out |
| Spring Press | Buttons | stiffness: 400-500, damping: 17-20 |
| Floating | Decorative elements | Continuous, subtle |
| Skeleton Shimmer | Loading states | 1.5s loop |
| Carousel | Use cases | 25-35s infinite linear scroll |

## Component Patterns

### Cards (Selection/Display)
```tsx
// White card with shadow (like DualCarousel)
<div className="bg-white/95 rounded-2xl border-2 border-white/60 p-4
               shadow-lg shadow-rose-900/10 hover:shadow-xl transition-shadow">
  {children}
</div>

// Rose background card
<div className="bg-rose-50 rounded-xl p-4 md:p-6 shadow-sm hover:shadow-md transition">
  {children}
</div>
```

### Input Fields
```tsx
<input
  className="w-full h-12 sm:h-14 px-5 rounded-full bg-white
             border-2 border-zinc-200 text-zinc-900
             placeholder:text-zinc-400
             focus:ring-2 focus:ring-rose-200 focus:border-rose-300
             shadow-md"
  style={{ fontFamily: "'Quicksand', sans-serif" }}
/>
```

### Headlines
```tsx
<h1
  className="text-4xl sm:text-5xl md:text-6xl text-zinc-900 leading-[0.95] tracking-tight"
  style={{ fontFamily: "'Righteous', cursive" }}
>
  Headline Text
</h1>
```

### Body Text
```tsx
<p
  className="text-lg text-zinc-600 leading-relaxed"
  style={{ fontFamily: "'Quicksand', sans-serif" }}
>
  Body text content
</p>
```

## Quality Checklist

- [ ] Righteous for headlines (via inline style), Quicksand for body (default)
- [ ] Rose palette with zinc text throughout
- [ ] Full pill buttons (`rounded-full`) with spring animations
- [ ] 3D arcade-style shadow on primary CTAs
- [ ] Selection pills use white bg with shadow (`bg-white/95 rounded-2xl shadow-lg`)
- [ ] 44px minimum touch targets on mobile
- [ ] Proper safe area handling
- [ ] Skeleton loading states (not spinners)
- [ ] No generic fonts (Inter, Roboto, Arial, system)
- [ ] No purple gradients or enterprise aesthetics
- [ ] Soft shadows — use `shadow-rose-900/10` for warmth

## Font Loading (Already in Project)

The fonts are loaded in `src/app/layout.tsx`:

```tsx
// Quicksand via next/font
import { Quicksand } from "next/font/google"
const nunito = Quicksand({ variable: "--font-nunito", subsets: ["latin"], weight: ["400", "500", "600", "700"] })

// Righteous via CDN in <head>
<link href="https://fonts.googleapis.com/css2?family=Righteous&display=swap" rel="stylesheet" />
```

## References

For detailed component code, animation examples, and platform-specific implementations, see [references/details.md](references/details.md).
