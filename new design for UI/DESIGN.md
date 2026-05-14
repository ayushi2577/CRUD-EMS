---
name: Vibrant Energy
colors:
  surface: '#fff7fa'
  surface-dim: '#e2d7dd'
  surface-bright: '#fff7fa'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#fcf1f7'
  surface-container: '#f6ebf1'
  surface-container-high: '#f0e5eb'
  surface-container-highest: '#eae0e6'
  on-surface: '#1f1a1e'
  on-surface-variant: '#464554'
  inverse-surface: '#342f33'
  inverse-on-surface: '#f9eef4'
  outline: '#767586'
  outline-variant: '#c7c4d7'
  surface-tint: '#494bd6'
  primary: '#4648d4'
  on-primary: '#ffffff'
  primary-container: '#6063ee'
  on-primary-container: '#fffbff'
  inverse-primary: '#c0c1ff'
  secondary: '#9d4300'
  on-secondary: '#ffffff'
  secondary-container: '#fd761a'
  on-secondary-container: '#5c2400'
  tertiary: '#b10e6b'
  on-tertiary: '#ffffff'
  tertiary-container: '#d23284'
  on-tertiary-container: '#fffbff'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#e1e0ff'
  primary-fixed-dim: '#c0c1ff'
  on-primary-fixed: '#07006c'
  on-primary-fixed-variant: '#2f2ebe'
  secondary-fixed: '#ffdbca'
  secondary-fixed-dim: '#ffb690'
  on-secondary-fixed: '#341100'
  on-secondary-fixed-variant: '#783200'
  tertiary-fixed: '#ffd9e4'
  tertiary-fixed-dim: '#ffb0cd'
  on-tertiary-fixed: '#3e0022'
  on-tertiary-fixed-variant: '#8c0053'
  background: '#fff7fa'
  on-background: '#1f1a1e'
  surface-variant: '#eae0e6'
typography:
  display-lg:
    fontFamily: Inter
    fontSize: 48px
    fontWeight: '800'
    lineHeight: 56px
    letterSpacing: -0.02em
  display-lg-mobile:
    fontFamily: Inter
    fontSize: 36px
    fontWeight: '800'
    lineHeight: 44px
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Inter
    fontSize: 32px
    fontWeight: '700'
    lineHeight: 40px
    letterSpacing: -0.01em
  headline-md:
    fontFamily: Inter
    fontSize: 24px
    fontWeight: '700'
    lineHeight: 32px
  body-lg:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: '400'
    lineHeight: 28px
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 24px
  label-lg:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '600'
    lineHeight: 20px
    letterSpacing: 0.02em
  label-sm:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '500'
    lineHeight: 16px
    letterSpacing: 0.04em
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  base: 8px
  xs: 4px
  sm: 12px
  md: 24px
  lg: 48px
  xl: 80px
  gutter: 24px
  margin-mobile: 16px
  margin-desktop: 64px
---

## Brand & Style
This design system is built for high-impact engagement, targeting an audience that thrives on dynamism and optimism. The brand personality is electric, approachable, and unapologetically bold. 

The aesthetic is a hybrid of **High-Contrast Modern** and **Soft Minimalism**. It leverages saturated primary colors to drive action and high-energy transitions, balanced by a "soft" structural foundation of generous whitespace and baby-pink tinted surfaces. The emotional goal is to evoke a sense of playfulness and digital-native confidence. It avoids the coldness of corporate UI by introducing warmth through its pastel-tinted backgrounds and smooth, tactile geometry.

## Colors
The palette is designed to maximize visual interest while maintaining clear information hierarchy.
- **Primary (Indigo):** Used for main navigational elements and critical action states.
- **Secondary (Orange):** Reserved for highlights, notifications, and secondary call-to-actions to create a high-contrast pop against indigo.
- **Tertiary (Pink):** Utilized for decorative elements, progress indicators, and playful accents.
- **Backgrounds:** The primary interface background is a very soft **Baby Pink** (#FDF2F8). Secondary surfaces like cards or sidebars use a **Light Purple** (#F5F3FF) to create subtle tonal separation without relying on gray.
- **Typography:** All text uses a deep indigo-tinted black (#1E1B4B) to ensure accessibility and high legibility against the vibrant background tones.

## Typography
The system uses **Inter** exclusively to provide a clean, modern, and highly legible anchor to the otherwise loud color palette. 

The type scale is aggressive, utilizing heavy weights (Bold and ExtraBold) for headlines to maintain the "high-energy" feel. To ensure the playful aesthetic doesn't compromise readability, body text maintains generous line heights. Display styles use slightly tighter letter spacing to create a compact, punchy editorial look. For mobile, the largest display sizes scale down significantly to prevent awkward word breaks while keeping the heavy font-weight intact.

## Layout & Spacing
The design system employs a **fluid 12-column grid** for desktop and a **4-column grid** for mobile. The layout philosophy centers on "breatheable energy"—using significant vertical rhythm to prevent the vibrant colors from becoming overwhelming.

Spacing is strictly based on an **8px linear scale**. Gutters are kept wide (24px) to ensure elements feel distinct. Containers should utilize the "md" (24px) or "lg" (48px) spacing for internal padding to maintain the soft, airy feel of the interface. On mobile, side margins are reduced to 16px to maximize content real estate while maintaining a clear safety zone.

## Elevation & Depth
Depth is created through **Tonal Layers** and **Tinted Ambient Shadows**. 

Instead of traditional neutral gray shadows, this design system uses soft shadows tinted with the Primary Indigo or Tertiary Pink (e.g., `rgba(99, 102, 241, 0.15)`). This reinforces the "colorful" brand narrative. 
- **Level 0 (Floor):** The Baby Pink background.
- **Level 1 (Cards/Containers):** Pure white surfaces with a very soft, diffused shadow.
- **Level 2 (Popovers/Floating Actions):** Use a slightly more saturated shadow and a 1px Indigo-tinted border (#E0E7FF) to provide crisp definition.

The system avoids heavy skeuomorphism in favor of subtle verticality, where active elements appear to "lift" closer to the user through shadow expansion rather than color change.

## Shapes
The shape language is defined by **Soft Continuity**. A `roundedness` of 2 (0.5rem base) ensures that all UI elements feel approachable and modern. 

- **Standard Elements (Buttons, Inputs):** 0.5rem (8px).
- **Large Containers (Cards, Sections):** 1.5rem (24px).
- **Special Elements (Chips, Tags):** Use pill-shapes (full rounding) to contrast against the more structured rectangular elements and add to the playful energy.

Consistency in corner radii is vital; avoid mixing sharp corners with rounded ones to maintain the soft, friendly aesthetic.

## Components
- **Buttons:** Primary buttons are Indigo with white text. Secondary buttons use Orange for high-energy highlights. Interactive states (hover/active) should involve a slight "squish" or scale-down effect (0.98x) to enhance the tactile feel.
- **Input Fields:** Use a white background with a 2px border in a very light purple. On focus, the border transitions to Primary Indigo with a soft outer glow.
- **Cards:** White backgrounds with `rounded-xl` corners. Use subtle colored headers or top-borders (Indigo or Pink) to categorize content.
- **Chips & Tags:** Fully rounded (pill-shaped). Use vibrant backgrounds (Pink or Orange) with high-contrast text for status indicators.
- **Checkboxes & Radios:** Should be oversized (20px+) to accommodate the playful style, using Indigo for the selected state and a bounce animation when toggled.
- **Progress Bars:** Use the Tertiary Pink for the fill, set against a Light Purple track, providing a soft but clear visualization of data.