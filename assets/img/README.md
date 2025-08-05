# Background Images

## Sidebar Background

To change the sidebar background image:

1. **Add your image** to this directory (e.g., `sidebar-bg.jpg`)
2. **Update `_config.yml`** with one of these options:

### Simple Image
```yaml
accent_image: /assets/img/sidebar-bg.jpg
```

### Image with Dark Overlay (Recommended)
```yaml
accent_image:
  background: /assets/img/sidebar-bg.jpg
  overlay: true
```

### Image with Custom Overlay
```yaml
accent_image:
  background: /assets/img/sidebar-bg.jpg
  overlay: 'linear-gradient(to bottom, rgba(0,0,0,0.4), rgba(0,0,0,0.6))'
```

## Image Requirements

- **Format**: JPG or PNG
- **Size**: 1920x1080px or larger (will be cropped/scaled)
- **Aspect Ratio**: Any (will fill sidebar area)
- **Optimization**: Compress for web (aim for <500KB)

## Tips

- **Dark overlay recommended** for text readability
- **High contrast images** work best
- **Avoid busy patterns** that compete with text
- **Test on mobile** - sidebar becomes full-width