# Shadcn UI Showcase

A beautiful, modern website built with [Next.js](https://nextjs.org/), [Tailwind CSS](https://tailwindcss.com/), and [Shadcn UI](https://ui.shadcn.com/) components.

## 🚀 Features

- **Modern Stack**: Built with Next.js 15, TypeScript, and Tailwind CSS
- **Beautiful Components**: Comprehensive showcase of Shadcn UI components
- **Responsive Design**: Mobile-first responsive layout
- **Dark Mode Support**: Built-in dark mode with CSS variables
- **Accessible**: All components follow accessibility best practices
- **Type Safe**: Full TypeScript support

## 🛠️ Tech Stack

- **Framework**: [Next.js 15](https://nextjs.org/) with App Router
- **Styling**: [Tailwind CSS](https://tailwindcss.com/)
- **Components**: [Shadcn UI](https://ui.shadcn.com/)
- **Language**: [TypeScript](https://www.typescriptlang.org/)
- **Icons**: [Lucide React](https://lucide.dev/)
- **Toast**: [Sonner](https://sonner.emilkowal.ski/)

## 📦 Installed Components

The following Shadcn UI components are installed and ready to use:

- **Button** - Interactive buttons with various styles
- **Card** - Content containers with headers
- **Input** - Form input fields
- **Label** - Form labels
- **Dialog** - Modal dialogs and overlays
- **Dropdown Menu** - Contextual menus
- **Navigation Menu** - Navigation components
- **Sheet** - Side panel overlays
- **Table** - Data tables
- **Tabs** - Tabbed interfaces
- **Textarea** - Multi-line text inputs
- **Badge** - Status indicators
- **Avatar** - User avatars
- **Form** - Form handling with validation
- **Sonner** - Toast notifications

## 🚀 Getting Started

### Prerequisites

- Node.js 18+ 
- npm or yarn

### Installation

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd debs-website-next
   ```

2. **Install dependencies**
   ```bash
   npm install
   ```

3. **Run the development server**
   ```bash
   npm run dev
   ```

4. **Open your browser**
   Navigate to [http://localhost:3000](http://localhost:3000)

## 📁 Project Structure

```
src/
├── app/                    # Next.js App Router
│   ├── globals.css        # Global styles
│   ├── layout.tsx         # Root layout
│   └── page.tsx           # Home page
├── components/
│   └── ui/               # Shadcn UI components
│       ├── button.tsx
│       ├── card.tsx
│       ├── dialog.tsx
│       └── ...           # Other components
└── lib/
    └── utils.ts          # Utility functions
```

## 🎨 Using Shadcn Components

### Adding New Components

To add more Shadcn UI components:

```bash
npx shadcn@latest add <component-name>
```

Example:
```bash
npx shadcn@latest add select
npx shadcn@latest add checkbox
npx shadcn@latest add radio-group
```

### Using Components

Import and use components in your React components:

```tsx
import { Button } from "@/components/ui/button"
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card"

export default function MyComponent() {
  return (
    <Card>
      <CardHeader>
        <CardTitle>My Card</CardTitle>
      </CardHeader>
      <CardContent>
        <Button>Click me</Button>
      </CardContent>
    </Card>
  )
}
```

## 🎯 Available Scripts

- `npm run dev` - Start development server
- `npm run build` - Build for production
- `npm run start` - Start production server
- `npm run lint` - Run ESLint
- `npm run type-check` - Run TypeScript type checking

## 🌙 Dark Mode

The project includes built-in dark mode support. The theme automatically adapts based on the user's system preferences and can be toggled programmatically.

## 📱 Responsive Design

All components are built with mobile-first responsive design using Tailwind CSS breakpoints:

- `sm:` - 640px and up
- `md:` - 768px and up
- `lg:` - 1024px and up
- `xl:` - 1280px and up

## 🔧 Customization

### Colors

Customize the color scheme by modifying the CSS variables in `src/app/globals.css`:

```css
:root {
  --background: 0 0% 100%;
  --foreground: 222.2 84% 4.9%;
  --primary: 222.2 47.4% 11.2%;
  /* ... other variables */
}
```

### Components

Shadcn UI components can be customized by editing the component files in `src/components/ui/`. Each component is built on top of Radix UI primitives and styled with Tailwind CSS.

## 📚 Resources

- [Shadcn UI Documentation](https://ui.shadcn.com/)
- [Next.js Documentation](https://nextjs.org/docs)
- [Tailwind CSS Documentation](https://tailwindcss.com/docs)
- [Radix UI Documentation](https://www.radix-ui.com/)

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License.

---

Built with ❤️ using [Shadcn UI](https://ui.shadcn.com/) and [Next.js](https://nextjs.org/)

