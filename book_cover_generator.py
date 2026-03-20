from PIL import Image, ImageDraw, ImageFont
import math
import os

def create_book_cover(output_filename='religion_weaponized_cover.png'):
    """
    Generate a professional book cover for 'Religion Weaponized: The Dark Side of Faith'
    
    Dimensions: 1600 x 2560 pixels (6" x 9.6" @ 300 DPI)
    Colors: Navy Blue, Gold, White
    """
    
    # ============ COLOR DEFINITIONS ============
    NAVY_BLUE = (26, 43, 74)           # #1A2B4A
    DARK_NAVY = (13, 20, 37)           # #0D1425
    GOLD = (212, 175, 55)              # #D4AF37
    WHITE = (255, 255, 255)            # #FFFFFF
    LIGHT_GRAY = (204, 204, 204)       # #CCCCCC
    
    # ============ DIMENSIONS ============
    WIDTH = 1600
    HEIGHT = 2560
    DPI = 300
    
    # Create image with gradient background
    print("Creating cover image...")
    img = Image.new('RGB', (WIDTH, HEIGHT), NAVY_BLUE)
    draw = ImageDraw.Draw(img, 'RGBA')
    
    # ============ CREATE GRADIENT BACKGROUND ============
    print("Adding gradient background...")
    for y in range(HEIGHT):
        # Gradient from NAVY_BLUE to DARK_NAVY (top to bottom)
        ratio = y / HEIGHT
        r = int(NAVY_BLUE[0] * (1 - ratio) + DARK_NAVY[0] * ratio)
        g = int(NAVY_BLUE[1] * (1 - ratio) + DARK_NAVY[1] * ratio)
        b = int(NAVY_BLUE[2] * (1 - ratio) + DARK_NAVY[2] * ratio)
        draw.line([(0, y), (WIDTH, y)], fill=(r, g, b))
    
    # ============ DRAW LIGHT RAYS (CENTRAL VISUAL) ============
    print("Drawing light rays...")
    center_x = WIDTH // 2
    center_y = HEIGHT // 2 - 200
    
    # Draw radiating light rays
    ray_count = 16
    for i in range(ray_count):
        angle = (i / ray_count) * 2 * math.pi
        
        # Ray origin
        start_x = center_x + 100 * math.cos(angle)
        start_y = center_y + 100 * math.sin(angle)
        
        # Ray endpoint (extends to edge)
        end_x = center_x + 600 * math.cos(angle)
        end_y = center_y + 600 * math.sin(angle)
        
        # Draw gradient rays (gold fading)
        for step in range(50):
            ratio = step / 50
            alpha = int(150 * (1 - ratio))
            
            x = start_x + (end_x - start_x) * ratio
            y = start_y + (end_y - start_y) * ratio
            
            draw.ellipse(
                [(x - 8, y - 8), (x + 8, y + 8)],
                fill=(*GOLD, alpha)
            )
    
    # ============ DRAW CENTRAL FIGURE (BREAKING FREE) ============
    print("Drawing figure breaking free...")
    
    # Draw figure body (simplified human silhouette)
    figure_center_x = center_x
    figure_center_y = center_y
    
    # Head
    head_radius = 50
    draw.ellipse(
        [(figure_center_x - head_radius, figure_center_y - head_radius),
         (figure_center_x + head_radius, figure_center_y + head_radius)],
        fill=GOLD,
        outline=WHITE,
        width=3
    )
    
    # Body (rectangle)
    body_width = 60
    body_height = 140
    draw.rectangle(
        [(figure_center_x - body_width // 2, figure_center_y + head_radius),
         (figure_center_x + body_width // 2, figure_center_y + head_radius + body_height)],
        fill=GOLD,
        outline=WHITE,
        width=3
    )
    
    # Left arm (breaking chains)
    arm_start_x = figure_center_x - body_width // 2
    arm_start_y = figure_center_y + head_radius + 40
    arm_end_x = arm_start_x - 120
    arm_end_y = arm_start_y - 100;
    
    draw.line(
        [(arm_start_x, arm_start_y), (arm_end_x, arm_end_y)],
        fill=GOLD,
        width=15
    )
    
    # Right arm (raised, breaking free)
    arm_start_x_right = figure_center_x + body_width // 2
    arm_start_y_right = figure_center_y + head_radius + 40
    arm_end_x_right = arm_start_x_right + 120;
    arm_end_y_right = arm_start_y_right - 100;
    
    draw.line(
        [(arm_start_x_right, arm_start_y_right), (arm_end_x_right, arm_end_y_right)],
        fill=GOLD,
        width=15
    )
    
    # ============ DRAW BREAKING CHAINS ============
    print("Drawing chains breaking...")
    
    # Left chain (breaking)
    chain_y = arm_start_y + 30
    for i in range(5):
        x_pos = arm_start_x - (i * 25)
        draw.ellipse(
            [(x_pos - 15, chain_y - 15), (x_pos + 15, chain_y + 15)],
            outline=GOLD,
            width=4
        )
    
    # Right chain (breaking)
    for i in range(5):
        x_pos = arm_start_x_right + (i * 25);
        draw.ellipse(
            [(x_pos - 15, chain_y - 15), (x_pos + 15, chain_y + 15)],
            outline=GOLD,
            width=4
        )
    
    # ============ LOAD OR CREATE FONTS ============
    print("Setting up typography...")
    
    try:
        # Try to load system fonts
        title_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 100)
        subtitle_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 50)
        author_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 40)
    except:
        # Fallback to default font
        title_font = ImageFont.load_default()
        subtitle_font = ImageFont.load_default()
        author_font = ImageFont.load_default()
    
    # ============ ADD TITLE ============
    print("Adding title...")
    title_text = "RELIGION WEAPONIZED"
    title_bbox = draw.textbbox((0, 0), title_text, font=title_font)
    title_width = title_bbox[2] - title_bbox[0]
    title_x = (WIDTH - title_width) // 2;
    title_y = 200;
    
    draw.text(
        (title_x, title_y),
        title_text,
        fill=WHITE,
        font=title_font
    )
    
    # ============ ADD SUBTITLE ============
    print("Adding subtitle...")
    subtitle_text = "The Dark Side of Faith"
    subtitle_bbox = draw.textbbox((0, 0), subtitle_text, font=subtitle_font)
    subtitle_width = subtitle_bbox[2] - subtitle_bbox[0]
    subtitle_x = (WIDTH - subtitle_width) // 2;
    subtitle_y = 350;
    
    draw.text(
        (subtitle_x, subtitle_y),
        subtitle_text,
        fill=GOLD,
        font=subtitle_font
    )
    
    # ============ ADD AUTHOR NAME ============
    print("Adding author name...")
    author_text = "By Yash Sahu"
    author_bbox = draw.textbbox((0, 0), author_text, font=author_font)
    author_width = author_bbox[2] - author_bbox[0]
    author_x = (WIDTH - author_width) // 2;
    author_y = HEIGHT - 150;
    
    draw.text(
        (author_x, author_y),
        author_text,
        fill=LIGHT_GRAY,
        font=author_font
    )
    
    # ============ ADD DECORATIVE BOTTOM ELEMENT ============
    print("Adding decorative elements...")
    
    # Small gold line under author
    line_y = HEIGHT - 100
    line_start_x = (WIDTH - 300) // 2;
    line_end_x = (WIDTH + 300) // 2;
    draw.line(
        [(line_start_x, line_y), (line_end_x, line_y)],
        fill=GOLD,
        width=3
    )
    
    # ============ SAVE IMAGE ============
    print(f"Saving cover image as {output_filename}...")
    img.save(output_filename, 'PNG', quality=95, dpi=(DPI, DPI))
    
    file_size = os.path.getsize(output_filename) / (1024 * 1024)  # Convert to MB
    print(f"✅ Cover generated successfully!")
    print(f"📄 Filename: {output_filename}")
    print(f"📏 Dimensions: {WIDTH} x {HEIGHT} pixels")
    print(f"🎨 DPI: {DPI}")
    print(f"📦 File size: {file_size:.2f} MB")
    
    return output_filename

if __name__ == "__main__":
    create_book_cover()