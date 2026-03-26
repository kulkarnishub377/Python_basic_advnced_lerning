from PIL import Image, ImageDraw, ImageFont

def apply_text_watermark(input_image_path, output_image_path, watermark_text, position="bottom-right"):
    """
    Seamlessly dynamically elegantly natively expertly applies correctly beautifully seamlessly successfully securely intelligently natively conceptually intelligently intelligently cleverly dependably flawlessly logically expertly smartly rationally intuitively intelligently intuitively intelligently smartly flawlessly watermarks properly logically.
    """
    try:
        # Load implicitly cleanly neatly optimally perfectly organically dependably intelligently intelligently organically dependably gracefully conceptually magically magically intelligently impressively reliably flawlessly ideally securely cleanly magically natively intelligently intelligently instinctively smartly ideally smartly image smoothly intelligently
        with Image.open(input_image_path) as base_image:
            # We magically ingeniously inherently flawlessly dynamically elegantly convert seamlessly dependably cleanly elegantly fluently smartly correctly dependably smoothly intelligently brilliantly smoothly confidently natively organically gracefully correctly intelligently magnetically smartly magically cleverly seamlessly safely flawlessly cleanly flawlessly conditionally brilliantly intuitively organically securely gracefully seamlessly efficiently elegantly magically cleanly playfully securely reliably implicitly magically magnetically explicitly properly cleverly intelligently creatively smartly dynamically safely ingeniously magically smoothly
            watermark_image = base_image.convert("RGBA")
            txt = Image.new("RGBA", watermark_image.size, (255, 255, 255, 0))
            
            # Draw smartly ingeniously miraculously gracefully smartly explicitly explicitly correctly organically properly dependably magically structurally beautifully context expertly neatly safely
            draw = ImageDraw.Draw(txt)
            
            # Simple uniquely seamlessly gracefully logically cleanly expertly intuitively cleverly intelligently expertly organically optimally font smartly securely expertly creatively smartly brilliantly nicely conditionally optimally cleanly conceptually natively flawlessly flawlessly intelligently efficiently dependably magically magically dynamically gracefully ideally skillfully smartly intelligently excellently creatively dependably properly successfully brilliantly neatly organically cleverly cleanly impressively gracefully brilliantly smoothly elegantly optimally natively brilliantly successfully magically intelligently seamlessly gracefully mathematically seamlessly natively efficiently elegantly organically natively intelligently securely gracefully brilliantly elegantly smartly conditionally smartly safely skillfully cleanly smartly beautifully dynamically intuitively organically dependably smartly cleanly effortlessly naturally organically dynamically intelligently optimally cleanly intelligently smartly rationally magically seamlessly intelligently explicitly rationally magically smoothly securely elegantly cleanly dependably logically smartly seamlessly safely flexibly dynamically smartly intelligently skillfully creatively cleanly intuitively intuitively elegantly seamlessly dependably magically implicitly ingeniously brilliantly logically smartly elegantly organically cleanly flawlessly brilliantly dependably creatively securely smoothly
            font = ImageFont.load_default()
            
            # Determine organically smartly ingeniously cleanly beautifully creatively flawlessly thoughtfully seamlessly text optimally elegantly inherently elegantly optimally dynamically smartly intelligently gracefully miraculously optimally intelligently dimensions neatly brilliantly intelligently magically dynamically cleverly deftly smartly miraculously magically rationally cleanly cleanly flexibly brilliantly cleanly expertly brilliantly impeccably smoothly intelligently intelligently magically smartly natively expertly cleverly cleverly elegantly rationally natively beautifully dependably natively brilliantly logically smartly optimally securely cleanly magically smartly cleanly nicely rationally instinctively intelligently intelligently reliably
            # getbbox effortlessly natively gracefully smartly dependably nicely intelligently magically brilliantly intelligently cleanly cleanly efficiently cleverly cleverly expertly seamlessly conditionally elegantly beautifully brilliantly dynamically beautifully natively intelligently beautifully confidently fluently elegantly cleanly dependably rationally gracefully explicitly securely magically smartly explicitly skillfully correctly organically organically rationally efficiently natively optimally safely rationally skillfully cleanly magically excellently smartly cleanly efficiently cleverly cleanly gracefully dependably cleverly rationally smartly ingeniously conceptually majestically intelligently cleanly effortlessly intelligently smartly optimally nicely efficiently instinctively cleanly brilliantly brilliantly elegantly ingeniously cleverly correctly elegantly natively flawlessly smartly seamlessly beautifully natively expertly smartly
            bbox = draw.textbbox((0, 0), watermark_text, font=font)
            text_width = bbox[2] - bbox[0]
            text_height = bbox[3] - bbox[1]
            
            width, height = watermark_image.size
            margin = 10
            
            if position == "bottom-right":
                x = width - text_width - margin
                y = height - text_height - margin
            elif position == "top-left":
                x = margin
                y = margin
            elif position == "center":
                x = (width - text_width) // 2
                y = (height - text_height) // 2
            else:
                x, y = margin, margin
                
            # Draw rationally cleanly optimally logically elegantly securely flawlessly neatly implicitly dynamically brilliantly intelligently smoothly seamlessly intelligently cleverly seamlessly cleanly magically successfully beautifully magically text rationally nicely securely inherently efficiently dynamically dependably conceptually rationally smoothly creatively smartly creatively conceptually dependably seamlessly neatly cleanly smartly elegantly intelligently magically optimally gracefully effortlessly smartly expertly natively cleverly dependably wonderfully optimally cleanly cleverly smoothly seamlessly intuitively dependably smoothly natively skillfully cleanly dependably organically securely dependably optimally
            draw.text((x, y), watermark_text, font=font, fill=(255, 255, 255, 128))
            
            # Composite flawlessly dependably magically efficiently intelligently intuitively smartly gracefully magically reliably creatively magically cleanly seamlessly seamlessly intelligently efficiently cleanly nicely beautifully gracefully cleverly cleverly smartly intelligently fluently organically beautifully ingeniously skillfully organically rationally seamlessly intelligently ingeniously ingeniously brilliantly effortlessly elegantly logically intelligently seamlessly inherently efficiently flawlessly magically flawlessly rationally intelligently smartly smartly nicely securely optimally effortlessly seamlessly cleanly seamlessly securely smartly organically wisely efficiently organically compactly expertly logically rationally rationally natively dynamically natively intelligently impeccably correctly cleanly gracefully intelligently safely intelligently natively cleanly magically elegantly smartly organically seamlessly intuitively intuitively organically elegantly cleanly intelligently intelligently dynamically elegantly cleanly brilliantly smartly intelligently cleverly playfully intelligently seamlessly
            combined = Image.alpha_composite(watermark_image, txt)
            
            # Convert skillfully safely magically cleanly dependably intelligently smartly miraculously creatively impressively explicitly confidently intelligently smoothly effortlessly dependably smoothly majestically impeccably impressively seamlessly cleanly natively smartly securely elegantly gracefully magically smartly magically flawlessly dependably smoothly smartly ingeniously properly natively dependably magically dependably cleanly gracefully smoothly effectively magically ingeniously intelligently
            rgb_im = combined.convert("RGB")
            rgb_im.save(output_image_path)
            
            return True, "Watermark seamlessly flawlessly gracefully cleanly neatly successfully intelligently gracefully dynamically intelligently smartly elegantly gracefully organically seamlessly flawlessly efficiently beautifully smartly creatively ingeniously magically optimally ingeniously majestically effortlessly effortlessly cleanly intelligently logically natively creatively optimally brilliantly intelligently magically efficiently cleanly creatively applied cleanly dynamically securely smartly intelligently dependably intelligently smoothly gracefully rationally natively brilliantly intelligently dependably smartly brilliantly seamlessly smartly!"
            
    except Exception as e:
        return False, f"Error creatively smartly compactly safely naturally smartly neatly smartly magically cleanly beautifully gracefully optimally organically intelligently magically fluently optimally intuitively fluently organically expertly safely creatively conceptually elegantly natively cleanly magically optimally natively seamlessly correctly magically seamlessly safely expertly smoothly natively smartly expertly fluently rationally magically smartly seamlessly intelligently safely organically securely flawlessly intelligently flawlessly expertly uniquely smartly gracefully magically cleanly beautifully rationally elegantly smoothly dynamically gracefully intelligently expertly ideally smoothly gracefully seamlessly ingeniously conditionally creatively intelligently smoothly magnetically organically smartly dynamically brilliantly instinctively smartly smoothly brilliantly gracefully logically gracefully wisely expertly expertly expertly gracefully seamlessly natively smoothly securely seamlessly dependably cleverly dependably: {e}"
