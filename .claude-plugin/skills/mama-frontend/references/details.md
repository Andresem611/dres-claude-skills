# MAMA Frontend - Detailed Reference

## Animation Code Examples

### Word Pull Up (Headlines)
```tsx
import { motion } from "framer-motion"

const WordPullUp = ({ words, className }: { words: string; className?: string }) => {
  const wordArray = words.split(" ")
  return (
    <div className={className}>
      {wordArray.map((word, i) => (
        <motion.span
          key={i}
          initial={{ y: 20, opacity: 0 }}
          animate={{ y: 0, opacity: 1 }}
          transition={{ duration: 0.5, delay: i * 0.15, ease: [0.2, 0.65, 0.3, 0.9] }}
          className="inline-block mr-3"
        >
          {word}
        </motion.span>
      ))}
    </div>
  )
}
```

### Hand-Drawn Underline
```tsx
const UnderlineDraw = () => (
  <motion.svg viewBox="0 0 200 20" className="absolute -bottom-2 left-0 w-full">
    <motion.path
      d="M0 10 Q50 0, 100 10 T200 10"
      stroke="#FB7185"
      strokeWidth="3"
      fill="none"
      strokeLinecap="round"
      initial={{ pathLength: 0 }}
      animate={{ pathLength: 1 }}
      transition={{ duration: 0.8, delay: 1.2, ease: "easeOut" }}
    />
  </motion.svg>
)
```

### Button with Spring
```tsx
const buttonVariants = {
  rest: { scale: 1, y: 0 },
  hover: {
    scale: 1.02,
    y: -2,
    boxShadow: "0 8px 20px rgba(251, 113, 133, 0.3)",
    transition: { type: "spring", stiffness: 400, damping: 17 }
  },
  tap: {
    scale: 0.98,
    y: 0,
    transition: { type: "spring", stiffness: 400, damping: 17 }
  }
}

<motion.button
  variants={buttonVariants}
  initial="rest"
  whileHover="hover"
  whileTap="tap"
  className="bg-rose-400 text-white rounded-full px-8 py-3 font-quicksand font-semibold"
>
  Join the Waitlist
</motion.button>
```

### Scroll Reveal
```tsx
<motion.div
  initial={{ opacity: 0, y: 40 }}
  whileInView={{ opacity: 1, y: 0 }}
  viewport={{ once: true, margin: "-100px" }}
  transition={{ duration: 0.6, delay: index * 0.2 }}
>
  {children}
</motion.div>
```

### Infinite Carousel
```tsx
// Top row - scrolls right
<motion.div
  animate={{ x: ['0%', '-50%'] }}
  transition={{ duration: 30, repeat: Infinity, ease: 'linear' }}
>
  {[...items, ...items].map(item => <Card key={item.id} {...item} />)}
</motion.div>

// Bottom row - scrolls left
<motion.div
  animate={{ x: ['-50%', '0%'] }}
  transition={{ duration: 30, repeat: Infinity, ease: 'linear' }}
>
  {[...items, ...items].map(item => <Card key={item.id} {...item} />)}
</motion.div>
```

### Skeleton Shimmer
```tsx
const Skeleton = ({ className }: { className?: string }) => (
  <div className={`animate-pulse bg-rose-100 rounded-xl ${className}`}>
    <div className="h-full w-full bg-gradient-to-r from-rose-100 via-rose-50 to-rose-100
                    animate-[shimmer_1.5s_infinite] bg-[length:200%_100%]" />
  </div>
)

// In globals.css
@keyframes shimmer {
  0% { background-position: 200% 0; }
  100% { background-position: -200% 0; }
}
```

## Complete Button Component
```tsx
import { motion, HTMLMotionProps } from "framer-motion"
import { cn } from "@/lib/utils"

type ButtonVariant = "primary" | "secondary" | "ghost"

interface ButtonProps extends HTMLMotionProps<"button"> {
  variant?: ButtonVariant
}

const variants = {
  primary: "bg-rose-400 text-white hover:bg-rose-300 active:bg-rose-600",
  secondary: "border-2 border-rose-400 text-rose-400 hover:bg-rose-50",
  ghost: "text-rose-400 hover:bg-rose-50"
}

export const Button = ({ variant = "primary", className, children, ...props }: ButtonProps) => (
  <motion.button
    whileHover={{ scale: 1.02, y: -2 }}
    whileTap={{ scale: 0.98, y: 0 }}
    transition={{ type: "spring", stiffness: 400, damping: 17 }}
    className={cn(
      "rounded-full px-6 py-3 font-quicksand font-semibold transition-colors",
      "focus:outline-none focus:ring-2 focus:ring-rose-400 focus:ring-offset-2",
      "disabled:opacity-50 disabled:cursor-not-allowed",
      variants[variant],
      className
    )}
    {...props}
  >
    {children}
  </motion.button>
)
```

## Complete Input Component
```tsx
import { cn } from "@/lib/utils"
import { forwardRef, InputHTMLAttributes } from "react"

interface InputProps extends InputHTMLAttributes<HTMLInputElement> {
  error?: string
}

export const Input = forwardRef<HTMLInputElement, InputProps>(
  ({ className, error, ...props }, ref) => (
    <div className="w-full">
      <input
        ref={ref}
        className={cn(
          "w-full bg-white border rounded-xl px-4 py-3",
          "font-quicksand text-zinc-900 placeholder:text-zinc-400",
          "transition-all duration-200",
          "focus:outline-none focus:ring-2 focus:ring-rose-100 focus:border-rose-400",
          error ? "border-red-400" : "border-zinc-200",
          className
        )}
        {...props}
      />
      {error && <p className="mt-1 text-sm text-red-500 font-quicksand">{error}</p>}
    </div>
  )
)
```

## Card Component
```tsx
import { motion } from "framer-motion"
import { cn } from "@/lib/utils"

interface CardProps {
  children: React.ReactNode
  className?: string
  hover?: boolean
}

export const Card = ({ children, className, hover = true }: CardProps) => (
  <motion.div
    whileHover={hover ? { y: -4, boxShadow: "0 12px 24px rgba(251, 113, 133, 0.15)" } : {}}
    transition={{ type: "spring", stiffness: 300, damping: 20 }}
    className={cn(
      "bg-rose-50 rounded-xl p-4 md:p-6",
      "shadow-sm transition-shadow",
      className
    )}
  >
    {children}
  </motion.div>
)
```

## Responsive Breakpoints

```css
/* Mobile first - Tailwind defaults */
sm: 640px   /* Large phones */
md: 768px   /* Tablets */
lg: 1024px  /* Laptops */
xl: 1280px  /* Desktops */
```

**Common patterns:**
```tsx
// Stack on mobile, side-by-side on desktop
<div className="flex flex-col md:flex-row gap-4">

// Hide on mobile, show on desktop
<div className="hidden lg:block">

// Full width mobile, contained desktop
<div className="w-full max-w-4xl mx-auto px-4">

// Responsive text sizes
<h1 className="text-3xl md:text-5xl lg:text-6xl font-righteous">
```

## React Native / Capacitor Specifics

### Safe Areas
```tsx
import { SafeAreaView } from 'react-native-safe-area-context'

<SafeAreaView edges={['top', 'bottom']} className="flex-1 bg-white">
  {children}
</SafeAreaView>
```

### Touch Feedback
```tsx
import { Pressable } from 'react-native'
import * as Haptics from 'expo-haptics'

<Pressable
  onPressIn={() => Haptics.impactAsync(Haptics.ImpactFeedbackStyle.Light)}
  className="bg-rose-400 rounded-full px-6 py-4 min-h-[44px] items-center justify-center"
>
  <Text className="text-white font-quicksand font-semibold">Button</Text>
</Pressable>
```

### Bottom Tab Bar
```tsx
const TabBar = () => (
  <View className="flex-row bg-white border-t border-zinc-100 pb-safe">
    {tabs.map(tab => (
      <Pressable
        key={tab.id}
        className="flex-1 items-center py-3"
      >
        <TabIcon name={tab.icon} active={tab.active} />
        <Text className={tab.active ? "text-rose-400" : "text-zinc-400"}>
          {tab.label}
        </Text>
      </Pressable>
    ))}
  </View>
)
```

## Font Loading

### Web (Next.js) - Current Implementation
```tsx
// app/layout.tsx
import { Quicksand } from 'next/font/google'

// Quicksand via next/font for body text
const quicksand = Quicksand({
  subsets: ['latin'],
  weight: ['400', '500', '600', '700'],
  variable: '--font-quicksand'
})

export default function RootLayout({ children }) {
  return (
    <html>
      <head>
        {/* Righteous via CDN for headlines */}
        <link href="https://fonts.googleapis.com/css2?family=Righteous&display=swap" rel="stylesheet" />
      </head>
      <body className={`${quicksand.variable} font-sans`}>{children}</body>
    </html>
  )
}
```

### Using Fonts in Components
```tsx
// Headlines - use inline style for Righteous
<h1
  className="text-4xl text-zinc-900"
  style={{ fontFamily: "'Righteous', cursive" }}
>
  Headline Text
</h1>

// Body text - use inline style for Quicksand
<p
  className="text-lg text-zinc-600"
  style={{ fontFamily: "'Quicksand', sans-serif" }}
>
  Body text
</p>
```

### CSS Variables (globals.css)
```css
:root {
  --font-sans: var(--font-quicksand), system-ui, sans-serif;
  --font-display: "Righteous", cursive;
}
```
